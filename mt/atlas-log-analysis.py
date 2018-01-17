#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 用于分析 atlas 日志，从中统计出连接 db 的机器

import sys
import os
import commands

mechines = {} # store the mechines find in atlas log, key is server ip

def parse_file(file_name):
    with open(file_name, "r") as f:
        while True:
            line_str = f.readline()
            if line_str:
                parse_line(line_str)
            else:
                break
    for ip_str in mechines.keys():
        # print ip_str
        print parse_ip(ip_str)


def parse_line(line_str):
    if line_str.find("C_begin") > 0:
        arr = line_str.split(" ")
        ip = arr[4].split(":")[1]
        if not mechines.has_key(ip):
            mechines[ip] = 1

def parse_ip(ip_str):
    status, output = commands.getstatusoutput("host " + ip_str)
    if status == 0:
        return output
    else:
        print status
        print output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "one param is needed and only one(file name)"
    else:
        parse_file("" + sys.argv[1])
