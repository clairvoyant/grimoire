#!/usr/bin/env python

import model
import glob
import os
import sys
import datetime


from sqlalchemy.sql import func



# loads a database file with following information
#    Date|Open|High|Low|Close|Volume|Adj Clos


if __name__ == "__main__":
   engine  = model.init_engine("price.db")
   session = model.create_session()

   for s,p in session.query(model.Symbol, model.Price).filter(model.Symbol.id==model.Price.symbol_id).filter(model.Symbol.name=='GAM.MC').all():
       print s, p

   for joined in session.query(model.Symbol).join(model.Price).filter(model.Symbol.name=='GAM.MC').all():
       print joined

   print session.query(model.Symbol.name, func.count('*')).group_by(model.Symbol.name).all()
