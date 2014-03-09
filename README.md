Anime picture tester
====================

This program tests if a picture is a real photo or from anime based on neural network techniques.
The main idea of this program is that anime pictures and real photos differ in their color range.

In our given data set, it showed 95%+ accuracy.

    $ pip install numpy neurolab PIL
    $ python main.py
    File path:test1.jpg
    [ -4.85186913e-09]
    Real picture
    $ python main.py
    File path:test2.jpg
    [ 1.]
    Anime picture


