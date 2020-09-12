'''
@Author: your name
@Date: 2020-07-23 19:34:35
@LastEditTime: 2020-07-23 19:36:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \py\test5.py
'''
a=u'成都'

b=str(a.encode('unicode_escape'))
c=b[-5:-1]
d=c.upper()
print(a,b,c,d)