import tflearn
from tflearn.data_utils import to_categorical,pad_sequences
from tflearn.datasets import imdb


#Network building
net = tflearn.input_data([None,100])
net = tflearn.embedding(net,input_dim=10000,output_dim=128)
net = tflearn.lstm(net,128,dropout=0.8)
net = tflearn.fully_connected(net,2,activation='softmax')
net = tflearn.regression(net,optimizer='adam', learning_rate=0.0001,loss='categorical_crossentropy')


#getting the model
model = tflearn.DNN(net,tensorboard_verbose=0)
model.load('emotional_model')
print(model.net)