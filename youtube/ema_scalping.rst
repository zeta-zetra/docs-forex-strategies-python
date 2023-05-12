EMA Scalping
===============

The strategy only uses three moving averages. The 50 EMA, the 100 EMA and the 150 EMA. Here is the `source <https://www.youtube.com/watch?v=ybmep_u5MeU>`_

Buy Rules 
---------

1. Open is less than the 50 EMA.

2. Close is greater than the 50 EMA.

3. Difference between Open and Low is less than Wick Limit.

4. 50 EMA is greater than 100 EMA, and 100 EMA is greater than 150 EMA. 


Sell Rules
----------

1. Open is greater than 50 EMA.

2. Close is less than 50 EMA.

3. Difference between High and Open is less than Wick Limit.

4. 50 EMA is less than 100 EMA, and 100 EMA is less than 150 EMA. 


Sample of Signal Points 
-----------------------

.. image:: /_static/images/ema-scalping.png
  :target: /_static/images/ema-scalping.png
  :width: 1080
  :alt: EMA Scalping Signal Points


Results 
-------

.. image:: /_static/results/ema-scalping.png
   :target: /_static/results/ema-scalping.png
   :width: 1080
   :height: 500
   :alt: EMA Scalping Results

Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.