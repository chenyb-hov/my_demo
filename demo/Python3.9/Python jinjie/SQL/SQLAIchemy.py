from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

import json
#对象基类
Base = declarative_base()

class Customer(Base):
    __tablename__='customer'

    id = Column(String(30), primary_key=True)
    name = Column(String(10))
    age = Column(Integer)
    gender = Column(Integer)
    # 一对多
    computes = relationship('Compute')

class Compute(Base):
    __tablename__ = 'compute'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 外键
    cid = Column(String(30), ForeignKey('customer.id'))

engine = create_engine('mysql+mysqlconnector://root:cyb101500@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

# session = DBSession()
# new_customer = Customer(id='TS0000002', name='cus2', age=18, gender=0)
# session.add(new_customer)
# session.commit()
# session.close()

session1 = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
customer = session1.query(Customer).filter(Customer.age==18).all()

print([j.__dict__ for j in customer[0].computes])
print([i.__dict__ for i in customer])

session1.close()