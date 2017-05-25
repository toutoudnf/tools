#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: toutoudnf@gmail.com
usage: do publish 1 or more commit to specified server
"""
"""
简单列举下业务：
- 根据commit信息，抓取文件，然后推送
- 难点
    - commit信息包含多个项目怎么办
    - 项目的构建，是分情况的，比如agent+server，发布方式是不同的；通用版本的话，如果项目变了怎么办？
    - 全量的覆盖式发布；或者一次性的发布几个commit，commit的顺序呢，是HEAD~
    - 根据commit的file，设置pattern
    - 本质就两步
        - 找到commit的全部change file
        - 针对文件的project + 文件类型做不同的处理
            - 文件类型
                - properties
                - xml
            - 项目
                - agent
                - common
                - sdk
                - server
                
"""

projects = {'Hans-Common':{'type':'jar', 'remote_path':''},
            'Hans-Server':{'type':'war', 'remote_path':'/usr/local/ics/ics-manager/apache-tomcat-7.0.64/webapps/ROOT/WEB-INF/'},
            'Hans-Agent':{'type':'jar', 'remote_path':'/usr/local/ics/ics-agent/'}} # 记录了发布支持的项目
file_types = ['.properties','.xml','.java'] # 记录了发布脚本支持的文件类型

# 获取指定commit的file change list
def get_file_list(commit_hash):
    # hash不能为空或者None
    # 获取file list如果为空，则返回，不处理；
    change_files = []
    return change_files
def publish_files(change_files):

def __main__():
    change_files = get_file_list()
    if None != change_files and len(change_files) != 0:
        # 有要处理的文件
        publish_files(change_files)
