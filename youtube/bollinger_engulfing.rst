Bollinger Bands and Engulfing candlestick
=========================================

This strategy uses the famous Bollinger Bands and the Engulfing candlestick. Here is the source for the `strategy <https://www.youtube.com/watch?v=LNQUvN7_NUQ>`_.

Buy Rules 
---------

1. Close is lower than Lower Bollinger Band.

2. Close is greater than the Open.

3. Close from one period ago is less than  the Open from one period ago.

4. Open is less than the Close from one period ago.

5. Close is greater than Open from one period ago. 


Sell Rules
----------

1. Close is greater than Upper Bollinger Band.

2. Close is less than the Open.

3. Close from one period ago is greater than the Open from one period ago.

4. Open is greater than the Close from one period ago.

5. Close is less than Open from one period ago.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-8.png
  :target: _build/_static/images/strategy-8.png
  :width: 1080
  :alt: Bollinger Bands and Engulfing Signal Points


Results 
-------

.. csv-table:: Table 11 : Bollinger Bands and Engulfing for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-8.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this https://github.com/zeta-zetra/code.