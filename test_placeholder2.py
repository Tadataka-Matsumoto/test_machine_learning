# tensorflowを取り込む
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# プレースホルダを定義
a = tf.placeholder(tf.int32, [None, 2])


# ベクトルを2倍にする演算を定義
two = tf.constant(2)
x2_op = a * two

# セッションを開始する
sess = tf.Session()


# tensorboardのためにグラフを出力
sample_list = [[1, 1],[2, 2],[3, 3],[4, 4]]
res = sess.run(x2_op, feed_dict={a : sample_list})
print(res)