Harami Candlestick pattern
===========================

Introduction
------------
Candlestick patterns have long been a valuable tool for traders and investors in the field of technical analysis. These patterns provide visual representations of price movements and offer insights into potential market reversals and trend continuations. One such pattern that has gained recognition among market participants is the Harami candlestick pattern.

The Harami pattern, derived from the Japanese word for "pregnant," is a two-candlestick pattern that signifies a potential reversal in the prevailing market trend. It is characterized by a small candlestick (the "inside" or "baby" candle) that is completely engulfed by the preceding larger candlestick (the "mother" candle). This pattern draws attention to a possible shift in market sentiment and offers traders an opportunity to make informed decisions.

We will delve into the intricacies of the Harami candlestick pattern, exploring its formation, interpretation, and practical application in trading. By understanding the Harami pattern and its significance, traders can enhance their ability to identify potential trend reversals and make well-informed trading decisions.

We will discuss both the bullish and bearish versions of the Harami pattern, examining the characteristics that define each and exploring real-life examples to illustrate their implications. We will also address the limitations and considerations associated with the Harami pattern, highlighting the importance of confirmation and the integration of additional technical analysis tools.

Understanding the Harami Candlestick Pattern
---------------------------------------------
The Harami candlestick pattern is a two-candlestick pattern that can provide valuable insights into potential market reversals. It is important to grasp the formation and characteristics of the Harami pattern to effectively utilize it in technical analysis.

There are two variations of the Harami pattern: the bullish Harami and the bearish Harami.

**Bullish Harami Pattern**: The bullish Harami pattern occurs during a downtrend and suggests a potential reversal towards an upward movement. In this pattern, the mother candle is bearish (with a downward close) and is followed by a smaller bullish baby candle entirely engulfed within the body of the mother candle. The smaller size of the baby candle indicates a decrease in selling pressure, potentially signaling a shift in market sentiment towards buying interest.

.. image:: /_static/images/bearish-harami.png
  :target: /_static/images/bearish-harami.png
  :width: 500
  :alt: Bearish Harami

**Bearish Harami Pattern**: Conversely, the bearish Harami pattern emerges during an uptrend, indicating a possible reversal towards a downward trend. In this case, the mother candle is bullish (with an upward close), and the subsequent baby candle is bearish and contained within the range of the mother candle. The presence of the smaller bearish candle suggests a reduction in buying pressure, potentially indicating an imminent shift towards selling pressure.
	
.. image:: /_static/images/bullish-harami.png
  :target: /_static/images/bullish-harami.png
  :width: 500
  :alt: Bullish Harami


Paramters for the backtests
----------------------------

For this particular analysis, we worked with the following parameters:

   -  Starting balance: $10,000
   -  Margin: 1:100
   -  Commission: None
   -  Testing period: From January 1, 2020, to December 31, 2022
   -  Timeframe: 15 minutes
   -  Currency pair: EURUSD
   -  Data Source: Dukascopy 

Backtesting the Harami bullish and bearish strategy
---------------------------------------------------

Backtesting the Harami candlestick pattern by going long on the bullish Harami and going short on the bearish Harami, while testing different exit strategies, is a crucial step in evaluating the effectiveness of this trading approach. By applying historical price data and defining specific trading rules, traders can simulate trades based on the occurrence of Harami patterns. To test the profitability and robustness of the strategy, different exit strategies can be employed.

By backtesting across different exit strategies, traders can gain insights into the potential profitability and risk management aspects of trading the Harami candlestick pattern.

**Buy Rules**

1. Identify the bullish Harami candlestick.

**Sell Rules**

1. Identify the bearish Harami candlestick.


**Results**

.. image:: /_static/results/harami-candlestick.png
   :target: /_static/results/harami-candlestick.png
   :width: 1080
   :height: 500
   :alt: Harami Candlestick Results


Backtesting the Harami candlestick and Pivot Points strategy
-------------------------------------------------------------

In our rigorous testing, we've explored two versions of this strategy that we can't wait to share with you. But that's not all - we're also going to push the boundaries and test it across a range of diverse exit strategies. Before we delve deeper, let's take a moment to introduce the pivot points that play a pivotal role in our analysis. The pivot points we use are:
 
- `Traditional <https://www.tradingview.com/chart/?symbol=SP%3ASPX&solution=43000521824>`_

- `Caramillia <https://www.tradingview.com/chart/?symbol=SP%3ASPX&solution=43000521824>`_

- `Dm <https://www.tradingview.com/chart/?symbol=SP%3ASPX&solution=43000521824>`_

- `Fibonacci <https://www.tradingview.com/chart/?symbol=SP%3ASPX&solution=43000521824>`_ 

*Version 1*

**Buy Rules** 

1. Close of the bullish Harami must be above the resistance pivot point.


**Sell Rules**


1. Close of the bearish Harami must be below the support pivot point.
    

**Results**

.. image:: /_static/results/harami-candlestick-and-pivot-point-version-1.png
   :target: /_static/results/harami-candlestick-and-pivot-point-version-1.png
   :width: 1080
   :height: 500
   :alt: Harami Candlestick and Pivot Point 1 Results



*Version 2*

**Buy Rules** 

1. Close of the bullish Harami must be below the support pivot point.


**Sell Rules**


1. Close of the bearish Harami must be above the resistance pivot point.
    

**Results**

.. image:: /_static/results/harami-candlestick-and-pivot-point-version-2.png
   :target: /_static/results/harami-candlestick-and-pivot-point-version-2.png
   :width: 1080
   :height: 500
   :alt: Harami Candlestick and Pivot Point 2 Results


Source Code
-----------

Here is the link to the source code for this https://github.com/zeta-zetra/code.