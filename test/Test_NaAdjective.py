__author__ = 'dan'

import conjugate.NaAdjective as NaAdjective

import unittest


class TestNaAdjectiveMethods(unittest.TestCase):

    def test_all(self):
        naadj = "元気な"
        self.assertEqual("元気だ", NaAdjective.plain(naadj))
        self.assertEqual("元気じゃない", NaAdjective.negate(naadj))
        self.assertEqual("元気だった", NaAdjective.past(naadj))
        self.assertEqual("元気じゃなかった", NaAdjective.negate_past(naadj)) # IS THIS RIGHT??
        self.assertEqual("元気で", NaAdjective.te_form(naadj))
        self.assertEqual("元気じゃなくて", NaAdjective.negate_te_form(naadj))
        self.assertEqual("元気です", NaAdjective.plain_formal(naadj))
        self.assertEqual("元気じゃありません", NaAdjective.negate_formal(naadj))
        self.assertEqual("元気でした", NaAdjective.past_formal(naadj))
        self.assertEqual("元気じゃありませんでした", NaAdjective.negate_past_formal(naadj))

if __name__ == '__main__':
    unittest.main()
