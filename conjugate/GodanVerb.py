__author__ = 'dan'

import conjugate.IAdjective as IAdjective
import conjugate.IchidanVerb as IchidanVerb

vowel_table = {
    u"う": [u'い', u'わ', u'え', u'お'],
    u"つ": [u'し', u'た', u'て', u'と'],
    u"る": [u'り', u'ら', u'れ', u'ろ'],
    u"く": [u'き', u'か', u'け', u'こ'],
    u"ぐ": [u'ぎ', u'が', u'げ', u'ご'],
    u"ぶ": [u'び', u'ば', u'べ', u'ぼ'],
    u"む": [u'み', u'ま', u'め', u'も'],
    u"す": [u'し', u'さ', u'せ', u'そ']
}


def stem(godan):
    return godan[0:-1]


def get_i_sound(godan):
    last_char = godan[-1]
    return vowel_table[last_char][0]


def get_a_sound(godan):
    last_char = godan[-1]
    return vowel_table[last_char][1]


def get_e_sound(godan):
    last_char = godan[-1]
    return vowel_table[last_char][2]


def get_o_sound(godan):
    last_char = godan[-1]
    return vowel_table[last_char][3]


def get_te_form_ending(godan):
    last_char = godan[-1]
    return {
        'う': 'って',
        'つ': 'って',
        'る': 'って',
        'く': 'いて',
        'ぐ': 'いで',
        'ぶ': 'んで',
        'む': 'んで',
        'す': 'して'
    }[last_char]


def get_ta_form_ending(godan):
    return get_te_form_ending(godan).replace('て', 'た').replace('で', 'だ')


def plain(godan):  # !
    return godan


def plain_polite(godan):
    return stem(godan) + get_i_sound(godan) + "ます"  # !


def negate_plain(godan):
    return stem(godan) + get_a_sound(godan) + "ない"  # !


def negate_plain_polite(godan):  # !
    return stem(godan) + get_i_sound(godan) + "ません"


def past(godan):  # !
    return stem(godan) + get_ta_form_ending(godan)  # た・て


def past_polite(godan):  # !
    return stem(godan) + get_i_sound(godan) + "ました"  # た・て


def negate_past(godan):  # !
    return stem(godan) + get_a_sound(godan) + IAdjective.past("ない")


def negate_past_polite(godan):  # !
    return negate_plain_polite(godan) + "でした"


def te_form(godan):  # !
    return stem(godan) + get_te_form_ending(godan)  # た・て


def te_form_polite(godan):  # !
    return stem(godan) + get_i_sound(godan) + "まして"  # た・て


def negate_te_form(godan):  # !
    return IAdjective.te_form(negate_plain(godan))


def negate_te_form_polite(godan):  # !
    return negate_plain_polite(godan) + "で"  # な　te form similarity


def potential(godan):  # !
    return stem(godan) + get_e_sound(godan) + "る"


def potential_polite(godan):  # !
    return IchidanVerb.plain_polite(potential(godan))


def negate_potential(godan):  # !
    return IchidanVerb.negate_plain(potential(godan))


def negate_potential_polite(godan):  # !
    return IchidanVerb.negate_plain_polite(potential(godan))


def passive(godan):  # !
    return stem(godan) + get_a_sound(godan) + "れる"


def passive_polite(godan):  # !
    return IchidanVerb.plain_polite(passive(godan))


def negate_passive(godan):  # !
    return IchidanVerb.negate_plain(passive(godan))


def negate_passive_polite(godan):  # !
    return IchidanVerb.negate_plain_polite(passive(godan))


def causative(godan):  # !
    return stem(godan) + get_a_sound(godan) + 'せる'


def causative_polite(godan):  # !
    return IchidanVerb.plain_polite(causative(godan))


def negate_causative(godan):  # !
    return IchidanVerb.negate_plain(causative(godan))


def negate_causative_polite(godan):  # !
    return IchidanVerb.negate_plain_polite(causative(godan))


def volitional(godan):  # !
    return stem(godan) + get_o_sound(godan) + 'う'


def volitional_polite(godan):  # !
    return stem(godan) + get_i_sound(godan) + 'ましょう'


def provisional(godan):  # !
    return stem(godan) + get_e_sound(godan) + 'ば'


def create_dictionary(godan):
    dict = {}

    def plain_polite_dictionary(plain, polite):
        ppd = {"plain": plain, "polite": polite}
        return ppd

    dict['plain'] = plain_polite_dictionary(plain(godan), plain_polite(godan))
    dict['plain negative'] = plain_polite_dictionary(negate_plain(godan), negate_plain_polite(godan))
    dict['past'] = plain_polite_dictionary(past(godan), past_polite(godan))
    dict['past negative'] = plain_polite_dictionary(negate_past(godan), negate_past_polite(godan))
    dict['te form'] = plain_polite_dictionary(te_form(godan), te_form_polite(godan))
    dict['te form negative'] = plain_polite_dictionary(negate_te_form(godan), negate_te_form_polite(godan))
    dict['potential'] = plain_polite_dictionary(potential(godan), potential_polite(godan))
    dict['potential negative'] = plain_polite_dictionary(negate_potential(godan), negate_potential_polite(godan))

    dict['passive'] = plain_polite_dictionary(passive(godan), passive_polite(godan))
    dict['passive negative'] = plain_polite_dictionary(negate_passive(godan), negate_passive_polite(godan))

    dict['causative'] = plain_polite_dictionary(causative(godan), causative_polite(godan))
    dict['causative negative'] = plain_polite_dictionary(negate_causative(godan), negate_causative_polite(godan))

    dict['volitional'] = plain_polite_dictionary(volitional(godan), volitional_polite(godan))

    dict['provisional'] = plain_polite_dictionary(provisional(godan), 'TODO')
    return dict

# todo implement other methods