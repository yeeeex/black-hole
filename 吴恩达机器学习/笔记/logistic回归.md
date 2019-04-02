**什么是logistic回归？**<br>
logistic回归又叫分类，它所预测的结果相对于线性回归来说，是离散的，例如：预测一封邮件是否是垃圾邮件，只对应是(1)<br>
不是(0)两种结果，其他值无法取到，这就是离散的。logistci回归虽然预测的结果是离散的，但是拟合的函数Hθ(x)却不一定是<br>
离散的，例如可以将Hθ(x)大于0.5时，使得预测的结果为1,logistci回归中，Hθ(x)更多的是预测一个概率，所以0<=Hθ(x)<=1<br>
<br>

**假设函数**<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=h_\Theta(x)&space;=g(\Theta&space;^Tx)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_\Theta(x)&space;=g(\Theta&space;^Tx)" title="h_\Theta(x) =g(\Theta ^Tx)" /></a>
<br>
<img src="https://latex.codecogs.com/gif.latex?g(Z)=\frac{1}{1&plus;e^{-Z}}=\frac{1}{1&plus;e^{-\Theta&space;^Tx}}" title="g(Z)=\frac{1}{1+e^{-Z}}=\frac{1}{1+e^{-\Theta ^Tx}}" />
