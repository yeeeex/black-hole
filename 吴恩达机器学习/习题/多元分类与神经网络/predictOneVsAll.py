from oneVsAll import*
from sigmoid import*


def predictOneVsAll(all_theta,X):
        m=X.shape[0]
        num_labels=all_theta.shape[0]
        X=np.c_[np.ones((m,1)),X]
        values=np.zeros(X.shape[0])
        temp=sigmoid(X.dot(all_theta.T)) # 5000X400 ,400X10=5000X10
        #然后找出5000行中最可能为哪个就行了
        values=np.argmax(temp,axis=1)
        #axis=1时按行返回每行最大值的索引
        values[values==0]=10 
        return values


