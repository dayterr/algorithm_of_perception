# Python program for analysis and recognition of reduced words in Russian #

[![Current version on PIP](9.0.2)]
[![Python versions](python 3.6)]

The programme takes as input a transcription of an utterance and outputs all possible variants of orthographic interpretation allowed by the given morphology.

### Start program ###
```
>> unpack zip archive
>> open command line
>> change to the program directory
>> run with command:
python run.py --input path_to_clause --morpho-dict ../data/dictionaries/GRANT-M.utf --ortho-dict "../data/dictionaries/GRANT-LX.utf -pred -l2r"
```

### How change clause? ###
```
>> open file "Test clause"
>> delete old example
>> insert another one
>> add gap with point in the end of the clause
Example:
i vasp'it@v@It' sopsnQg d'it'e:# .
```

### How does the program work? ###

1. The program reads the input clause written in SAMPA transcription from the file 'TestClause'.
2. Words in a clause are separated by spaces.
3. All possible pronunciation variants for each word are got from the LEXICON ('GRANT-LX.utf').
4. Morphological description for each variant is taken from the MOPHOLOGICAL DICTIONARY ('GRANT-M.utf') and parsed with the *ExtractionOfMorphology.py* module. In the result of this step, all words are instances, which include pronunciation variants and their morphological description. Morphological description can be reached as attributes. See the available attributes for different POSs in the Appendix below.
5. Every variant of the current word is compared to each variant of the previous word. A decision to arrange words into syntactic groups is taken on the basis of the rules for word form processing and syntactic grouping (module *RulesOfAgreement.py*).

### Test examples ###

