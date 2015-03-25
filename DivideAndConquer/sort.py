"""
xinyulrsm@gmail.com

sort from large to small by divide in conquer algorithm
"""

import unittest


def DCsort(myList):
    if len(myList) == 1:
        return myList

    midPoint = len(myList) / 2

    leftList = DCsort(myList[:midPoint])
    rightList = DCsort(myList[midPoint:])

    return DCmerge(leftList, rightList)


def DCmerge(LL, RL):

    # store merged list
    res = []
    # left list cursor
    Lcur = 0
    # right list cursor
    Rcur = 0

    while Lcur < len(LL) and Rcur < len(RL):
        if LL[Lcur] >= RL[Rcur]:
            res += [LL[Lcur]]
            Lcur += 1
        else:
            res += [RL[Rcur]]
            Rcur += 1
    if Lcur == len(LL) and Rcur < len(RL):
        res += RL[Rcur:]

    if Lcur < len(LL) and Rcur == len(RL):
        res += LL[Lcur:]

    return res


class DCsortTest(unittest.TestCase):
    def testLessOne(self):
        cal = DCsort([1.5, 2.0, 1.7, 0.26])
        real = [2.0, 1.7, 1.5, 0.26]
        self.assertEquals(cal, real)

        cal = DCsort([1.5, 2.0, 1.7, 1.7, 0.26])
        real = [2.0, 1.7, 1.7, 1.5, 0.26]
        self.assertEquals(cal, real)

if __name__ == '__main__':
    unittest.main()
