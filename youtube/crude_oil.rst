Pullback Strategy
===================

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

.. image:: /_static/images/pullback-crude.png
  :target: /_static/images/pullback-crude.png
  :width: 1080
  :alt: Pullback Crude Signal Points


Results 
-------

.. image:: /_static/results/pullback-crude.png
   :target: /_static/results/pullback-crude.png
   :width: 1080
   :height: 500
   :alt: Pullback Crude Results


Source Code 
-----------

Here is the link to the source code for this `strategy <https://github.com/zeta-zetra/code>`_.
