import extra_info


class Agreement:
    '''
    '''

    def pred_subj_agreement(self, w1, w2):
        ''' Check agreement of w1=VERB - w2=(PRO)NOUN
        '''
        if w2.pos_tag in extra_info.pos_dict['pronoun']:
            if hasattr(w1, 'gender'):
                if (w1.gender == w2.gender) and \
                        (w1.number == w2.number):
                    return True
                elif (w1.number == w2.number) and \
                        (w1.gender == "0"):
                    return True
                else:
                    return False
            else:
                if (w1.person == w2.person) and (w1.number == w2.number):
                    return True
                else:
                    return False
        else:
            if w1.number == 'sg':
                if (w1.number == w2.number) and (w1.gender == w2.gender):
                    return True
                else:
                    return False
            elif w1.number == 'pl':
                if (w1.number == w2.number):
                    return True
                else:
                    return False

    def pass_pred_subj_agreement(self, w1, w2):
        ''' Check agreement of w1=VV0 - w2=NN0
        '''
        if w1.number == 'sg':
            if (w1.number == w2.number) and (w1.gender == w2.gender) and \
               (w1.case[0] == w2.case[0]):
                return True
            else:
                return False
        elif w1.number == 'pl':
            if (w1.number == w2.number) and (w1.case[0] == w2.case[0]):
                return True
            else:
                return False

    def obj_adj_agreement(self, w1, w2):
        ''' Check agreement of w1=NOUN - w2=ADJ
        '''
        if hasattr(w2, 'animateness'):
            # print(w1.wordform)
            if (w1.number == w2.number) and (w1.gender == w2.gender) and \
               (w1.animateness == w2.animateness) and (w1.case[0] == w2.case[0]):
                return True
            else:
                return False
        else:
            if w1.number == 'sg':
                if (w1.number == w2.number) and (w1.gender == w2.gender) and \
                   (w1.case[0] == w2.case[0]):
                    return True
                else:
                    return False
            elif w1.number == 'pl':
                if (w1.number == w2.number) and (w1.case[0] == w2.case[0]):
                    return True
                else:
                    return False

    def mod_subj_agreement(self, w1, w2):
        ''' Check agreement of w1=NOUN - w2=VV0
        '''
        if w2.shortness == 'sht' and w2.case[0] == '0':
            if w1.number == 'sg':
                if (w1.number == w2.number) and (w1.gender == w2.gender):
                    return True
                else:
                    return False
            elif w1.number == 'pl':
                if (w1.number == w2.number):
                    return True
                else:
                    return False

    def adj_func_agreement(self, w1, w2):
        ''' Check agreement of w1=ADJ, w2=AUX самая главная
        '''
        if w1.number == 'sg':
            if (w1.number == w2.number) and (w1.gender == w2.gender) and \
               (w1.case[0] == w2.case[0]):
                return True
            else:
                return False
        elif w1.number == 'pl':
            if (w1.number == w2.number) and (w1.case[0] == w2.case[0]):
                return True
            else:
                return False

    #добавлено
    def valence_agreement(self, w1, w2):
        '''Check agreement of w1=(PRONOUN), w2=VERB'''

        if w1.valence is not None:
            if w1.valence.strip() in extra_info.verb_to_be.get(str(w2), []):
                return True
            else:
                return False
        return False

    def l2r_agreement(self, w1, w2):

        pos_w1 = w1.pos_tag
        pos_w2 = w2.pos_tag
        nonconstituents = []
        """ ... """

        # Adjectives with nouns and other adjectives:
        if (pos_w1.startswith('AJ') or pos_w1.startswith('PA') or
            pos_w1 == 'AUX') and \
            (pos_w2 in extra_info.pos_dict['noun'] or
             pos_w2.startswith('A') or
             pos_w2.startswith('PA')):

            if (w1.number != w2.number or
                    w1.gender != w2.gender or
                    w1.case[0] != w2.case[0]):
                nonconstituents.append(w1.wordform)
                nonconstituents.append(w2.wordform)
                return 0

        # # Nouns with adjectives:
        # if pos_w1 in extra_info.pos_dict['noun'] \
        #     and (pos_w2.startswith('AJ') or pos_w2.startswith('PA')
        #          or pos_w2 == 'AUX'):

        #     if (w1.number != w2.number
        #         or w1.gender != w2.gender
        #         or w1.case[0] != w2.case[0]):

        #         nonconstituents.append(w1.wordform)
        #         nonconstituents.append(w2.wordform)
        #         return 0

        # Pronouns with nouns
        if pos_w1.startswith('PN') and \
                pos_w2 in extra_info.pos_dict['noun']:
            if (w1.number != w2.number or
                w1.animateness != w2.animateness or
                w1.gender != w2.gender or
                w1.case[0] != w2.case[0]):

                nonconstituents.append(w1.wordform)
                nonconstituents.append(w2.wordform)
                return 0

        # Pronouns with adjectives:
        if pos_w1.startswith('PN') and \
                (pos_w2.startswith('AJ') or
                 pos_w2.startswith('PA') or
                 pos_w2 == 'AUX'):

            if (w1.number != w2.number or
                    w1.gender != w2.gender or
                    w1.case[0] != w2.case[0]):
                nonconstituents.append(w1.wordform)
                nonconstituents.append(w2.wordform)
                return 0

        # # Nouns with pronouns
        # if pos_w1 in extra_info.pos_dict['noun'] \
        #         and pos_w2.startswith('PN'):
        #     if (w1.number != w2.number
        #         or w1.animateness != w2.animateness
        #         or w1.gender != w2.gender
        #         or w1.case[0] != w2.case[0]):

        #         nonconstituents.append(w1.wordform)
        #         nonconstituents.append(w2.wordform)
        #         return 0

        # Intro words:
        if (pos_w1.startswith('AJ') or pos_w1.startswith('PA') or
                pos_w1.startswith('PN') or
                pos_w1 == 'AUX') and \
                pos_w2 in extra_info.pos_dict['intro']:
            nonconstituents.append(w1.wordform)
            nonconstituents.append(w2.wordform)
            return 0

        if pos_w1 in extra_info.pos_dict['intro'] and \
                pos_w2 in extra_info.pos_dict['noun']:
            nonconstituents.append(w1.wordform)
            nonconstituents.append(w2.wordform)
            return 0

        # Proper words:
        if (pos_w1 == 'NP1' and pos_w2 == 'NP3'):
            if (w1.number == w2.number and w1.gender == w2.gender) and \
                    (w1.case[0] == '0' or w2.case[0] == '0'):
                return 1

            elif (w1.number != w2.number or
                    w1.gender != w2.gender or
                    w1.case[0] != w2.case[0]):
                nonconstituents.append(w1.wordform)
                nonconstituents.append(w2.wordform)
                return 0

        else:
            return 1
