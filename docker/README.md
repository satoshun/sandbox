# Docker


## Mysql

https://github.com/satoshun/docker-mysql

```
$ docker pull satoshun/mysql

# run mysqld_safe
$ docker run -d --name mysql -v /var/lib/mysql:/var/lib/mysql satoshun/mysql

# connect mysql server
$ docker run -it --rm --link mysql:mysql satoshun/mysql bash -c 'mysql -h $MYSQL_PORT_3306_TCP_ADDR'
or
$ docker run -it --rm --link mysql:mysql satoshun/mysql bash -c 'mysql -h mysql'
```


## Ghost

https://github.com/satoshun/docker-ghost

```
$ docker pull satoshun/ghost

# run ghost
$ docker run -d --name blog -p 2368:2368 --link mysql:db satoshun/ghost
```


## nginx

```shell
$ docker pull dockerfile/nginx

# run nginx
$ docker run -d --name nginx -p 80:80 -p 443:443 --link blog:blog -v /home/core/nginx/conf.d/:/etc/nginx/conf.d/:ro dockerfile/nginx
```
