# 用于清理 MySQL 服务器端连接过多的情况
# 参考的是：https://serverfault.com/questions/11357/bulk-or-mass-killing-misbehaving-mysql-queries

mysql> SELECT concat('KILL ',id,';') FROM information_schema.processlist WHERE user='root' INTO OUTFILE '/tmp/a.txt';
mysql> source /tmp/a.txt;

# 其中，where 查询条件是可以替换的，比如换成 host like '192.168.4.1%' 就变成清理该主机发起的所有conn
# 注意 kill 支持 option 选择是 kill 连接还是 kill query，格式如：KILL [CONNECTION | QUERY] processlist_id
# and 上面这个操作需要拥有 FILE 权限
