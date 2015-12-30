# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""


import os

basedir = os.path.abspath(os.path.dirname(__file__))



class BaseConfig:
    SECRET_KEY = 'adsasdasfafd@$$DSADASD'

    @staticmethod
    def init_app(app):
        pass





class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



my_config = {
    'default': DevelopmentConfig
}
