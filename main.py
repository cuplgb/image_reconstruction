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
1) Test whether it works
2) Loss and optimiser - proerties of trainer or of the network
3) Noise mask
4) Validation mask
5) Test mask
6) Multiple images
7) Better way of loading train and test images (see pytorch)
8) Track progress
9) Overlapping patches
10) When testing make sure that account for the fact that less informtaion is fed, 
i.e. decrease the magnitude of input inversly proportional to the increase in data information
'''


if __name__ =="__main__":

    patch_dims = [16,16]
    image_dims = [512,512]
    input_units = patch_dims[0]* patch_dims[1]
    learning_rate = 0.0001
    dataLoader = DataLoader(patch_dims,image_dims)
    trainer = Trainer()
    patches, patch_dims, image_dims = dataLoader.extract_image_patches()

    net = Network(input_units,learning_rate)
    trainer.train(net,dataLoader)
    #g = trainer.test(net,dataLoader)

    #patches_new = g[0].reshape(int(image_dims[0]/patch_dims[0]*image_dims[1]/patch_dims[1]),
    #                               patch_dims[0],
    #                               patch_dims[1])*256
    #image = dataLoader.combine_image_patches(patches_new)
    #imageio.imsave("rec.png",im=image)