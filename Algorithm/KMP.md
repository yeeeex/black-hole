***关于KMP算法***
KMP算法是字符串匹配算法，假设检测一个字符串s1"ababaababaca"中是否有s2"ababaca",按照常规的办法，<br>我们是逐个检查s1中的每个
字符，如果s1中的某个字符和s2的第一个字符相等，则循环下去直到不等或者完全匹配，然后查<br>找s1的
下一个字符，如此的时间复杂度是O(m*n),KMP算法可以提供更高的效率<br><br><br>


首先我们对待匹配数组s2求出next解数组，next.size()和s2.size()相同，next[]解数组的主要作用是标记当我<br>
目前s2与s1中字符部分匹配，而当前s2下标指向的字符与s1下标字符不再匹配时，s1的下标前进去寻找下一个<br>
匹配而s2的的下标却不用退回到数组头部，具体退回到何处由next的数组确定，下面我们来看next实现代码与<br>
原理：<br>
vector<int> ComputePrefix(string &s) {    <br>
（&nbsp；）（&nbsp；）（&nbsp；）int n = s.length();<br>
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

