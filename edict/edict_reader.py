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

        for pos in self.get_part_of_speech():
            if 'Ichidan verb' in pos:
                # self.print_info()
                self.add_self_to_dictionary()
                break
        for pos in self.get_part_of_speech():
            if 'Godan verb' in pos:
                # self.print_info()
                self.add_self_to_dictionary()
                break

    def add_self_to_dictionary(self):
        for each in self.get_kanji_representations():
            kanji_dict[each] = self
        for each in self.get_hiragana_representations():
            kanji_dict[each] = self

    def print_info(self):
        print(self.ent_seq)
        print('\t' + str(self.k_ele))
        print('\t' + str(self.r_ele))
        print('\t' + str(self.sense))
        print('\t' + str(self.get_kanji_representations()))
        print('\t' + str(self.get_hiragana_representations()))
        print('\t' + str(self.get_part_of_speech()))


    def get_kanji_representations(self):
        elements = []
        for k_ele_list in self.k_ele:
            for k_element in k_ele_list:
                if k_element[0] == 'keb':
                    elements.append(k_element[1])
        return elements

    def get_hiragana_representations(self):
        elements = []
        for r_ele_list in self.r_ele:
            for r_element in r_ele_list:
                if r_element[0] == 'reb':
                    elements.append(r_element[1])
        return elements

    def get_part_of_speech(self):
        elements = []
        for sense_list in self.sense:
            for sense_element in sense_list:
                if sense_element[0] == 'pos':
                    elements.append(sense_element[1])
        return elements


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

def load():
    parse_edict('static/JMdict_e.gz')

def parse_edict(file):
    tree = etree.parse(file)
    root = tree.getroot()
    for entry in root:
        read_edict_entry(entry)

def read_edict_entry(entry):
    element(entry)