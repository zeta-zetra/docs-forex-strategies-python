Parabolic SAR
=============

This is a simple strategy that uses the Parabolic SAR. Click `here <https://www.youtube.com/watch?v=gfRO2_QS6gM>`_ for the source of the strategy.


What is the Parabolic SAR?
--------------------------
The Parabolic SAR (Stop and Reverse) is a technical indicator used to analyze market trends and identify potential points of trend reversals in financial markets. It was developed by J. Welles Wilder, Jr. and first introduced in his book "New Concepts in Technical Trading Systems".

The Parabolic SAR is plotted on a chart as a series of dots, either above or below the price bars depending on the direction of the trend. The dots are calculated based on the previous period's price and the acceleration factor, which determines the speed at which the dots move closer to the price bars.

When the dots are below the price bars, it suggests an uptrend, and traders may look for long positions. Conversely, when the dots are above the price bars, it suggests a downtrend, and traders may look for short positions. If the price moves in the opposite direction to the trend indicated by the dots, the Parabolic SAR will flip to the other side of the price bars, signaling a potential trend reversal.

The Parabolic SAR is often used in combination with other technical indicators and chart patterns to help traders make informed trading decisions. It's important to note that like any technical indicator, the Parabolic SAR is not infallible and should be used in conjunction with other analysis techniques and risk management strategies.



Buy Rules
----------
1. Enter when High is above the long Parabolic SAR but below the short Parabolic SAR dots.


Sell Rules
-----------
1. Enter when the Low is below the short Parabolic SAR but above the long Parabolic SAR dots.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-1.png
  :target: _build/_static/images/strategy-1.png
  :width: 1080
  :alt: Parabolic SAR Signal Points


Results 
-------

.. csv-table:: Table 2 : Parabolic SAR for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-1.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.