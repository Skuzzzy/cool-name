__author__ = 'dan'

import conjugate.IchidanVerb as IchidanVerb

import unittest


class TestIchidanVerbMethods(unittest.TestCase):

    def test_all(self):
        ichidan = "食べる"
        self.assertEqual("食べる", IchidanVerb.plain(ichidan))
        self.assertEqual("食べます", IchidanVerb.plain_polite(ichidan))
        self.assertEqual("食べない", IchidanVerb.negate_plain(ichidan))
        self.assertEqual("食べません", IchidanVerb.negate_plain_polite(ichidan))
        self.assertEqual("食べた", IchidanVerb.past(ichidan))
        self.assertEqual("食べました", IchidanVerb.past_polite(ichidan))
        self.assertEqual("食べなかった", IchidanVerb.negate_past(ichidan))
        self.assertEqual("食べませんでした", IchidanVerb.negate_past_polite(ichidan))
        self.assertEqual("食べて", IchidanVerb.te_form(ichidan))
        self.assertEqual("食べまして", IchidanVerb.te_form_polite(ichidan))
        self.assertEqual("食べられる", IchidanVerb.potential(ichidan))
        self.assertEqual("食べられます", IchidanVerb.potential_polite(ichidan))
        self.assertEqual("食べられない", IchidanVerb.negate_potential(ichidan))
        self.assertEqual("食べられません", IchidanVerb.negate_potential_polite(ichidan))


if __name__ == '__main__':
    unittest.main()