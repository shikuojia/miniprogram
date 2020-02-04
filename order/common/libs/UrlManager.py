class UrlManager(object):
    def __init__(self):
        pass
    @staticmethod
    def buildUrl(path):
        return path
    @staticmethod
    def buildStaticUrl(path):
        ver = '{}'.format(20200202)
        path = '/static' + path +"?ver=" +ver
        return UrlManager.buildUrl(path)