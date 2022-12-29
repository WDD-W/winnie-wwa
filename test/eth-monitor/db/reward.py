from .base_db import Base
from sqlalchemy import Column, Integer, String, DateTime, Float

class Reward(Base):
    __tablename__ = 'eth_reward'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String(64))
    pub_key = Column(String(64))
    reward = Column(Float)
    block = Column(Integer)
    timestamp = Column(Integer)

    def __repr__(self):
        return "<Reward( currency='%s', pub_key='%s', reward='%f', block = '%f', timestamp='%s')>" % (
                   self.currency, self.pub_key, self.reward, self.block, self.timestamp)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
