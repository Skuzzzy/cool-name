__author__ = 'dan'
import conjugate.IAdjective as IAdjective
import conjugate.NaAdjective as NaAdjective
import conjugate.IchidanVerb as IchidanVerb
import conjugate.GodanVerb as GodanVerb
import utils.charset_utility as charset_utility
import edict.edict_reader as edict
import json

def get_verb_json(verb):

    verb_tuple = charset_utility.get_kanji_hiragana_romaji_tuple(verb)

    entry = edict.dict[verb]
    if entry is None:
        return None
    parts_of_speech = entry.get_part_of_speech()
    for pos in parts_of_speech:
        if 'Ichidan verb' == pos:
            print(verb + ' is an　一段 verb')
            return json.dumps({'kanji':IchidanVerb.create_dictionary(verb_tuple[0]), 'hiragana':IchidanVerb.create_dictionary(verb_tuple[1])}, ensure_ascii=False).encode('utf8'), 200
        if 'verb' in pos:  # If we get past ichidan and it's still a verb then it's godan
            print(verb + ' is an　五段 verb')
            return json.dumps({'kanji':GodanVerb.create_dictionary(verb_tuple[0]), 'hiragana':GodanVerb.create_dictionary(verb_tuple[1])}, ensure_ascii=False).encode('utf8'), 200
    return None  # If we fall through something went wrong, passibly a non verb was passed in


def get_i_adjective_json(iadj):
    return json.dumps(IAdjective.create_dictionary(iadj), ensure_ascii=False).encode('utf8')


def get_na_adjective_json(naadj):
    return json.dumps(NaAdjective.create_dictionary(naadj), ensure_ascii=False).encode('utf8')