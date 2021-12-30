#IMPORT THƯ VIỆN
from tkinter.ttk import * #THƯ VIỆN COMBO BOX
from tkinter import * #THƯ VIỆN CỬA SỔ TKINTER
from pyautocad import Autocad #THƯ VIỆN PYAUTOCAD

#CODE TẠO CỬA SỔ TKINTER
window = Tk()
window.title('NEW LAYERS MINI-TOOL')
window.geometry('400x400') 

#CODE TẠO LABEL
lbl = Label(window, text = 'Danh sách layer', font = ('Times New Roman',14))
lbl.place(x = 20, y = 20)
lb2 = Label(window, text = 'Nhập tên layer', font = ('Times New Roman',14))
lb2.place(x = 20, y = 100)

#CODE TẠO ENTRY
txt = Entry(window, width = 15, font = ('Time New Roman', 14))
txt.place(x = 150, y = 100)
txt.focus()

#CODE TẠO COMBO BOX
a = Autocad()
layer_count = a.doc.Layers.count #ĐẾM SỐ LƯỢNG LAYER
layers_names = [a.doc.Layers.Item(i).Name for i in range(layer_count)] # LẤY TÊN TẤT CẢ LAYER
combo = Combobox(window, font = ('Times New Roman',14), width=20) #THIẾT LẬP HIỂN THỊ COMBO BOX
combo['value'] = layers_names #HIỂN THỊ LIST TÊN LAYER TRONG COMBO BOX
combo.current(0) #VỊ TRÍ HIỂN THỊ CỦA DANH SÁCH TÊN TRONG COMBO BOX
combo.place(x = 150, y = 20)

#CODE TẠO BUTTON
def clicked():
    layer_new = a.doc.Layers.Add(str(txt.get()))
    layer_count = a.doc.Layers.count #ĐẾM SỐ LƯỢNG LAYER
    layers_names = [a.doc.Layers.Item(i).Name for i in range(layer_count)] # LẤY TÊN TẤT CẢ LAYER
    combo = Combobox(window, font = ('Times New Roman',14), width=20) #THIẾT LẬP HIỂN THỊ COMBO BOX
    combo['value'] = layers_names #HIỂN THỊ LIST TÊN LAYER TRONG COMBO BOX
    combo.current(layer_count-1) #VỊ TRÍ HIỂN THỊ CỦA DANH SÁCH TÊN TRONG COMBO BOX
    combo.place(x = 150, y = 20)

btn = Button(window, text= 'Thực thi', command=clicked)
btn.place(x = 150, y = 300)


#VÒNG LẶP TKINTER
window.mainloop()