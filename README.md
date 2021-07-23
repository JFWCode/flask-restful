# Api Server

### Quick  start

1. 获取镜像

   将api-server.tar拷贝到本地

   导入镜像

   ​	docker loads < api-server.tar

2. 启动容器

   1. 修改docker-compose.yml配置

      没有变动可以直接使用默认配置

      ```
      # 数据库所用ip
      DATABASE_HOST
      # 数据库所用端口
      DATABASE_PORT
      ```

   2. su，切换到root用户

   3. 启动

      ```
      docker-compose up -d
      ```

3. 开启防火墙

   ```shell
   firewall-cmd --zone=public --add-port=5000/tcp --permanent
   firewall-cmd --reload
   ```

   

4. 访问接口

   1. 获取某个case_run_id的bug信息

      ```shell
      curl -X GET http://127.0.0.1:5000/api/v0.1/bugs\?case_run_id\=11500991
      ```

