# test01

## docker  指令

docker image pull hello-world   

docker run -d -p 80:8000 docker/getting-started    

docker container run -it ubuntu bash  (自動下載DOCKER中的ubuntu 最新版及開啟 bash)   
docker container ls
docker container stop 310dc5acd52f
docker container rm 310dc5acd52f  
docker image rm ubuntu  

docker image ls  
docker image build -t pyramid-app  .  
docker image build . -t pyramid-app  
docker build . -t pyramid-app 
docker build . --tag pyramid-app 

docker container ls  
docker container run pyramid-app
docker run pyramid-app
docker container kill 4efxxxx 
docker container rm 036664aeeff3        




# https://www.youtube.com/watch?v=BLBC-7sRJq4

# 安裝 Flask 套件
+ pip install Flask

# 步驟二 : 將以下代碼存檔為 app.py
```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
```
# 步驟三 : 終端機指令執行
```
$ flask run 
```

