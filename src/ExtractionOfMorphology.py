import re
import os
import extra_info

""" 16 POS classes: noun, pronoun, adjective, verb, participle, gerund, adverb,
numeral, predicate, interjection, preposition, conjunction, intro,
connectedWords, particles, aplphabeticLetter

35 POS labels: see extra_info.pos_dict
"""


class Noun:
    """Существительное"""

    def __init__(self, wordform, pos_tag, gender, animateness, number,
                 case, frequency, valence=None):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.gender = gender
        self.animateness = animateness
        self.number = number
        self.case = case
        self.frequency = frequency
        self.valence = valence

    def __repr__(self):
        return self.wordform

    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Pronoun:
    """Местоимение"""

    def __init__(self, wordform, pos_tag, person, gender, animateness, number,
                 case, frequency, valence):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.person = person
        self.gender = gender
        self.animateness = animateness
        self.number = number
        self.case = case
        self.frequency = frequency
        self.valence = valence

    def __repr__(self):
        return self.wordform

    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Adjective:
    """Прилагательное"""

    def __init__(self, wordform, pos_tag, shortness, number, gender,
                 case, frequency, valence):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.shortness = shortness
        self.number = number
        self.gender = gender
        self.case = case
        self.frequency = frequency
        self.valence = valence

    def __repr__(self):
        return self.wordform

    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Verb:
    """Глагол"""

    def __init__(self, wordform, pos_tag, aspect, transitivity, voice, mood,
                 tense, number, person, gender, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.aspect = aspect
        self.transitivity = transitivity
        self.voice = voice
        self.mood = mood
        self.tense = tense
        self.number = number
        self.person = person
        self.gender = gender
        self.frequency = frequency
    
    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Participle:
    """Причастие"""

    def __init__(self, wordform, pos_tag, aspect, transitivity, voice,
                 shortness, tense, number, gender, case, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.aspect = aspect
        self.transitivity = transitivity
        self.voice = voice
        self.shortness = shortness
        self.tense = tense
        self.number = number
        self.gender = gender
        self.case = case
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Gerund:
    """Деепричастие"""

    def __init__(self, wordform, pos_tag, aspect, transitivity, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.aspect = aspect
        self.transitivity = transitivity
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform

    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Adverb:
    """Наречие"""

    def __init__(self, wordform, pos_tag, comparative, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.comparative = comparative
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Numeral:
    """Числительное"""

    def __init__(self, wordform, pos_tag, number, animateness,
                 gender, case, frequency, valence):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.number = number
        self.animateness = animateness
        self.gender = gender
        self.case = case
        self.frequency = frequency
        self.valence = valence
    
    def __repr__(self):
        return self.wordform

    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Predicate:
    """Предикат"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Interjection:
    """Междометие"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Preposition:
    """Предлог"""

    def __init__(self, wordform, pos_tag, frequency):  # valences
        self.wordform = wordform
        self.pos_tag = pos_tag
        # self.valences = valences
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Conjunction:
    """Союз"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Intro:
    """Вводное слово"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class ConnectedWords:
    """Слитное слово"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency
        #self.case = case
    
    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class Particle:
    """Частица"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency

    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class AlphabeticLetter:
    """Буква"""

    def __init__(self, wordform, pos_tag, frequency):
        self.wordform = wordform
        self.pos_tag = pos_tag
        self.frequency = frequency
    
    def __str__(self):
        return self.wordform

    def __repr__(self):
        return self.wordform
    
    def __hash__(self):
        return hash(self.wordform)

    def __eq__(self, other):
        return self.wordform is self.wordform


class MorphoDescription:

    def fill_tags(self, word, morph_info, frequency):
        """ Parse the string with the morphological information;
            analyse different POSs separately.
        """
        morph_info = morph_info.split(',')
        #print(f'morph_info is {morph_info}')
        pos_tag = morph_info[0][:3]

        # pos_start = re.search(r'[A-Z0-9]{3,4}', pos_tag).start()
        # pos_end = re.search(r'[A-Z0-9]{3,4}', pos_tag).end()
        # pos_tag = pos_tag[pos_start:pos_end]
        # print(pos_tag)
        # gender = morph_info[1]
        # animateness = morph_info[2]
        # number = morph_info[3]
        # case = morph_info[4]

        if pos_tag in extra_info.pos_dict["noun"]:
            """рассматриваем существительное,
            сохраняем основные характеристики из строки
                <словоформа>{<часть речи>=<частеречн. маркер>,<род>,
                <одушевленность>=,<число>,<падеж>}"""
            gender_of_variant = morph_info[1]
            animateness_of_variant = morph_info[2]
            number_of_variant = morph_info[3]
            case_of_variant = morph_info[4][0:2]
            valence = None
            if len(morph_info) > 5:
                valence = morph_info[5]
            variant = Noun(word, pos_tag, gender_of_variant,
                           animateness_of_variant, number_of_variant,
                           case_of_variant, frequency, valence)
            return variant

        if pos_tag in extra_info.pos_dict["pronoun"]:
            """рассматриваем местоимение,
            сохраняем основные характеристики из строки
                <словоформа>{<часть речи>=<частеречн. маркер>,<лицо>,<род>,
                <одушевленность>=,<число>,<падеж>} """
            person_of_variant = morph_info[1]
            gender_of_variant = morph_info[2]
            animateness_of_variant = morph_info[3]
            number_of_variant = morph_info[4]
            case_of_variant = morph_info[5][0:2]
            #добавлено
            valence = None
            if len(morph_info) > 6:
                valence = morph_info[6]
            variant = Pronoun(word, pos_tag, person_of_variant,
                              gender_of_variant, animateness_of_variant,
                              number_of_variant, case_of_variant, frequency, valence)
            return variant

        if pos_tag in extra_info.pos_dict["adjective"]:
            """ рассматриваем прилагательное,
            сохраняем основные характеристики из строкис общим  видом
                < словоформа > { < часть речи == AJ0 =, < краткость >, < число >, < род >, < падеж >}"""
            shortness_of_variant = morph_info[1]
            number_of_variant = morph_info[2]
            gender_of_variant = morph_info[3]
            case_of_variant = morph_info[4][0:2]
            valence = None
            if len(morph_info) > 5:
                valence = morph_info[5]
            variant = Adjective(word, pos_tag, shortness_of_variant,
                                number_of_variant, gender_of_variant,
                                case_of_variant, frequency, valence)
            return variant

        if pos_tag in extra_info.pos_dict["adj_superlatives"]:
            """ рассматриваем прилагательное(в превосходной степени, притяжательное,
            имеющее только мн.ч.), сохраняем основные характеристики из строки с общим  видом
                <словоформа>{<часть речи>=ТЕГ=,0,<число>,<род>,<падеж>}"""
            shortness_of_variant = morph_info[1]
            number_of_variant = morph_info[2]
            gender_of_variant = morph_info[3]
            case_of_variant = morph_info[4][0:2]
            valence = None
            variant = Adjective(word, pos_tag, shortness_of_variant,
                                number_of_variant, gender_of_variant,
                                case_of_variant, frequency, valence)
            return variant

        if pos_tag in extra_info.pos_dict["functional"]:
            """ рассматриваем СЛУЖЕБНЫЕ СЛОВА (более, менее, самый и т.п.),
            сохраняем основные характеристики из строки  с общим  видом:
                самый    – <словоформа>{<часть речи>=AUX=,<число>,<род>,<падеж>}
                более     – <словоформа>{<часть речи>=AUX=,0,0,0}
                пусть     – <словоформа>{<часть речи>=AUX=,0,0,0}
            """
            shortness_of_variant = None
            number_of_variant = morph_info[1]
            gender_of_variant = morph_info[2]
            case_of_variant = morph_info[3][0:2]
            valence = None
            variant = Adjective(word, pos_tag, shortness_of_variant,
                                number_of_variant, gender_of_variant,
                                case_of_variant, frequency, valence)
            return variant

        if pos_tag in extra_info.pos_dict["adj_analytical"]:
            """ рассматриваем аналитическое прилагательное,
            сохраняем основные характеристики из строки с общим  видом
                плащ–-палатка (пла+щ-{пла+щ-=AJA}"""
            shortness_of_variant = None
            number_of_variant = None
            gender_of_variant = None
            case_of_variant = None
            variant = Adjective(word, pos_tag, shortness_of_variant,
                                number_of_variant, gender_of_variant,
                                case_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["verb"]:
            """рассматриваем глагол,
            сохраняем основные характеристики из строки вида
                <словоформа>{<часть речи>=VV0,<вид>,<переходность>=,<залог>,
                <наклонен.>,<время>,<число>,<лицо>,<род>}"""
            if morph_info[2].__contains__('tran=VVI') or morph_info[2].__contains__('intr=VVI'):
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = morph_info[3][0:1]
                mood_of_variant = None
                tense_of_variant = None
                number_of_variant = None
                person_of_variant = None
                gender_of_variant = None
                variant = Verb(word, pos_tag, aspect_of_variant,
                               transitivity_of_variant, voice_of_variant,
                               mood_of_variant, tense_of_variant,
                               number_of_variant, person_of_variant,
                               gender_of_variant, frequency)
            elif morph_info[2].__contains__('VVP'):
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = morph_info[3][0:1]
                shortness_of_variant = morph_info[4]
                tense_of_variant = morph_info[5]
                number_of_variant = morph_info[6]
                gender_of_variant = morph_info[7]
                case_of_variant = morph_info[8]
                variant = Participle(word, pos_tag, aspect_of_variant,
                                     transitivity_of_variant, voice_of_variant,
                                     shortness_of_variant, tense_of_variant,
                                     number_of_variant, gender_of_variant,
                                     case_of_variant, frequency)
            elif morph_info[2].__contains__('VVG'):
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = None
                mood_of_variant = None
                tense_of_variant = None
                number_of_variant = None
                person_of_variant = None
                gender_of_variant = None
                variant = Verb(word, pos_tag, aspect_of_variant,
                               transitivity_of_variant, voice_of_variant,
                               mood_of_variant, tense_of_variant,
                               number_of_variant, person_of_variant,
                               gender_of_variant, frequency)
            else:
                # print(morph_info)
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = morph_info[3]
                mood_of_variant = morph_info[4]
                tense_of_variant = morph_info[5]
                number_of_variant = morph_info[6]
                person_of_variant = morph_info[7]
                gender_of_variant = morph_info[8][0:1]
                variant = Verb(word, pos_tag, aspect_of_variant,
                               transitivity_of_variant, voice_of_variant,
                               mood_of_variant, tense_of_variant,
                               number_of_variant, person_of_variant,
                               gender_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["verb_aux"]:
            """рассматриваем вспомогательный глагол в форме,
            сохраняем основные характеристики из строки вида
                <словоформа>{<часть речи>=VAX,<вид>,<переходность> =,<залог>,
                <наклонен.>,<время>,<число>,<лицо>,<род>}"""
            aspect_of_variant = morph_info[1]
            transitivity_of_variant = morph_info[2]
            voice_of_variant = None
            mood_of_variant = None
            tense_of_variant = None
            number_of_variant = None
            person_of_variant = morph_info[3][0:1]
            gender_of_variant = None
            variant = Verb(word, pos_tag, aspect_of_variant,
                           transitivity_of_variant, voice_of_variant,
                           mood_of_variant, tense_of_variant,
                           number_of_variant, person_of_variant,
                           gender_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["verb_unclassified"]:
            """рассматриваем вспомогательный глагол в форме,
            сохраняем основные характеристики из строки вида
                рабо+тал{рабо+тать=VUC,impf,tran=,act,sbjn,0,sg,0,m} или
                рабо+тать{рабо+тать=VUC,impf,tran=VVI,0}<изготовить> """
            if morph_info[2].__contains__("VVI"):
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = morph_info[3]
                mood_of_variant = None
                tense_of_variant = None
                number_of_variant = None
                person_of_variant = None
                gender_of_variant = None
            else:
                aspect_of_variant = morph_info[1]
                transitivity_of_variant = morph_info[2]
                voice_of_variant = morph_info[3]
                mood_of_variant = morph_info[4]
                tense_of_variant = morph_info[5]
                number_of_variant = morph_info[6]
                person_of_variant = morph_info[7][0:1]
                gender_of_variant = morph_info[8]

            variant = Verb(word, pos_tag, aspect_of_variant,
                           transitivity_of_variant, voice_of_variant,
                           mood_of_variant, tense_of_variant,
                           number_of_variant, person_of_variant,
                           gender_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["verb_impers"]:
            """рассматриваем глагол в форме инфинитива,
            сохраняем основные характеристики из строки вида
                <словоформа>{<часть речи>=IPS,<вид>,<переходность>=VVI,0}"""
            aspect_of_variant = morph_info[1]
            transitivity_of_variant = morph_info[2]
            voice_of_variant = None
            mood_of_variant = None
            tense_of_variant = None
            number_of_variant = None
            person_of_variant = morph_info[3][0:1]
            gender_of_variant = None
            variant = Verb(word, pos_tag, aspect_of_variant,
                           transitivity_of_variant, voice_of_variant,
                           mood_of_variant, tense_of_variant,
                           number_of_variant, person_of_variant,
                           gender_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["adverb"] or \
                pos_tag in extra_info.pos_dict["pronoun_adverb"]:
            """рассматриваем наречие,
            сохраняем основные характеристики из строки вида
                <словоформа>{<часть речи>=AV0=}, сравнительная степень: <словоформа>{<часть речи>=AV0=AVC}
            """
            if len(morph_info) > 1:
                if len(morph_info[2]) > 1:
                    comparative_of_variant = morph_info[2][0:2]
            else:
                comparative_of_variant = None
            variant = Adverb(word, pos_tag, comparative_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["numeral"]:
            """Рассматриваем числительные"""
            if pos_tag == 'CRD':
                """количественные числительные с характеристиками,
                представленными в виде строки:
                    <словоформа>{<часть речи>=CRD=,<род>,<падеж>}
                """
                number_of_variant = None
                animateness_of_variant = None
                gender_of_variant = morph_info[1]
                case_of_variant = morph_info[2][0:2]
                valence = None
                if len(morph_info) > 8:
                    valence = morph_info[8]
                variant = Numeral(word, pos_tag, number_of_variant,
                                  animateness_of_variant,
                                  gender_of_variant, case_of_variant, frequency, valence)
                return variant

            if pos_tag == 'ORD':
                """порядковые числительные с характеристиками,
                представленными в виде строки:
                    <словоформа>{<часть речи>=ORD=,<число>,<род>,<падеж>} """
                number_of_variant = morph_info[1]
                animateness_of_variant = None
                gender_of_variant = morph_info[2]
                case_of_variant = morph_info[3][0:2]
                variant = Numeral(word, pos_tag, number_of_variant,
                                  animateness_of_variant,
                                  gender_of_variant, case_of_variant, frequency, valence=None)
                return variant
            if pos_tag == 'CNU':
                """собирательные числительные с характеристиками,
                представленными в виде строки:
                    <словоформа>{<часть речи>=CNU=,<одушевленность>,<падеж>}"""
                number_of_variant = None
                animateness_of_variant = morph_info[1]
                gender_of_variant = None
                case_of_variant = morph_info[2][0:2]
                variant = Numeral(word, pos_tag, number_of_variant,
                                  animateness_of_variant,
                                  gender_of_variant, case_of_variant, frequency)
                return variant

        if pos_tag in extra_info.pos_dict["predicative"]:
            """предикативы с характеристиками, представленными в виде строки:
                <словоформа>{<часть речи>=PD0=}"""
            variant = Predicate(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["pronoun_pred"]:
            """ с характеристиками, представленными в виде строки:
                <словоформа>{<часть речи>=PD0=}"""
            person_of_variant = None
            gender_of_variant = None
            animateness_of_variant = None
            number_of_variant = None
            case_of_variant = None
            variant = Pronoun(word, pos_tag, person_of_variant,
                              gender_of_variant, animateness_of_variant,
                              number_of_variant, case_of_variant, frequency, valence=None)
            return variant

        if pos_tag in extra_info.pos_dict["interjection"]:
            """междометия с характеристиками, представленными в виде строки:
                <словоформа>{<часть речи>=ITJ}"""
            variant = Interjection(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["conjunction"]:
            """союзы с характеристиками, представленными в виде строки:
                <словоформа>{<часть речи>=ITJ}"""
            variant = Conjunction(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["intro"]:
            """Вводные слова с характеристиками, представленными в виде строки:
            <словоформа>{<часть речи>=PTH}"""
            variant = Intro(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["connectedWords"] and 'BWR' in pos_tag:
            """Связанные слова(англо-, немецко-, тёмно-, буро-, турко-, греко-) с характеристиками,
             представленными в виде строки: <словоформа>{<часть речи==ловоформа>=BWR}
             се+веро-{се+веро-=BWR}  1"""
            word = morph_info[1][:len(morph_info) - 2]
            variant = Intro(word, pos_tag, frequency)
            return variant
        
        if pos_tag in extra_info.pos_dict["connectedWords"]:
            variant = ConnectedWords(word, pos_tag, frequency)
            return variant


        if pos_tag in extra_info.pos_dict["preposition"]:
            """предлоги с характеристиками, представленными в виде строки:
            <словоформа>{<часть речи>=PRP}"""
            # valences = morph_info[1][0:2]
            variant = Preposition(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["particles"]:
            """частица с характеристиками, представленными в виде строки:
             <словоформа>{<часть речи>=PRT}"""
            variant = Particle(word, pos_tag, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["pronoun_numeral"]:
            """местоимения–числительные  с характеристиками, представленными в виде строки:
             <словоформа>{<часть речи>=PNU=,<падеж>}"""
            person_of_variant = None
            gender_of_variant = morph_info[1]
            animateness_of_variant = None
            number_of_variant = None
            case_of_variant = None
            variant = Pronoun(word, pos_tag, person_of_variant,
                              gender_of_variant, animateness_of_variant,
                              number_of_variant, case_of_variant, frequency, valence=None)
            return variant

        if pos_tag in extra_info.pos_dict["pronoun_pred"]:
            """местоимения–предикативы  с характеристиками, представленными в виде строки:
             <словоформа>{<часть речи>=PPD}"""
            person_of_variant = None
            gender_of_variant = None
            animateness_of_variant = None
            number_of_variant = None
            case_of_variant = None
            variant = Pronoun(word, pos_tag, person_of_variant,
                              gender_of_variant, animateness_of_variant,
                              number_of_variant, case_of_variant, frequency)
            return variant

        if pos_tag in extra_info.pos_dict["aplphabeticLetter"]:
            """буква алфавита с характеристиками, представленными в виде строки:
             <словоформа>{<часть речи>=ZZ0}"""
            variant = AlphabeticLetter(word, pos_tag, frequency)
            return variant

    @staticmethod
    def get_morph_file(word, directory):
        dos_code = extra_info.dos_code
        vowel_letters = extra_info.vowels_cyr
        letter_code = dos_code.get(word[0])
        n_vowels = 0
        stressed_vowel_pos = 0

        for i in word:
            if i.lower() in vowel_letters:
                n_vowels += 1
            elif (word[word.index(i) - 1].lower() in vowel_letters) and i == '+':
                stressed_vowel_pos = n_vowels

        return os.path.join(directory,
                            "{0}_{1}_{2}.mrf".format(str(letter_code),
                                                     str(stressed_vowel_pos),
                                                     str(n_vowels)))

    @staticmethod
    def get_morph_info(tokens_variants, morph_dict_path):
        """Эта функция достает морфологию вариантов произнесенного слова из файлов
        с морфологией, и помещает ее в экземпляры класса Variant.
        В результате чего каждый вариант нашего слова
        становится 'капсулой', инстансом класса, с морфологической информацией

        :param self:
        :param tokens_variants: список экземпляров, в каждом из которых
        есть атрибут слово - строка, и атрибут - список вариантов
        :return: тот же список, но уже для каждого слова вариант является не строкой,
        а экземпляром класса с атрибутами,
        соответствующими определенной морфологической информации
        """

        morph_tokens_variants = {}
        tokens_sequence = [token.audio_word for token in tokens_variants]

        for token in tokens_variants:
            variants = token.potential_variants

            morph_variants = []  # for the current token
            # Iterate over a list of variants where each variant is a tuple
            # with a pronunciation variant and its frequency: [('беда+', '3')].
            for variant in variants:
                # Get the path to the file in the dictionary of morphology for
                # the current pronunciation variant.
                token_morph_dict_path = MorphoDescription().get_morph_file(variant[0],
                                                                           morph_dict_path)
                #print(token, token_morph_dict_path)
                try:
                    morph_dict = open(token_morph_dict_path,
                                    # encoding='cp866',  # for the old version of dictionaries
                                    encoding='utf-8').readlines()
                except FileNotFoundError:
                    pass
                    #print(f'{variant} not found in {token_morph_dict_path}')
                
                #print(token, token_morph_dict_path)
                for line in morph_dict[:-1]:
                    line = line.strip().split('{')
                    word = line[0]
                    frequency = line[1][-1]
                    if variant[0] == word:
                        morph_info = line[1].split('}')[0]
                        # Get morphological description passing a pronunciation
                        # variant and its morphological annotations as arguments.
                        morph_var = MorphoDescription().fill_tags(word, morph_info, frequency)
                        if morph_var is not None:
                            morph_variants.append(morph_var)
                        morph_tokens_variants[token.audio_word] = morph_variants
                
            if token.audio_word not in morph_tokens_variants:
                #print(f'ATTENTION: {token} not found')
                wordform = token.potential_variants[0][0]
                morph_variants = [ConnectedWords(wordform, 'CW', 1)]
                morph_tokens_variants[token.audio_word] = morph_variants

        for token in tokens_variants:
            if token.audio_word not in morph_tokens_variants.keys():
                raise Exception('Morphs were not found for some tokens')

        return morph_tokens_variants, tokens_sequence
