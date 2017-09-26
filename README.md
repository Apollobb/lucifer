# Lucifer运维平台 #

[![python2.7.x](https://img.shields.io/badge/python-2.7.X-brightgreen.svg)](https://www.python.org/)/
[![python3.x](https://img.shields.io/badge/python-3.X-brightgreen.svg)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-1.11.4-brightgreen.svg)](https://www.djangoproject.com/)
[![django-rest-framework](https://img.shields.io/badge/djangorestframework-3.6.3-brightgreen.svg)](http://www.django-rest-framework.org/)
[![django-rest-framework-jwt](https://img.shields.io/badge/djangorestframeworkjwt-1.11.0-brightgreen.svg)](https://github.com/GetBlimp/django-rest-framework-jwt)
[![django-channels](https://img.shields.io/badge/channels-1.1.8-brightgreen.svg)](https://channels.readthedocs.io/en/stable/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/itimor/lucifer-frontend/blob/master/LICENSE)

**Lucifer运维平台是采用的前后端分离开发，本项目是lucifer运维平台的后端**

**注意：该项目支持python2.7X和python3.X**

**注意：Lucifer运维平台使用 `django rest framework` 提供的restful API功能进行开发，后端主要提供api数据支持，前端负责路由和页面渲染，访问正常页面请配和使用前端项目** [点我到前端](https://github.com/itimor/lucifer-frontend.git)

## 功能
- 登录/注销
- 权限验证
- 主机管理
- 用户管理
- 角色管理
- 权限管理
- 远程执行命令
- 远程修改配置

## 开发
```bash
    # 克隆项目
    git clone https://github.com/itimor/lucifer.git

    # 安装依赖
    cd lucifer
   pip install -r requirements.txt
 
    #初始化数据库
    python manage.py migrate
    
    #创建admin用户
    python manage.py createsuperuser 
    
    #启动
    python manage.py runserver 0.0.0.0:8000

```
浏览器访问API `http://localhost:8000/api/`， 若前端项目已经部署好，可以直接访问前端

## 效果图

### api界面
![api](https://github.com/itimor/lucifer/blob/master/statics/images/api.png)

### 前端界面
![realtime](https://github.com/itimor/lucifer/blob/master/statics/images/realtime.gif)

## 目录结构
```shell
├── hosts                      
├── jobs
├── LICENSE
├── lucifer
├── lucifer.db
├── manage.py
├── README.md
├── requirements.txt
├── salts
├── statics
├── tools
├── upload
├── users
└── utils

```

## 待开发功能
- [ ] 因为已经实现了使用 `djanog-channels` 执行命令实时查看日志以及在线修改配置等功能，后面考虑可以用这个东西实现webXshell的功能，做一个web终端，可以直接在主机管理也远程连接机器。
- [ ] 做个任务计划管理器
- [ ] 发布系统只做了一半，接下来准备把它补全
