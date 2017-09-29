import gym
import random
import numpy as np
import tensorflow as tf



env = gym.make("CarRacing-v0")
env.reset()

num_actions = env.action_space.n
print(num_actions)

#env.render()



action = env.action_space.sample()
observation, reward, done, info = env.step(action)
print(observation, reward, sep='\n\n\n')
for x in range(100):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(observation, reward, sep='\n\n\n')

def create_model():
    tf.layers.conv3d()

