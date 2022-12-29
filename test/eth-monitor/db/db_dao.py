from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, UniqueConstraint, Float, \
    DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


engine = create_engine('sqlite:///eth-info.db',echo=False)
metadata = MetaData(engine)

reward_table = Table('eth_reward',metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("currency", String(64)),
                    Column("pub_key", String(64)),
                    Column("reward", Float),
                    Column("block",Integer),
                    Column("timestamp", Integer))
metadata.create_all(engine,checkfirst=True)
session_factory = sessionmaker(bind=engine, autoflush=False)
Session = scoped_session(session_factory)