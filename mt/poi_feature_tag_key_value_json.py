import json
import xlrd

def _load_data():
	_poi_tags = xlrd.open_workbook('poi_tags.xlsx')
	_table = _poi_tags.sheets()[0]
	nrows = _table.nrows
	_field_arr = [];

	_fields = {}
	for i in range(nrows):
		_id = _table.cell(i,0).value
		_fields[_id] = '1'
		_field_arr.append(_id.encode('utf-8'))

	#print "total count:" + str(len(ids))
	#print "total count no distinct:" + str(len(ids_arr))

	#_do_print(_fields)

	print len(_field_arr)
	print _field_arr

def _do_print(data):
	json_data = json.dumps(data)
	print len(json_data)
	print json_data


if __name__ == "__main__":
    _load_data()