# CMPE-788-Resampling-Network-Data

## 1. Overview:

This project aims to implement a resampling technique for imbalanced Network Traffic Datasets. It combines various state-of-the-art resampling techniques and conducts several experiments with different techniques and compare their performances.

## 2. Files structure:

The `src` folder contains three Jupyter Notebook files aka three parts of the project, which implement different re-sampling techniques on two different datasets. The following are brief descriptions of each source file:

- `CMPE_788_final_project_part1.ipynb`: This file works with UNSW-NB15 dataset. It implements preprocessing, feature engineering, models building, and Random Undersampling technique

- `CMPE_788_final_project_part2.ipynb`: This file works with the CICIDS2018 dataset as a better alternative to the UNSW-NB15 dataset. It performs preprocessing, feature engineering,and dimensionality reduction and generate new dataset that is more suitable for model buidling and conducting further experiments.

- `CMPE_788_final_project_part3.ipynb`: This file is an extension of part 2. It builds ML models and testing different re-sampling techniques.

Each source file contains a detailed description of the algorithm used, the dataset it is applied to, and the performance metrics used to evaluate the model's performance.

## 3. How to run this project
- Run the `CMPE_788_final_project_part2.ipynb` file either locally or via Google Colab to generate the preprocessed dataset. Once the file is created, run the `CMPE_788_final_project_part3.ipynb` file. Simply hit the `Play` button to run ipynd files.
- The `CMPE_788_final_project_part1.ipynb` is obsolete. User can run this file as a reference but can totally ignore this file

## 4. Contributor:
- Steve Nguyen (sn4227@rit.edu)