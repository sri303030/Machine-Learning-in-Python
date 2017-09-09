import tensorflow as tf

# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)


with tf.Session() as sess:
    output = sess.run(result)
    print(output)