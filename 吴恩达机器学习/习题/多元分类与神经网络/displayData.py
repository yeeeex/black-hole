import matplotlib.pyplot as plt
import random as rd
import numpy as np

def displayData(x):
    (m, n) = x.shape   #100*400
 
    
    example_width=(np.round(np.sqrt(n))).astype(int)  #显示宽度
    #这个宽度是指一个字符的宽度
    example_height=(n/example_width).astype(int) #显示高，一个1字符的高
    display_rows=(np.floor(np.sqrt(m))).astype(int) 
    display_cols=(np.ceil(m/display_rows)).astype(int)  #n^2样本按照nxn显示
    # 待显示的每张图片之间的间隔
    pad = 1
 
    # 显示的布局矩阵 初始化值为-1
    display_array = - np.ones((pad + display_rows * (example_height + pad),
                              pad + display_rows * (example_height + pad)))
    #置位-1代表黑色
 
    curr_ex = 0
    for j in range(display_rows):
        for i in range(display_cols):#m个字符中迭代
            if curr_ex >= m:
                break
 
           
            max_val = np.max(np.abs(x[curr_ex]))
            display_array[pad + j * (example_height + pad) + np.arange(example_height),\
                 pad + i * (example_width + pad) + np.arange(example_width)[:,np.newaxis]] = \
                          x[curr_ex].reshape((example_height, example_width)) /max_val
            #对于第(i,j)个字符，在d_a里的位置
            #(pad + j * (example_height + pad) + np.arange(example_height),
            #pad + i * (example_width + pad) + np.arange(example_width)[:, np.newaxis])
            #其中np.arange(example_height)表示返回对应行的0-example_height列
            #np.neaxis为将np.arange返回一个横着的排列竖着。类似于reshape(10,1)
            #/max_val应该是为了灰度？
            curr_ex += 1
            


 
            
    plt.figure(0)
    plt.imshow(display_array,cmap='gray',extent=[-1, 1, -1, 1])
    plt.show()

         



            





