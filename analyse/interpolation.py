import numpy as np
import shutil, sys, os, pickle
sys.path.append("..")

from MMI import *
from VAE import *
from utils import save_volume, data_IO, arg_parser, model

from utils import model
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

ConFig=tf.ConfigProto()
ConFig.gpu_options.allow_growth=True
session=tf.Session(config=ConFig)


def main():

    latent_dims = 128

    interpolation_save_path = '/home/zmy/Desktop/test/test_sub_image_input/interpolation'
    latent_vector_file = open('/home/zmy/TrainingData/2021.2.17/2021_02_25_17_59_00/test/image_latent_dict/latent_dict.pkl', 'rb')
    weights_path = '/home/zmy/TrainingData/2021.2.17/2021_02_25_17_59_00/end_weights.h5'

    # Get the latent vector of two objects
    latent_vector_dict1 = pickle.load(latent_vector_file)
    p1, p2 = latent_vector_dict1['2afa06a01a0a15fc504721639e19f609_z'], latent_vector_dict1['2c250a89e731a3d16f554fd9e81f2ffc_z']
    print("The type of p1", type(p1))
    print("The shape of p2", p1.shape)
    latent_vectors = np.linspace(p1, p2, 11)
    print("The type of latent vector", type(latent_vectors))
    print("The shape of latent vector", latent_vectors.shape)


    # Define the decoder model

    decoder = model.get_voxel_decoder(latent_dims)
    decoder.load_weights(weights_path,by_name=True)
    reconstructions = decoder.predict(latent_vectors)

    reconstructions[reconstructions > 0] = 1
    reconstructions[reconstructions < 0] = 0

    if not os.path.exists(interpolation_save_path):
        os.makedirs(interpolation_save_path)

    for i in range(reconstructions.shape[0]):
        name = str(i)
        save_volume.save_binvox_output_2(reconstructions[i, 0, :], name, interpolation_save_path, '_gen', save_bin= True, save_img= True)

if __name__ == '__main__':
    main()