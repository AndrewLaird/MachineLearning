import tensorflow as tf
import cv2
import pong
import numpy as np
import random
from collections import deque

#define hyperprameters
ACTIONS = 3
#learning rate
GAMMA = 0.99
#update our gradient or training time
INITIAL_EPSILON = 1.0
FINAL_EPSILON = .05

#how many frames to anneal epsion (reach it)
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
#batch size
BATCH = 100

#create TF graph
def createGraph():
    #five layer convolutional neural network

    #first convolutional layer, bias vector
    W_conv1 = tf.Variable(tf.zeros([8,8,4,32]))
    b_conv1 = tf.Variable(tf.zeros([32]))

    #second layer
    W_conv2 = tf.Variable(tf.zeros([4,4,32,64]))
    b_conv2 = tf.Variable(tf.zeros([64]))

    #third layer
    W_conv3 = tf.Variable(tf.zeros([3,3,64,64]))
    b_conv3 = tf.Variable(tf.zeros([64]))

    #fourth
    W_fc4 = tf.Variable(tf.zeros([784,ACTIONS]))
    b_fc4 = tf.Variable(tf.zeros([784]))

    #fifth and last
    W_fc5 = tf.Variable(tf.zeros[784,ACTIONS])
    b_fc5 = tf.Variable(tf.zeros[ACTIONS])


    #input for the pixel data
    s = tf.placeholder("float",[None,84,84,84])


    #compute RELU activation function
    #on 2d convolutions
    #given 4D inputs and filter tensors

    conv1 = tf.nn.relu(tf.nn.conv2d(s,W_conv1,strides[1,4,4,1] padding = "VALID") + b_conv1)

    conv1 = tf.nn.relu(tf.nn.conv2d(s,W_conv1,strides[1,4,4,1] padding = "VALID") + b_conv1)


def main():
    #create session
    sess = tf.InteractiveSession()
    #input output layer
    inp, out = CreateGraph()
    trainGraph(inp,out,sess)

if __name__ == "__main__":
    main()