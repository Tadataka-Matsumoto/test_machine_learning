
# tensorflow2の場合
import tensorflow as tf
msg = tf.constant('Hello, tensorflow2')
tf.print(msg)
print(tf.__version__)



# tensorflow1にversiondownする場合
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()

# sess= tf.Session()
# hello = tf.constant('Hello, tensorflow1')
# print(sess.run(hello))