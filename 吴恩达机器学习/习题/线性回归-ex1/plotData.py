import matplotlib.pyplot as plt


def plot_data(x, y):
   
    plt.scatter(x,y,marker='o',s=50,cmap='Blues',alpha=0.3)  #绘制散点图
    plt.xlabel('population')  #设置x轴标题
    plt.ylabel('profits')   #设置y轴标题 
    
    plt.show()

#need complete
def plot_data_self(x,y):
    plt.scatter(x,y,c="b",marker="o",)
    plt.xlabel("population")
    plt.ylabel("profit")

    plt.show()