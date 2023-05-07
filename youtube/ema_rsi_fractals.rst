EMA, RSI and Fractals 
=====================

This is a scalping strategy from the "Moving Average" channel. The strategy uses the Williams Fractals, the RSI and 3 moving averages, 
namely: the 21 MA, the 50 MA, and the 200 MA. Here is the `source <https://www.youtube.com/@TheMovingAverage>`_.  

Buy Rules 
---------

1. 21 EMA is greater than the 50 EMA.

2. 50 EMA is greater than the 200 EMA. 

3. RSI(14) is greater than 50. 

4. Bullish Williams Fractals is present. 

5. Close greater than 21, 50 and 200 EMA.



Sell Rules
----------

1. 21 EMA is less than the 50 EMA.

2. 50 EMA is less than the 200 EMA. 

3. RSI(14) is less than 50. 

4. Bearish Williams Fractals is present. 

5. Close is less than 21, 50 and 200 EMA.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-6.png
  :target: _build/_static/images/strategy-6.png
  :width: 1080
  :alt: EMA, RSI, Fractals Signal Points


Results 
-------

.. csv-table:: Table 7 : EMA, RSI, Fractals Algo for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-6.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.
