
#ES快速上手(5.4.0版本)

## ES安装
 1. 下载并安装较新jdk8
 2. 创建并切到es用户 adduser es && su - es
 下载: [https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.0.tar.gz](https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.0.tar.gz
)
 3. 配置系统参数:
  
    1. vim /etc/security/limits.conf
    
            es - nofile 65536 #按需修改es用户最大打开文件数, 需>= 65536
            es soft memlock unlimited #解除es用户使用内存限制
            es hard memlock unlimited #解除es用户使用内存限制
   
    2. vim /etc/security/limits.d/90-nproc.conf
        
            es    nproc   127979 #如果你的es吞吐量大, 还得修改es用户可以打开的最大线程数, 防止出现最大线程数满, 无法创建本地线程的问题 
    
  
 4. 配置jvm参数(修改 config/jvm.options 文件):
    
        -Xms2g
        -Xmx2g #按需配置内存大小, 如果内存较大可以使用G1gc(建议8G以上必须使用G1), 内存设置建议小于32G(某些jdk版本大于等于32G时会关闭指针压缩, 较为浪费内存) , 由于es的docvalues索引会使用文件缓存, 一般要求服务器要有大于es堆容量的内存冗余供系统文件cache使用
    
        #输出gc日志
        -XX:+PrintGCDetails
        -XX:+PrintGCDateStamps
        -Xloggc:${logdir}/gc.log #配置输出gc日志
    
 5. 按需修改配置文件(demo见 src/main/config目录)   
 启动: 使用es用户, 先kill所有data节点, 再kill所有master节点
 重启: 使用es用户, 先启动所有data节点, 再启动所有master节点(启动命令: 在对应es的bin目录下执行 ./elasticsearch -d) 
 
 
 ## 安全
     
远程服务器可以配置路由表来屏蔽非内网访问, 如需调试, 开发人员可以建立本地ssh端口转发来模拟内网访问
     
    # 首先要安装并启动iptables
        
    chkconfig iptables on  #让iptables开机启动
     
    #屏蔽9xxx端口的访问, 按需配置多条
    iptables -I INPUT -p TCP --dport 9xxx -j DROP
     
    #打开9xxx端口的内网网段(10.x, 172.16.x, 192.168.x)访问
    iptables -I INPUT -s 192.168.100.0/24 -p TCP --dport 9xxx -j ACCEPT
     
    #打开9xxx端口的内网网段localhost访问
    iptables -I INPUT -s localhost -p TCP --dport 9xxx -j ACCEPT
     
    #此时如需用开发机连接对应服务, 可以打开ssh端口转发, 模拟内网访问
    ssh -NTL 9876:localhost:9xxx es@server
     
    #如需删除某行规则, 可以先执行 iptables -nL INPUT --line-numbers , 再执行 ptables -D INPUT n #n为行号, 需要注意执行删除后行号会变, 要得到新的行号, 需要再次执行 iptables -nL INPUT --line-numbers
     
    service iptables save  #将当前iptables配置刷到/etc/sysconfig/iptables
     
 为了方便可以在本地开发机添加如下 ssh config配置(需修改 ~/.ssh/config 文件)
  
     #多条连接共享, 让第二条连接在瞬间就建立好
     ControlMaster auto
     ControlPath /tmp/ssh_mux_%h_%p_%r
     
     #连接保持4个小时，即使在你退出服务器之后，这条连接依然
     可以重用
     ControlPersist 4h
 

## 插件

### cerebro, 集群管理插件(原kopf), 必装
[https://github.com/lmenezes/cerebro](https://github.com/lmenezes/cerebro)

### elasticsearch-sql, 方便数据开发
[https://github.com/NLPchina/elasticsearch-sql](https://github.com/NLPchina/elasticsearch-sql)
sql插件可以

### kibana, 方便开发/数据展示
[下载](https://artifacts.elastic.co/downloads/kibana/kibana-5.4.0-linux-x86_64.tar.gz)
[文档](https://www.elastic.co/guide/en/kibana/current/index.html)

### elasticsearch-analysis-ik, 常用中文分词插件, 可选
[https://github.com/medcl/elasticsearch-analysis-ik](https://github.com/medcl/elasticsearch-analysis-ik)

### elasticsearch-head , 可选
[https://github.com/mobz/elasticsearch-head](https://github.com/mobz/elasticsearch-head)

    git clone git://github.com/mobz/elasticsearch-head.git
    cd elasticsearch-head
    npm install
    npm run start
    open http://localhost:9100/  
    
   head插件很多功能可以用cerebro等插件替代, 建议需要时安装








   









