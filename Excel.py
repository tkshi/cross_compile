import xlwt
rows = [
['a','b','c','error'],
['a1','b1','c1',],
['a2','b2','c2','error']
]


def getSheet(fileName="test.xlsx",sheetName="Accounts"):
	import xlrd
	 
	book = xlrd.open_workbook(fileName)
	 

	sheet = book.sheet_by_index(0)
	 

	result = []

	for i in range(sheet.nrows):
		row = sheet.row(i)
		_row = []
		for cell in row:
			_row.append(cell.value)
		result.append(_row)

	return result

def writeSheet(fileName="sample.xls",sheetName="Accounts",rows=rows):
	book = xlwt.Workbook()
	newSheet_1 = book.add_sheet(sheetName)

	for row_i,row in enumerate(rows):
		if 'error' in row:
			xlwt.add_palette_colour("custom_colour", 0x21)
			book.set_colour_RGB(0x21, 251, 228, 228)
			style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
		else:
			style = False
		for i,cell in enumerate(row):
			if style == False:
				newSheet_1.write(row_i,i,cell)
			else:
				newSheet_1.write(row_i,i,cell,style)
	book.save(fileName)

def setColor(sheetName="Accounts",rows=rows):
	book = xlwt.Workbook()
	sheet1 = book.add_sheet(sheetName)
	xlwt.add_palette_colour("custom_colour", 0x21)
	book.set_colour_RGB(0x21, 251, 228, 228)
	style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
	sheet1.write(0, 0, 'Some text', style)
	book.save('out.xls')

if __name__ == '__main__':
	writeSheet()
