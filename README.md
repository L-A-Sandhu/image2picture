# image2picture

## Introduction 

This repo converts the a time series data into images using the Gramian Angular Field.To clone the repository using the following commands 

```
git clone https://github.com/L-A-Sandhu/image2picture.git
cd image2picture

```

## Requirements 

This repo requires the following libraries for the conversion 

* Pyts
* Sklearn
* Pandas 
* Argparse
* Cv2
 
 To install all dependencies  make an environment using  the following commands 
 
```
conda create -n < env_name>  python=3.7
conda activate <env-name>
pip install -r requirements.txt

```

# Time Series to Image Conversion 

Run the following command to convert time series data in to images. 

```
cd im2pic
python main.py --csv_path < complete path for the csv file > --col_num < Coulm number of label intrested in such as wind is in coulm 0> --sample_len < Length of  samples you want to transform into image for 1000 sample image will be 1000x2000> --label_len < The length of label image> --out_path < The path for saving labels and images >
```
