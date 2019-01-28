### 关于_cdecl和_stdcall
`int _cdecl/_stdcall/_fastcall input(int i){`<br>
`　　i++;`<br>
`　　return 0;`<br>
`}`<br>
假设这个函数被main函数调用，情况如下：<br>
\_cdecl为<br>
![image](https://user-images.githubusercontent.com/26924058/51824332-ef28dd80-231c-11e9-9e72-aa7ceeecd7c3.png)<br>
在main函数内执行完input后为<br>
![image](https://user-images.githubusercontent.com/26924058/51824375-0798f800-231d-11e9-8bd5-88de6536b2b7.png)<br>
<br>
\_stdcall为<br>
![image](https://github.com/yeeeex/black-hole/blob/master/Programming%20Applications%20for%20Microsoft%20Windows/pictures/1.png)<br>
在main里执行完了input为<br>
![image](https://github.com/yeeeex/black-hole/blob/master/Programming%20Applications%20for%20Microsoft%20Windows/pictures/2.png)<br>
<br>
我们可以看出\_cdecl里返回是ret而\_stdcall里返回时ret 4而在main函数里input结束以后，\_cdecl由主调函数恢复<br>
栈，即add esp,4于此同时\_stdcall确是在input尾部即由被调函数恢复栈即ret 4，这导致可变参数函数只能用\_cdecl<br>
来调用，因为被调函数无法实现确切知道需要弹出的数量而主调函数却可以，ret指令类似与pop IP,pop以后还需要再+相应<br>
位置来跳过压入栈的参数以恢复栈，推测ret 4就是弹出ip以后，直接加，所以用\_cdecl方式才能可变参数，例如下栈:<br>
　　　1<br>
call input   栈里实际是input的地址 (IP)<br>
只有主调函数参知道是压了一个栈进去，而不是两个<br>
<br>
然后是可执行文件大小的问题，\_cdecl的可执行文件会比\_stdcall大因为假设main里对input函数调用1000次<br>
\_cdecl会产生100次add esp 4的操作，而\_stdcall只用再input末尾ret 4一次就行了,他们的压栈方式相同<br>
<br>
### 关于_fastcall
`input(1, 2, 3, 4);`<br>
`00B6173E　　push　　4`<br>
`00B61740　　push　　3` <br>
`00B61742　　mov　　　edx,2` <br>
`00B61747　　mov　　　ecx,1`  <br>
`00B6174C　　call　　input (0B6107Dh)`  _fastcall其余和_stdcall一样，只是会将最右两个参数扔进<br>
寄存器edc,ecx增加传参速度

### 关于naked call
__declspec(naked) 类似于内联汇编的inline函数
