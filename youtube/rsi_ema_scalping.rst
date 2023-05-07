RSI and EMA Scalping
====================

The strategy uses the RSI and EMA indicators. Here is the `source <https://www.youtube.com/watch?v=MzEX4XumtEE>`_

Buy Rules 
---------

1. High is greater than 200 EMA.

2. RSI(3) is less than 10.



Sell Rules
----------

1. High is less than 200 EMA.

2. RSI(3) is greater than 90.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-7.png
  :target: _build/_static/images/strategy-7.png
  :width: 1080
  :alt: RSI and EMA Scalping Signal Points


Results 
-------

.. csv-table:: Table 12 : RSI and EMA Scalping for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-7.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.