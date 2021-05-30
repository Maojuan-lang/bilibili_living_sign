# b站直播签到脚本
需要在腾讯云部署云函数 https://console.cloud.tencent.com/  
环境变量说明：  
1.必须  
COOKIE：b站的cookie，支持多个cookie，cookie之间用 # 隔开（例如cookie1#cookie2#cookie3）  
2.非必须  
SERVER：Server酱码    
  
第三方库  
pip3 install requests  
pip3 install json  
  
获取Cookie方法  
浏览器无痕模式打开 https://www.bilibili.com/ ，登录账号  
按F12，打开开发者工具，找到并点击Network  
按F5刷新页面，按下图复制 Cookie：(复制两个箭头中间的全部字符串)  
![image](https://user-images.githubusercontent.com/75521125/120108305-3185b200-c197-11eb-85c0-ffe622beca0c.png)
  
部署方法--腾讯云函数  
1.下载压缩包文件（项目右侧） 
![image](https://user-images.githubusercontent.com/75521125/120108563-3860f480-c198-11eb-8a77-ecbc6e74f47c.png)
![image](https://user-images.githubusercontent.com/75521125/120108570-4282f300-c198-11eb-9533-74794292ea2a.png)

2.打开控制台：https://console.cloud.tencent.com/  
登录后选择  
![image](https://user-images.githubusercontent.com/75521125/120108434-ae189080-c197-11eb-91eb-3764872b1dc6.png)
![image](https://user-images.githubusercontent.com/75521125/120108451-bec90680-c197-11eb-824a-b5dbeb02a126.png)
![image](https://user-images.githubusercontent.com/75521125/120108470-d4d6c700-c197-11eb-9f8a-92562b250c23.png)
![image](https://user-images.githubusercontent.com/75521125/120108493-eddf7800-c197-11eb-9397-edff0f6e26d5.png)
上传刚刚下载的压缩包文件
![image](https://user-images.githubusercontent.com/75521125/120108677-de146380-c198-11eb-891e-1ec38754f00f.png)
SERVER选填，COOKIE必填，这两个必须大写
![image](https://user-images.githubusercontent.com/75521125/120108692-ee2c4300-c198-11eb-96fd-e8a7003166f4.png)
![image](https://user-images.githubusercontent.com/75521125/120108725-13b94c80-c199-11eb-84b8-83e3a8a14818.png)
这些填完后点击页面左下角附近的完成
