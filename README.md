# mysql-table-swapcopy
Atomically copies table data between two databases

Handles foreign key constraints, but the operation of removing/readding
constraints is not atomic, unlike the data swap.

THIS UTILITY WILL NOT COPY TRIGGERS. IF YOU'RE USING TRIGGERS THEY MUST
ALREADY EXIST ON THE DESTINATION SCHEMA

Designed to work under python2 or python3.

Requires: mysqldump and mysql cli tools

```
usage: mysql-table-swapcopy.py [-h] --shost SHOST --dhost DHOST --sschema
                               SSCHEMA --dschema DSCHEMA --suser SUSER --spass
                               SPASS --duser DUSER --dpass DPASS [-m]
                               tablename [tablename ...]

positional arguments:
  tablename            the name of one or more tables to copy

optional arguments:
  -h, --help           show this help message and exit
  --shost SHOST        the mysql source host name
  --dhost DHOST        the mysql destination host name
  --sschema SSCHEMA    the mysql source schema name
  --dschema DSCHEMA    the mysql destination schema name
  --suser SUSER        the username to use for the mysql source
  --spass SPASS        the password to use for the mysql source
  --duser DUSER        the username to use for the mysql destination
  --dpass DPASS        the password to use for the mysql destination
  -m, --version-match  (magento2 only) all schema versions must match for copy
                       to run
```
