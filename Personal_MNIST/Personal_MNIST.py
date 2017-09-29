import tensorflow as tf
import numpy as np

#get the mnist dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

print(len(mnist.train.next_batch(100)[1][0]),len(mnist.train.next_batch(100)[0][1]))

def build_model(input_size):

    input_layer = tf.placeholder(tf.float32,shape=[None,input_size])

    network = tf.nn.conv1d(input_layer,)