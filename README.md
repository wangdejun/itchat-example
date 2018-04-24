### itchat-example

* 两种方式，第一种，命令行方式
    * 第一步，引入itchat库
        ```
        >>> import itchat
        ```
    * 第二步，调用 itchat的方法, 参数hotReload设置为True
        ```
        >>> itchat.auto_login(hotReload=True)
        ```
    * 第三步 想给谁发信息，先查找到这个朋友,name后填微信备注即可
        ```
        >>> users = itchat.search_friends(name='dejun')
        ```

    * 获取好友全部信息,返回一个列表,列表内是一个字典，打印看下
        ```
        >>> print(users)
        ```

    * 第四步，获取`UserName`,用于发送消息
        ```
        >>> userName = users[0]['UserName']
        ```
    * 第五步，正式发送消息，发送信息"hello"
        ```
        >>> itchat.send("hello,this is a new message!", toUserName = userName)
        ```

* 或者直接run这段脚本，
    * run the code below in terminal or a shell
    ```
    python itchat_sendmessage_sample.py 
    ```


* 有用的相关链接
    * <a href='https://blog.csdn.net/co_zy/article/details/73302984'>Python利用itchat库向好友或者公众号发消息</a>
    * <a href='https://github.com/littlecodersh/ItChat'>itchat开源库地址</a>
    * <a href='http://itchat.readthedocs.io/zh/latest/'>itchat使用指南</a>