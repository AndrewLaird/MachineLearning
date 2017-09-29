import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean

LR = 1e-3 #how fast the game learns
env = gym.make('Acrobot-v1')
env.reset()

goal_steps = 1000
#score_requirement = 50 #take the better random games
initial_games = 10000#how many games we train on
inital_batch = 100
epochs = 5


def startup_games():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            #env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            print(observation)
            if(done):
                break
#startup_games()

def initial_game_population():
    training_data = []
    scores = []
    accepted_scores = []
    for _ in range(initial_games):
        score = 0
        game_memory = []
        prev_observation = []
        for _ in range(goal_steps):
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            if(len(prev_observation) > 0):
                game_memory.append([prev_observation,action])
            prev_observation = observation
            score += reward
            if(done):
                break
        if(score > -200):
            print(score)
            accepted_scores.append(-score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0,1,0]
                elif data[1] == 0:
                    output = [1,0,0]
                elif data[1] == 2:
                    output = [0,0,1]

                training_data.append([data[0],output])
        env.reset()
        scores.append(score)

    training_data_save = np.array(training_data)
    np.save('saved.npy',training_data_save)

    print("Average accepted score:", mean(accepted_scores))
    print("Median accepted score:", median(accepted_scores))
    return training_data

def neural_network_model(input_size):
    network = input_data(shape=[None,input_size,1], name='input')
    #                         input tensor, output tensor and activation function
    network = fully_connected(network,128,activation='relu')
    network = dropout(network, 0.8)
    #doing that for 5 more layers
    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network,3,activation='softmax')

    network = regression(network, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(network,tensorboard_dir='log')

    return model

def train_model(training_data, model=False):
    #taking the training data and reformating it into a flat shape
    X = np.array([i[0] for i in training_data]).reshape(-1,len(training_data[0][0]), 1)
    y = np.array([i[1] for i in training_data])

    if not model:
        model = neural_network_model(input_size=len(X[0]))

    model.fit({'input':X}, {'targets':y}, n_epoch=epochs, snapshot_step=500, show_metric=True,
              run_id='openaistuff')

    return model
#
# training_data = initial_game_population()
#model = train_model(training_data)
observation, reward, done, info = env.step(env.action_space.sample())
model = neural_network_model(len(observation))
model.load("acrobot")

for x in range(10):
    env.reset()
    observation, reward, done, info = env.step(env.action_space.sample())
    score = 0
    for _ in range(goal_steps):
        env.render()
        action = np.argmax(model.predict(observation.reshape(-1,len(observation),1))[0])
        observation, reward, done, info= env.step(action)
        if(done):
            break
        score += reward
    print("Score:", score)