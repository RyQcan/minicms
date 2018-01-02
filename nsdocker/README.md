##### 以下所有命令需要进入`nsdocker`目录执行



##### 配置文件

目录下有两个配置文件 `local_db.yml` 和 `centre_db.yml`，分别对应本地数据库环境和中心数据库环境

使用的时候通过`-f` 参数来指定配置文件

在配置文件里的`servicename`只有两个，`nswiki`和`mysql`

##### 从零构建，构建后自动会开始运行

[]里的是可选参数，如果指定了服务名，则表示只构建并启动指定的服务

```shell
docker-compose -f 选择的配置文件 up -d --build [servicename]
```

##### 停止

[]里的是可选参数，如果指定了服务名，则表示停止指定的服务，否则两个都停止。

使用的时候不要加[]符号

```shell
docker-compose -f 选择的配置文件 stop [servicename]
```

##### 启动已经up过的服务

```shell
docker-compose -f 选择的配置文件 start [servicename]
```

##### 整体销毁

[]里的是可选参数，`-v`表示连同映射的volume一起删除，慎用，会删除本地数据库所存储的volume

```shell
docker-compose -f 选择的配置文件 down [-v]
```

