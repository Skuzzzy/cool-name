__author__ = 'dan'

import conjugate.IAdjective as IAdjective

# General


def stem(naadj):
    return naadj[0:-1]


def degree(naadj):  # !
    return stem(naadj) + "さ"


def adverbial(naadj):  # !
    return stem(naadj) + "に"


def provisional(naadj):  # !
    return stem(naadj) + "なら"


def conditional(naadj):  # !
    return provisional(naadj) + "(ば)"


def negate_conditional(naadj):
    return IAdjective.conditional(negate(naadj))


def volitional(naadj):  # !
    return plain(naadj) + "ろう"

# Plain


def plain(naadj):  # !
    return stem(naadj) + "だ"


def negate(naadj):  # !
    return stem(naadj) + "じゃ" + "ない"  # TODO SEE OTHER JYA


def past(naadj):  # !
    return plain(naadj) + "った"


def negate_past(naadj):  # !
    return IAdjective.past(negate(naadj))


def te_form(naadj):  # !
    return stem(naadj) + "で"


def negate_te_form(naadj):  # !
    return IAdjective.te_form(negate(naadj))


# Formal


def plain_formal(naadj):  # !
    return stem(naadj) + "です"


def negate_formal(naadj):  # !
    return stem(naadj) + "じゃ" + "ありません"  # TODO SEE OTHER JYA


def past_formal(naadj):  # !
    return stem(naadj) + "でした"

def negate_past_formal(naadj): #!
    return past_formal(negate_formal(naadj) + " ")  # space is a fix for routing through two stem calls

def create_dictionary(naadj):
    dict = {}

    def plain_polite_dictionary(plain, polite):
        ppd = {"plain": plain, "polite": polite}
        return ppd

    dict['plain'] = plain_polite_dictionary(plain(naadj), plain_formal(naadj))
    dict['plain negative'] = plain_polite_dictionary(negate(naadj), negate_formal(naadj))
    dict['past'] = plain_polite_dictionary(past(naadj), past_formal(naadj))
    dict['past negative'] = plain_polite_dictionary(negate_past(naadj), negate_past_formal(naadj))
    dict['te form'] = {'plain': te_form(naadj)}
    dict['te form negative'] = {'plain': negate_te_form(naadj)}
    dict['conditional'] = plain_polite_dictionary(conditional(naadj), "Todo")  # Todo
    dict['conditional negative'] = {'plain': negate_conditional(naadj)}
    dict['volitional'] = plain_polite_dictionary(volitional(naadj), "Todo")  # Todo
    dict['causative'] = plain_polite_dictionary("Todo", "Todo")  # Todo
    dict['causative negative'] = plain_polite_dictionary("Todo", "Todo")  # Todo
    dict['causative passive negative'] = plain_polite_dictionary("Todo", "Todo")  # Todo
    dict['degree'] = {'plain': degree(naadj)}
    dict['adverbial'] = {'plain': adverbial(naadj)}

    return dict
