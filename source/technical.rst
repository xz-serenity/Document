GPT
===============================



GPT 修改语句
-------------------------------

.. note::

    Please carefully check the spell and grammar, tell me all the mistakes and issues and give a detailed analysis of how to fix them. Make the sentences more logical and smooth if necessary. Appropriately add some transitional sentences.

.. code-block:: bash

    Please carefully check the spell and grammar, tell me all the mistakes and issues and give a detailed analysis of how to fix them. Make the sentences more logical and smooth if necessary. Appropriately add some transitional sentences.

.. note::
    
    Rewritten all the sentences. Change the word and order to put each sentence in another way to say. Do not contain any repetition compared to the origin one.

.. code-block:: bash

    Rewritten all the sentences. Change the word and order to put each sentence in another way to say. Do not contain any repetition compared to the origin one.

.. note::

    Make the sentences more logical and smooth. Appropriately add some transitional sentences. Better to conclude some long sentences into one or two sentence(s).

.. code-block:: bash

    Make the sentences more logical and smooth. Appropriately add some transitional sentences. Better to conclude some long sentences into one or two sentence(s).

.. note::

    Please carefully check the spell and grammar, tell me all the mistakes and issues and give a detailed analysis of how to fix them. Do not alter the sentence order or unnecessarily rephrase.

.. code-block:: bash

    Please carefully check the spell and grammar, tell me all the mistakes and issues and give a detailed analysis of how to fix them. Do not alter the sentence order or unnecessarily rephrase.



Linux
===============================



Linux 命令行
-------------------------------

重命名/移动文件: 

.. code-block:: bash

    mv [oldfile] [newfile]

复制文件:

.. code-block:: bash

    cp [oldfile] [newfile]

删除文件:

.. code-block:: bash

    rm [file]

切换目录:

.. code-block:: bash

    cd [directory]

C++ 执行命令:

.. code-block:: bash

    g++ [file.cpp] -o [execute]
   ./[execute]

查看文件所有的内容:

.. code-block:: bash
    
    cat [file]

复制本地文件到大集群/小集群 (在 *本地* 操作):

.. code-block:: bash

    scp -P 10190 ./[file] suzhaogang@10.4.3.17:/share/home/suzhaogang/xiaozhou/
    rsync -r ./[file] xiaozhou@10.1.20.53:/share/home/xiaozhou/[directory]  #密码: xz2022

复制大集群/小集群文件到本地 (在 *本地* 操作):

.. code-block:: bash

    scp -P 10190 suzhaogang@10.4.3.17:/share/home/suzhaogang/xiaozhou/[directory] ./
    rsync -r xiaozhou@10.1.20.53:/share/home/xiaozhou/[directory] ./  #密码: xz2022

复制大集群文件到小集群 (在 *大集群* 操作):

.. code-block:: bash

    rsync -r ./[file] xiaozhou@10.1.20.53:/share/home/xiaozhou/[directory]

解压文件: 
    
    - .zip 解压:
    
    .. code-block:: bash

        unzip [文件名]

    - .gz 解压:

    .. code-block:: bash
        
        gzip -d [文件名]
    
    - tar.gz 解压:

    .. code-block:: bash

        tar -zxvf [文件名]

    - .tar 解压:

    .. code-block:: bash

        tar -xvf [文件名]


参考的对象类型不支持尝试的操作

.. code-block:: bash

    管理员运行 powershell:
    netsh winsock reset

查看ip

.. code-block:: bash
    
    sudo apt-get install net-tools
    ifconfig
    
查看进程 

.. code-block:: bash
    
    bjobs

查看进程状态

.. code-block:: bash

    ps -aux | grep ""

杀死所有进程 (大集群)

.. code-block:: bash

    ps -aux | grep "suzhao" | awk '$1=="suzhaog+" {print $2}' | xargs kill -9

杀死所有进程 (小集群)

.. code-block:: bash
    
    ps -aux | grep "" | awk '$1=="xiaozhou" {print $2}' | xargs kill -9

结束进程

.. code-block:: bash 

    #结束所有任务
    ./killall
    #结束指定任务
    bkill [JobID]

检查容量

.. code-block:: bash
    
    du -sh *

后台运行

.. code-block:: bash
    
    ./run.sh &

删除 core

.. code-block:: bash
    
    # check 目录下: 
    nohup ./rmcore.sh &


统计文件中重复字符串出现的次数: 

.. code-block:: bash
    
    grep -o '字符串' file |wc -l







Vim
===============================

Vim 配置
-------------------------------

主要是配置 .vimrc 文件, 具体如下:

#. 设置ctags: <https://blog.csdn.net/qq_29350001/article/details/77162347>

#. 自动补全括号

.. code-block:: bash

    # inoremap ( ()<Esc>i
    # inoremap [ []<Esc>i
    # inoremap < <><Esc>i
    # inoremap { {}<Esc>i
    # inoremap ' ''<Esc>i
    # inoremap " ""<Esc>i

Vim 命令
-------------------------------

- 命令模式

#. 打开多个文件:  vim [file1] [file2]
#. 查看打开多个文件的序号: :ls
#. 打开文件后进行切换:  :b[数字]
#. 分屏显示文件: vim -o[数字] [file1] [file2]
#. 上下分割当前打开的文件: ctrl + w s  或 :sp
#. 左右分割当前的文件:  ctrl + w v  或  :vs
#. 关闭当前的分屏: ctrl + w c 或者 ctrl + w q
#. 删除从光标处开始到该单词结束的所有字符, 并进入插入模式: cw
#. 把全文中的 <1> 替换成 <2>:  :%s/<1>/<2>/g
#. 将光标位置开始的3个字母改变其大小写:  3~
#. 折叠代码: zf[行序号]G
#. 打开所有折叠的代码: zR

