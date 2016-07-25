#!/usr/bin/env bash

# NOTE: Requires mysql connector for python
# On centos: https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.3-1.el7.x86_64.rpm

if [[ $(uname -a) == *".el7.x86_64"* ]]; then
    rpm -ivh https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.3-1.el7.x86_64.rpm
fi

mkdir -p /opt/slidewave
cp -f mysql-table-swapcopy.py /opt/slidewave
chmod +x /opt/slidewave/mysql-table-swapcopy.py
