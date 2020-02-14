import hashlib,base64


class UserService():

    @staticmethod
    def genAuthCode(user_info):
        m = hashlib.md5()
        cookies_str = '{}-{}-{}-{}'.format(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(cookies_str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def genPwd(pwd,salt):
        m = hashlib.md5()
        strs = '{}-{}'.format(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(strs.encode('utf-8'))
        return m.hexdigest()