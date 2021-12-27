#IMPORT THƯ VIỆN
from tkinter.ttk import * #THƯ VIỆN COMBO BOX
from tkinter import * #THƯ VIỆN CỬA SỔ TKINTER
from pyautocad import Autocad #THƯ VIỆN AUTOCAD


#CODE TẠO CỬA SỔ TKINTER
window = Tk()
window.title('DANH SÁCH LAYER')
window.geometry('400x400') 

#CODE TẠO LABEL
lbl = Label(window, text = 'TÊN LAYER', font = ('Times New Roman',14))
lbl.place(x = 20, y = 20)

#CODE TẠO COMBO BOX
a = Autocad()
layer_count = a.doc.Layers.count #ĐẾM SỐ LƯỢNG LAYER
layers_names = [a.doc.Layers.Item(i).Name for i in range(layer_count)] # LẤY TÊN TẤT CẢ LAYER

combo = Combobox(window, font = ('Times New Roman',14), width=20) #THIẾT LẬP HIỂN THỊ COMBO BOX
combo['value'] = layers_names #LIST DANH SÁCH TRONG COMBO BOX
combo.current(0)
combo.place(x = 150, y = 20)


#VÒNG LẶP TKINTER
window.mainloop()
