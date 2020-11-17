# import tensorflow as tf
# msg = tf.constant('Hello, tensorflow2')
# tf.print(msg)

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# tensorflow1の場合
sess= tf.Session()
hello = tf.constant('Hello, tensorflow1')
print(sess.run(hello))