import tensorflow as tf

sess = tf.InteractiveSession()
a = tf.constant('hello')
print(a.eval())
