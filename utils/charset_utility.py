__author__ = 'dan'
import edict.edict_reader as edict
import re
import romkan


def get_kanji_hiragana_romaji_tuple(word):

    contains_kanji = check_if_contains_kanji(word)

    if contains_kanji:
        kanji = word
        hiragana = get_hiragana(word)
    else:
        kanji = get_kanji(word)
        hiragana = word

    romaji = romanize(hiragana)

    return (kanji, hiragana, romaji)


def check_if_contains_kanji(word):
    regexp = re.compile(r'[\u4e00-\u9faf]')  # todo precompile this regex
    if regexp.search(word) is not None:
        return True
    else:
        return False


def get_kanji(word):
    return edict.dict[word].get_kanji_representations()[0]


def get_hiragana(word):
    return edict.dict[word].get_hiragana_representations()[0]


def romanize(word):
    return romkan.to_hepburn(word)