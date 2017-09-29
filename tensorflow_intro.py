import tensorflow as tf

x1 = tf.constant([6,5,4,3],shape=(2,2))
x2 = tf.constant([31,30,29,28],shape=(2,2))
w1 = tf.constant([10])
w2 = tf.constant([50])

result = tf.matmul(x1,x2)
print(tf.multiply(x1,x2))
print(result)

with tf.Session() as sess:
    print(sess.run(result))
    print(sess.run(tf.multiply(x1, x2)))
    print(sess.run(tf.multiply(w1,w2)))
