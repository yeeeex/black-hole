### 首先什么是文件映射对象
即磁盘上的物理文件在内存中的映射，这样会将整个文件映射到内存中，是否就避免了ReadFile每次都要<br>
进行I/O的花费呢？是映射到虚拟内存类似于显存那样不在主存中的映射呢还是在物理主存内存中也有分配呢呢？<br>
通过查阅MSDN<br>
![image](https://github.com/yeeeex/black-hole/blob/master/Programming%20Applications%20for%20Microsoft%20Windows/pictures/3.png)<br>
我们可以得知这是利用了操作系统的虚拟存储机制，用户进程所能看到的虚拟存储空间里，认为文件是已经在内存中的<br>
但是实际时文件可能并不在，或者只有部分，最多可能全部在物理内存中这是由分配给文件的物理页所决定的，而用户所看到的<br>
确实认为他们需要的文件部分，或者是全部，已经在内存中，所以当访问到没有对应物理页的虚拟页时，将产生缺页中断<br>
这本身和虚拟内存机制没多少区别。<br>
文件映射对象的另外一个重要作用是文件共享，物理内存中只保留一份该文件，但是因为在连个进程的虚拟地址空间里都有<br>
映射，提升了共享的效率。<br>
通过查阅资料和自己的理解，**我觉得如果只有一个进程创建了文件映射对象，那么应该和虚拟内存机制是类似的(不太确定)**<br>
**但是注意，虚拟内存机制一开始并不会映射磁盘里的内容，所以要手动调用，那么如果我不调用CreateFileMapping函数**<br>
**其他方式操作文件，会自动将文件映射到虚拟内存中吗？还是说只能对readfile读进来的部分进行操作？文件映射是否**<br>
**能够省略掉读这一步，不对啊，例如fwrite本来就不用先fread啊**
以上可能是口胡，接下来可能是真正的理解，CreateFileMapping函数只是告诉OS要创建一个文件映射对象，具体还没有映射上去<br>
用户可以指定映射的地址，然后通过MapViewOfFile将映射放到用户指定的虚拟地址，然后用户对这段虚拟地址读写，便会通过<br>
虚拟内存机制，MMU对地址翻译，缺页中断之类的完成最终对磁盘上文件的读写，省区了fread,fwrite，之类对内存读写即可<br>
但是多个进程创建了文件映射对象时，却能极大的提高效率



![image](https://github.com/yeeeex/black-hole/blob/master/Programming%20Applications%20for%20Microsoft%20Windows/pictures/5.png)<br>
**在这段代码中发现如果将CreateFile的第二个参数设置为STANDARD_RIGHTS_ALL，则需要管理员云权限才能使CF函数跳过error1，但是在第二**<br>
**个函数，即CreateFileMapping时，依然GetLastError()会返回5，即出现了权限问题，但是如果CF函数里填GENERIC_READ之类的不论是CF函数**<br>
**还是CFM函数，不论是管理员权限，还是普通权限都能够运行，我推测的原因是，STANDARD_RIGHT_ALL里包含了五种标准控制权限，而GENERIC_READ**<br>
**是通用控制权限，CF和CFM权限之间的矛盾导致了这个问题，标准控制权限需要管理员运行，但是标准控制权限和CFM里的权限矛盾了。明天我将试着**<br>
**对SECURITY_ATTRIBUTES进行初始化来测试
