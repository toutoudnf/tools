import json
import xlrd

def _fixErrorDataFromXls():
	_error_data = xlrd.open_workbook('error_data.xlsx')
	_table = _error_data.sheets()[1]
	nrows = _table.nrows

	ids = set()
	ids_arr = []
	for i in range(nrows):
		_id = _getIdFromErrorData(_table.cell(i,0).value)
		ids.add(_id)
		ids_arr.append(_id)

	#print "total count:" + str(len(ids))
	#print "total count no distinct:" + str(len(ids_arr))

	_do_print(ids)

def _getIdFromErrorData(_content):
	_content_obj = json.JSONDecoder().decode(_content);
	_data_str = _content_obj['data']
	_id = json.loads(_data_str)['id']
	return _id

def _do_print(ids):
	for id in ids:
		print id

if __name__ == "__main__":
    _fixErrorDataFromXls()