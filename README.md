# SwitchVAE: Learning Better Latent Representations from Objects of Different 3D Euclidean Formats

of Different 3D Euclidean Formats

### Packages

```markdown
python 3.6
tensorflow-gpu 1.13.1
matplotlib 3.3.2
scikit-image 0.17.2 
pillow 8.0.1
```

### Dataset

We use the [ShapeNetCore](https://www.shapenet.org/download/shapenetcore) dataset for training and use ModelNet for testing.

- ShapeNetCore

The complete dataset is available in website above, it requires an account to download them. Besides, Stanford university also provide the same dataset under: https://cvgl.stanford.edu/data2/, which is convenient to download. The volumetric data is under `ShapeNetVox32.tgz` and the image data is under `ShapeNetRendering.tgz`.

Use our script to process the dataset, which makes the dataset compatible with training and test. We design the processed dataset, the process dataset of one category will contains voxel/image folders, each folder is divided into 3 subsets respectively: `train`, `test` and `test_sub`, we make a special design for in voxel folder, `test_sub_visualization` is added for visualize the models in `test_sub`.

Set the [process_dataset.sh](https://github.com/Mingy2018/MMI-VAE/blob/main/process_shapenet.sh) with your local dataset path after downloading.

Process the dataset:

```shell
sh process_dataset.sh
```

**Attention:** Processing the whole dataset takes about 2 hours.

- ModelNet

The complete dataset is available under: http://modelnet.cs.princeton.edu/, which contains **ModelNet10** and **ModelNet40**.

 The original dataset contains only 3D objects in `.off` form, **voxelization** is needed for training in MMI-VAE. Use the following command to transform the `.off` files to `.binvox` files.

```
for f in ModelNet10/*/*/*.off; do binvox -cb -pb -e -c -d 32 $f; done
```







There is also other configurations you can set, like split scale etc, the details are in the script.

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

- Latent space analyse & Interpolation

After training, you could load the `.h` weights file into model. `analyse/generate_latent.py` supports to map the volumetric input or image input to latent vectors and save them in `.pkl` form, then you could use `analyse/interpolation.py` to load the saved latent information and choose 2 objects and do interpolation between them.



### Visualization

To visualize the loss during the training process, use tensorboard to load the training data. After training, the loss during training was saved in the folder named by the timestamp.

To visualize the loss:

```sh
tensorboard --logdir path_of_training_data_folder
```

