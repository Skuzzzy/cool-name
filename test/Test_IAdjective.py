__author__ = 'dan'

import conjugate.IAdjective as IAdjective

import unittest


class TestIAdjectiveMethods(unittest.TestCase):

    def test_all(self):
        iadj = "煩い"
        self.assertEqual("煩い", IAdjective.plain(iadj))
        self.assertEqual("煩くない", IAdjective.negate(iadj))
        self.assertEqual("煩かった", IAdjective.past(iadj))
        self.assertEqual("煩くなかった", IAdjective.negate_past(iadj))
        self.assertEqual("煩くて", IAdjective.te_form(iadj))
        self.assertEqual("煩くなくて", IAdjective.negate_te_form(iadj))
        self.assertEqual("煩いです", IAdjective.plain_formal(iadj))
        self.assertEqual("煩くありません", IAdjective.negate_formal(iadj))
        self.assertEqual("煩かったです", IAdjective.past_formal(iadj))

if __name__ == '__main__':
    unittest.main()
