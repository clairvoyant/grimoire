#!/usr/bin/env python
#
# loads a database file with following information
#    Date|Open|High|Low|Close|Volume|Adj Clos
#

import model
import glob
import os
import sys
import datetime




def string2date(s):
    result = None
    try:
        result = datetime.datetime.strptime(s, "%Y-%m-%d")
    except:
        pass

    return result

def load_file(session, fpath):
    f = open(fpath, "r")
    fname = os.path.basename(fpath)
    (symbol_name, ext) = os.path.splitext(fname)

    # check if the symbol is already present!!!!
    # TODO play with the unique in the name!!!
    # TODO find a simpler way to do it. 

    symbol = session.query(model.Symbol).filter(model.Symbol.name==symbol_name).first()
    if symbol == None:
       symbol = model.Symbol(name=symbol_name)
       session.add(symbol)
       session.commit()


    for line in f.readlines():
        tokens = line.split("|")

        if len(tokens) < 5:
           continue

        try:
           date = string2date(tokens[0])
           if date != None:
              price = session.query(model.Price).filter(model.Price.symbol_id==symbol.id).filter(model.Price.date==date).first()
              if price == None:
                 price  = model.Price(
                           symbol_id=symbol.id,
                           date=date,
                           opening=tokens[1],
                           high=tokens[2],
                           low=tokens[3],
                           closing=tokens[4])
                 session.add(price)
        except Exception as e:
            print e


    session.commit()


def load_dir(session, path):

    files = glob.glob(os.path.join(path, "*.*"))
    for fpath in files:
        print "loading %s:%s" %(datetime.datetime.now(), fpath)
        sys.stdout.flush()
        load_file(session, fpath)






if __name__ == "__main__":
   engine  = model.init_engine("price.db")
   session = model.create_session()
   load_dir(session, "data")