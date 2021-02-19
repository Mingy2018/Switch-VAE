
import numpy as np
import matplotlib.pyplot as plt
from utils import data_IO, metrics
import os

# using in test_VAE.py
def save_binvox_output(output_arr, output_hash, output_dir, outname, save_bin = False, save_img = True):

    # save objedt as .binvox
    if save_bin:
        s1 = output_dir + '/' + output_hash + outname + '.binvox'
        print('The s1 is', s1)
        s1 = bytes(s1, 'utf-8')
        data_IO.write_binvox_file(output_arr, s1)

    # save the model image
    if save_img:
        fig = plt.figure()
        ax =fig.gca(projection = '3d')
        ax.voxels(output_arr.astype(np.bool), edgecolors='k')
        plt.savefig(output_dir + '/' + output_hash + outname + '.png')
        plt.close()

# using in test_MMI.py
def save_binvox_output_2(output_array, hash_id, output_dir, outname, save_bin = False, save_img = True):

    # save objedt as .binvox
    if save_bin:
        s1 = output_dir + '/' + hash_id + outname + '.binvox'
        print('The s1 is', s1)
        s1 = bytes(s1, 'utf-8')
        data_IO.write_binvox_file(output_array, s1)

    # save the model image
    if save_img:
        fig = plt.figure()
        ax =fig.gca(projection = '3d')
        voxel_array = np.swapaxes(output_array, 1, 2)
        ax.voxels(voxel_array.astype(np.bool), edgecolors='k')
        plt.savefig(output_dir + '/' + hash_id + outname + '.png')
        plt.close()


def binvox2image(voxel_file, hash_id, output_dir, outname=''):

    voxel_array = data_IO.read_voxel_data(voxel_file)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxel_array.astype(np.bool), edgecolors='k')
    plt.savefig(output_dir + '/' + hash_id + outname + '.png')
    plt.close()

def binvox2image_2(voxel_file, hash_id, output_dir, outname=''):

    voxel_array = data_IO.read_voxel_data(voxel_file)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    voxel_array=np.swapaxes(voxel_array, 1,2)

    ax.voxels(voxel_array.astype(np.bool), edgecolors='k')
    plt.savefig(output_dir + '/' + hash_id + outname + '.png')
    plt.close()

def save_metrics(predictions, gt, voxelPath,imagePath,inputform,output_dir):
    """
    Save the metrics into .txt form
    Args:
        output_array: the output of voxel decoder
        gt: voxel ground truth
        output_dir: save path
    Returns:
    """
    metrics_file = os.path.join(output_dir, 'metrics.txt')
    metrics_file = open(metrics_file, 'w')

    precision, IoU, recall =metrics.evaluate_voxel_prediction(predictions, gt, threshold=1)
    metrics_file.write(voxelPath + '\n')
    metrics_file.write(imagePath + '\n')
    metrics_file.write(inputform + '\n')
    metrics_file.write("Object number:" +str(predictions.shape[0]) +'\n')
    metrics_file.write("Precision:" + str(precision) + '\n')
    metrics_file.write("IoU:" + str(IoU) + '\n')
    metrics_file.write("Recall:" + str(recall) + '\n')
    metrics_file.close()

    # for i in range(predictions.shape[0]):
    #     precision, IoU, recall = metrics.evaluate_voxel_prediction(predictions[i], gt[i], threshold=1)
    #     metrics_file.write(str(hash_id[i]) + ',')
    #     metrics_file.write(str(precision) + ',')
    #     metrics_file.write(str(IoU) + ',')
    #     metrics_file.write(str(recall) + '\n')
    # metrics_file.close()

