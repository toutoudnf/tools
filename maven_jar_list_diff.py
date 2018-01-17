# -*- coding: utf-8 -*- 
# author: liruifeng
# 脚本用于比较 pom 修改前后的 jar 变更情况，目前支持：新增 、版本变更、删除的检测
# 需要修改的有：old_jar_list_file_name，new_jar_list_file_name，其中：
# old_jar_list_file_name：旧版本的jar列表信息
# new_jar_list_file_name：新版本的jar列表信息
# jar 列表信息来自于 mvn dependency:list
# 需要把每行的 [INFO] 信息替换掉，最终信息应当如：com.meituan.mtrace:idl-mtrace:jar:1.1.14:compile

old_jar_list_file_name = 'old-jar-list-from-pom.txt'
new_jar_list_file_name = 'new-jar-file-list-from-pom.txt'

new_added_jars = {}
upgrade_jars = {}
remove_jars = {}

def parse_jar_list_file(file_name):
	file_object = open(file_name,'rU')
	jar_and_versions = {}
	try:
		for line in file_object:
			infos = line.split(":")
			jar_and_versions[infos[0] + ":" + infos[1]] = infos[3] + ":" + infos[4][0:-1]
	finally:
		file_object.close()
	return jar_and_versions

def diff_jar_list(old_jar_list, new_jar_list):
	for (jar, old_version) in old_jar_list.items():
		if new_jar_list.get(jar) is None:
			remove_jars[jar] = old_version
		elif old_version != new_jar_list.get(jar):
			upgrade_jars[jar] = old_version + " to " + new_jar_list[jar]

	for (jar, new_version) in new_jar_list.items():
		if old_jar_list.get(jar) is None:
			new_added_jars[jar] = new_version

def print_map(my_map):
	for (key, value) in my_map.items():
		print "jar [%s]，版本情况：[%s]" % (key,value)

def print_diff_result():
	print "************************开始************************"
	print "************************新增的 jar 列表************************"
	print print_map(new_added_jars)
	print "************************版本发生变更的 jar 列表************************"
	print print_map(upgrade_jars)
	print "************************删除的 jar 列表************************"
	print print_map(remove_jars)
	print "************************结束************************"

def diff_pom():
	old_jar_list = parse_jar_list_file(old_jar_list_file_name)
	new_jar_list = parse_jar_list_file(new_jar_list_file_name)
	diff_jar_list(old_jar_list, new_jar_list)
	print_diff_result()


if __name__ == "__main__":
	diff_pom()