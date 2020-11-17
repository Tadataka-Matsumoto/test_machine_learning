import tensorflow as tf

print('111111')

gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices: tf.config.experimental.set_memory_growth(device, True)

print('222222')

a = tf.constant(100)
b = tf.constant(30)

add_op = a + b

print('3333333')

# sess = tf.Session()
# res = sess.run(add_op)
# print(res)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.1)
y = np.sin(x)*np.sin(x)
plt.plot(x, y)
plt.show()







