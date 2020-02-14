SERVER_PORT = 5000
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = 'minitest'
#过滤无需登录的url
IGNORE_URLS = [
    '^/user/login'
]
IGNORE_CHECK_LOGIN_URLS=[
    '^/static',
    '^/favicon.ico'
]