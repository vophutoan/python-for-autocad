#!/usr/bin/env python
# coding: utf-8

# In[29]:


#VẼ ĐƯỜNG TRÒN
from pyautocad import Autocad, APoint
a = Autocad()
radius = '100 '

a.doc.SendCommand('c ' + '30,20 ' + radius)


# In[35]:


#LOAD LINETYPE
from pyautocad import Autocad, APoint
a = Autocad()

a.doc.SendCommand('filedia ' + '0 ')
a.doc.SendCommand("-lt "+ "load "+ "DOTX2\n" + "C:/Users/Vo Phu Toan/AppData/Roaming/Autodesk/AutoCAD 2007/R17.0/enu/Support/acad.lin\n\n\u001b\u001b")
a.doc.SendCommand('filedia ' + '1 ')


# In[ ]:


#CÁC BUTTON THƯỜNG DÙNG
\u00094 : tab
\u001b : esc
\n : enter
    
#CÁC BUTTON KHÁC
https://codepoints.net/basic_latin

