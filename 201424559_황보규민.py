#-------------------------------------------------------------------------------
#-*- coding:utf-8 -*-
# Name:        module1
# Purpose:
#
# Author:      ghkdq
#
# Created:     16-05-2019
# Copyright:   (c) ghkdq 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import tkinter as tk
import tkinter.font
import csv

df = pd.read_csv('3.csv',sep=",",dtype='unicode',encoding = 'utf-8')

df2 = df[["휴게소명","도로종류","매점유무"]]


window=tkinter.Tk()

def find(event):
    strg = str(entry.get())
    df4=df[df['휴게소명']==strg]
    df3 = df4[['휴게소명','도로종류','도로노선번호','도로노선명','도로노선방향','도로점용면적']]
    df5 = df4[['위도','경도','휴게소종류','휴게소운영시작시각','휴게소운영종료시각']]
    df6 = df4[['주차면수','경정비가능여부','주유소유무','LPG충전소유무','전기차충전소유무','버스환승가능여부']]
    df7 = df4[['쉼터유무','화장실유무','약국유무','수유실유무','매점유무','음식점유무']]
    df8 = df4[['기타편의시설','휴게소대표음식명','휴게소전화번호','데이터기준일자','제공기관코드','제공기관명']]

    str(df3)
    print(df3)

    label.config(text=df3)
    label2.config(text=df5)
    label3.config(text=df6)
    label4.config(text=df7)
    label5.config(text=df8)
def countUP():
    global count
    count += 1
    label.config(text=str(count))
def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

window.title("전국 고속도로정보")
window.geometry("900x500+100+100")
window.resizable(False, True)

font = tkinter.font.Font(family="맑은 고딕", size=20 )
font2 = tkinter.font.Font(family="맑은 고딕", size=10)

label =tkinter.Label(window,text="컴퓨터시스템입문 기말과제",relief="solid",font=font)
label.pack()
label =tkinter.Label(window,text="201424559 황보규민",width=640,anchor="e")
label.pack()
label =tkinter.Label(window,text="고속도로이름 입력.",height=4,width=640,anchor="s",font=font2, fg="blue" )
label.pack()

entry=tkinter.Entry(window)
entry.bind("<Return>",find)
entry.pack()

count =0


label = tkinter.Label(window,text="")
label.pack()

label2 = tkinter.Label(window,text="")
label2.pack()

label3 = tkinter.Label(window,text="")
label3.pack()

label4 = tkinter.Label(window,text="")
label4.pack()

label5 = tkinter.Label(window,text="")
label5.pack()






window.mainloop()

##infile = codecs.open('final2.csv','r',encoding='utf-8')

##for line in infile:
##    line = line.replace(u'\xa0', ' ')
##    print(line)


##infile.close()
