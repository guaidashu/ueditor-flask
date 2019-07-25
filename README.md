# **Flask ueditor Backstage, designed by yy**

## Installing and Getting started

1. Install
  
    You can clone flask_ueditor from github.

  	    pip install flask-ueditor
  
        git clone git@github.com:guaidashu/ueditor-flask.git
   
2. Start

    Example

  	    from flask_ueditor.action import Action
	    from flask import request, Response

	    from app.api import api


	    @api.route("/upload/ueditorUploadImage", methods=['POST', 'GET'])
	    def ueditor_upload_image():
	        action = Action(request, "", "static/assets/ueditor", "config.json")
	        result = action.exec()
	        return Response(data, mimetype="application/json;charset=utf-8")


## Usage

None

## FAQ

None

## Running Tests

## Finally Thanks 

Thanks for your support.