import numpy as np
import tensorflow as tf
import math

out = np.array([[4.0, 5.0, 10.0], [1.0, 5.0, 4.0], [1.0, 15.0, 4.0]])
y = np.array([[0, 0, 1], [0, 1, 0], [0, 1, 0]])

out1 = np.array([0.0, 1.0])
y1 = np.array([0.05, 0.95])
y2 = np.array([0, 1])

o1 = tf.nn.softmax(out1)
loss = tf.nn.log_softmax(out1)
print(tf.Session().run(loss))
print(np.log(math.exp(1)/(1+math.exp(1))))
a1 = 0.95 * (np.log(0.95) - np.log(math.exp(1)/(1+math.exp(1))))
a2 = 0.05 * (np.log(0.05) - np.log(1/(1+math.exp(1))))
print('kl_div is :', a1+a2)

a11 = 0.95 * (-np.log(math.exp(1)/(1+math.exp(1))))
a22 = 0.05 * (-np.log(1/(1+math.exp(1))))

print('cross entropy is:', a11+a22)

res = tf.losses.softmax_cross_entropy(onehot_labels=y1, logits=out1, label_smoothing=0)
print(tf.Session().run(res))

res1 = tf.losses.softmax_cross_entropy(onehot_labels=y2, logits=out1, label_smoothing=0.1)
print(tf.Session().run(res1))

res2 = tf.losses.softmax_cross_entropy(onehot_labels=y, logits=out, label_smoothing=0.001)
print(tf.Session().run(res2))

# new_onehot_labels = onehot_labels * (1 - label_smoothing)
#                           + label_smoothing / num_classes

new_onehot_labels = y * (1 - 0.001) + 0.001 / 3
print(y)
print(new_onehot_labels)
res3 = tf.losses.softmax_cross_entropy(onehot_labels=new_onehot_labels, logits=out, label_smoothing=0)
print(tf.Session().run(res3))