# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
from utils.utils import ConfigParserCustomer

Base = declarative_base()

# 初始化数据库连接:
glo = 'mysql'
configParserCustomer = ConfigParserCustomer()
sql_url = configParserCustomer.getProperty(glo, 'sql_url')
username = configParserCustomer.getProperty(glo, 'username')
password = configParserCustomer.getProperty(glo, 'password')
host = configParserCustomer.getProperty(glo, 'host')
dbname = configParserCustomer.getProperty(glo, 'dbname')
charset = configParserCustomer.getProperty(glo, 'charset')
engine = create_engine(sql_url % (username, password, host, dbname, charset))


# 返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
