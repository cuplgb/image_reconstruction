from scipy import misc 
import tensorflow as tf
import numpy as np
import imageio
from DataLoader import DataLoader
from Network import Network
from Trainer import Trainer


'''
TO RUN:

source ~/tensorflow/bin/activate

THEN
deactivate


TODO:
+1) Test whether it works
+2) Loss and optimiser - proerties of trainer or of the network
+3) Noise mask
+4) Validation mask
+5) Test mask
6) Multiple images
+7) Better way of loading train and test images (see pytorch)
8) Track progress
+9) Overlapping patches
10) When testing make sure that account for the fact that less informtaion is fed, 
i.e. decrease the magnitude of input inversly proportional to the increase in data information
'''


if __name__ =="__main__":
    # Set parameters
    patch_dims = [16,16]
    image_dims = [512,512]
    steps = [1,1]
    input_units = patch_dims[0]*patch_dims[1]
    learning_rate = 0.05
    batch_size = 32
    epoches = 10
    hiddent_units = 128
    
    # Create dataloader
    dataLoader = DataLoader(patch_dims,image_dims,batch_size,steps)
    
    # Create network
    net = Network(input_units,learning_rate,hiddent_units)
    
    # Create trainer
    trainer = Trainer(net,batch_size,epoches)
    
    # Train the network
    trainer.train(dataLoader)

    # Test the network and save the image
    g = trainer.test(dataLoader)
    
    dataLoader.combine_and_save_image_patches(g[0])

    
    # Close the tensorflow session opened in trainer
    trainer.close()
    

