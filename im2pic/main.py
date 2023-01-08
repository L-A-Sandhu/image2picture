
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField
import pandas as pd
import cv2
import os.path as o
from sklearn import preprocessing
import argparse
import os
# Sample_len=1000
# Pred_len = 4
# path='../Dataset/wind_dataset.csv'

def im2pic(path,Sample_len,Pred_len,OP):
    df = pd.read_csv(path, index_col=0)
    X=df[df.columns[0]]
    X = X.to_numpy()
    for i in range(len(X)-(Sample_len+4)):
        # Image genration
        Y=X[i:i+Sample_len]
        Y=np.reshape(Y,[1,Sample_len])
        gasf = GramianAngularField(method='summation')
        X_gasf = gasf.fit_transform(Y)
        X_gasf = np.reshape(X_gasf,[Sample_len,Sample_len])
        gadf = GramianAngularField(method='difference')
        X_gadf = gadf.fit_transform(Y)
        X_gadf =  np.reshape(X_gadf,[Sample_len,Sample_len])
        f_img  =  cv2.hconcat([X_gadf,X_gasf])
        a=(np.min(f_img))
        b=(np.max(f_img))
        f_img=f_img+(-1)*a
        cv2.imwrite(OP+'images/'+str(i)+'.png',f_img)
        # Mask genration 
        pre=X[i+Sample_len+1:i+Sample_len+Pred_len+1]
        pre=np.reshape(pre,[1,Pred_len])
        gasf = GramianAngularField(method='summation')
        X_gasf = gasf.fit_transform(pre)
        X_gasf = np.reshape(X_gasf,[Pred_len,Pred_len])
        gadf = GramianAngularField(method='difference')
        X_gadf = gadf.fit_transform(pre)
        X_gadf =  np.reshape(X_gadf,[Pred_len,Pred_len])
        f_img  =  cv2.hconcat([X_gadf,X_gasf])
        a=(np.min(f_img))
        b=(np.max(f_img))
        f_img=f_img+(-1)*a
        cv2.imwrite(OP+'labels/'+str(i)+'.png',f_img)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description=' Image to Picture Conversion ') 
        parser.add_argument("--csv_path", type= str , default='../Dataset/wind_dataset.csv', help='path to the')    
        parser.add_argument("--sample_len", type= int, default= 1000, help='input sample length')
        parser.add_argument("--label_len", type=int,default=4, help="prediction sample size")
        parser.add_argument("--out_path", type= str, default='../Dataset/', help="prediction sample size")
        args = parser.parse_args()
        if not os.path.exists(args.out_path+'/images/'):
            os.makedirs(args.out_path+'/images/')
        if not os.path.exists(args.out_path+'/labels/'):
            os.makedirs(args.out_path+'/labels/')
        im2pic(args.csv_path, args.sample_len, args.label_len, args.out_path)
