##WSGI接口
# from wsgiref.simple_server import make_server
# # 导入我们自己编写的application函数:
# from hello import application
#
# # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# # 开始监听HTTP请求:
# httpd.serve_forever()


##WEB框架 flask
# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='123456':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
# if __name__ == '__main__':
#     app.run()

### MVC Model View  Control  using flask  jinja2
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123456':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
