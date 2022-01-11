# -*- coding: utf-8 -*-

import os, importlib
import copy
import argparse
from collections import defaultdict, Counter
import itertools
import sys

from pymorphy2 import MorphAnalyzer

import extra_info, ExtractionOfMorphology, RulesOfAgreement


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

module_info = os.path.join(ROOT_DIR, "extra_info.py")
module_morph = os.path.join(ROOT_DIR, "ExtractionOfMorphology.py")
module_rules = os.path.join(ROOT_DIR, "RulesOfAgreement.py")

morph_analyzer = MorphAnalyzer(lang='ru')

def is_all_str(the_list):
    for item in the_list:
        if isinstance(item, int):
            return False
    return True

def added_token(token):
    print(f'\n  Добавили {token}\n')

def get_str(element):
    new_repr = ''
    for variant in element:
        new_repr += str(variant)
        new_repr += '{'
        new_repr += ','.join([value for _, value in variant.__dict__.items() if value is not None])
        new_repr += '}\n '
    return new_repr

def print_result(all_clauses):

    #print(all_clauses)

    print('\n\nРЕЗУЛЬТАТ:')
    print('----------\n')

    if isinstance(all_clauses[0], tuple):
        
        length = len(all_clauses)
        for ind, clause in enumerate(all_clauses):
                
            #clause_pos = [item.pos_tag for item in clause]
            #clause_case = [item.case if item.pos_tag in extra_info.words_with_cases else '--' for item in clause]
            clause_str = [item.wordform for item in clause if not isinstance(item, str)]
            #print(' '.join(clause_pos))
            #print(' '.join(clause_case))
            print(' '.join(clause_str))
            if ind != length - 1:
                print('\n**********\n')
    else:
        length = 1
        print(all_clauses)


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

    print(f'Транскрипция, полученная на вход: \n\n{utterance}')
    utterance_splitted = utterance.strip().split(" ")

    print(f'\nСловарь: {ortho_dict_path}\n')

    for token in utterance_splitted:
        n_vowels = 0
        code = ord(token[0])
        # code = extra_info.ascii_chart[token[0]]
        for letter in token:
            if letter in extra_info.vowels_lat:
                n_vowels += 1
        trn_doc = os.path.join(ortho_dict_path,
                               "{0}_0_{1}.TRN".format(code, n_vowels))
        try:
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
                tokens = set((i[0], i[1]) for i in tokens_variants_dict[token])
                for token in tokens:
                    print(token, end=' ')
                #print(f'\nКоличество вариантов: {len(tokens)}\n')
                print()
        except FileNotFoundError:
            if token in tokens_variants_dict:
                pass
            else:
                print(f'{token} is not found anywhere')
    
    print(tokens_variants_list)
    if len(tokens_variants_list) != len(utterance_splitted):
        raise Exception('Some words forms are missing')
    

    #print(f'token dict {tokens_variants_dict}')

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
    #ortho_dict = "../data/dictionaries/GRANT-LX.utf"
    ortho_dict = "../data/dictionaries/FON-LX.utf"
    morpho_dict = "../data/dictionaries/GRANT-ME.utf"
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

    schema = ['' for i in range(len(token_list))]

    morph_tokens_variants, tokens_sequence = predict(token_list, morpho_dict)
    
    clause = [i for i, _ in enumerate(tokens_sequence)]

    buffer_dict = {}

    #print(f'seq is {tokens_sequence}')
    for ind, token in enumerate(tokens_sequence):
        buffer_dict[ind] = set()
        variants = morph_tokens_variants[token]
        if len(set(variants)) == 1:
            clause[ind] = variants[0]
            buffer_dict[ind].add(variants[0])

    print('\nВсе орфографические и морфологические варианты получены')
    print(f'\nКлауза: {" ".join([str(i) for i in clause])}')


    if is_all_str(clause):
        print_result(' '.join([word.wordform for word in clause]))
    else:
        print('\nПроверяем согласование соседних элементов')
        last = len(tokens_sequence) - 1
        for ind, word in enumerate(clause):
            if isinstance(word, int):
                str_buff_repr = ' '.join(['|'.join([str(w) for w in word]) if word else str(key) for key, word in buffer_dict.items()])
                print(f'\n\nКлауза: {str_buff_repr}')
        
                if ind < last:
                    if ind == 0:
                        print('\nПредыдущий элемент = \n')
                    else:
                        prev = morph_tokens_variants[tokens_sequence[ind-1]]
                        prev_el = get_str(prev)
                        print(f'\nПредыдущий элемент = {prev_el}\n')
                    el = morph_tokens_variants[tokens_sequence[ind]]
                    the_el = get_str(el)
                    print(the_el)
                    nex = morph_tokens_variants[tokens_sequence[ind+1]]
                    next_el = get_str(nex)
                    print(f'\nСледующий элемент: {next_el}\n')
                    next = clause[ind+1]
                    if not isinstance(next, int):
                        #print(token.__dict__)
                        for token in morph_tokens_variants[tokens_sequence[ind]]:
                            print('\n Если у словоформы тэг ITJ – пропускаем')
                            if token.pos_tag == 'ITJ':
                                continue
                            if next.pos_tag.startswith('V'):
                                print(('Если следующая словоформа – глагол, а у проверяемого элемента есть категория лица, проверяем согласование по лицу и числу'))
                                if hasattr(next, 'person'):
                                    if hasattr(token, 'person'):
                                        if next.person == token.person and next.number == token.number:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                            if next.pos_tag.startswith('AJ'):
                                print('\nЕсли следующая словоформа – прилагательное, а у проверяемого элемента есть падеж, проверяем согласование по падежу, числу и роду')
                                if hasattr(token, 'case'):
                                    if token.case == next.case and token.number == next.number and token.gender == next.gender:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                            if ind == 0:
                                if token.pos_tag == 'CJN':
                                    print('\nЕсли это первая позиция и проверяемый элемент – союз, добавляем')
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                if token.pos_tag == 'PNP' and token.person == '2p':
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if next.pos_tag == 'VV0':
                                if token.pos_tag.startswith('V'):
                                    print('\nЕсли проверяемый элемент – вспомогательный глагол, а следующий – причастие, проверяем согласование по роду')
                                    if next.number == 'sg':
                                        if  next.gender == token.gender:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                                    else:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                                if token.pos_tag.startswith('PN'):
                                    print('\nЕсли проверяемый элемент - местоимение в именительном падеже, а следующий – глагол, то проверяем согласование по лицу, числу')
                                    if (next.person == '0' or token.person == next.person) and token.number == next.number and token.case == 'nm':
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                            if ind == 0:
                                if token.pos_tag == 'PNS' and token.gender == 'n':
                                    print('\nЕсли проверяемый элемент – местоимение в среднем роде на первом месте в клаузе, добавляем')
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                if token.pos_tag == 'CJN':
                                    print('\nЕсли проверяемый элемент – союз на первом месте в клаузе, добавляем')
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                if token.pos_tag in ['PRT']:
                                    print('\nЕсли проверяемый элемент – PRT и он находится на первом месте в клаузе – добавляем')
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                if token.pos_tag == 'PAJ':
                                    print('\n Если проверяемый элемент – местоименное прилагательное, а следующий элемент – существительное, проверяем аогласование по падежу, числу и роду')
                                    if not isinstance(next, int) and next.pos_tag.startswith('NN'):
                                        if next.case == token.case and next.number == token.number:
                                            if next.number == 'sg':
                                                if next.gender == token.gender:
                                                    added_token(token)
                                                    buffer_dict[ind].add(token)
                                if token.pos_tag == 'PAJ' and (next.pos_tag.startswith('AJ') or next.pos_tag == 'PAJ'):
                                    print('\nЕсли проверяемый элемент – местоименное прилагательное, а следующий – (местоименное) прилагательное, проверяем согласование по числу, роду и падежу')
                                    if token.number == next.number and token.case == next.case:
                                        if token.number == 'sg':
                                            if token.gender == next.gender:
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                                        else:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                            if next.pos_tag.startswith('N'):
                                if token.pos_tag in ['PNS', 'PAJ']:
                                    print('Если следующий элемент – существительное, а проверяемый – местоименное прилагательное, то проверяем согласование по роду, числу и падежу')
                                    if next.number == 'sg':
                                        if next.number == token.number and next.case == token.case and next.gender == token.gender:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                                    else:
                                        if next.number == token.number and token.case == next.case:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                                if token.pos_tag.startswith('N') and next.case == '0':
                                    buffer_dict[ind].add(token)
                            if token.pos_tag.startswith('N'):
                                if next.pos_tag.startswith('V') and next.wordform != 'придё+тся':
                                    print('Если проверяемый элемент – существительное, а следующий – глагол, то проверяем согласование по роду (если прошедшее время), лицу и числу')
                                    if next.person == '3p':
                                        if (token.gender == next.gender or next.gender == '0') and token.number == next.number and token.case == 'nm':
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                                    if next.person == '0' and token.case == 'nm':
                                        buffer_dict[ind].add(token)
                            if token.pos_tag == 'PD0':
                                print('\nЕсли проверяемый элемент – PD0, добавляем')
                                added_token(token)
                                buffer_dict[ind].add(token)
                            if next.pos_tag == 'IPS':
                                print('\nЕсли проверяемый элемент – местоимение в дательном падеже, а следующий элемент – IPS')
                                if token.pos_tag == 'PNS' and token.case == 'dt':
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if ind > 0 and token.pos_tag == 'CJN' and token.wordform in ['и']:
                                print('\nЕсли проверяемый элемент – союз "и", проверяем, что предыдущий и следующий элементы – существительные и могут быть связаны')

                                key = list(morph_tokens_variants.keys())[ind-1]
                                for previous in morph_tokens_variants[key]:
                                    if (previous.pos_tag.startswith('N') and next.pos_tag.startswith('N')) and previous.case == next.case:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                            if token.wordform == 'ни+' and next.wordform == 'при':
                                buffer_dict[ind].add(token)
                            if token.pos_tag == 'PRP' and hasattr(next, 'case'):
                                print('\nЕсли проверяемый элемент – предлог, а следующий элемент имеет падеж, проверяем, могут ли они сочетаться')
                                if next.pos_tag.startswith('N') and next.case in extra_info.preposition_cases[str(token.wordform)]:
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                else:
                                    key = list(morph_tokens_variants.keys())[ind+1]
                                    for next in morph_tokens_variants[key]:
                                        if hasattr(next, 'case') and next.case in extra_info.preposition_cases[str(token)]:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                            if token.pos_tag == 'PRT' and ind > 0:
                                print('\nЕсли проверяемый элемент – частица, добавляем')
                                added_token(token)
                                buffer_dict[ind].add(token)
                            if token.pos_tag == 'PAJ' and next.pos_tag.startswith('V'):
                                print('\nЕсли проверяемый элемент – местоименное прилагательное, а следующий – глагол')
                                if next.tense == 'futr':
                                    if token.number == next.number:
                                        added_token(token)
                                        buffer_dict[ind].add(token) 
                            if token.pos_tag == 'VV0' and token.gender == '0' and token.person == '0':
                                print('\nЕсли проверяемый элемент – безличный глагол, а следующий – местоимение в косвенном падеже, добавляем')
                                if next.pos_tag.startswith('PN') and next.case != 'nm':
                                    added_token(token)
                                    buffer_dict[ind].add(token) 
                            
                            
                    else:
                        for token in morph_tokens_variants[tokens_sequence[ind]]:
                            if token.pos_tag == 'ITJ':
                                continue
                            if token.pos_tag in ['PRT']:
                                print('\nЕсли следующий элемент пока неизвестен, а проверяемый – частица, добавляем')
                                added_token(token)
                                buffer_dict[ind].add(token)
                            if token.pos_tag == 'PRP':
                                print('\nЕсли проверяемый элемент – предлог, а следующий элемент имеет падеж, проверяем, могут ли они сочетаться')
                                form = token.wordform
                                key = list(morph_tokens_variants.keys())[ind+1]
                                for next in morph_tokens_variants[key]:
                                    if next.pos_tag.startswith('N') or next.pos_tag.startswith('P'):
                                        if hasattr(next, 'case') and next.case in extra_info.preposition_cases[form]:
                                            added_token(token)
                                            added_token(next)
                                            buffer_dict[ind].add(token)
                                            buffer_dict[ind+1].add(next)
                            if token.pos_tag.startswith('N'):
                                key = list(morph_tokens_variants.keys())[ind+1]
                                print('\nЕсли проверяемый элемент  – существительное, а следующий – местоименное прилагательное, проверяем их согласование по числу, роду и падежу')
                                for next in morph_tokens_variants[key]:
                                    if next.pos_tag == 'PAJ' and token.case == next.case and token.number == next.number:
                                        if token.number == 'sg':
                                            if token.gender == next.gender:
                                                added_token(token)
                                                added_token(next)
                                                buffer_dict[ind].add(token)
                                                buffer_dict[ind+1].add(next)
                                        else:
                                            added_token(token)
                                            added_token(next)
                                            buffer_dict[ind].add(token)
                                            buffer_dict[ind+1].add(next)
                            if token.pos_tag == 'PAJ':
                                print('\nЕсли проверяемый элемент  – местоименное прилагательное, а следующий – существительное, проверяем их согласование по числу, роду и падежу')
                                key = list(morph_tokens_variants.keys())[ind+1]
                                for next in morph_tokens_variants[key]:
                                    if next.pos_tag.startswith('NN'):
                                        if next.number == token.number and token.case == next.case:
                                            if next.number == 'sg' and next.gender == token.gender:
                                                buffer_dict[ind].add(token)

                if ind > 0: 
                    previous = clause[ind-1]
                    if isinstance(previous, int):
                        if len(buffer_dict[ind-1]) > 0:
                            previous = list(buffer_dict[ind-1])[0]
                        else:
                            pass
                    if not isinstance(previous, int):
                        if ind == 0:
                            print('\nПредыдущий элемент = \n')
                        else:
                            prev = morph_tokens_variants[tokens_sequence[ind-1]]
                            prev_el = get_str(prev)
                            print(f'\nПредыдущий элемент = {prev_el}\n')
                        el = morph_tokens_variants[tokens_sequence[ind]]
                        the_el = get_str(el)
                        print(the_el)
                        if ind + 1 < last:
                            nex = morph_tokens_variants[tokens_sequence[ind+1]]
                            next_el = get_str(nex)
                            print(f'\nСледующий элемент = {next_el}\n')
                        else:
                            print('\nСледующий элемент = ')
                        
                        for token in morph_tokens_variants[tokens_sequence[ind]]:
                            if token.pos_tag.startswith('N') and previous.pos_tag == 'PAJ':
                                print('Если следующий элемент – существительное, а проверяемый – местоименное прилагательное, то проверяем согласование по роду, числу и падежу')
                                if token.number == previous.number and token.case == previous.number:
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                                key = list(morph_tokens_variants.keys())[ind-1]
                                key2 = list(morph_tokens_variants.keys())[ind]
                                from_buff = buffer_dict.get(ind-1, None)
                                vars = from_buff if from_buff is not None else morph_tokens_variants[key]
                                for previous in vars:
                                    for token in morph_tokens_variants[key2]:
                                        if hasattr(token, 'case') and token.case == previous.case and token.number == previous.number:
                                            if token.number == 'sg':
                                                if token.gender == previous.gender:
                                                    added_token(token)
                                                    buffer_dict[ind].add(token)
                                            else:
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                            if token.pos_tag.startswith('N') and previous.pos_tag.startswith('N'):
                                print('\nЕсли проверяемый элемент – существительное в родительном падеже, а предыдущий – существительное')
                                if token.pos_tag == 'ITJ':
                                    continue
                                if token.case.startswith('g'):
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('V') and previous.wordform.startswith('в'):
                                if hasattr(token, 'case') and ('c' in token.case) and token.pos_tag.startswith('N'):
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('AJ'):
                                print('\nЕсли у проверяемого элемента есть падеж, а предыдущий – прилагательное, провеярем их согласование по падежу, числу и роду')
                                if hasattr(token, 'case'):
                                    if token.case == previous.case and token.number == previous.number and token.gender == previous.gender:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('V') and token.pos_tag.startswith('NN'):
                                print('\nЕсли проверяемыый элемент – существительное в локативе, а предыдущий – глагол, добавляем')
                                if token.case == 'in':
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('A') and hasattr(previous, 'number'):
                                if token.pos_tag.startswith('N'):
                                    print('\nЕсли проверяемый элемент – существительное, а предыдущий – прилагательное, проверяем их согласование по роду, числу и падежу')
                                    if previous.number == 'sg':
                                        if token.case == previous.case and token.number == previous.number and token.gender == previous.gender:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                                        else:
                                            key = list(morph_tokens_variants.keys())[ind-1]
                                            for other in morph_tokens_variants[key]:
                                                if token.case == other.case and token.number == other.number and token.gender == other.gender:
                                                    added_token(token)
                                                    buffer_dict[ind].add(token)
                                    if previous.number == 'pl':
                                        if token.case == previous.case and token.number == previous.number:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                            if previous.pos_tag == 'PNP':
                                if token.pos_tag.startswith('V') or token.pos_tag.startswith('AJ'):
                                    print('\nЕсли предыдущий элемент – PNP, а следующий – глагол или прилагательное, проверяем согласование по числу и падеж')
                                    if previous.number == token.number and previous.case in ['nm', 'ac', 'ac2']:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                            if token.pos_tag == 'AJ0' and token.shortness == 'sht':
                                    if previous.number == 'sg' and previous.pos_tag.startswith('N'):
                                        if token.number == previous.number and token.gender == previous.gender:
                                            if previous.case == 'nm':
                                                print('\nЕсли проверяемый элемент – AJ0 в краткой форме, а предыдущий – существительное в номинативе, то проверяем согласование по числу и роду')
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('V') or previous.pos_tag == 'PNS':
                                print('Если предыдущий элемент – глагол, а проверяемый – частица, добавляем')
                                if token.pos_tag == 'PRT':
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('N') and previous.case == 'nm':
                                if token.pos_tag.startswith('V'):
                                    if token.tense == 'past':
                                        print('\nЕсли проверяемый элемент – глагол в прошедшем времени, а предыдущий – существительное в номинативе, проверяем согласование по роду и числу')
                                        if previous.gender == token.gender and previous.number == token.number:
                                            added_token(token)
                                            buffer_dict[ind].add(token)
                            if previous.pos_tag == 'PAJ' and token.pos_tag.startswith('N'):
                                print('\nЕсли предыдущий элемент – местоименное прилагательное, а проверяемый – существительное, проверяем их согласование по роду, числу и падежу')
                                if previous.number == 'pl' and token.number == 'pl':
                                    if previous.case == token.case:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                                else:
                                    if previous.number == token.number and previous.case == token.case and previous.gender == token.gender:
                                        added_token(token)
                                        buffer_dict[ind].add(token)
                                key = list(morph_tokens_variants.keys())[ind-1]
                                for previous in morph_tokens_variants[key]:
                                    if previous.pos_tag == 'PAJ':
                                        if previous.number == token.number and previous.case == token.case:
                                            if previous.number == 'sg' and previous.gender == token.gender:
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                                            else:
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                            if previous.pos_tag == 'CJN':
                                pass
                            if previous.wordform == 'при' and token.wordform == 'чё+м':
                                buffer_dict[ind].add(token)
                            if previous.wordform == 'и' and token.wordform == 'е+сли':
                                buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('V'):
                                if token.pos_tag == 'PNS' and token.person == token.gender and token.case == '0':
                                    print('\nЕсли предшествующий элемент – глагол, а проверяемый – местоимение в косвенном падеже')
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag == 'PRT':
                                if token.pos_tag == 'PNP':
                                    if not isinstance(next, int) and next.pos_tag.startswith('NN'):
                                        if token.number == next.number and token.case == next.case:
                                            print('\nЕсли предыдущий элемент – частица, проверяемый – местоимение, а следующий – существительное, проверяем согласование по роду, числу и падежу')
                                            if token.number == 'sg':
                                                if token.gender == next.gender:
                                                    added_token(token)
                                                    buffer_dict[ind].add(token)
                                            else:
                                                added_token(token)
                                                buffer_dict[ind].add(token)
                            if previous.pos_tag == 'PRP':
                                print('\nЕсли предыдущий элемент – предлог, а следующий – существительное – проверяем, могут ли они сочетаться')
                                if token.pos_tag.startswith('N') and token.case in extra_info.preposition_cases[str(previous.wordform)]:
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag.startswith('N') and token.pos_tag.startswith('PN'):
                                print('\nЕсли предыдущий элемент – существительное, а проверяемый – местоимение в дательном падеже, добавляем')
                                if previous.case != token.case and token.case == 'dt':
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if previous.pos_tag == 'CW2' and token.pos_tag.startswith('NN'):
                                print('\nЕсли предыдущий элемент – составная словоформа (существительное), а проверяемый – существительное в родительном падеже, добавляем')
                                if token.case.startswith('gn'):
                                    added_token(token)
                                    buffer_dict[ind].add(token)
                            if hasattr(previous, 'case') and previous.case != 'nm' and token.pos_tag.startswith('VV0'):
                                if token.tense is None and token.person is None:
                                    print('\nЕсли предыдущий элемент – часть речи, имеющая падеж, в косвенном падеже, а проверяемый – инфинитив, добавляем')
                                    added_token(token)
                                    buffer_dict[ind].add(token)

                            

        to_combine = []
        for i in range(len(tokens_sequence)):
            to_combine.append(buffer_dict.get(i))

        all_clauses = list(itertools.product(*to_combine))
        print_result(all_clauses)

            

main()