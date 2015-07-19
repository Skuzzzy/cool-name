__author__ = 'dan'


# General

def is_exception(iadj):
    if 'いい' == iadj:
        return True
    # Space here
    return False


def fix_exception(iadj):  # Todo find a better way to handle i adj exceptions
    if 'いい' == iadj:
        return 'よい'
    return iadj

def stem(iadj):
    return iadj[0:-1]


def degree(iadj):
    return stem(iadj) + "さ"


def adverbial(iadj):
    return stem(iadj) + "く"


def conditional(iadj):
    return stem(iadj) + "ければ"


def negate_conditional(iadj):
    return conditional(negate(iadj))


def past_conditional(iadj):
    return past(iadj) + "ら"


def volitional(iadj):
    return stem(iadj) + "かろう"

# Plain


def plain(iadj):
    return iadj


def negate(iadj):
    return adverbial(iadj) + "ない"  # Aru


def past(iadj):
    return stem(iadj) + "かった"


def negate_past(iadj):
    return past(negate(iadj))


def te_form(iadj):
    return adverbial(iadj) + "て"


def negate_te_form(iadj):
    return te_form(negate(iadj))


# Formal


def plain_formal(iadj):
    return iadj + "です"


def negate_formal(iadj):
    return adverbial(iadj) + "ありません"  # Aru


def past_formal(iadj):
    return past(iadj) + "です"

def negate_past_formal(iadj):
    return adverbial(iadj) + "ありませんでした"  # Aru # OR 汚くなかった

def create_dictionary(iadj):
    dict = {}

    def plain_polite_dictionary(plain, polite):
        ppd = {"plain": plain, "polite": polite}
        return ppd

    dict['plain'] = plain_polite_dictionary(plain(iadj), plain_formal(iadj))
    dict['plain negative'] = plain_polite_dictionary(negate(iadj), negate_formal(iadj))
    dict['past'] = plain_polite_dictionary(past(iadj), past_formal(iadj))
    dict['past negative'] = plain_polite_dictionary(negate_past(iadj), negate_past_formal(iadj))
    dict['te form'] = {'plain': te_form(iadj)}
    dict['te form negative'] = {'plain': negate_te_form(iadj)}
    dict['conditional'] = {'plain': conditional(iadj)}
    dict['conditional negative'] = {'plain': negate_conditional(iadj)}
    dict['past conditional'] = {'plain': past_conditional(iadj)}
    dict['volitional'] = {'plain': volitional(iadj)}
    dict['causative'] = {'plain': "Todo"}  # TODO
    dict['causative negative'] = {'plain': "Todo"}  # TODO
    dict['causative passive'] = {'plain': "Todo"}  # TODO
    dict['causative passive negative'] = {'plain': "Todo"}  # TODO
    dict['degree'] = {'plain': degree(iadj)}
    dict['adverbial'] = {'plain': adverbial(iadj)}

    return dict