#. z回车 将光标所在行移动到屏幕顶端
    
    z. 将光标所在行移动到屏幕中间 
    
    z- 将光标所在行移动到屏幕低端

#. 两文件进行切换: ctrl + 6	
#. 下一个文件:  :bn
#. 上一个文件:  :bp
#. 两窗口进行切换: ctrl + w + <上下左右方向键>
#. tab切换: gt 或者 , + 数字
#. 关闭当前tab: :tabc

#. 跳转到当前文件内标识符首次出现的位置, 可用于跳转到变量的定义处: gD
#. 跳转到当前函数内标识符首次出现的位置, 可用于跳转到局部变量的定义处: gd
#. 跳转到光标上次所在位置: ''

#. h 或 向左箭头键(←): 光标向左移动一个字符
#. j 或 向下箭头键(↓): 光标向下移动一个字符
#. k 或 向上箭头键(↑): 光标向上移动一个字符
#. l 或 向右箭头键(→): 光标向右移动一个字符

#. [Ctrl] + [f]: 屏幕 [向下] 移动一页, 相当于 [Page Down] 按键 (常用)
#. [Ctrl] + [b]: 屏幕 [向上] 移动一页, 相当于 [Page Up] 按键 (常用)
#. [Ctrl] + [d]: 屏幕 [向下] 移动半页
#. [Ctrl] + [u]: 屏幕 [向上] 移动半页

#. +: 光标移动到非空格符的下一行
#. -: 光标移动到非空格符的上一行
#. n<space>: 按下数字后再按空格键, 光标会向右移动这一行的 n 个字符
#. 0 或功能键[Home]: 移动到这一行的最前面字符处 (常用)
#. $ 或功能键[End]: 移动到这一行的最后面字符处(常用)

#. H: 光标移动到这个屏幕的最上方那一行的第一个字符
#. M: 光标移动到这个屏幕的中央那一行的第一个字符
#. L: 光标移动到这个屏幕的最下方那一行的第一个字符
#. G: 移动到这个档案的最后一行 (常用)
#. nG: n 为数字.移动到这个档案的第 n 行.例如 20G 则会移动到这个档案的第 20 行
#. gg: 移动到这个档案的第一行, 相当于 1G 啊！ (常用)
#. n<Enter>: 光标向下移动 n 行 (常用)

#. /[word]: 向光标之下寻找一个名称为 word 的字符串
#. ?[word]: 向光标之上寻找一个字符串名称为 word 的字符串.
#. n: 重复前一个搜寻的动作
#. *:[n1],[n2]s/[word1]/[word2]/g*: 在第 n1 与 n2 行之间寻找 word1 这个字符串, 并将该字符串取代为 word2
#. *:1,$s/word1/word2/g* 或 *:%s/word1/word2/g*: 从第一行到最后一行寻找 word1 字符串, 并将该字符串取代为 word2!
#. *:1,$s/word1/word2/gc* 或 *:%s/word1/word2/gc*: 从第一行到最后一行寻找 word1 字符串, 并将该字符串取代为 word2! 且在取代前显示提示字符给用户确认 (confirm) 是否需要取代

#. x, X: 在一行字当中, x 为向后删除一个字符 (相当于 [del] 按键),  X 为向前删除一个字符(相当于 [backspace] 亦即是退格键)
#. nx: 连续向后删除 n 个字符
#. dd: 删除游标所在的那一整行(常用)
#. ndd: 删除光标所在的向下 n 行, 例如 20dd 则是删除 20 行 (常用)
#. d1G: 删除光标所在到第一行的所有数据
#. dG: 删除光标所在到最后一行的所有数据
#. d$: 删除游标所在处, 到该行的最后一个字符
#. d0: 删除游标所在处, 到该行的最前面一个字符
#. yy: 复制游标所在的那一行(常用)
#. nyy: 复制光标所在的向下 n 行, 例如 20yy 则是复制 20 行(常用)
#. y1G: 复制游标所在行到第一行的所有数据
#. yG: 复制游标所在行到最后一行的所有数据
#. y0: 复制光标所在的那个字符到该行行首的所有数据
#. y$: 复制光标所在的那个字符到该行行尾的所有数据
#. p, P: p 为将已复制的数据在光标下一行贴上, P 则为贴在游标上一行
#. J: 将光标所在行与下一行的数据结合成同一行
#. c: 重复删除多个数据, 例如向下删除 10 行 [ 10cj ]
#. u: 复原前一个动作
#. Ctrl+r: 重做上一个动作
#. .: 不要怀疑！这就是小数点！意思是重复前一个动作的意思. 如果你想要重复删除、重复贴上等等动作, 按下小数点就好了

#. ma: 在该行打上标记  a
#. 'a: 移动到标记a处
#. 'A: 用大写打标记不会因为退出而更改
#. '': 两次单引号, 跳转到光标上次所在位置
#. ctrl + o: 跳转到光标早些时候的位置 
#. n==: 处理代码不对齐不缩进的情况
#. esc + q : 处理recording @w




- insert模式

