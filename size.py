#ライブラリインポート
import cv2
import numpy as np
from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img

def predict_size(input_filename):
    #認識させたい画像の読み込み
    picgray=cv2.imread(input_filename,cv2.IMREAD_GRAYSCALE)
    picgray2=cv2.resize(picgray, dsize=(224, 224))
    #picgray = image.load_img(input_filename, grayscale=True, target_size=(224,224))

    #画像の解像度を指定
    pixel=0.89 #mm/pixel

    #長さを測る高さを指定
    analysis_row=200


    #二値化データの作成
    ret, thresh = cv2.threshold(picgray2, 5, 255, cv2.THRESH_BINARY)

    #輪郭抽出
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    max_cnt =max(contours, key=lambda x: cv2.contourArea(x))

    #輪郭内を塗りつぶし
    pic_thresh = cv2.drawContours(picgray2, [max_cnt], -1, 255, -1)

    #指定行のデータを週出
    bright_data=pic_thresh[analysis_row,:]

    #長さを算出
    num_pix=np.count_nonzero(bright_data)
    length=round(num_pix*pixel,1)

    return length