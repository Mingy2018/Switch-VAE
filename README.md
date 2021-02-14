# Keras Implementation of 3D-VAE

### Packages

```markdown
python 3.6
tensorflow-gpu 1.13.1
matplotlib 3.3.2
scikit-image 0.17.2 
```

### Dataset

We use the [ShapeNetCore](https://www.shapenet.org/download/shapenetcore) dataset, for space consideration, in this repository we only provide the **volumetric data** in .binvox files of **chair class(03001627)** for training and testing VAE, which is under `./dataset`. 

If you want to train with many other different type of objects, the complete dataset is available in website above, it requires an account to download them. Besides, Stanford university also provide the same dataset under: https://cvgl.stanford.edu/data2/, which is convenient to download. The volumetric data is under `ShapeNetVox32.tgz` and the image data is under `ShapeNetRendering.tgz`.



- Volumetric data

There are 6778 elements in the chair class, the full object is available under `/dataset/03001627`. 

We also divide it into a train set and a test set, the `/dataset/03001627_train` folder consists of 5778 elements and the`/dataset/03001627_test` folder consists of 1000 elements.

In testing, if you want to generate images of the reconstructed objects at the same time, **it is recommended** to use this `/dataset/03001627_test_sub`, which consists of 100 objects from the 1000 test objects, because we use CPU to generate images, it takes about 10 minutes to test and generate images on 100 objects.

In `03001627_test_sub_visualization`, you could see the ground truth image of the 100 test objects.

- Image data

If you want to train the MMI-VAE model, both volumetric data and image data are required. You should download the dataset and process it with our script, to make the dataset compatible with training.

Set the path of volumetric data and image data in `process_dataset.sh`, the original dataset of one category will be  divided into 3 subsets respectively: `train`, `test` and `test_sub`. There is also other configurations you can set, like split scale etc, the details are in the script.

Process the dataset:

```
sh process_dataset.sh
```

 

### Training

Set your configuration in the `run_training.py` includes hyper parameters, train dataset, **save path** (it's recommended to set it out of the repository) etc, there are the options you could choose in [arg_parser.py](https://github.com/Mingy2018/MMI-VAE/blob/main/utils/arg_parser.py)

- Volumetric Data VAE

Set training configurations in `run_training.sh` file, which uses `train_VAE.py`. Use the 'chair' dataset under this repository to train and test. Other categories will be added in the future.

Start training:

```shell
sh run_training.sh
```

- MMI-VAE (Multi-Modal Input VAE)

Set training configurations in `run_training.sh` file, which uses `train_MMI.py`.

**Attention:**

Train set of volumetric data and image is generated by the script in chapter **Dataset**. Normally, the dataset option are in the following form:

```sh
--binvox_dir /home/zmy/Datasets/3d-r2n2-dataset/04256520_processed/voxel/train
--image_dir /home/zmy/Datasets/3d-r2n2-dataset/04256520_processed/image/train
```

Start training:

```sh
sh run_training.sh
```



### Test

- Test in Volumetric Data VAE

After training the weights of models is saved as `.h5` file and used for testing, set the test configuration in `run_testing,sh`, such as **set the weights file path** and test dataset path. You could also set the path where save the reconstructed objects in `save_dir`, and choose if generate the images or not for **visualization**. Furthermore, you could also choose if save the original data for comparison by setting `save_ori`.

Start testing

```shell
sh run_testing.sh
```

- Test in MMI-VAE

We use `test_MMI.py` to test MMI model, the test model take only one input, either voxel or image, you could define the `input_from` in `run_testing.sh`. Once you select the `input_form`, also define the corresponding test dataset in `run_testing.sh`.

Start testing

```sh
sh run_testing.sh
```



### Visualization

To visualize the loss during the training process, use tensorboard to load the training data. After training, the loss during training was saved in the folder named by the timestamp.

To visualize the loss:

```sh
tensorboard --logdir path_of_training_data_folder
```

