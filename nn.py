
import tensorflow as tf
import numpy as np
import random

import time

class NeuralNetwork:
    def __init__(self, a,b,c,d=0):
        tf.keras.backend.set_learning_phase(0)
        if (isinstance(a,type(tf.keras.Sequential()))):
            self.model = a
            self.input_nodes = b
            self.hidden_nodes = c
            # self.hidden_layers = d
            self.output_nodes = d
        else:
            self.input_nodes = a
            self.hidden_nodes = b
            self.output_nodes = c
            self.model = self.createModel()
    
    def copy(self):
        modelCopy = self.createModel()
        weights = self.model.get_weights()
        weightCopies = []
        for i in range(len(weights)):
            weightCopies.append(weights[i].copy())
        modelCopy.set_weights(weightCopies)
        return NeuralNetwork(modelCopy,self.input_nodes,self.hidden_nodes,self.output_nodes)
    
    def mutate(self,rate):
        weights = self.model.get_weights()
        mutated_weights = []
        for i in range(len(weights)):
            tensor = weights[i]
            shape = weights[i].shape
            values = tensor.flatten()
            # values = tensor.slice()
            for j in range(len(values)):
                if random.random() < rate*0.5:
                    w = values[j]
                    values[j] = w + random.gauss(0,1)*0.8
            new_tensor = values.reshape(shape)
            mutated_weights.append(new_tensor)
        self.model.set_weights(mutated_weights)

    def dispose(self):
        pass
        # self.model.dispose()

    def predict(self,inputs):
        # print(inputs)
        x = np.expand_dims(inputs,axis=0)
        # start = time.time()
        y = self.model.predict(x).squeeze()
        # print(time.time()-start)
        return y

    def createModel(self):
        model = tf.keras.Sequential()
        # model.add(tf.keras.layers.InputLayer(self.input_nodes)
        model.add(tf.keras.layers.Dense(self.hidden_nodes,
                                    input_dim=self.input_nodes,
                                    activation=tf.keras.layers.Activation('sigmoid')))
        # model.add(tf.keras.layers.Dense(self.output_nodes,  activation=tf.keras.layers.Activation('sigmoid')))
        model.add(tf.keras.layers.Dense(self.output_nodes,  activation=tf.keras.layers.Activation('sigmoid')))

        # model.compile(tf.keras.optimizers.Adam(),loss=tf.keras.losses.MeanSquaredError())
        # print(model.get_weights())
        return model
        
       

 

# x = NeuralNetwork(1,3,1)
# # a = x.copy()
# print(x.model.get_weights())
# x.mutate(1.5)
# print(x.model.get_weights())
# print(a.model.get_weights())
# x_in = np.array(np.expand_dims([1,2 ],axis=0))
# print(x_in.shape)
# print(x.model.predict(x_in))
# tf.keras.utils.plot_model(x.model, to_file='model.png',show_shapes=True)