#. 进入输入模式 (Insert mode): 
    
    i: 从目前光标所在处输入,  I: 在目前所在行的第一个非空格符处开始输入
    
    a: 从目前光标所在的下一个字符处开始输入,  A: 从光标所在行的最后一个字符处开始输入
    
    o: 在目前光标所在的下一行处输入新的一行, O: 在目前光标所在的上一行处输入新的一行

#. Esc: 退出编辑模式, 回到一般模式中 (常用)



- 底行模式

#. :w	将编辑的数据写入硬盘档案中
#. :w!	若文件属性为<只读>时, 强制写入该档案
#. :q	离开 vim
#. :q!	若曾修改过档案, 又不想储存, 使用 ! 为强制离开不储存档案
#. :wq	储存后离开, 若为 :wq! 则为强制储存后离开 (常用)
#. ZZ	如果修改过, 保存当前文件, 然后退出！效果等同于(保存并退出)
#. ZQ	不保存, 强制退出.效果等同于 :q!
#. :w [filename]: 将编辑的数据储存成另一个档案 (类似另存新档)
#. :r [filename]: 在编辑的数据中, 读入另一个档案的数据.亦即将 [filename] 这个档案内容加到游标所在行后面
#. :n1,n2 w [filename]: 将 n1 到 n2 的内容储存成 filename 这个档案.
#. :! [command]: 暂时离开 vi 到指令行模式下执行 command 的显示结果！例如
#. :! ls /home: 即可在 vi 当中察看 /home 底下以 ls 输出的档案信息






Git 
===============================

Git 初始化
-------------------------------

安装 git

.. code-block:: bash

    sudo apt-get install git

创建目录并进入目录

.. code-block:: bash

    mkdir [directory]
    cd [directory]

初始化 git

.. code-block:: bash

    git init

创建 README, 并放入暂存区

.. code-block:: bash

    touch README.md
    git add [file]

提交文件到仓库

.. code-block:: bash

    git commit -am [message]

建立与 github/gitee/gitlab 的连接

    - 在 git 的主目录下输入, 并一直回车
    
    .. code-block:: bash

        ssh-keygen -t rsa -C "email@example.com"

查看公钥 

.. code-block:: bash

    cat ~/.ssh/id_rsa.pub


git 命令
-------------------------------

查看分支

.. code-block:: bash

    git branch

创建分支

.. code-block:: bash 

    git branch [name] 

切换分支

.. code-block:: bash 

    git checkout [name]

创建+切换分支

.. code-block:: bash 

    git checkout -b [name] 

合并某分支到当前分支

.. code-block:: bash 

    git merge --no-ff [name]

删除分支

.. code-block:: bash 

    git branch -d [name]

分支推送

.. code-block:: bash 

    git push origin [branchname]

查看修改的内容

.. code-block:: bash 
    
    git diff

推送标签至远程

.. code-block:: bash 
    
    git push origin [name]

克隆远程仓库到新文件夹

.. code-block:: bash 
    
    git clone [repository] [new directory]

更改命令名

.. code-block:: bash 
    
    git config --global alias.[co checkout]

不跟踪文件

.. code-block:: bash 
    
    git rm -r --cached [filename]

版本回退

.. code-block:: bash 
    
    git reset --hard [id]

git clone 远程仓库时重命名本地文件夹

.. code-block:: bash 
    
    git clone [http:]  [dirname]

git 将一个分支的文件夹移动到当前分支

.. code-block:: bash 
    
    git checkout 来源分支 -- 文件路径

git 比较两个分支的某个文件异同

.. code-block:: bash 
    
    git diff branch1 branch2 [path-to-file]

git stash 回退: 

.. code-block:: bash 
    
    git stash list
    git stash apply stash@{id}


新仓库: 

.. code-block:: bash 

    git init
    git add [filename]
    git commit -am 'xx'
    git remote add origin [repository-address]
    git push -u origin master

    # fatal: 'main' does not appear to be a git repository
    git remote -v #查看远程信息
    git remote remove main 
    git remote add origin [repository-address]
    git push -u origin master





Shell
====================================================

文件(夹)添加权限:

.. code-block:: bash
    
    # 查看权限
    ls -l [文件名] 
    # u (用户), g (组), o (其他人), a (所有人)
    # + (添加权限)，- (移除权限)，= (设置为指定权限)
    # r (读)，w (写)，x (执行)
    # 执行权限
    chmod +x [文件名]
    # 将其他人的权限设置为只读
    chmod o=r filename   

统计当前目录下文件数量: 

.. code-block:: bash

    ls -l |grep "^-" |wc -l

分割字符串: <https://blog.csdn.net/bandaoyu/article/details/120659630>

`if` 与 `[` 必须隔开:

.. code-block:: bash

    if [command]
    then
    ...
    elif []
    then
    ....
    else
    fi

if else 结构

.. code-block:: bash

    if [ condition ]; then
        [command1]
    else
        [command2]
    fi

if...elif...else 结构

.. code-block:: bash

    if [ condition1 ]; then
        [command1]
    elif [ condition2 ]; then
        [command2]
    else
        [command3]
    fi

for 结构

.. code-block:: bash

    for ((i=1;i<10;i++))
    do
    ...
    done







AWK
===============================


内置变量: 

    - FILENAME: 文件名

    - NF: 列数

    - NR: 行数

    - -F: 设置分隔符

使用变量: 

.. code-block:: bash

    ${varname}

if 语句

.. code-block:: bash

  if(condition)
  {
    ...
  }

  

