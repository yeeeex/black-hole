***关于KMP算法***<br>
KMP算法是字符串匹配算法，假设检测一个字符串s1"ababaababaca"中是否有s2"ababaca",按照常规的办法，<br>我们是逐个检查s1中的每个
字符，如果s1中的某个字符和s2的第一个字符相等，则循环下去直到不等或者完全匹配，然后查<br>找s1的
下一个字符，如此的时间复杂度是O(m*n),KMP算法可以提供更高的效率<br><br><br>


首先我们对待匹配数组s2求出next解数组，next.size()和s2.size()相同，next[]解数组的主要作用是标记当我<br>
目前s2与s1中字符部分匹配，而当前s2下标指向的字符与s1下标字符不再匹配时，s1的下标前进去寻找下一个<br>
匹配而s2的的下标却不用退回到数组头部，具体退回到何处由next的数组确定，下面我们来看next实现代码与<br>
原理：以前v[]=next[]<br>
vector<int> ComputePrefix(string &s) {    <br>
　　　　　int n = s.length();<br>
　　　　　vector<int> v(n, -1);<br>
　　　　　int k = -1;<br>
　　　　　for (int q = 1;q!= n; q++) {<br>
　　　　　　　　while (k > -1 && s[k + 1] != s[q])<br>
　　　　　　　　　　　k = v[k];<br>
　　　　　　　　if (s[k + 1] == s[q])<br>
　　　　　　　　　　　k += 1;<br>
　　　　　　　　　　　v[q] = k;<br>
　　　　　　}<br>
　　　　　return v;<br>
}<br>
首先函数会从头部和第二个字符还是扫描，如果如果s[k+1]和s[q]相等了那么当匹配时在q点失败了时便可以退回到q+1点<br>
而不用退回到头部，大大节省了效率，如果不相等，则一直回溯到到找到前面一个相等的或者是k=-1即头部<br>

接下来看匹配串函数的实现：<br>
vector<int> KMPtest(string& text, string& pattern) {<br>
　　　　　　　　　vector<int> res;<br>
　　　　　　　　　int n = text.length();<br>
　　　　　　　　　int m = pattern.length();<br>
　　　　　　　　　vector<int> v(ComputePrefix(pattern));<br>
　　　　　　　　　for (auto&e : v) {<br>
　　　　　　　　　　　　cout << e << endl;<br>
　　　　　　　　　}
　　　　　　　　　int q = -1;<br>
　　　　　　　　　for (int i = 0; i != n;i++) {<br>
　　　　　　　　　　　　while (q > -1 && pattern[q + 1] != text[i])<br>
　　　　　　　　　　　　　　　　　q = v[q];<br>
　　　　　　　　　　　　if (pattern[q + 1] == text[i])<br>
　　　　　　　　　　　　　　　　　q += 1;<br>
　　　　　　　　　　　　if (q == m - 1)<br>
　　　　　　　　　　　　{<br>
　　　　　　　　　　　　　　　　　res.push_back(i);<br>
　　　　　　　　　　　　　　　　　q = v[q];<br>
　　　　　　　　　　　　}<br>
　　　　　　　　　}<br>
　　　　　　　　　return res;<br>
　　　　}<br>
函数会遍历s1，每当s1和s2部分相等，而当前下标不相等时，s2不用再退回头部，而是退回q=v[q]直到q=-1无法回溯时
