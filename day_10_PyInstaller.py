#PyInstaller.py
#PyInstaller库的使用
'''
PyInstaller库可将.py源代码转换成无需源代码的可执行文件


.py -> PyInstaller -> Windows(exe文件)/Linux/Mac OS X
PyInstaller是第三方库
http://www.pyinstaller.org
安装第三方库需使用pip工具

(cmd行命令) pyinstaller -F <文件名.py>
eg:
pyinstaller -F day_09_sevendigitV2.py

PyInstaller库常用参数
参数                      描述
-h                   查看帮助
--clean              清理打包过程中的临时文件
-D,--onedir          默认值，生成dist文件夹
-F,--onefile         在dist文件夹中只生成独立的打包文件
-i<图标文件名.ico>   指定打包程序使用的图标(ico)文件

eg:
pyinstaller -i curve.ico -F SevenDigitsDrawV2.py

'''
