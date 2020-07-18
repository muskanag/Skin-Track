import pandas as pd
import numpy as np
from numpy import matrix
import xlwt
import myfeat
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter 
from scipy.fftpack import fft
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet",cell_overwrite_ok=True)
i=0
for i in range(5):
    mydata=pd.read_excel('touch%d.xls'%(i))
    mydata1=mydata.iloc[:,:4]
    mydata1.as_matrix() 
    col1=matrix(mydata1).transpose()[0].getA()[0]
    col2=matrix(mydata1).transpose()[1].getA()[0]
    col3=matrix(mydata1).transpose()[2].getA()[0]
    col4=matrix(mydata1).transpose()[3].getA()[0]
    col1=signal.medfilt(col1[:],7)
    col2=signal.medfilt(col2[:],7)
    col3=signal.medfilt(col3[:],7)
    col4=signal.medfilt(col4[:],7)
    col1=col1[50:len(col1)-50]
    col2=col2[50:len(col1)-50]
    col3=col3[50:len(col1)-50]
    col4=col4[50:len(col1)-50]
    col1 = signal.savgol_filter(col1,401,3)
    col2 = signal.savgol_filter(col2,401,3)
    col3 = signal.savgol_filter(col3,401,3)
    col4 = signal.savgol_filter(col4,401,3) 
    arr_p1 = col1
    arr_p2 = col2

    arr_m1 = col3

    arr_m2 = col4
#mean

    mean_p1 = np.mean(arr_p1)

    mean_p2 = np.mean(arr_p2)

    mean_m1 = np.mean(arr_m1)

    mean_m2 = np.mean(arr_m2)

    sheet1.write(i,0,mean_p1)
    sheet1.write(i,1,mean_p2)
    sheet1.write(i,2,mean_m1)
    sheet1.write(i,3,mean_m2)

    #max

    max_p1 = np.amax(arr_p1)

    max_p2 = np.amax(arr_p2)

    max_m1 = np.amax(arr_m1)

    max_m2 = np.amax(arr_m2)
    sheet1.write(i,4,max_p1)
    sheet1.write(i,5,max_p2)
    sheet1.write(i,6,max_m1)
    sheet1.write(i,7,max_m2)


    iqr_p1 = myfeat.IQR(arr_p1)
    iqr_p2 = myfeat.IQR(arr_p2)
    iqr_m1 = myfeat.IQR(arr_m1)
    iqr_m2 = myfeat.IQR(arr_m2)
    sheet1.write(i,8,iqr_p1)
    sheet1.write(i,9,iqr_p2)
    sheet1.write(i,10,iqr_m1)
    sheet1.write(i,11,iqr_m2)


    #min

    min_p1 = np.amin(arr_p1)

    min_p2 = np.amin(arr_p2)

    min_m1 = np.amin(arr_m1)

    min_m2 = np.amin(arr_m2)

    sheet1.write(i,12,min_p1)
    sheet1.write(i,13,min_p2)
    sheet1.write(i,14,min_m1)
    sheet1.write(i,15,min_m2)

    #median

    med_p1 = np.median(arr_p1)

    med_p2 = np.median(arr_p2)

    med_m1 = np.median(arr_m1)

    med_m2 = np.median(arr_m2)
    sheet1.write(i,0+16,med_p1)
    sheet1.write(i,1+16,med_p2)
    sheet1.write(i,2+16,med_m1)
    sheet1.write(i,3+16,med_m2)


    #range

    range_p1 = max_p1-min_p1
    range_p2 = max_p2-min_p2

    range_m1 = max_m1-min_m1
    range_m2 = max_m2-min_m2
    sheet1.write(i,0+20,range_p1)
    sheet1.write(i,1+20,range_p2)
    sheet1.write(i,2+20,range_m1)
    sheet1.write(i,3+20,range_m2)


    #standard deviation

    std_p1 = np.std(arr_p1)

    std_p2 = np.std(arr_p2)

    std_m1 = np.std(arr_m1)

    std_m2 = np.std(arr_m2)

    sheet1.write(i,0+24,std_p1)
    sheet1.write(i,1+24,std_p2)
    sheet1.write(i,2+24,std_m1)
    sheet1.write(i,3+24,std_m2)

    #sum

    sum_p1 = np.sum(arr_p1)

    sum_p2 = np.sum(arr_p2)

    sum_m1 = np.sum(arr_m1)

    sum_m2 = np.sum(arr_m2)

    sheet1.write(i,0+28,sum_p1)
    sheet1.write(i,1+28,sum_p2)
    sheet1.write(i,2+28,sum_m1)
    sheet1.write(i,3+28,sum_m2)

    #rms
    rms_p1 = myfeat.rms(arr_p1)
    rms_p2 = myfeat.rms(arr_p2)
    rms_m1 = myfeat.rms(arr_m1)
    rms_m2 = myfeat.rms(arr_m2)

    sheet1.write(i,0+32,rms_p1)
    sheet1.write(i,1+32,rms_p2)
    sheet1.write(i,2+32,rms_m1)
    sheet1.write(i,3+32,rms_m2)
    #IQR

    

    #entropy
"""
    ent_p1 = myfeat.entropy(arr_p1)
    ent_p2 = myfeat.entropy(arr_p2)
    ent_m1 = myfeat.entropy(arr_m1)
    ent_m2 = myfeat.entropy(arr_m2)
    sheet1.write(i,0,ent_p1)
    sheet1.write(i,1,ent_p2)
    sheet1.write(i,2,ent_m1)
    sheet1.write(i,3,ent_m2)
"""
book.save("features2.xls")        