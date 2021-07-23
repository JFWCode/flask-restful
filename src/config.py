import os

DATABASE_HOST = os.environ.get('DATABASE_HOST', '192.168.8.71')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@{}:{}/postgres'.format(DATABASE_HOST, DATABASE_PORT)
    # 查询时会显示原始SQL语句
    if DEBUG:
        SQLALCHEMY_TRACK_MODIFICATIONS = True
        SQLALCHEMY_ECHO = True
    else:
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_ECHO = False