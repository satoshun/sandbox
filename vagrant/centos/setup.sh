#!/bin/sh

yum update -y

yum install -y \
    bzip2-devel cyrus-sasl-devel libcurl-devel libevent-devel libjpeg libjpeg-devel libpng libpng-devel libxslt-devel make ncurses-devel openssl openssl-devel perl-devel readline-devel rsyslog sqlite-devel tk-devel zlib-devel \
    python-devel python-libs python-passlib python-pip python-setuptools \
    docker-io

chkconfig docker on
yum docker start

pip install fig
