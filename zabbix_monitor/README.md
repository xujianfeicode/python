#### 概述
监控consul中的服务状态

#### 使用
安装python-consul
```
$ sudo pip install python-consul
```

获取服务列表
```
$ consul_monitor.py--list
```

获取服务状态
```
$ consul_monitor.py -s SERVICE_NAME
```
正常返回0，有服务存在异常返回1


#### 集成zabbix
使用zabbix low level discovery,自动发现生成监控和报警项