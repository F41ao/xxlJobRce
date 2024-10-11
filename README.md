# xxlJobRce
XXL_Job命令执行批量检测脚本_!
![图片](https://github.com/user-attachments/assets/c1e85330-9152-4517-98e4-8c0259985813)
```shell
# 漏洞描述信息
XXL-JOB 是一款开源的分布式任务调度平台，用于实现大规模任务的调度和执行。XXL-JOB 默认配置下，用于调度通讯的 accessToken 不是随机生成的，
而是使用 application.properties 配置文件中的默认值。在实际使用中如果没有修改默认值，攻击者可利用此绕过认证调用 executor，执行任意代码，
从而获取服务器权限。经分析和研判，该漏洞利用难度低，可导致远程代码执行。

# 资产搜索语法
Fofa:"invalid request, HttpMethod not support" && port="9999"
360QuaKe:html_hash: "1b5af7109cb2b269eb02ba1ef4629bd8"

# 使用说明信息
xxl_jobRce.py --url http://www.xxx.com --cmd "Dnslog外带或反弹shell命令"
批量漏洞检测:xxl_jobRce.py --file urls.txt 结果请查看success.txt文件！
```

