__author__ = 'dan'

import xml.etree.ElementTree as etree

kanji_dict = {}
hiragana_dict = {}

class element:
    def __init__(self, xml_element):
        self.ent_seq = xml_element.findall('ent_seq')[0].text  # 1
        self.k_ele = parse_k_ele_multiple(xml_element.findall('k_ele'))  # 0 or more
        self.r_ele = parse_r_ele_multiple(xml_element.findall('r_ele'))  # 1 or more
        self.sense = parse_sense_multiple(xml_element.findall('sense'))  # 1 or more
        print(self.ent_seq)
        print('\t' + str(self.k_ele))
        print('\t' + str(self.r_ele))
        print('\t' + str(self.sense))

def parse_k_ele_multiple(k_ele_multiple):
    elements = []
    for k_ele in k_ele_multiple:
        elements.append(parse_k_ele_single(k_ele))
    return elements

def parse_k_ele_single(k_ele):
    elements = []
    for subelement in k_ele:
        elements.append((subelement.tag, subelement.text))
    return elements


def parse_r_ele_multiple(r_ele_multiple):
    elements = []
    for r_ele in r_ele_multiple:
            elements.append(parse_r_ele_single(r_ele))
    return elements

def parse_r_ele_single(r_ele):
    elements = []
    for subelement in r_ele:
        elements.append((subelement.tag, subelement.text))
    return elements

def parse_sense_multiple(sense_multiple):
    elements = []
    for sense in sense_multiple:
            elements.append(parse_sense_single(sense))
    return elements

def parse_sense_single(sense):
    elements = []
    for subelement in sense:
        elements.append((subelement.tag, subelement.text))
    return elements

def default():
    parse_edict('static/JMdict_e.gz')

def parse_edict(file):
    tree = etree.parse(file)
    root = tree.getroot()
    for entry in root:
        read_edict_entry(entry)

def read_edict_entry(entry):
    element(entry)