Simple Dusty Musty Crusty
=========================

This is a complicated strategy but we have implemented the simple components of it to test. Here is the `source <https://www.youtube.com/watch?v=CPLkQQDN-Xw&list=PL3Jd92exRxKTGkeWFT4V-z8Gu3svBJ6ap&index=14>`_.  

Buy Rules 
---------

1. Current ADX(14) is greater than 15.

2. Current ADX(14) is greater than previous ADX(14) plus 0.40.

3. DM+ is greater than DM-.



Sell Rules
----------

1. Current ADX(14) is greater than 15.

2. Current ADX(14) is greater than previous ADX(14) plus 0.40.

3. DM+ is less than DM-.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-5.png
  :target: _build/_static/images/strategy-5.png
  :width: 1080
  :alt: Simple Dusty Musty Crusty Signal Points


Results 
-------

.. csv-table:: Table 6 : Simple Dusty Musty Crusty for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-5.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.
