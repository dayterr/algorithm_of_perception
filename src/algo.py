# -*- coding: utf-8 -*-

import os, imp
import copy
import argparse
from collections import defaultdict, Counter
import itertools
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

module_info = os.path.join(ROOT_DIR, "extra_info.py")
module_morph = os.path.join(ROOT_DIR, "ExtractionOfMorphology.py")
module_rules = os.path.join(ROOT_DIR, "RulesOfAgreement.py")

extra_info = imp.load_source('extra_info', module_info)
ExtractionOfMorphology = imp.load_source('ExtractionOfMorphology', module_morph)
RulesOfAgreement = imp.load_source('RulesOfAgreement', module_rules)


def print_result(all_clauses):
    length = len(all_clauses)

    print('\n----------')
    print('РЕЗУЛЬТАТ:')
    print('----------\n')

    for ind, clause in enumerate(all_clauses):
            
        clause_pos = [item.pos_tag for item in clause]
        clause_case = [item.case if item.pos_tag in extra_info.words_with_cases else '--' for item in clause]
        clause_str = [item.wordform for item in clause]
        print(' '.join(clause_pos))
        print(' '.join(clause_case))
        print(' '.join(clause_str))
        if ind != length - 1:
            print('\n**********\n')

    print('\n----------')
    print(f'ВСЕГО ВАРИАНТОВ: {length}')
    print('----------')


def get_args():
    ''' Reads the command line options
    '''
    my_desc = 'Parsing an input utterance to get its possible morphological ' \
              'discriptions.'
    parser = argparse.ArgumentParser(description=my_desc)
    parser.add_argument('--input', '-i', help='A file with an input utterance' \
                        'in SAMPA transcription.',
                        required=False)
    parser.add_argument('--output', '-o', help='A file name for writing output.',
                        required=False)
    parser.add_argument('--morpho-dict', '-md', help='Morphological dictionary.',
                        required=False)
    parser.add_argument('--ortho-dict', '-od', help='Transcription-Orthogragphy.',
                        required=False)
    parser.add_argument('--predicate', '-pred', action='store_true',
                        help='Analyze with the predicate.', required=False)
    parser.add_argument('--left2right', '-l2r', action='store_true',
                        help='Analyze with word pairs, word-by-word.', required=False)
    args = parser.parse_args()

    return args


class TokenWithVariants:
    ''' Документация в разработке...'''

    def __init__(self, audio_word, potential_variants):
        """ Конструктор для создания экземпляра класса - токена.
        Каждый токен содержит репрезентацию в транскрипции и список
        потенциально возможных орфографических вариантов для данной транскрипции.

        :param audio_word: слово в транскрипции
        :param potential_variants:список с орфографическими вариантами
        """
        self.audio_word = audio_word
        self.potential_variants = potential_variants
    
    def __str__(self):
        return self.audio_word
    
    def __repr__(self):
        return self.audio_word


def get_tokens(utterance, ortho_dict_path):

    tokens_variants_dict = defaultdict(list)
    tokens_variants_list = []

    for token in utterance.strip().split(" "):
        n_vowels = 0
        code = ord(token[0])
        # code = extra_info.ascii_chart[token[0]]
        for letter in token:
            if letter in extra_info.vowels_lat:
                n_vowels += 1
        trn_doc = os.path.join(ortho_dict_path,
                               "{0}_0_{1}.TRN".format(code, n_vowels))

        with open(trn_doc, "r", encoding="utf-8") as trn_fin:
            for pronunc_var in trn_fin.readlines():
                pronunc_var = pronunc_var.strip().split(" ")
                if pronunc_var[0] == token:
                    variants = pronunc_var[1][1:-1].split("|")
                    variants = [(v[:-1].split("<")[0],
                                 v[:-1].split("<")[1]) for v in variants]
                    tokens_variants_dict[token] = variants
                    token_instance = TokenWithVariants(token, variants)
                    tokens_variants_list.append(token_instance)

    return tokens_variants_dict, tokens_variants_list


def predict(tokens_variants, morpho_dict_path):
    ''' Данная функция принимает на вход список экземпляров класса TokenWithVariants,
    обращается к методу get_morph_info и преобразует передаваемый список в словарь,
    где ключом является аудио-токен, а значения - список с экземплярами классов
    соответствующих частей речи. Т.е. каждый вариант содержит всю морфологическую информацию,
    записанную в виде атрибутов, к которой легко обратиться.

    :param list od TokenWithVariants instances
    :return: dictionary: key=token; value=list of POS class instances
    '''
    # for i in tokens_variants:
    morph_tokens_variants = ExtractionOfMorphology.MorphoDescription().get_morph_info(
        tokens_variants, morpho_dict_path)
    # print(morph_tokens_variants)
    return morph_tokens_variants


def main():

    input_file = 'input.txt'
    output_file = "./output.txt"
    ortho_dict = "../data/dictionaries/GRANT-LX.utf"
    morpho_dict = "../data/dictionaries/GRANT-M.utf"
    left2right = False
    with_predicate = True

    agens = False
    quasiagens = False

    # Get the command line options:
    args = get_args()

    if args.input:
        input_file = args.input
    if args.output:
        output_file = args.output
    if args.morpho_dict:
        morpho_dict = args.morpho_dict
    if args.ortho_dict:
        ortho_dict = args.ortho_dict
    if args.left2right:
        left2right = args.left2right
    if args.predicate:
        with_predicate = args.predicate

    input_utt = open(input_file, "r").read()
    token_dict, token_list = get_tokens(input_utt, ortho_dict)
    print(token_list)

    # здесь все возможнеы клаузы
    all_clauses = [] 
    
    schema = ['' for i in range(len(token_list))]

    morph_tokens_variants, tokens_sequence = predict(token_list, morpho_dict)

    #валентности субъекта
    subj_valences = ['agens', 'quasiagens']
    #
    adj_cases = ['' ,'in']

    predicates = []
    predicates2 = []
    adverbs = []
    nouns = []
    pairs = []
    adjectives = []
    prepositions = []
    fillers = []

    subj_indexes = []
    verb_indexes = []
    valences_indexes = []

    persons = ['1p', '2p', '3p']
    numbers = ['sg', 'pl']

    for ind, i in enumerate(token_list):
        for variant in morph_tokens_variants[str(i)]:
            if (variant.pos_tag in extra_info.pos_dict['verb'] or variant.pos_tag in extra_info.pos_dict['verb_aux']) and variant.wordform in extra_info.verb_to_be.keys():
                # сначала найдём все финитные формы глаголов и запишем их в предикаты
                print(variant)
                verb_indexes.append(ind)
                predicates.append((ind, variant))
            if variant.pos_tag in extra_info.syntactic_roles['adverb']:
                adverbs.append((ind, variant))
            if variant.pos_tag in extra_info.syntactic_roles['subj_obj']:
                if hasattr(variant, 'valence'):
                    if variant.valence in subj_valences:
                        subj_indexes.append(ind)
                nouns.append((ind, variant))
            if variant.pos_tag in extra_info.syntactic_roles['adjective']:
                if variant.valence == 'adjective':
                    if variant.case is not None:
                        if variant.case.startswith('n'):
                            subj_indexes.append(ind)
                adjectives.append((ind, variant)) 
            if variant.pos_tag in extra_info.syntactic_roles['preposition']:
                prepositions.append((ind, variant))
            if  variant.pos_tag in extra_info.syntactic_roles['filler']:
                fillers.append((ind, variant))









    if __name__ == '__main__':
        main()