awk 字符串转数字: 只需要将变量通过”+”连接运算.自动强制将字符串转为整型.非数字变成0, 发现第一个非数字字符, 后面自动忽略.

.. code-block:: bash

    awk 'BEGIN{a="a";b="b";print (a+b+0);}'	



awk 使用外部变量: 

.. code-block:: bash

    awk -v typenode="name" -f read-dnndp.awk networks/nsf2.nd

集群检查 collection 输出: 

.. code-block:: bash

    awk '/column/{print FILENAME}' *


分隔指定字符串

.. code-block:: bash

    echo "8_sf.out" | awk -F '.' '{split($1,a,"_"); print a[1],a[2]}'


最大值, 平均值

.. code-block:: bash

    awk 'BEGIN{ max = 0} {if ($1 > max) max = $1;} END{printf max}'

字符串拼接: 用空格隔开, awk 自动拼接字符串, 输出为 "abc"

.. code-block:: bash

    "a" "b" "c" 


处理多个文件

- ARGIND # 当前被处理参数标志
    
.. code-block:: bash
    
    awk 'ARGIND==1{...}ARGIND==2{...}ARGIND==3{...}... ' [file1] [file2] [file3] ...

- ARGV # 命令行参数数组

.. code-block:: bash 
    
    awk 'FILENAME==ARGV[1]{...}FILENAME==ARGV[2]{...}FILENAME==ARGV[3]{...}...' [file1] [file2] [file3] ...




CMIP
===============================

Gitlab 账号密码

.. code-block:: bash 

    账号: xiaozhou1
    密码: xiao@2023

服务器账号密码 

.. code-block:: bash 
    
    scp -r xiaozhou@159.226.92.26:/home/xiaozhou/
    xz@2021

编译

.. code-block:: bash 
    
    make clean
    make -j
    make test

debug

.. code-block:: bash

    make ver=debug -j
    ./val ./bin/cmip_debug -f check/instances/testeasy/p0548.mps
    vim ./valgrind_report.log

debugsol

.. code-block:: bash 

    ./bin/cmip_debug -f [check/instances/testeasy/p0548.mps] -s check/solution sol.sol

检查解得结果

.. code-block:: bash
    
    ./check/checker/bin/solchecker ~/cmipwork/check/instances/collection/app2-1.mps.gz sol.sol

检查内存泄漏

.. code-block:: bash 
    
    ./val ./bin/cmip -f [check/instances/testeasy/p0548.mps]

单个例子测试

.. code-block:: bash 	
    
    ./bin/cmip -f check/instances/testeasy/misc03.mps # (-t 可以用来生成预处理后的文件)
    ./bin/cmip -f ~/cmipwork/check/instances/collection/[file]

单个例子带控制方法

.. code-block:: bash
    
    ./bin/cmip -f check/instances/testeasy/atm_5_10_1.mps -set NoTwoRow.set

    #Example:NoTwoRow.set 中控制方法使用:
    presolve/isOpen_DetectReduntancy  0
    presolve/isOpen_KnapsackScale  0

测试库测试

.. code-block:: bash

    make testcluster TEST=[测试库] TIME=7200 OUTFILE=[文件夹] SETTING=[设置文件] 

    make ver=opt testcluster TEST=collection TIME=300 OUTFILE=CMIPTEST SETTING=CMIPdefault.set # 示例

集群测试

.. code-block:: bash
    
    make ver=opt testcluster TEST=[time60] TIME=100 OUTFILE=gubtime60-sec

    make ver=release testcluster TEST=[] OUTFILE=[] SETTING=[].set TIME=7200 SEEDFILE=default MPICORE=360

CPLEX 测试提交 (在 cmipwork/check 目录下提交)

.. code-block:: bash

    #在 check/bin 下执行 
    ln -s [path/to/cplex]

    make ver=release testcluster SOLVER=cplex TEST=gubbenchmark TIME=7200 SETTING=offgub.prm OUTFILE=cplexoffgub SEEDFILE=default MPICORE=108

    bsub -J rocI-4-11 -q batch -R "span[ptile=2]" -n 2 -e cplexgubtest/rocI-4-11.mps.gz.err -o cplexgubtest/rocI-4-11.mps.gz.out "cplex -c read /share/data/collection/rocI-4-11.mps.gz read cplex.prm opt "

    #对应的提交设置文件
    scripts/cplex_run 

SCIP 测试提交 (在 cmipwork/check 目录下提交)	

.. code-block:: bash
    
    #在 check/bin 下执行 
    ln -s ~/scipoptsuite-8.0.0/bin/scip 
    #在 cmipwork/check 下
    make ver=release testcluster SOLVER=scip BIN=scip TEST= SETTING=.set OUTFILE= MPICORE=360 TIME=7200 SEEDFILE=default

跑遍 collection 测试集

.. code-block:: bash
    
    make ver=opt testcluster TEST=collection TIME=600 OUTFILE=[parallelcols]
    make ver=opt testcluster TEST=[mergevar] TIME=7200 OUTFILE=[onParallelCol]
    make ver=opt testcluster TEST=[mergevar] TIME=7200 OUTFILE=[offParallelCol] SETTING=[ParallelCols.set]

CMIP 中 result_compare.awk 使用

.. code-block:: bash

    awk -f result_compare.awk [./TEST1/time600.res] [./TEST2/time600.res]


在 results 目录下执行

