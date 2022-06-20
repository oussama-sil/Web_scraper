import xlsxwriter

def write_to_excel(file_name,headers,content):
    book=xlsxwriter.Workbook(file_name)
    sheet=book.add_worksheet()
    row = 0
    col = 0
    #writing the headers 
    for hd in headers:
        sheet.write(row,col,hd)
        col +=1
    #writing items 
    row +=1
    for item in content:
        col = 0
        for key in item:
            sheet.write(row,col,item[key])
            col += 1
        row += 1
    book.close()


# headers = ['a','b','c']
# items = [{'a':5,'b':'ff','c':445},{'a':5,'b':'ff','c':445},{'a':5,'b':'ff','c':445},{'a':5,'b':'ff','c':445}]
# write_to_excel('sx.xlsx',headers,items)