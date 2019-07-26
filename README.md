# **Flask ueditor Backstage, designed by yy**

[![](https://img.shields.io/github/release/guaidashu/ueditor-flask.svg)](https://github.com/guaidashu/ueditor-flask/releases)
[![python](https://img.shields.io/badge/python-3.5-blue)](https://github.com/python)
[![](https://img.shields.io/badge/pypi-v1.0.0-blue)]()
[![npm](https://img.shields.io/npm/l/express.svg)]()

## Installing and Getting started

1. Install

    The easiest way to install.
    
        pip install flask-ueditor
  
    Or you can clone source code from github.
  
        git clone git@github.com:guaidashu/ueditor-flask.git

2. Config

    You need to configure the following requirements.
    
        # 允许上传的文件大小
        # Allowed file size to upload
        MAX_CONTENT_LENGTH = 16 * 1024 * 1024

        # 文件上传文件夹(必须)
        # Upload file store location(must)
        UPLOAD_FOLDER = "static/upload"

        # 允许上传的文件类型
        # Allowed file types to upload
        ALLOW_FILE_TYPE = {
            "jpg": 1,
            "png": 2,
            "gif": 3,
            "JPEG": 4,
            "jpeg": 5
        }
        
        # 目前默认为七牛云存储，所以你也需要添加如下内容
        QINIU_ACCESS_KEY = ''
        QINIU_SECURE_KEY = ''

        QINIU_BUCKET_NAME = '七牛云bucket的名字'


3. Start

    Example

  	    from flask_ueditor.action import Action
	    from flask import request, Response

	    from app.api import api


	    @api.route("/upload/ueditorUploadImage", methods=['POST', 'GET'])
	    def ueditor_upload_image():
	        action = Action(request, "", "static/assets/ueditor", "config.json")
	        result = action.exec()
	        return Response(result.__dict__, mimetype="application/json;charset=utf-8")


## Usage

None

## FAQ

None

## Running Tests

## Finally Thanks 

Thanks for your support.