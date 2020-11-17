# tensorflowを取り込む
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 定数を定義
a = tf.constant(100)
b = tf.constant(30)

# 演算を定義
add_op = a+b

# セッションを開始する
sess = tf.Session()
res = sess.run(add_op)
print(res)