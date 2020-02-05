#第三方库自动安装脚本
'''
库名              用途                   pip安装指令
NumPy         N维数据表示和运算      pip install numpy
Matplotlob    二维数据可视化         pip install matplotlib
PIL           图像处理               pip install pillow
Scikit-learn  机器学习和数据挖掘     pip install sklearn
Requests      HTTP协议访问及网络爬虫 pip install requests
jieba         中文分词               pip install jieba
Beautiful Soup HTML和XML解析器       pip install beautifulsoup4
Wheel         Python第三方库文件打包工具 pip install wheel
PyInstaller   打包Python源文件为可执行文件 pip install pyinstaller
Django        Python最流行的Web开发框架 pip install django
Flask         轻量级Web开发框架      pip install flask
WeRoBot       微信机器人开发框架     pip install werobot
SymPy         数学符号计算工具       pip install sympy
Pandas        高效数据分析和计算     pip install pandas
Networkx      复杂网络和图结构的建模和分析 pip install networkx
PyQt5         基于Qt的专业级GUI开发框架 pip install pyqt5
PyOpenGL      多平台OpenGL开发接口   pip install pyopengl
PyPDF2        PDF文件内容提前及处理  pip install pypdf2
docopt        Python命令行解析       pip install docopt
PyGame        简单小游戏开发框架     pip install pygame
'''

#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}

try:
    for lib in libs:
        os.system("pip install "+lib)
    print("successful")
except:
    print("Falied somehow")
