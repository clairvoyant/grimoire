

# begin sql alchemy dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy import Sequence

from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
# end sql alchemy


# The Base is metacreated, and shall be inherited by model classes
# create the metaclass singletons.
Base = declarative_base()
Session = sessionmaker()

#
# Mandatory fields for the object are
#  __tablename__
#  one columen
#
class Symbol(Base):
    __tablename__ = 'symbols'
    id   = Column(Integer, primary_key=True)
    name = Column(String,  unique=True )

    def __repr__(self):
        return "symbol=%s" %(self.name)

class Price(Base):
    __tablename__ = "prices"
    id        = Column(Integer, Sequence('price_id_seq'), primary_key=True)
    symbol_id = Column(String, ForeignKey('symbols.id'))
    date      = Column(DateTime, index=True)
    high      = Column(Float)
    low       = Column(Float)
    opening   = Column(Float)
    closing   = Column(Float)

    symbol    = relationship("Symbol", backref=backref('symbols', order_by=id))

    def __repr__(self):
        return "%s,%f,%f,%f,%f" %(self.date, self.high, self.low, self.opening, self.closing)



def init_engine(connection_string='sqlite:///prices.db'):
    # TODO create the engine, it shall be "turnkey for each DB.
    # note the session initialization... It congures the "metaclass".
    
    #engine = create_engine(conn, echo=True)
    engine = create_engine(connection_string, echo=False)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    return engine

def create_session():
    return Session()

