import tensorflow as tf
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import re
# a=tf.constant("hello world")
# sess=tf.Session()
# print(sess.run(a))

#
# m=re.search(r'\bthe','bite the dog')
# if m is not None:
#    print( m.group())



m=re.findall(r'(th\w+) and (th\w+)','this and that....')
if m is not None:
   for each in m:
       print(each)

