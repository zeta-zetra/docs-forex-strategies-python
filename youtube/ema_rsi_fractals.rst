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

.. image:: /_static/images/ema-rsi-fractals.png
  :target: /_static/images/ema-rsi-fractals.png
  :width: 1080
  :alt: EMA, RSI, Fractals Signal Points


Results 
-------

.. image:: /_static/results/ema-rsi-fractals.png
   :target: /_static/results/ema-rsi-fractals.png
   :width: 1080
   :height: 500
   :alt: EMA, RSI, Fractals Results


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.
