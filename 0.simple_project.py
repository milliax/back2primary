#coding=utf-8
""" This is the simple project for first class """

# 判斷閏年

year = int(input("請輸入想查詢的年分: "))

if year % 4 == 0:
    if year % 100 == 0:
        print("不是閏年")
    else:
        print("是閏年")
else:
    print("不是閏年")