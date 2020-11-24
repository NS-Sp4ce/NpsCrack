# NpsCrack
一款适用于爆破NPS服务器的脚本

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

