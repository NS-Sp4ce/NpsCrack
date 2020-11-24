# NpsCrack
一款适用于爆破NPS服务器的脚本

# 功能

1. 测试登录帐号
2. 提取客户端信息
3. 提取隧道信息
4. 获取NPS服务器信息

获取完以上信息后会在同级目录下生成result目录，内含成功的IP/域名命名的文件夹，文件夹内保存客户端、服务器、隧道信息

同级目录下载登录成功时生成success.txt并写入登录成功的IP/域名、用户名、密码

# 使用

需求：

- python3
  - requests

```
λ python3 nps-crack.py

     _   _              _____                _
    | \ | |            / ____|              | |
    |  \| |_ __  ___  | |     _ __ __ _  ___| | __
    | . ` | '_ \/ __| | |    | '__/ _` |/ __| |/ /
    | |\  | |_) \__ \ | |____| | | (_| | (__|   <
    |_| \_| .__/|___/  \_____|_|  \__,_|\___|_|\_\
          | |
          |_|                 Author: Sp4ce

usage: nps-crack.py [-h] [-target TARGETFILE] [-username USERNAMEFILE] [-password PASSWORDFILE]

optional arguments:
  -h, --help            show this help message and exit
  -target TARGETFILE, --targetFile TARGETFILE
                        Load targets file or single target.
  -username USERNAMEFILE, --usernameFile USERNAMEFILE
                        Load usernames file or single username.(default admin)
  -password PASSWORDFILE, --passwordFile PASSWORDFILE
                        Load passwords file or single password.(default 123)

```
单目标：
`python3 nps-crack.py -target http://xxx.xxx.xxx.xxx [-username USERNAMEFILE] [-password PASSWORDFILE]`

多目标：
`python3 nps-crack.py -target /path/to/file [-username USERNAMEFILE] [-password PASSWORDFILE]`

缺省用户：admin/123

# 截图

![](1.png)
