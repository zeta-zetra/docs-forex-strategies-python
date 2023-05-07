Pullback Strategy
==================

This strategy was developed to be applied to `crude oil <https://www.youtube.com/watch?v=bdi6zQ7g-r4&t>`_. Now, we have applied it to the forex market. 

Buy Rules 
---------

1. Current close greater than current open.

2. Current close less than close 200 periods ago.

3. Current close is greater than close 20 periods ago.

4. Current close is less than close 10 periods ago.


Sell Rules
----------

1. Current close less than current open.

2. Current close greater than close 200 periods ago.

3. Current close is less than close 20 periods ago.

4. Current close is greater than close 10 periods ago.


Sample of Signal Points 
-----------------------

.. image:: _build/_static/images/strategy-2.png
  :target: _build/_static/images/strategy-2.png
  :width: 1080
  :alt: Pullback - Crude Oil Signal Points


Results 
-------

.. csv-table:: Table 3 : Pullback for EURUSD (2020-01-1-01 until 2022-12-31)
   :file: _build/_static/results/result-strategies-limited-2.csv
   :header-rows: 1


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.
