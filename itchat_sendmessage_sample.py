#coding=utf8
# 第一步，引入itchat库
import itchat
# 第二步，调用 itchat的方法, 参数hotReload设置为True
itchat.auto_login(hotReload=True)
# 第三步 想给谁发信息，先查找到这个朋友,name后填微信备注即可
# 例如我的名字是dejun
users = itchat.search_friends(name='dejun')

# 获取好友全部信息,返回一个列表,列表内是一个字典，打印看下
print(users)

# 第四步，获取`UserName`,用于发送消息
userName = users[0]['UserName']
# 第五步，正式发送消息，发送信息"hello"
itchat.send("hello,this is a new message!", toUserName = userName)