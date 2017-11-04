#!/usr/bin/python

import sys
import os


def get_method_name(method_name_line):
    return method_name_line[16:-5];


def get_crane_task_name(crane_anno_line):
    return crane_anno_line[12:-3]


def get_crane_infos(file_name):
    crane_file = open(file_name)

    results = []  # store the results

    while 1:
        line = crane_file.readline()
        if not line:
            break
        if "@Crane" in line:
            crane_task_name = get_crane_task_name(line)
            method_line = crane_file.readline()
            if method_line:
                method_name = get_method_name(method_line)
                results.append("method: " + method_name + ", crane: " + crane_task_name)

    if results:
        print "for file %s, there are %d crane jobs:" % (file_name, len(results))
        for result in results:
            print(result)


def get_files(file_or_dir):
    if os.path.isdir(file_or_dir):
        # handle as dir
        for root, sub_dirs, sub_files in os.walk(file_or_dir):
            for sub_file in sub_files:
                get_crane_infos( os.path.join(root, sub_file))
    else:
        # handle as a file
        get_crane_infos(file_or_dir)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "one param is needed and only one(file name)"
    else:
        get_files("" + sys.argv[1])
