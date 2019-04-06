**什么是logistic回归？**<br>
logistic回归又叫分类，它所预测的结果相对于线性回归来说，是离散的，例如：预测一封邮件是否是垃圾邮件，只对应是(1)<br>
不是(0)两种结果，其他值无法取到，这就是离散的。logistci回归虽然预测的结果是离散的，但是拟合的函数Hθ(x)却不一定是<br>
离散的，例如可以将Hθ(x)大于0.5时，使得预测的结果为1,logistci回归中，Hθ(x)更多的是预测一个概率，所以0<=Hθ(x)<=1<br>
<br>

**假设函数（以0,1分类）**<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=h_\Theta(x)&space;=g(\Theta&space;^Tx)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_\Theta(x)&space;=g(\Theta&space;^Tx)" title="h_\Theta(x) =g(\Theta ^Tx)" /></a>
<br>
<img src="https://latex.codecogs.com/gif.latex?g(Z)=\frac{1}{1&plus;e^{-Z}}=\frac{1}{1&plus;e^{-\Theta&space;^Tx}}" title="g(Z)=\frac{1}{1+e^{-Z}}=\frac{1}{1+e^{-\Theta ^Tx}}" />
<br>
我们可以得知g(z)函数的值是大于0小于1的，因为e^(-x)是大于0，小正无穷的<br>
h(x)其实是预测的P(y=1|x;θ)与P(y=0|x;θ),下面给出ng课上分类的几个例子：<br>
![image](https://github.com/yeeeex/black-hole/blob/master/%E5%90%B4%E6%81%A9%E8%BE%BE%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E4%B8%80%E4%BA%9B%E5%85%AC%E5%BC%8F/%E7%BA%BF%E6%80%A7%E5%88%86%E7%B1%BB%E8%BE%B9%E7%95%8C.png)<br>
↑↑↑这是线性分类边界<br>
![image](https://github.com/yeeeex/black-hole/blob/master/%E5%90%B4%E6%81%A9%E8%BE%BE%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E4%B8%80%E4%BA%9B%E5%85%AC%E5%BC%8F/%E9%9D%9E%E7%BA%BF%E6%80%A7%E5%88%86%E7%B1%BB%E8%BE%B9%E7%95%8C.png)<br>
↑↑↑这是非线性分类边界<br>
<br>
**关于代价函数**<br>
<img src="https://latex.codecogs.com/gif.latex?J(\Theta)=\frac{1}{m}\sum_{i=1}^{m}\frac{1}{2}(h_\Theta(x^{(i)})-y^{(i)})^2&space;\newline&space;\rightarrow&space;Cost(h_\Theta&space;,y)=\left\{\begin{matrix}&space;-log(h_\Theta(x))&space;\qquad&space;if(y==1)&space;\\&space;-log(1-h_\Theta&space;(x))&space;\qquad&space;if(y==0)&space;\end{matrix}\right." title="J(\Theta)=\frac{1}{m}\sum_{i=1}^{m}\frac{1}{2}(h_\Theta(x^{(i)})-y^{(i)})^2 \newline \rightarrow Cost(h_\Theta ,y)=\left\{\begin{matrix} -log(h_\Theta(x)) \qquad if(y==1) \\ -log(1-h_\Theta (x)) \qquad if(y==0) \end{matrix}\right." />
<br>
关于这个Cost函数，如果y本身为1但是预测结果为接近0,COST的值将会非常的大，所以模型会受到较大的惩罚，如果y本身为0但是<br>
预测结果为1，同理，我们带入参数即可验证<br>
关于J(Θ)，我们可以改写为如下形式:<br>
<img src="https://latex.codecogs.com/gif.latex?J(\Theta)=\frac{-1}{m}[\sum_{i=1}^{m}y^{(i)}log(h_\Theta(x^{(i)}))&plus;(1-y^{(i)})log(1-h_\Theta(x^{(i)}))]" title="J(\Theta)=\frac{-1}{m}[\sum_{i=1}^{m}y^{(i)}log(h_\Theta(x^{(i)}))+(1-y^{(i)})log(1-h_\Theta(x^{(i)}))]" />
<br>
也更方便求导，然后我们同样要min j(Θ)，当可以求导以后，便用梯度下降的方法下降参数即可，同时ng的视频中还提到了 conjugate gradient<br>
BFGS,L-BFGS等高阶优化方法，等我以后来填坑<br>
<br>
**多标签分类问题**<br>
即标签不止为0,1还有2,3,4。。。等等，面对多标签分类，我们可以将其转化为双标签，即将与需要预测的标签一致的标签看作是一类标签<br>
其他任何标签都视为另外一类标签。<br><br>

**过拟合问题**<br>
过拟合问题即拟合的曲线和样本点完全的重合，但是拟合结果的泛化能力较差，例如ng如下给出的例子：<br>
![image](https://github.com/yeeeex/black-hole/blob/master/%E5%90%B4%E6%81%A9%E8%BE%BE%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E4%B8%80%E4%BA%9B%E5%85%AC%E5%BC%8F/%E8%BF%87%E6%8B%9F%E5%90%88%E4%BE%8B%E5%AD%90.png)<br>
如何减少过拟合呢？第一个方法是减少特征值的数量，将范围有重叠的特征值删去，二是减小参数θ的值，这样可以让曲线看起来平滑些<br>
第二种适用于每个特征都很重要无法删除的情况<br>

**之前我一直没想通COST函数究竟怎么来了，看了西瓜书以后我来补完**<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=z=\frac{1}{1&plus;e^{-\Theta^TX}}&space;\rightarrow&space;ln\frac{z}{1-z}=\Theta^TX" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z=\frac{1}{1&plus;e^{-\Theta^TX}}&space;\rightarrow&space;ln\frac{z}{1-z}=\Theta^TX" title="z=\frac{1}{1+e^{-\Theta^TX}} \rightarrow ln\frac{z}{1-z}=\Theta^TX" /></a>
<br>
因为z是求出来的概率，z/(1-z)实际上是样本为1比上样本为0的比率，所以又可以写为特定x条件下，y为概率与y为0概率比:<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=ln\frac{z}{1-z}=ln\frac{P(y=1|x)}{P(y=0|x)}=\Theta^TX\\&space;\therefore&space;P(y=1|x)=\frac{\Theta^TX}{1&plus;\Theta^TX},P(y=0|x)=\frac{1}{1&plus;\Theta^TX}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ln\frac{z}{1-z}=ln\frac{P(y=1|x)}{P(y=0|x)}=\Theta^TX\\&space;\therefore&space;P(y=1|x)=\frac{\Theta^TX}{1&plus;\Theta^TX},P(y=0|x)=\frac{1}{1&plus;\Theta^TX}" title="ln\frac{z}{1-z}=ln\frac{P(y=1|x)}{P(y=0|x)}=\Theta^TX\\ \therefore P(y=1|x)=\frac{\Theta^TX}{1+\Theta^TX},P(y=0|x)=\frac{1}{1+\Theta^TX}" /></a>
<br>
然后我们可以根据极大似然估计法，对于已知的x,y，估计出能使他们以最大概率成立的Θ，我们有如下估计函数：
<a href="https://www.codecogs.com/eqnedit.php?latex=L(\Theta)=\prod_{i=1}^{m}P(y_i|x_i;\Theta&space;)\\&space;\because&space;\prod_{i=1}^{m}P(y_i|x_i;\Theta)=P(y_i|x_i;\Theta&space;)^{1-y}P(y_i|x_i;\Theta&space;)^{1-y_i}&space;\\&space;\therefore&space;\zeta&space;(\Theta&space;)=\sum_{i=1}^{m}lnP(y_i|x_i;\Theta&space;)&space;\\&space;\rightarrow&space;\zeta&space;(\Theta&space;)=\sum_{i=1}^{m}y_iln(P(y_i|x_i,b))&plus;(1-y_i)ln(1-(P(y_i|x_i,b))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L(\Theta)=\prod_{i=1}^{m}P(y_i|x_i;\Theta&space;)\\&space;\because&space;\prod_{i=1}^{m}P(y_i|x_i;\Theta)=P(y_i|x_i;\Theta&space;)^{1-y}P(y_i|x_i;\Theta&space;)^{1-y_i}&space;\\&space;\therefore&space;\zeta&space;(\Theta&space;)=\sum_{i=1}^{m}lnP(y_i|x_i;\Theta&space;)&space;\\&space;\rightarrow&space;\zeta&space;(\Theta&space;)=\sum_{i=1}^{m}y_iln(P(y_i|x_i,b))&plus;(1-y_i)ln(1-(P(y_i|x_i,b))" title="L(\Theta)=\prod_{i=1}^{m}P(y_i|x_i;\Theta )\\ \because \prod_{i=1}^{m}P(y_i|x_i;\Theta)=P(y_i|x_i;\Theta )^{1-y}P(y_i|x_i;\Theta )^{1-y_i} \\ \therefore \zeta (\Theta )=\sum_{i=1}^{m}lnP(y_i|x_i;\Theta ) \\ \rightarrow \zeta (\Theta )=\sum_{i=1}^{m}y_iln(P(y_i|x_i,b))+(1-y_i)ln(1-(P(y_i|x_i,b))" /></a>


