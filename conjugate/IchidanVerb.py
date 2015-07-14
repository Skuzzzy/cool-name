__author__ = 'dan'

import conjugate.IAdjective as IAdjective


#  I form and stem are the same for Ichidan verbs
def stem(ichidan):
    return ichidan[0:-1]


def plain(ichidan):
    return ichidan


def plain_polite(ichidan):
    return stem(ichidan) + "ます"


def negate_plain(ichidan):
    return stem(ichidan) + "ない"


def negate_plain_polite(ichidan):
    return stem(ichidan) + "ません"


def past(ichidan):
    return stem(ichidan) + "た"  # た・て


def past_polite(ichidan):
    return stem(ichidan) + "ました"  # た・て


def negate_past(ichidan):
    return stem(ichidan) + IAdjective.past("ない")


def negate_past_polite(ichidan):
    return negate_plain_polite(ichidan) + "でした"


def te_form(ichidan):
    return stem(ichidan) + "て"  # た・て


def te_form_polite(ichidan):
    return stem(ichidan) + "まして"  # た・て


def negate_te_form(ichidan):
    return IAdjective.te_form(negate_plain(ichidan))


def negate_te_form_polite(ichidan):
    return negate_plain_polite(ichidan) + "で"  # な　te form similarity


def potential(ichidan):
    return stem(ichidan) + "られる"


def potential_polite(ichidan):
    return plain_polite(potential(ichidan))


def negate_potential(ichidan):
    return negate_plain(potential(ichidan))


def negate_potential_polite(ichidan):
    return negate_plain_polite(potential(ichidan))



# todo implement other methods
