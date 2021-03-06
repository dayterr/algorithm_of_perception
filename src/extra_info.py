#!/usr/bin/env python 3
# -*- coding:utf-8 -*-


vowels_lat = ["@", "Q", "a", "e", "i", "o", "u", "y"]
vowels_cyr = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']


dos_code = {'А': 128, 'Б': 129, 'В': 130, 'Г': 131, 'Д': 132, 'Е': 133,
            'Ж': 134, 'З': 135, 'И': 136, 'Й': 137, 'К': 138, 'Л': 139,
            'М': 140, 'Н': 141, 'О': 142, 'П': 143, 'Р': 144, 'С': 145,
            'Т': 146, 'У': 147, 'Ф': 148, 'Х': 149, 'Ц': 150, 'Ч': 151,
            'Ш': 152, 'Щ': 153, 'Ъ': 154, 'Ы': 155, 'Ь': 156, 'Э': 157,
            'Ю': 158, 'Я': 159, 'а': 160, 'б': 161, 'в': 162, 'г': 163,
            'д': 164, 'е': 165, 'ж': 166, 'з': 167, 'и': 168, 'й': 169,
            'к': 170, 'л': 171, 'м': 172, 'н': 173, 'о': 174, 'п': 175,
            'р': 224, 'с': 225, 'т': 226, 'у': 227, 'ф': 228, 'х': 229,
            'ц': 230, 'ч': 231, 'ш': 232, 'щ': 233, 'ъ': 234, 'ы': 235,
            'ь': 236, 'э': 237, 'ю': 238, 'я': 239, 'Ё': 240, 'ё': 241}


words_with_cases = ['NN0', 'NP1', 'NP2', 'NP3', 'NGS', 'NUC', 'NNS', 'NNP',
                    'AJ0', 'PAJ', 'AJU', 'PAP', 'AUX', 'PNN', 'PNS', 'PNP']


pos_dict = {'noun': ['NN0', 'NP1', 'NP2', 'NP3', 'NGS', 'NUC', 'NNS', 'NNP'],
            'pronoun': ['PNN', 'PNS', 'PNP'],
            'adjective': ['AJ0', 'PAJ', 'AJU', 'PAP'],
            'adj_superlatives': ['AJS', 'APS', 'AJP'],
            'adj_analytical': ['AJA'],
            'verb': ['VV0', 'VVG'],
            'verb_aux': ['VAX'],
            'verb_unclassified': ['VUC'],
            'verb_inf': ['VVI'],
            'verb_impers': ['IPS'],
            'adverb': ['AV0'],
            'functional': ['AUX'],
            'numeral': ['CRD', 'ORD', 'CNU'],
            'predicative': ['PD0'],
            'interjection': ['ITJ'],
            'conjunction': ['CJN'],
            'intro': ['PTH'],
            'connectedWords': ['BWR', 'CW1=PTH', 'CW1', 'CW2'],
            'preposition': ['PRP'],
            'particles': ['PRT'],
            'pronoun_numeral': ['PNU'],
            'pronoun_adverb': ['PAV'],
            'pronoun_pred': ['PPD'],
            'aplphabeticLetter': ['ZZ0'],
            }

syntactic_roles = {'subj_obj': ['NN0', 'NP1', 'NP2', 'NP3', 'NGS', 'NUC',
                                'NNS', 'NNP', 'PNN', 'PNS', 'PNP', 'PNU',
                                'CRD', 'ORD', 'CNU'],
                   'adjective': ['AJ0', 'PAJ', 'AJU', 'PAP', 'AJS', 'APS',
                                 'AJP', 'AJA'],
                   'functional': ['AUX', 'BWR'],
                   'predicate': ['VV0', 'VVG', 'VAX', 'VUC', 'VVI', 'IPS'],
                   'predicate_2': ['VVI'],
                   'predicative': ['PD0', 'PPD'],
                   'adverb': ['AV0', 'PAV'],
                   'filler': ['ITJ', 'CJN', 'PTH', 'PRT'],
                   'preposition': ['PRP']
                   }

