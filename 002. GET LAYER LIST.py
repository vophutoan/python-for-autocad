#IMPORT THƯ VIỆN
from pyautocad import Autocad
a = Autocad()


layer_count = a.doc.Layers.count #ĐẾM SỐ LƯỢNG LAYER
print("Số layer là: " + str(layer_count)) #IN RA SỐ LƯỢNG LAYER
layers_names = [a.doc.Layers.Item(i).Name for i in range(layer_count)] # LẤY TÊN TẤT CẢ LAYER
for i in layers_names: 

    print('Tên layer là: ' + i) #IN RA TOÀN BỘ TÊN LAYER
