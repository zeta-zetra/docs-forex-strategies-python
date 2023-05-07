Bollinger Bands and Doji candlestick
====================================

This strategy uses the famous Bollinger Bands and the Doji candlestick. Here is the source for the `strategy <https://www.youtube.com/watch?v=LNQUvN7_NUQ>`_.

Buy Rules 
---------

1. Close is lower than Lower Bollinger Band.

2. Close is greater than the Open.

3. Close from one period ago is equal to the Open from one period ago.

4. Close from two periods ago is less than the Open from two periods ago.


Sell Rules
----------

1. Close is greater than Upper Bollinger Band.

2. Close is less than the Open.

3. Close from one period ago is equal to the Open from one period ago.

4. Close from two periods ago is greater than the Open from two periods ago.



Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-8.png
  :target: _build/_static/images/strategy-8.png
  :width: 1080
  :alt: Bollinger Doji Signal Points


Results 
-------

.. csv-table:: Table 10 : Bollinger Bands and Doji for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-8.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this https://github.com/zeta-zetra/code.