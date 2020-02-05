'''
政府工作报告词云
步骤1:读取文件，分词整理
步骤2:设置并输出词云
步骤3:观察结果，优化迭代
'''
#GovRptwordCloudv1.py
import jieba
import wordcloud

f = open("I:\download\使用说明.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc",\
                        width = 1000,height = 700,background_color = "white",\
                        )
w.generate(txt)
w.to_file("grwordcloud.png")


#GovRptWordCloudv1.py
import jieba
import wordcloud
f = opne("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = wordcloud.WordCloud(font_path = "msyh.ttc",\
                          width = 1000,height = 700,background_color = "white",\
                          max_words = 15)
w.generate(txt)
w.to_file("grwordcloud.png")
