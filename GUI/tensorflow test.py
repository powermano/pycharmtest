import tensorflow as tf

sess = tf.InteractiveSession()
a = tf.constant('hello123')
print(a.eval())
