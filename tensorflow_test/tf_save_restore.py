import tensorflow as tf
import os
import numpy as np

v1 = tf.get_variable("v1", shape=[3])
v2 = tf.get_variable("v2", shape=[5])
#v3 = tf.get_variable('v3', shape=[1,2])
init_op = tf.global_variables_initializer()
saver = tf.train.Saver()

path = "E:/savetest/"
with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.

  # Save the variables to disk.
  save_path = saver.save(sess, os.path.join(path, 'model2.ckpt'))
  print("Model saved in file: %s" % save_path)

tf.reset_default_graph()

# Create some variables.
h1 = tf.get_variable("v1", shape=[3])
h2 = tf.get_variable("v2", shape=[5])


# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
 # v3.initializer.run()
  # Restore variables from disk.
  saver.restore(sess, save_path)
  print("Model restored.")
  # Check the values of the variables
  print("v1 : %s" % h1.eval())
  print("v2 : %s" % h2.eval())

  #print('v3: %s' %v3.eval())
