import numpy as np
from numpy import exp,array,random,dot

class NeuralNetwork():
    def __init__(self):
        #seed the random number generator, so that it is the same every time
        random.seed(1)

        #assign random weights to the neurons between 1 and -1
        self.synaptic_weights  = 2 * random.random((3,1)) - 1

    def __sigmoid_derivative(self,x):
        return x * (1-x)

    #sigmoid or activation function
    def __sigmoid(self,x):
        return 1/(1 + exp(-x))

    def train(self,training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            #pass the training set through our neural net
            output = self.predict(training_set_inputs)
            #calculate the error
            error = training_set_outputs - output

            #multiply the rror by the input and again by the gradient of the sigmoid curve
            adjustment = dot(training_set_inputs.T,error*self.__sigmoid_derivative(output))

            #adjust the weights
            self.synaptic_weights += adjustment

    def predict(self,inputs):
        #pass inputs through our neural network (our single neuron)
        return self.__sigmoid(dot(inputs,self.synaptic_weights))



if __name__ == '__main__':

    #initialize neuron network
    neural_network = NeuralNetwork()

    print('random starting synaptic weights:')
    print(neural_network.synaptic_weights)

    #The training set we have 4 exmples each with 3 input values and 1 output value
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    #train the neural network
    #iterate 10,000 times and make small adjustments each time
    neural_network.train(training_set_inputs,training_set_outputs,10000)

    print("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    #test the neural network with a new situation
    print("Considering new situation [1,0,0] -> ?:")
    print(neural_network.predict(np.array([1,0,0])))