* vot sam@ glavnQ b'ida gar'i potra -- вот самая главная беда Гарри Поттера
* s'u:vod@SnQ naS r@zgauor -- сегодняшний наш разговор
* (n#u v asnavnom de#) s'@m'a: m'e: p@dgatoel@ k @tQ  -- ну в основном да, семья меня подготовила к этой
* je: x@ICu: vot @br@It'it' vn'imaIn'o: oId'itor'i n@ g@kuI v'e:$ -- я хочу вот обратить внимание аудитории на какую вещь
* d@vaIt' s'e: zd@Id'im s'e: v@pros -- давайте все зададим себе вопрос

##### TEST CLAUSE #####
WORK:
* ete slovQ n'i sxod'it sQ stren'is naSQ gez'e:t
* ix pr'im'e:ru pesl'e:dQv@l'i m@nog'i k@l'ikt'ivQ
* kak u n'ix s'iCa:s idud d'e:la
* s kaZdQm dn'o:m rQSer'a:ecQ io: gren'ice f k@zaxstan'
* m'il'ionQ ton z'irna dalZnQ dat' gasudarstvu v etam gadu kalxozQ i savxozQ kQzaxstana
* ab etQm p'iZQt f pravdi kQnd'idad b'e:eleg'iCsk'ix nauh beb'a:n
* r'e:C id'o:t a prudav@m rQbavoctv'i
* vaZn'iSQ m'e:zdunarodnQ t'e:m'i pQsv'i$ina s'ivodn'i p'ir'idavee stet'ja pravd@
* katorQ uZe n'ikto n'i moZQt ignQr'ir@v@t'

obzor-02
* bQlQ pr'in'ito r'e:Sen'e: ab uICer'iZd'en'e: et@va prazn'ike
* d'iv'izom smotr@ stal'i slava

gue01-19
* k@t@re rabot@l' @ u:sp'iSna pabot@l'e: v goreId'e:
* z'it'e: vQstavl'a:ed z@ paruk
* n'i kaZdum@I r'ibo:nku moSn@ pamQC
* en'i ponQs't'u: p@dgatol'inQ g ZQz'n'i
* dv'igQc@ fs'e: sel'nQ v@prosQ
* e:ta rabot@ pr@dalZaec@

DOES NOT WORK:
* l'iSbQ paboIl'Se narodu pr@ICitalQ tu kn'iSku
* **tQs' ed** n'i kaZdum@I r'ibo:nku moSn@ pamQC
* **tes'** en'i ponQs't'u: p@dgatol'inQ g ZQz'n'i
* vo **toIs'** e:ta rabot@ pr@dalZaec@

##### Final Test 2020: #####
0. ete slovQ n'i sxod'it sQ stren'is naSQ gez'e:t - э+то сло+во не схо+дит со страни+ц на+ших газе+т
1. a# k@k'imn'ibQt' o:brQz@m gracke @m'in'strace f'inans'irQt
2. katrQ xoIit f porvan@x StaIn'iSk@x - кото+рый хо+дит в по+рванных штани+шках
3. katorQ uZe n'ikto n'i moZQt ignQr'ir@v@t'
4. r'e:C id'o:t a prudav@m rQbavoctv'i
5. ix pr'im'e:ru pesl'e:dQv@l'i m@nog'i k@l'ikt'ivQ
6. i mQ vot p'ir'israem sve rabotu m'is'i s raIio:n edm'israceI - и мы+ во+т перестра+иваем свою+ рабо+ту вме+сте с райо+нной администра+цией
7. a kak vap$e: m'e:stnQ ZQt'@l'@ etnoIs'c@ ke r'ib'a:t@m @s kamun@
8. Sto# m#Q b'ir'o:m n'i kaS@ve r'b'o:mka
9. @I n'ix i#e:z duSevn@ n@streIe:n'e: rabot@ z' d'it'm'i


##### OTHERS #####
* n@ dl'a: et@va dalZnQ bQ teIk'i srukturu
* kak'i prabl'e:m@ imuI r'iSaIt' (f) same bl'iZeSe vr'e:m'@ prQd'o:c
* etQI je:s# Ca:s@ sluICo: v@sp'itaIn'a:
* a n'e:kte Skol pQd'o:c p@dn'e:maIt' reId'it'l'e:m reId'it'@sk'e:m k@m'it'e:t
* _@I n'ix i#e:z duSevn@ n@streIe:n'e: rabot@ z' d'it'm'i
* et@ @t samaI g@lavne funkcQ v@spQtaIn'
* etQI je:s# Ca:s@ sluICo: v@sp'itaIn'a:
* et@ druge str@neI d'e:la
* spoIr'it'e: xat'a: u nas s vaIm'e: sxodne paIz'iCe#
* nu at@# vapros Qn't'e:r'e:sne
* nu take bQlaI s'ituace#
* n'e:k@t@rQ Skol@ padn'im@c@ v et'x usloIv'e:x sam'e
* na sam d'il' Qt@ uZasn@
* vot sam@ glavnQ b'ida gar'i potra
* at et@vQ d'e:ck@ fp'iCitl'in'@ tQ r'iSQ St@ Skol n'i moZ@t vasp'it@
* i vasp'it@v@It' sopsnQg d'it'e:#

### About project ###
```
Although the process of speech recognition has been analyzed for a long time, it is still not described accurately. We are developing an algorithm of reduced word forms recognition as the phonetic reduction is one of the crucial features of spontaneous speech.
The previous experimental psycholinguistic studies have shown the key role of the semantic and grammatical context in the restoration of reduced words [Ernestus et al. 2002, Nigmatulina et al. 2016]. Furthermore, at least some reduced word forms were shown to be stored in the mental lexicon of a native speaker and, thus, they do not require restoration [Raeva & Riekhakaynen 2016]. Based on the assumptions mentioned above, the following model of spontaneous speech recognition can be proposed: a listener while recognizing speech chooses among all possible variants stored in the mental lexicon the interpretation of a reduced word form that is the most suitable in a given grammatical and semantic context.
In order to check this model, the algorithm of reduced word forms recognition was implemented using the Python language. Test data were collected from the Corpus of Transcribed Oral Russian Texts (around 115 minutes of radio interviews and talk shows), where both the orthographic and acoustic-phonetic annotations of all recordings are provided. The implementation of the algorithm is a multimodal program that consists of the main block, the module that retrieves the morphological information about candidates for recognition and the rules for word form processing and syntactic grouping. The lexicon used by the program contains all possible realizations of each pronounced word found in the corpus.
```

### References ###

* Ernestus М., Baayen H., Schreuder R. The Recognition of Reduced Word Forms // Brain and Language. 2002. Vol. 81, № (1–3). P. 162-173.
* Nigmatulina Ju., Rajeva O., Riechakajnen E., Slepokurova N., Vencov A., How to Study Spoken Word Recognition: Evidence from Russian, Slavic Languages in Psycholinguistics: Chances and Challenges for Empirical and Experimental Research, Tübinger Beiträge zur Linguistik, 554. 2016. P. 175-190.
* Raeva O., Riekhakaynen E. Frequent Word Forms in Spontaneous Russian: Realization and Recognition. Linguistica Lettica. 2016. Vol. 24. P.122-139.


### APPENDIX ###
Parts of Speech and their attributes
**Noun**
        wordform
        pos_tag
        gender
        animateness
        number
        case

**Pronoun**
        wordform
        pos_tag
        person
        gender
        animateness
        number
        case

**Adjective**
        wordform
        pos_tag
        shortness
        number
        gender
        case

**Verb**
        wordform
        pos_tag
        aspect
        transitivity
        voice
        mood
        tense
        number
        person
        gender

**Participle**
        wordform
        pos_tag
        aspect
        transitivity
        voice
        shortness
        tense
        number
        person
        gender

**Gerund**
        wordform
        pos_tag
        aspect
        transitivity

**Adverb**
        wordform
        pos_tag
        comparative

**Numeral**
        wordform
        pos_tag
        number
        animateness
        gender
        case

**Predicate**
        wordform
        pos_tag

**Interjection**
        wordform
        pos_tag

**Preposition**
        wordform
        pos_tag
        # valences

**Conjunction**
        wordform
        pos_tag

**Intro**
        wordform
        pos_tag

**ConnectedWords**
        wordform
        pos_tag

**Particle**
        wordform
        pos_tag

**AlphabeticLetter**
        wordform
        pos_tag
