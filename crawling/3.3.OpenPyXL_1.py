import openpyxl

#워크북(엑셀파일) 생성
wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = "hello world!"
sheet.cell(row=3, column=3).value = "BYE!!"

subject = ["Python", "Java", "HTML", "JavaScript"]
sheet.append(subject)

wb.save('test.xlsx')
