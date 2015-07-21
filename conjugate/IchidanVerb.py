__author__ = 'dan'

import conjugate.IAdjective as IAdjective

#  I form and stem are the same for Ichidan verbs
def stem(ichidan):
    return ichidan[0:-1]


def plain(ichidan):  # !
    return ichidan


def plain_polite(ichidan):
    return stem(ichidan) + "ます"  # !


def negate_plain(ichidan):
    return stem(ichidan) + "ない"  # !


def negate_plain_polite(ichidan):  # !
    return stem(ichidan) + "ません"


def past(ichidan):  # !
    return stem(ichidan) + "た"  # た・て


def past_polite(ichidan):  # !
    return stem(ichidan) + "ました"  # た・て


def negate_past(ichidan):  # !
    return stem(ichidan) + IAdjective.past("ない")


def negate_past_polite(ichidan):  # !
    return negate_plain_polite(ichidan) + "でした"


def te_form(ichidan):  # !
    return stem(ichidan) + "て"  # た・て


def te_form_polite(ichidan):  # !
    return stem(ichidan) + "まして"  # た・て


def negate_te_form(ichidan):  # !
    return IAdjective.te_form(negate_plain(ichidan))


def negate_te_form_polite(ichidan):  # !
    return negate_plain_polite(ichidan) + "で"  # な　te form similarity


def potential(ichidan):  # !
    return stem(ichidan) + "られる"


def potential_polite(ichidan):  # !
    return plain_polite(potential(ichidan))


def negate_potential(ichidan):  # !
    return negate_plain(potential(ichidan))


def negate_potential_polite(ichidan):  # !
    return negate_plain_polite(potential(ichidan))


def passive(ichidan):
    return stem(ichidan) + "られる"  # Note, for ichidan verbs the passive is identical to the potential


def passive_polite(ichidan):  # !
    return plain_polite(passive(ichidan))


def negate_passive(ichidan):  # !
    return negate_plain(passive(ichidan))


def negate_passive_polite(ichidan):  # !
    return negate_plain_polite(passive(ichidan))


def create_dictionary(ichidan):
    dict = {}

    def plain_polite_dictionary(plain, polite):
        ppd = {"plain": plain, "polite": polite}
        return ppd

    dict['plain'] = plain_polite_dictionary(plain(ichidan), plain_polite(ichidan))
    dict['plain negative'] = plain_polite_dictionary(negate_plain(ichidan), negate_plain_polite(ichidan))
    dict['past'] = plain_polite_dictionary(past(ichidan), past_polite(ichidan))
    dict['past negative'] = plain_polite_dictionary(negate_past(ichidan), negate_past_polite(ichidan))
    dict['te form'] = plain_polite_dictionary(te_form(ichidan), te_form_polite(ichidan))
    dict['te form negative'] = plain_polite_dictionary(negate_te_form(ichidan), negate_te_form_polite(ichidan))
    dict['potential'] = plain_polite_dictionary(potential(ichidan), potential_polite(ichidan))
    dict['potential negative'] = plain_polite_dictionary(negate_potential(ichidan), negate_potential_polite(ichidan))

    dict['passive'] = plain_polite_dictionary(passive(ichidan), passive_polite(ichidan))
    dict['passive negative'] = plain_polite_dictionary(negate_passive(ichidan), negate_passive_polite(ichidan))
    return dict

# todo implement other methods