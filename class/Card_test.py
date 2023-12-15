#!/usr/bin/python3

from __future__ import print_function, division

import unittest
from Card import Card, Deck


class Test(unittest.TestCase):

    def testDeckRemove(self):
        deck = Deck()
        card23 = Card(2, 3)
        #card23 = Card(5, 3) Get ERROR
        deck.remove_card(card23)

if __name__ == "__main__":
    unittest.main()
