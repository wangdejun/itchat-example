#coding=utf8
import itchat

itchat.auto_login(hotReload=True)  
#获取通讯录信息
account=itchat.get_friends()
# #获取自己的UserName
userName = account[0]['dejun']

#获取公众号信息
# mps = itchat.get_mps()
# print(mps)

lines = []
#读取txt文件
f = open("./
aaa.txt")  
lines = f.readlines()#读取全部内容  
#循环发送文本内容
for i in range(90): 
    #UserName需要用上面获取的自己修改
    itchat.send(lines[i],toUserName='UserName')  
print("Success")
