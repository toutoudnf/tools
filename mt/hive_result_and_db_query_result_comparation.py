#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 用于比对 hive 的查询结果（xls）与 MySQL 的查询结果（csv）是否一致
# 目前实现了的业务逻辑包括：
# - C端商家特征数据比对

import sys
import os
import csv
import json
import xlrd

source_datas = []
source_keys = []
des_datas = {}
des_keys = []
max_diff_count = 10
diff_countttt = 0

def source_load(source_file):
    data = xlrd.open_workbook(source_file)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    for i in range(nrows):
        if i == 0:
            for p in range(ncols):
                source_keys.append(table.cell(i,p).value)
        else:
            source_datas.append([])
            for p in range(ncols):
                if p == 0:
                    source_datas[i - 1].append(str(int(table.cell(i,p).value)))
                else:
                    source_datas[i - 1].append(table.cell(i,p).value)
    print "**************** source loading finish ********************"

def des_load(des_file):
    csvfile = file(des_file, 'rb')
    reader = csv.reader(csvfile, delimiter=';',quotechar='\'')
    for line in reader:
        if reader.line_num == 1:
            continue
        des_datas[line[0]]=json.loads(line[1][1:-1])
    print "**************** des loading finish ********************"

def compare():
    global diff_countttt
    for i in range(len(source_datas)):
        source_data = source_datas[i]
        # print source_data
        poi_id = source_data[0]
        # print poi_id
        des_data = des_datas[poi_id]
        # print des_data
        if not des_data:
            result = check_equals_with_c_poi_features(source_datas[i], des_data)
            if not result:
                diff_countttt = diff_countttt + 1
        else:
            diff_countttt = diff_countttt + 1
        if diff_countttt > max_diff_count:
            break
    print "compare finish!"

def check_equals_with_c_poi_features(source_data, des_data):
    for index in range(len(source_keys)):
        source_value = source_data[index]
        source_key = source_key[index]
        des_value = des_data[source_key]
        if source_value != des_value:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "error params format, params should contains: source_file, des_file"
    else:
        print "start comparing"
        source_file = sys.argv[1] + ""
        des_file = sys.argv[2] + ""
        source_load(source_file)
        des_load(des_file)
        compare()