def index():
    return "这是主页"


def register():
    return "这是注册页"


def login():
    return "这是登录页"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/register.py":
        return register()
    elif file_name == "/index.py":
        return index()
    else:
        return 'Hello World! 我爱你中国....'
