# CPS843-PPE-Detection
Repo to house the training scripts for our YOLO model


# Test Results

Link to the Google Drive with the test results:
```
https://drive.google.com/drive/folders/13XorQ8ePIG2wy0UVAimjc1wL8P9X5nif?usp=drive_link
```

# Installation

Clone this repo by running

```bash
git clone git@github.com:Louis-Chevalier/CPS843-PPE-Detection.git
```
Navigate to the project directory and run the command to create a new python virtual enviromnment.
```bash
python3 -m venv .venv
```

To enter the virtual environment you must run 
```bash
source .venv/bin/active
```
> [!IMPORTANT]
> You must run the above command before first running the scripts (i.e., if you reboot your computer or open a new terminal window)

Next install the necessary python libraries
```bash
pip install ultralytics
```
> [!NOTE]
> YOU ARE NOT DONE.
> Ensure you are on a linux distro compatible with 
> If you are running an AMD gpu like I am you need to follow the steps to install ROCm
> [AMD guide to installing ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)
>
> Ensure you also install the ROCm package in your python virutal environment
> 
> ```bash
> pip install wheel setuptools
> ```
> 
> And the following as per the [PyTorch guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html)
>
> ```bash
>  pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.0
> ```


This will give you the necessary models and scripts needed to run the YOLOv11 model

# Roboflow
Go to the workspace and click on `Versions` tab and click on `Create new Version`.

<img width="1660" height="830" alt="image" src="https://github.com/user-attachments/assets/c512ff37-61f9-4d7e-8df0-c8e518d2a8ea" />

You can add `Preprocessing` and `Augmentations` to the dataset. The `Augmentations` step can easily double datasets since it copies and modifies images in certain way and then adds them back into the dataset.

<img width="678" height="759" alt="image" src="https://github.com/user-attachments/assets/aa86060d-8414-43d2-a319-6fcab94a3640" />


Keep clicking on `Continue` and then `Create`. 

> [!IMPORTANT]
> Before you create this "Version" of the dataset, please ensure to add a simple message to decscribe the dataset in the `Version Notes` field.
> <img width="1108" height="468" alt="image" src="https://github.com/user-attachments/assets/319dfa4c-9312-4bcf-ac66-1aeb6fafab0a" />


## Using created `Version`

Once you have your version of the dataset to train on, click on `Download Dataset`.

<img width="1511" height="528" alt="image" src="https://github.com/user-attachments/assets/d47411a8-f2d7-42b6-8aef-1eed68f872c7" />

> [!IMPORTANT]
> DO NOT click on `Custom Train` this will train on the Roboflow website which is not what we want. We want to train local, hence why we need to download the dataset.

Select the `Yolov11` model as the Image and Annotation Format. Also select `Download ZIP to computer`; we already have the code. Finally deselect `Also train a model for Label Assist with Roboflow Train`.

<img width="803" height="473" alt="image" src="https://github.com/user-attachments/assets/e92bc3bc-1352-4f0a-ae1a-9415cc5f7779" />

Lastly, unzip the files into the git directory
```bash
unzip ~/Downloads/PPE.v1i.yolov11.zip -d ~/CPS843-PPE-Detection/
```

Go into the project directory.

```bash
cd CPS843-PPE-Detection/
```
You should see that the directory is already populated with the folders and most importantly the `data.yaml`

<img width="808" height="42" alt="image" src="https://github.com/user-attachments/assets/b84ee24e-48b1-4c83-9853-5a893924f38f" />


# Train

To train the model on the dataset simply run

```bash
python3 train.py trained_model_name location_model_size
```

Thus to train a YOLO model using the YOLO11n size looks like this:
```bash
python3 train.py sample_model_n ./yolo11n.pt
```
