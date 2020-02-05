#Python库之图形用户界面
'''
PyQt5:Qt开发框架的Python接口
提供了创建Qt5程序的Python API接口
Qt是非常成熟的跨平台桌面应用开发系统，完备GUI
推荐的Python GUI开发第三方库

wxPython:跨平台GUI开发框架
提供了专用于Python的跨平台GUI开发框架
理解数据类型与索引的关系，操作索引即操作数据
Python最主要的数据分析功能库，基于Numpy开发

eg:
import wx
app = wx.App(False)
frame = wx.Frame(None,wx.ID_ANY,"Hello World")
frame.show(True)
app.MainLoop()

PyGObject:使用GTK+开发GUI的功能库
提供了整合GTK+，WebKitGTK+等库的功能
GTK+:跨平台的一种用户图形界面GUI框架
实例:Anaconda采用该哭构建GUI

eg:
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World")
window.show()
window.connect("destory",Gtk.main_quit)
Gtk.main()

Python库之游戏开发
PyGame:简单的游戏开发功能库
提供了基于SDL的简单游戏开发功能及实现引擎
理解游戏对外部输入的响应机制及角色构建和交互机制
Python游戏入门最主要的第三方库

Panda3D:开源，跨平台的3D渲染和游戏开发库
一个3D游戏引擎，提供Python和C++两种接口
支持很多先进特性:法线贴图，光泽贴图，卡通渲染等
由迪士尼和卡内基梅隆大学共同开发

cocos2d:构建2D游戏和图形界面交互式应用的框架
提供了基于OpenGL的游戏开发图形渲染功能
支持GPU加速，采用树形结构分层管理游戏对象类型
适用于2D专业级游戏开发


Python库之虚拟现实
VR Zero:在树莓派上开发VR应用的Python库
提供大量与VR开发相关的功能
针对树莓派的VR开发库，支持设备小型化，配置简单化
非常适合初学者实践VR开发及应用

pyovr:Oculus Rift的Python开发接口
针对Oculus VR设备的Python开发库
基于成熟的VR设备，提供全套文档，工业级应用设备
Python+虚拟现实领域探索的一种思路

Vizard:基于Python的通用VR开发引擎
专业的企业级虚拟现实开发引擎
提供详细的官方文档
支持多种主流的VR硬件设备，具有一定通用性

Quads：迭代的艺术
对图片进行四份迭代，形成像素风
可以生成动图或静图图像
简单易用，具有很高展示度

ascii_art:ASCII艺术库
将普通图片转为ASCII艺术风格
输出可以是纯文本或彩色文本
可采用图片格式输出

turtle:海龟绘图体系


'''
