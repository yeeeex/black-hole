### 关于_cdecl和_stdcall和_fastcall
`int _cdecl/_stdcall/_fastcall input(int i){`<br>
`　　i++;`<br>
`　　return 0;`<br>
`}`<br>
假设这个函数被main函数调用，情况如下：<br>
\_cdecl为<br>
![image](https://user-images.githubusercontent.com/26924058/51824332-ef28dd80-231c-11e9-9e72-aa7ceeecd7c3.png)<br>
在main函数内执行完input后为<br>
![image](https://user-images.githubusercontent.com/26924058/51824375-0798f800-231d-11e9-8bd5-88de6536b2b7.png)<br>
\_stdcall为<br>
