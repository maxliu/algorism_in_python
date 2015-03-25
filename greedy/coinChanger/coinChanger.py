"""

Coin change by greedy algorism

xinyulrsm@gmail.com
"""
import unittest

coinDic = {25:"Quarter",  10:"Dime", 5:"Nickel", 1:"Penny"}


def getChange(amount, coinDic=coinDic):
    """

    it is trouble to compare float, convert to int for comparison

    """
    remain = int(100 * amount)

    for coin in reversed(sorted(coinDic.keys())):
        while remain >= coin:
            #print remain, coin
            yield coinDic[coin]
            remain -= coin


class changeConverterTest(unittest.TestCase):
    def testLessOne(self):
        cal = list(getChange(0.26))
        real = [coinDic[v] for v in [25, 1]]
        #print cal
        #print real
        self.assertEquals(cal, real)
        cal = list(getChange(0.37))
        real = [coinDic[v] for v in [25, 10, 1, 1]]
        #print cal
        #print real
        self.assertEquals(cal, real)

if __name__ == '__main__':
    unittest.main()
