.. Strategies coded in Python documentation master file, created by
   sphinx-quickstart on Wed May  3 19:53:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Forex Strategies tested in Python
=================================

.. meta:: 
   :google-site-verification: A-twZ8lQDA0wjhOnm46byhk8CJHnAdfOaxxCRfBH4pc

The main aim of this project is to collect strategies in one place. This will serve
as a resource for trading ideas and start up code that can be used to backtest
them. 

The strategies included here are taken from books, videos, blogs, etc. For each
strategy we run 7 exits. The exits are shown in the table below. The literature on
trading is heavily focused on entries and not exits. We wanted to make a point 
in this project that exits do matter as well. The exits were inspired by Kevin 
Davey's book, `Entry and Exit Confessions of a Champion Trader <https://www.amazon.com/Entry-Exit-Confessions-Champion-Trader/dp/1095328557>`_.


We present the results for each strategy across all these exits. Please note the limitations of the backtests before
deciding to trade the ones that have 'good' results. 

Limitations
------------

Here are the current limitations of the project.

1. *No Multiprocessing*

   Given the number of strategies it would be wise to use Multiprocessing to speed up the results. 


2. *No Optimisation*

   In all the strategies default values were used. No attempt was made to get the 'best' parameters for the indicators, etc. 

3. *No Tick data* 

   Using tick data is the gold standard when backtesting a strategy. This was not used in the backtests 

4. *Walk Forward Analysis*

   No test were done to see if the strategies work out of sample.

5. *Deployment*

   Quite a bit of work has be done to get the strategies ready for deployment.

6. *No multi-timeframe or machine learning strategies*

   We kept to simple strategies. 

7. *Only EURUSD on 15 minute data*

   We used EURUSD on the 15-minute timeframe to run the backtests. The data starts from 2020-01-01 until 2022-12-31.
 
8. *Strategies are not automagically composable*

   You cannot take two strategies (i.e. entries) and form a new strategy and run a test.  

Source Code 
-----------

You can get access to all of the source code on this `Github repo <https://github.com/zeta-zetra/code>`_.


Contact
-------
You can reach me at the following email address: info at zetra dot io. Or you can post a comment on the `YouTube Channel <https://www.youtube.com/@zetratrading/featured>`_ or on this Reddit `post <https://www.reddit.com/r/Forex/comments/139kx1n/testing_strategies_using_python/>`_.

Disclaimer
----------
We want to emphasize that this is purely for educational purposes only. We do not offer any financial advice, recommendations, or make any guarantees of profit or success. Trading carries a risk of loss, and it is important to always consult with a qualified professional before making any trading decisions.



.. toctree::
   youtube/index
   books/index
   requests/index
   chatgpt/index
   blogs/index
   charts/index
   candlestick/index
   results
   references
   :maxdepth: 2
   :caption: Table of Contents






