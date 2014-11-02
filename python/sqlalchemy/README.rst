

========
Rationale
========
This grimorie spell is focused on performance using SQLAlchemy. 
It uses real data from the spanish stock market, near 300.000 stock prices. 

The objetive is measure the speed of inserts using the ORM, and the Core libraries. The results have been quite suprising. 

The databases used in the analysis are the usual open source ones. All of them have been turnkey to have the best writting performance. 

* sqlite
* mysql
* mariadb
* postgress
* firebird


==========
Methodology
==========
The database model is a relationship one with foreing keys and some restrictions in the keys. 

Measurements are taken inserting into an empty database. Total time is aggregated anaverage over three executions. Same data is inserted each time for each database. 
For each database, there has been measurements of

* ORM: commiting the result for each Stock symbol. 
* Bulk: insert using Core. Not a real bulk insert. Commiting the result for each Stock symbol. 

========
Tools
========
During the development the tool RunPythonRun has been used in order to find hot spot.
   $ python -m cProfile -o load.prof ./load.py
   $ python runsnake.py load.prof

======
Results
=======
One surprising result is the low performance of sqlite when there are "datetime" columns. It seems the system is spending most of the time converting back and forth the dates from string to datetime variable presentations.