.. code-block:: bash
   
    awk -f parse_cmip_check.awk OUTFILE/*.out  #会统计预处理、启发式、割平面耗时的算例

比较开关平行列的结果

.. code-block:: bash
    
    awk -f result_compare.awk ./onParallelCol/mergevar.cmip.1threads.7200s.res ./offParallelCol/mergevar.cmip.1threads.7200s.res

    awk -f result_compare.awk ./benchmark-ongub/benchmark_cmip.cmip.1threads.7200s.res ./benchmark-offgub/benchmark_cmip.cmip.1threads.7200s.res

替换成 TEST 可读形式

.. code-block:: bash
    
    :%s/collection\./..\/..\/..\/cmipwork\/check\/instances\/collection\//g
    
    :%s/0\.cmip\.1threads\.600s\.out/mps\.gz/g

集群检查 collection 输出

.. code-block:: bash
    
    # shell
    awk '/ParallelColumns/{print FILENAME}' * > effectConsPara
    awk '/M_/{print FILENAME}' * > effectMergevar
    awk '/DiffObj/{print FILENAME}' * > effectDiffobj
    awk '/Parallel But Not Merge/{print FILENAME}' * > effectNotmerge

去掉重复的行

.. code-block:: bash

    #shell
    awk '!a[$0]++' effectConsPara > ConsPara
    awk '!a[$0]++' effectMergevar > Mergevar
    awk '!a[$0]++' effectDiffobj > Diffobj
    awk '!a[$0]++' effectNotmerge > Notmerge

各部分 awk 位于

.. code-block:: bash
    
    cmipwork/check/scripts


错误: 
*./bin/cmip: error while loading shared libraries: libClp.so.1: cannot open shared object file: No such file or directory* 

.. code-block:: bash 
    
    cp -r cmipwork/interface xz/cmipwork/

更新 ctags

.. code-block:: bash 
    
    ctags -R

g++ 或 make 编译不成功: 
*g++: fatal error: Killed signal terminated program cc1plus compilation terminated.*

**法1:**

.. code-block:: bash 
    
    # 先删除原先分区
    sudo swapoff /var/cache/swap/swap0
    sudo rm /var/cache/swap/swap0
    # 设置分区的大小
    # bs=64M是块大小, count=64是块数量, 所以swap空间大小是bs*count=4096MB=4GB
    sudo dd if=/dev/zero of=/var/cache/swap/swap0 bs=64M count=64
    # 设置该目录权限
    sudo chmod 0600 /var/cache/swap/swap0
    # 创建SWAP文件
    sudo mkswap /var/cache/swap/swap0
    # 激活SWAP文件
    sudo swapon /var/cache/swap/swap0
    # 查看SWAP信息是否正确
    sudo swapon -s

**法2**

.. code-block:: bash 

    sudo dd if=/dev/zero of=/swapfile bs=1G count=6
    # count的大小就是增加的swap空间的大小, 1G是块大小为1G, 所以空间大小是bs*count=6G
    sudo mkswap /swapfile
    # 把刚才空间格式化成swap格式
    su
    chmod 0600 /swapfile
    sudo swapon /swapfile
    # 使用刚才创建的swap空间





大集群
===============================

大集群 IP 为 10.4.3.17

.. code-block:: bash 
    
    suzhaogang
    SuZhaoGang@2021

    ythu
    yutinghu@1578

    diaoruoyu
    LyTo&Mjy5J

    zhangyuhang
    1r0i@1maQV








小集群
===============================

小集群 IP 为: 10.1.20.53

外网请使用 vpn: <https://159.226.47.20/>

小集群账号:

.. code-block:: bash

    team_daiyuhong

小集群密码:

.. code-block:: bash

    dyh@lsec.0621

[新] 小集群 VPN 登录方式: https://amssvpn.amss.ac.cn/

登录时选择登录方式为 "本地密码认证", 然后输入用户名及密码

小集群账号:

.. code-block:: bash

    team_daiyuhong

小集群密码:

.. code-block:: bash

    Dyh@lsec.0722

.. code-block:: bash
    
    xiaozhou
    xz2022

    lvwei
    h#Z79DnjdC

    yuchengyang
    $8yMgyQ13x

    liuyachen
    rcTWd9^Se1

小集群配置

.. code-block:: bash

    x86_64 架构
    具有 52 个 CPU 核心
    每个核心有 1 个线程
    Intel Xeon Gold 6230R 处理器
    主频为 2.10GHz
    内存为 250 G







CPLEX
===============================

CPLEX 执行命令

.. code-block:: bash
    
    cplex -c read [instance].lp opt
    cplex -c read [instance].lp opt wr [instance].sol
    cplex -c read [instance].lp set mip tol mipgap 0 opt wr [instance].sol
    cplex -c read [instance].lp set mip tol mipgap 0 set timelim 3 opt

设置参数: 
<https://www.ibm.com/docs/en/icos/12.10.0?topic=s-cpxxsetintparam-cpxsetintparam>

Julia 安装 CPLEX 

.. code-block:: bash 

    # version 20.1.0
    ENV["CPLEX_STUDIO_BINARIES"] = "/share/home/suzhaogang/xiaozhou/CPLEX/cplex/bin/x86-64_linux/"

    # version 22.1.0
    ENV["CPLEX_STUDIO_BINARIES"] = "/share/home/suzhaogang/tools/cplex2210/cplex/bin/x86-64_linux/"

    import Pkg
    Pkg.add("CPLEX")
    Pkg.build("CPLEX")






Polymake
===============================


读顶点 (第一项规定必须为1)

.. code-block:: bash
    
    open(INPUT,"<","[Fea].poly");$matrix=new Matrix<Rational>(<INPUT>); print $matrix;$p=new Polytope<Rational>(POINTS=>$matrix);print_constraints($p); print($p->FACETS);

读所有约束: 

.. code-block:: bash
    
    open(INPUT1,"<","Ine.txt");open(INPUT2,"<","Aeq.txt");$Ine=new Matrix<Rational>(<INPUT1>);$Aeq=new Matrix<Rational>(<INPUT2>); print $Ine;print $Aeq;$p=new Polytope<Rational>(INEQUALITIES=>$Ine,EQUATIONS=>$Aeq);

读 lp 文件

.. code-block:: bash
    
    $f=lp2poly('conv.lp');$p = new Polytope<Rational>($f);$s=new Polytope(POINTS=>$p->LATTICE_POINTS, COORDINATE_LABELS=>$p->COORDINATE_LABELS);print_constraints($s);

求无界多面体 

.. code-block:: bash
    
    # 注意$pin->DIM+1 维数, 要等于变量数+1
    $f = lp2poly('example.lp');$pin = new Polytope<Rational>($f);$rays = $pin->VERTICES->minor($pin->FAR_FACE, All);$zero = unit_vector<Rational>($pin->DIM + 1, 0);$B = new Polytope<Rational>(POINTS=>$zero);

    foreach my $r (@$rays) { $M = new Matrix<Rational>(primitive($r));$M->[0]->[0] = 1;$M = $M / $zero;$ptemp = new Polytope<Rational>(POINTS=>$M);$B = minkowski_sum($B, $ptemp); }

    $Qpoints = $pin->VERTICES->minor($pin->BOUNDED_VERTICES, All);$Q = new Polytope<Rational>(POINTS=>$Qpoints);$p = minkowski_sum($Q, $B);

    $latticemat = new Matrix<Rational>($p->LATTICE_POINTS);$newpoints = new Matrix<Rational>($latticemat / $rays);$q = new Polytope(POINTS=>$newpoints, COORDINATE_LABELS=>$pin->COORDINATE_LABELS);print_constraints($q);


读取文件

.. code-block:: bash
    
    load_data("facet.txt");


利用 julia 扩展包 **Polymake.jl**






MATLAB
=====================================

整体缩进 

.. code-block:: bash
    
    ctrl + i

命令行

.. code-block:: bash
    
    sum(sum(Aeq*X'~=0))
    sum(sum(A*X'>1))


只保留矩阵第一列的数据

.. code-block:: bash
    
    FA (:,1)=[];

去掉矩阵中的全 0 行

.. code-block:: bash
    
    a(all(a==0,2),:) = [];

去掉矩阵中的全 0 列

.. code-block:: bash
    
    a(:,all(a==0,1)) = [];

找出矩阵的全零行

.. code-block:: bash
    
    find(all(A==0,2))

从数组中随机挑选 n 个数

.. code-block:: bash
    
    A(randperm(numel(A),5))






Excel
======================================

按照已知的顺序排列

.. code-block:: bash
    
    =VLOOKUP(D1,A:B,2,0)











Linux
=============================

在原文件后面新添内容

.. code-block:: bash
    
    ls ./* >> file

把目录下的所有文件放入同一个文件内

.. code-block:: bash
    
    ls * > file

查找文件

.. code-block:: bash
    
    find -name 'filename'
    
    locate filename

查找文件夹

.. code-block:: bash
    
    find . -type d -iname "***"






VS code
===============================

vscode + latex + 语法错误检查: **TeX 插件**

VS code 设置背景为黑色:

.. code-block:: bash
    
    "workbench.colorCustomizations": {
        "editor.background": "#000000"
    }

解决 vscode 已配置 ssh 但仍需输密码: 

.. code-block:: bash
    
    cd .ssh
    chmod 700 ../
    chmod 700 .
    chmod 600 authorized_keys

    chmod g-w authorized_keys

   [(11条消息) SSH配置公钥后仍需要输入密码问题解析_ghimi的博客-CSDN博客_为什么配置了ssh还要输入密码](https://blog.csdn.net/qq_19922839/article/details/117488663)
   [(11条消息) SSH免密登录配置后还是需要密码的问题解决_L_学无止境的博客-CSDN博客_ssh免密设置后仍然需要密码](https://blog.csdn.net/u011489186/article/details/111469786)

   






Gurobi
===============================

grbgetkey 80b3d968-a5e1-11ec-a5de-0242c0a81004

linux 安装 gurobi: <https://zhuanlan.zhihu.com/p/79524375>

问题: 
*LoadError: Gurobi Error 10009: No Gurobi license found*

.. code-block:: bash

    gurobi 官网申请 license
    官网-> Academic-> request a license
    在 bin 目录下执行 获取的license


问题:
*LoadError: Gurobi Error 10009: HostID mismatch (licensed to 5d3d09d7, hostid is 5dcc7d5c)*

.. code-block:: bash
    
    # 原因: 
    Licence Manage hostid (lmhostid)

    #命令行执行
    ifconfig
    # eth0 中找到 ether, 核对后面的地址与“5dcc7d5c”是否一致
    #若一致, 则更改mac地址 
    sudo ip link set dev eth0 down
    sudo ip link set dev eth0 address 00:15:5d:3d:09:d7 # or any address, which will be fixed. 保持与license中的id一致
    sudo ip link set dev eth0 up
    #参考: <https://github.com/microsoft/WSL/issues/5352>


Gurobi 需要生成新的 libgurobi_c++.a 才能有完整的接口功能 API (Application Programming Interface)[应用程序接口]


.. code-block:: bash

    # 重新编译c++库, 并替换旧的库, 以解决任何 ABI (Application Binary Interface) [应用程序二进制接口] 不兼容的问题, 步骤如下: 

    cd gurobi950/linux64/src/build
    make
    cp libgurobi_c++.a ../../lib/






SCIP
===============================

SCIP 添加新求解问题目录: 

.. code-block:: bash
    
    在目录 ~/SCIP/scipoptsuite-8.0.0/scip/examples/ 下新建求解问题目录: 如 ABC
    将 CMakeList.txt Makefile src 放到目录 ABC 下
    在 ~/SCIP/scipoptsuite-8.0.0/scip/examples/ 的 CMakeList.txt 中添加 ABC
    转到目录 ~/SCIP/scipoptsuite-8.0.0/build 后执行 cmake .. 和 make -j
    在 ~/SCIP/scipoptsuite-8.0.0/build/scip/examples/ 下会自动出现目录ABC

 
SCIP 添加 debug 目录

.. code-block:: bash
    
    cd ~/SCIP/scipoptsuite-8.0.0/
    scp -r ./build/ ./debug
    cd debug
    # (optional) cmake . -DREADLINE=off -DIPOPT=off -DZIMPL=off -DGCG=off -DCMAKE_BUILD_TYPE=Debug -DNOBLKBUFMEM=off -DDEBUGSOL=on
    cmake -DNOBLKBUFMEM=off ..


SCIP 进入 debug 模式

.. code-block:: bash
    
    cmake -DCMAKE_BUILD_TYPE=Debug .. -DNOBLKBUFMEM=off


SCIP 进入 release 模式

.. code-block:: bash
    
    cmake -DCMAKE_BUILD_TYPE=Release .
    # (optional) cmake . -DREADLINE=off -DIPOPT=off -DZIMPL=off -DGCG=off -DCMAKE_BUILD_TYPE=Release -DNOBLKBUFMEM=off -DDEBUGSOL=off

SCIP debug solution 步骤

.. code-block:: bash
    
    根据生成的执行文件进入交互模式 -> read -> 传入数据文件路径 -> opt -> write -> sol -> right.sol (正确解文件)
    debug 模式下: cmake .. -DDEBUGSOL=on (off)  
    打开错误问题的设置(如: propagator等)
    在对应的目录下 make -j
    根据生成的执行文件进入交互模式 -> set -> misc -> debugsol -> right.sol -> read -> 传入数据文件路径 -> opt (后续会显示冲突) 


SCIP 将文件移至 debug 目录下

.. code-block:: bash
    
    scp -r <> /home/xiaozhou/SCIP/scipoptsuite-8.0.0/debug/scip/examples/unsplit/
    mv <> /home/xiaozhou/SCIP/scipoptsuite-8.0.0/debug/scip/examples/unsplit/


SCIP 输出预处理后的文件步骤

.. code-block:: bash
    
    进入交互模式  ->  read (输入数据文件)  -> presolve -> write -> transproblem (文件名)



SCIP 参数

- 设置关闭割平面

.. code-block:: bash
    
    关掉所有: set/separating/emphasis off 

    关掉割平面: set -> separating -> <cutname> -> freq : -1
    #例如关闭背包割: set -> separating -> knapsackcover -> freq : -1
    #设置完成提示:  separating/knapsackcover/freq = -1


- 设置只求到根节点

.. code-block:: bash
    
    set -> limits -> totalnodes : 1
    #设置完成提示:  limits/totalnodes = 1


- 将设置的参数写入文件

.. code-block:: bash
    
    set -> diffsave -> <filename>.set


- 关闭预处理

.. code-block:: bash
    
    set -> presolving -> maxrounds : 0




安装流程: <https://www.scipopt.org/doc-7.0.3/html/INSTALL_8md_source.php>

- 报错: Could NOT find Readline (missing: Readline_INCLUDE_DIR Readline_LIBRARY)

.. code-block:: bash
    
    sudo apt-get install libreadline-dev

- 报错: Could NOT find IPOPT (missing: IPOPT_LIBRARIES) (Required is at least version "3.12.0")

.. code-block:: bash

    # 参考以下链接
    https://github.com/coin-or/Ipopt
    https://coin-or.github.io/Ipopt/INSTALL.html

- 报错: Provided package HSL is not working or does not contain MA27

.. code-block:: bash
    
    # 需要下载 HSL 包
    make 
    make check

- 报错: Exception message: libhsl.so: cannot open shared object file: No such file or directory

.. code-block:: bash
    
    # 链接: 
    https://blog.csdn.net/weixin_42268975/article/details/107708414

    make install


Julia 安装 SCIP

.. code-block:: bash
    
    tar xvzf scipoptsuite-8.0.0.tgz
    cd scipoptsuite-8.0.0
    mkdir build 
    cd build
    cmake ..


报错: Assertion 'chkmem->lazyfreesize == 0' failed.

.. code-block:: bash
    
    将 SCIPallocBlockMemory 换成 SCIPallocBuffer
    不要在 debug 检查内存时打开 debugsol 

报错: assert (getNusedMemory->Buffer == 0) failed

.. code-block:: bash
    
    Buffer 改为 BlockMemory

报错:
corrupted size vs. prev_size 
realloc(): invalid next size:
malloc(): memory corruption
malloc(): smallbin double linked list corrupted
segment fault
free(): corrupted unsorted chunks
malloc(): memory corruption (fast)

.. code-block:: bash

    # 以上错误大概率由<数组越界>引起, 参考链接:
    https://rushanshi.blog.csdn.net/article/details/122479455




报错: 链接的g++版本不对

.. code-block:: bash
    
    # 参考链接: https://blog.csdn.net/fpcc/article/details/102664881
    命令行设置 export CXX=/usr/bin/g++ 或 export CXX=/usr/local/bin/g++




警告: constraint handler <...> cannot print requested format

.. code-block:: bash

    # 参考链接: http://listserv.zib.de/pipermail/scip/2016-April/002794.html
    This happens because you are trying to write your problem into a format that does not necessarily supports the type of constraints your constraint handler generates.






GCC
===============================

../configure --prefix=/usr/local/gcc-10.2.0/ --enable-checking=release --enable-languages=c,c++ --disable-multilib 

编译报错

- undefined reference to 'MCFDRReadData(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)' collect2: error: ld returned 1 exit status

.. code-block:: bash

    执行命令加上 -D_GLIBCXX_USE_CXX11_ABI=0

- undefined reference to 'MCFDRReadData(std::string, std::string)' collect2: error: ld returned 1 exit status


- c++17 须使用 g++10.0.0 以上版本编译

.. code-block:: bash
    
    升级g++: https://code.bytecho.net/d/152

- undefined reference to xxx

.. code-block:: bash 

    原因是构造函数后面要加 “= default();”











C++
===============================


编译报错: "vector"does not name a type

.. code-block:: bash 
    
    #include <vector>
    using std::vector






Xshell
===============================

xftp 传输文件出错 :  磁盘内存不够, du -sh * 查看内存空间, 删除内存大的文件 (如core)







CMake
===============================

CMake Error in CMakeLists.txt: Target "runMCFDR" requires the language dialect "CXX17" (with compiler extensions), but CMake does not know the compile flags to use to enable it.

.. code-block:: bash 
    
    编译时用 cmake .. -DCMAKE_CXX_COMPILER=/usr/bin/g++ 


Debug 模式

.. code-block:: bash 
    
    -DCMAKE_BUILD_TYPE=Debug






Julia
===============================

Julia 与 JuMP

.. code-block:: bash

    # julia 官网
    https://julialang.org

    # JuMP 官网
    https://jump.dev/JuMP.jl/stable/

    # 在 Linux 上安装 Julia
    wget https://julialang-s3.julialang.org/bin/linux/x64/1.11/julia-1.11.7-linux-x86_64.tar.gz
    tar zxvf julia-1.11.7-linux-x86_64.tar.gz

    # 不同操作系统的安装详见:
    https://julialang.org/downloads/platform/ 



julia 安装 cplex

.. code-block:: bash

    ENV["CPLEX_STUDIO_BINARIES"] = "/Applications/CPLEX_Studio221/cplex/bin/x86-64_osx/"
    import Pkg
    Pkg.add("CPLEX")
    Pkg.build("CPLEX")


Mac julia 安装 cplex 报错: ERROR: LoadError: Unable to install CPLEX.jl.

.. code-block:: bash
    
    # 解决方案: 
    https://discourse.julialang.org/t/problem-installing-cplex-jl-with-cplex-22-1-1-on-mac-os/111967/10


.. note::
    julia 建模不要用等式, 数值问题太多！！







Python
===============================

不输出warning 内容

.. code-block:: python
    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)






MySQL
===============================

安装 MySQL 软件:

下载 MySQL Server: <https://dev.mysql.com/downloads/mysql/>
下载 MySQL Workbench: <https://dev.mysql.com/downloads/workbench/>


在 MySQL Workbench 中, 可以通过以下步骤创建数据库并将 paparams.sql 文件导入到该数据库中:

**步骤 1: 打开 MySQL Workbench 并连接到 MySQL 服务器**

- 点击主界面上的一个连接, 输入您的用户名和密码, 登录到 MySQL 服务器.

**步骤 2: 创建一个新数据库**

- 在顶部工具栏, 点击 *File -> New Query Tab*, 打开一个新的 SQL 查询窗口.

- 在查询窗口中输入以下 SQL 语句来创建一个新的数据库 (例如, 命名为 my_database), 并运行该命令

.. code-block:: bash

    CREATE DATABASE my_database;

- 点击窗口上方的 **闪电图标(Execute)** 按钮, 执行上述语句

- 刷新数据库列表: 在左侧的 *SCHEMAS* 面板中, 右键点击空白处, 然后选择 *Refresh All*

**步骤 3: 将 paparams.sql 文件导入到数据库中**

- 选择目标数据库: 在左侧 *SCHEMAS* 面板中, 右键点击您刚创建的数据库 my_database, 然后选择 *Set as Default Schema*.

- 开始导入文件: 点击菜单栏上的 *Server -> Data Import*

- 设置导入选项: 在导入窗口中, 选择 *Import from Self-Contained File*

- 点击右侧的文件选择按钮, 找到您的 paparams.sql 文件.

- 选择目标数据库: 在 *Default Target Schema* 下拉框中选择 my_database

- 执行导入: 点击右下角的 *Start Import* 按钮, MySQL Workbench 会开始导入 paparams.sql 文件中的数据

- 验证导入是否成功: 导入完成后, 您可以刷新 *SCHEMAS* 面板, 然后展开 my_database, 查看导入的表和数据是否正确