preposition_cases = {'перед': ['in'],
                     'ввиду^': ['gn', 'g2', 'g3'],
                     'относи+тельно': ['gn', 'g2', 'g3'],
                     'кро^ме': ['gn', 'g2', 'g3'],
                     'про': ['ac', 'a2'],
                     'через': ['ac', 'a2'],
                     'пре+жде': ['gn', 'g2', 'g3'],
                     'до': ['gn', 'g2', 'g3'],
                     'по^сле': ['gn', 'g2', 'g3'],
                     'для': ['gn', 'g2', 'g3'],
                     'ко': ['dt'],
                     'всле+д': ['dt'],
                     'по': ['dt'],
                     'соотве+тственно': ['dt'],
                     'про^тив': ['gn', 'g2', 'g3'],
                     'к': ['dt'],
                     'о': ['lc', 'l2'],
                     'ми^мо': ['gn', 'g2', 'g3'],
                     'при': ['lc', 'l2'],
                     'из-з': ['gn', 'g2', 'g3'],
                     'ра+ди': ['gn', 'g2', 'g3'],
                     'от': ['gn', 'g2', 'g3'],
                     'поря+дка': ['gn', 'g2', 'g3'],
                     'во': ['lc', 'l2', 'ac'],
                     'без': ['gn', 'g2', 'g3'],
                     'у': ['gn', 'g2', 'g3'],
                     'из-за': ['gn', 'g2', 'g3'],
                     'из': ['gn', 'g2', 'g3'],
                     'ми+мо': ['gn', 'g2', 'g3'],
                     'со': ['in'],
                     'ме^жду': ['in'],
                     'вы+ше': ['gn', 'g2', 'g3'],
                     'под': ['ac', 'a2', 'in'],
                     'на': ['ac', 'a2', 'lc', 'l2'],
                     'за': ['in', 'ac'],
                     'се+вернее': ['gn', 'g2', 'g3'],
                     'путё+м': ['gn', 'g2', 'g3'],
                     'о^коло': ['gn', 'g2', 'g3'],
                     'ти+па': ['gn', 'g2', 'g3'],
                     'об': ['lc', 'l2'],
                     'навстре+чу': ['lc', 'l2'],
                     'внизу+': ['gn', 'g2', 'g3'],
                     'среди^': ['gn', 'g2', 'g3'],
                     'вперё+д': ['gn', 'g2', 'g3'],
                     'над': ['in'],
                     'благодаря+': ['dt'],
                     'впереди+': ['gn', 'g2', 'g3'],
                     'ме^ж': ['in'],
                     'вокру^г': ['gn', 'g2', 'g3'],
                     'с': ['in'],
                     'вро^де': ['gn', 'g2', 'g3'],
                     'поперё+к': ['gn', 'g2', 'g3'],
                     'поми+мо': ['gn', 'g2', 'g3'],
                     'вме^сто': ['gn', 'g2', 'g3'],
                     'в': ['lc', 'l2', 'ac']
                     }

with_prepositions = {'не+й': ['к', 'с', 'о', 'за', 'перед', 'по', 'при',
                             'ме^жду', 'над', 'под'],
                     'неё': ['у', 'про', 'относительно', 'за', 'из-за', 'под',
                             'около', 'кро^ме', 'через', 'пре+жде', 'до',
                             'по^сле', 'для', 'про^тив', 'ми^мо', 'ми+мо',
                             'ра+ди', 'от', 'в', 'без', 'на', 'ти+па', 'об',
                             'внизу+', 'среди^', 'вперё+д', 'впереди+', 'вро^де',
                             'поми+мо', 'вме^сто', 'с'],
                     'ни+м': ['к', 'с', 'за', 'перед', 'ме^жду', 'над', 'под'],
                     'нему+': ['к', 'по'],
                     'нём': ['о', 'при'],
                     'него+': ['у', 'про', 'относительно', 'за', 'из-за', 'под',
                             'около', 'кро^ме', 'через', 'пре+жде', 'до',
                             'по^сле', 'для', 'про^тив', 'ми^мо', 'ми+мо',
                             'ра+ди', 'от', 'в', 'без', 'на', 'ти+па', 'об',
                             'внизу+', 'среди^', 'вперё+д', 'впереди+', 'вро^де',
                             'поми+мо', 'вме^сто', 'с'],
                     'ни+ми': ['с', 'за', 'перед', 'ме^жду', 'над', 'под'],
                     'ни+х': ['у', 'про', 'относительно', 'за', 'из-за', 'под',
                             'около', 'кро^ме', 'через', 'пре+жде', 'до',
                             'по^сле', 'для', 'про^тив', 'ми^мо', 'ми+мо',
                             'ра+ди', 'от', 'в', 'без', 'на', 'ти+па', 'об',
                             'внизу+', 'среди^', 'вперё+д', 'впереди+', 'вро^де',
                             'поми+мо', 'вме^сто', 'с'],
                     }

non_prep_pronoms = ['его', 'его+', 'её', 'их', 'и+х', 'ей', 'е+й', 'ему', 'ему+']

valence = ['nm', 'gn', 'g2', 'g3', 'dt', 'd2', 'ac', 'a2', 'in', 'lc', 'l2', 'vo', '0']

#добавлено
#словарь для форм глагола "быть" и их валентностей
verb_to_be = {'е+сть': ['quasiagens', 'place', 'nominal_part', 'posession', 'posessor', 'object', 'adjective'], 'быть': [], 
'бы+ли': ['quasiagens', 'nominal_part', 'time_when', 'adjective', 'object'], 'была+': ['quasiagens', 'nominal_part', 'time_when', 'adjective'], 
'бу+дь': ['quasiagens', 'price'], 'бы+ло': ['quasiagens', 'object'], 'бы+л': ['adjective'], 'бу+ду': ['agens', 'role', 'quasiagens'],
'бу+дет': ['quasiagens', 'place'], 'бу+дут': ['quasiagens']}
preps_valence = {'у': ['posessor'], 'в': ['place'],}
cases_valence = {'dt': ['posessor'], 'lc': ['place'],}
