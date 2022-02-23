import winreg

root = winreg.ConnectRegistry(None,winreg.HKEY_CLASSES_ROOT) 

newKey = winreg.CreateKey(root,"demoapp")
winreg.SetValue(root,"demoapp",winreg.REG_SZ,"demoapp")
winreg.SetValueEx(newKey,"URL Protocol",0,winreg.REG_SZ,"D:\\demo.exe")

defaultIcon = winreg.CreateKey(newKey,"DefaultIcon")
winreg.SetValue(newKey,"DefaultIcon",winreg.REG_SZ,"D:\\demo.exe,1")

Shell = winreg.CreateKey(newKey,"Shell")
Open = winreg.CreateKey(Shell,"Open")
Command = winreg.CreateKey(Open,"Command")
winreg.SetValue(Open,"Command",winreg.REG_SZ,'''"D:\\demo.exe""%1"''')

# #给新创建的键添加键值
winreg.CloseKey(root)
winreg.CloseKey(defaultIcon)
winreg.CloseKey(Shell)
winreg.CloseKey(Open)
winreg.CloseKey(Command)
