from pyautocad import Autocad, APoint #CHÈN THƯ VIỆN AUTOCAD
import pandas as pd #CHÈN THƯ VIỆN PANDAS

#ĐƯỜNG DẪN MỞ FILE EXCEL
duong_dan = r'C:\Users\Vo Phu Toan\Contacts\Desktop\link\cad-excel.xlsx' 
#ĐƯỜNG DẪN SAVE FILE EXCEL
vi_tri_luu = r'C:\Users\Vo Phu Toan\Contacts\Desktop\link\cad-excel_edited.xlsx'

acad = Autocad() 
file_excel = pd.read_excel(duong_dan,sheet_name = 0) #MỞ FILE EXCEL, SHEET1


#VẼ ĐOẠN THẲNG AB
a = APoint(file_excel.loc[0,'X'],file_excel.loc[0,'Y'])
b = APoint(file_excel.loc[1,'X'],file_excel.loc[1,'Y'])
ab = acad.model.AddLine(a,b)
file_excel.loc[1,'CHIỀU DÀI'] = ab.length

#VẼ ĐOẠN THẲNG BC
c = APoint(file_excel.loc[2,'X'],file_excel.loc[2,'Y'])
bc = acad.model.AddLine(b,c)
file_excel.loc[2,'CHIỀU DÀI'] = bc.length

#VẼ ĐOẠN THẲNG CD
d = APoint(file_excel.loc[3,'X'],file_excel.loc[3,'Y'])
cd = acad.model.AddLine(c,d)
file_excel.loc[3,'CHIỀU DÀI'] = cd.length

#VẼ ĐOẠN THẲNG DE
e = APoint(file_excel.loc[4,'X'],file_excel.loc[4,'Y'])
de = acad.model.AddLine(d,e)
file_excel.loc[4,'CHIỀU DÀI'] = de.length

file_excel.to_excel(vi_tri_luu) #LƯU FILE EXCEL


#file_excel.head()





