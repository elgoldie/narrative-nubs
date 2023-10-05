# Defining Classes for Parts-of-Speech
import wordbank
import random
from enum import Enum
import sys
class Case(Enum):
    NOMINATIVE = 0
    ACCUSATIVE = 1
    GENITIVE = 2

class Gender(Enum):
    MASCULINE = 0
    FEMININE = 1
    NEUTER = 2

class Number(Enum):
    SINGULAR = 0
    PLURAL = 1

class Transitivity(Enum):
    INTRANS = 0
    TRANS = 1



class Noun:
    def __init__(self, base, number, gender, article) -> None:
        self.base = base # actual word
        self.plural = number # plural or not
        self.gender = gender # determines which pronouns can be used
        self.article = article # determines if it takes "a" or "an"
        self.opener = self.plural
        self.closer = True
    def __str__(self):
        return self.base

class Masculine(Noun):
    def __init__(self, base) -> None:
        super().__init__(base, Number.SINGULAR, Gender.MASCULINE, "a")

class Feminine(Noun):
    def __init__(self, base) -> None:
        super().__init__(base, Number.SINGULAR, Gender.FEMININE, "a")

class NeuterA(Noun):
    def __init__(self, base) -> None:
        super().__init__(base, Number.SINGULAR, Gender.NEUTER, "a")

class NeuterAn(Noun):
    def __init__(self, base) -> None:
        super().__init__(base, Number.SINGULAR, Gender.NEUTER, "an")

class Plural(Noun):
    def __init__(self, base) -> None:
        super().__init__(base, Number.PLURAL, Gender.NEUTER, None)

class ProperNoun(Noun):
    def __init__(self, base, ProperGender, basis) -> None:
        super().__init__(base, number=Number.SINGULAR, gender = ProperGender, article=None)
        self.gender = ProperGender
        self.basis = basis # basis of the proper noun (boy, girl, cat, dog, bumpus)
        self.opener = True

###### VERBS

class Verb:
    def __init__(self, base, transitive, plural) -> None:
        self.base = base # actual word
        self.plural = plural
        self.transitive = transitive
        self.opener = False
        self.closer = True
    def __str__(self):
        return self.base
    
class IntransSing(Verb):
    def __init__(self,base) -> None:
        super().__init__(base, transitive=Transitivity.INTRANS, plural=Number.SINGULAR)

class IntransPlur(Verb):
    def __init__(self,base) -> None:
        super().__init__(base,transitive=Transitivity.INTRANS, plural=Number.PLURAL)

class TransSing(Verb):
    def __init__(self,base) -> None:
        super().__init__(base,transitive=Transitivity.TRANS, plural=Number.SINGULAR)

class TransPlur(Verb):
    def __init__(self,base) -> None:
        super().__init__(base, transitive=Transitivity.TRANS, plural=Number.PLURAL)


class Pronoun:
    def __init__(self, base, plural, gender, case) -> None:
        self.base = base # article its based on
        self.plural = plural # boolean
        self.gender = gender
        self.case = case # nominative (eg. he), accusative (eg. him), possessive (eg. his)
        if self.case == Case.ACCUSATIVE:
            self.opener = False
            self.closer = True
        else: 
            self.opener = True
            self.closer = False
    def __str__(self):
        return self.base

class HeHim(Pronoun):
    def __init__(self, base, case, refer) -> None:
        super().__init__(base, Number.SINGULAR, Gender.MASCULINE, case)

class SheHer(Pronoun):
    def __init__(self, base, case, refer) -> None:
        super().__init__(base, Number.SINGULAR, Gender.FEMININE, case)

class ItIts(Pronoun):
    def __init__(self, base, case, refer) -> None:
        super().__init__(base, Number.SINGULAR, Gender.NEUTER, case)

class TheyThem(Pronoun):
    def __init__(self, base, case) -> None:
        super().__init__(base, Number.PLURAL, Gender.NEUTER, case)

## Pronoun Processing

def PronounProcessing(pronounClass):
    for i in sentence:  ### EVENTUALLY CHANGE THIS TO TEXT
        if i.gender != None:
            if i.gender == pronounClass.gender:
                pronounClass.refer = True

class Article:
    def __init__(self, base, plural) -> None:
        self.base = base 
        self.plural = plural # true if plural, false if singular
        self.opener = True
        self.closer = False
    def __str__(self):
        return self.base
    
class SingArt(Article):
    def __init__(self, base) -> None:
        super().__init__(base, Number.SINGULAR)

class PlurArt(Article):
    def __init__(self, base) -> None:
        super().__init__(base, Number.PLURAL)


class Adverb:
    def __init__(self,base) -> None:
        self.base = base
        self.closer = True
    def __str__(self):
        return self.base
class Preposition:
    def __init__(self,base) -> None:
        self.base = base
        self.closer = False
    def __str__(self):
        return self.base

### PROPERNOUN PROCESSING

editedPropernouns = []
for i in wordbank.assignedproperNouns:
    if i[1] == "M":
        correctedGender = Gender.MASCULINE
    elif i[1] == "F":
        correctedGender = Gender.FEMININE
    else: 
        correctedGender = Gender.NEUTER
    j = [i[0],correctedGender,i[2]]
    editedPropernouns.append(j)
        

def ProperNounChoosing(wordAttributeList):
    classedWord = ProperNoun(wordAttributeList[0],wordAttributeList[1],wordAttributeList[2])
    return classedWord




# ALLOW PRONOUN OPENERS



openers = [Plural,ProperNoun,PlurArt,SingArt]
nonclosers = [Preposition,Article,SingArt,PlurArt]
minimumRequirements = [[Noun,Pronoun],[Verb]]

classWordbankEquivalence = {Masculine: wordbank.malea,
                            Feminine: wordbank.femalea,
                            NeuterA: wordbank.neutera,
                            NeuterAn: wordbank.neuteran,
                            Plural: wordbank.pluralnoun,
                            IntransSing: wordbank.intransSingVerb,
                            IntransPlur: wordbank.intransPlurVerb,
                            TransSing: wordbank.transSingVerb,
                            TransPlur: wordbank.transPlurVerb,
                            SingArt: wordbank.articleSingular,
                            PlurArt: wordbank.articlePlural,
                            ProperNoun: editedPropernouns,
                            Adverb: wordbank.adverbs,
                            Preposition: wordbank.prepositions,
                            HeHim: wordbank.mascPronouns,
                            SheHer: wordbank.femPronouns,
                            ItIts: wordbank.neuterPronouns,
                            TheyThem: wordbank.pluralPronouns
                            }

def WordChoosing(Class):
    wordList = classWordbankEquivalence[Class]
    chosenWord = random.choice(wordList)
    return chosenWord

# Defining how sentences can get built

classSubclassEquivalence = {Noun:[Masculine,Feminine,NeuterA,NeuterAn,Plural],
                            Verb: [IntransSing,IntransPlur,TransSing,TransPlur],
                            Article: [SingArt,PlurArt],
                            Pronoun: [HeHim,SheHer,TheyThem,ItIts]}

sentenceCount = int(sys.argv[1])

fullText = ""

for iteration in range(sentenceCount):

    sentenceContinue = True
    sentenceLength = 0



    sentence = []
    nounPresent = False
    verbPresent = False
    permitEnd = False

    for pronounType in classSubclassEquivalence[Pronoun]:
        PronounProcessing(pronounType)

    # First Word
    wordClass = random.choice(openers)
    word = WordChoosing(wordClass)
    if type(word) == list:
        classedWord = ProperNounChoosing(word)
    else:
        classedWord = wordClass(word)

    sentence.append(classedWord)


    ### subsequent words

    ### determining valid classes




    while sentenceContinue:
        sentenceLength += 1

        validClasses = [Noun,Verb,Article, Adverb, Preposition] # pronouns are giving me a nightmare so i am: simply ignoring them for the time being


        finalWord = sentence[-1]
        
        
        if type(finalWord) in [HeHim,SheHer,TheyThem,ItIts]:
            if finalWord.case == Case.NOMINATIVE:
                validClasses.remove(Noun)
                validClasses.remove(Article)
                #validClasses.remove(Pronoun)
            elif finalWord.case == Case.ACCUSATIVE:
                validClasses.remove(Article)
                #validClasses.remove(Pronoun)
                validClasses.remove(Verb)
        elif type(finalWord) in [Noun,Masculine,Feminine,NeuterA,NeuterAn,Plural,ProperNoun]:
            validClasses.remove(Noun)
            validClasses.remove(Article)
            validClasses.remove(Preposition)
            #validClasses.remove(Pronoun)
        elif type(finalWord) in [IntransSing,IntransPlur,TransSing,TransPlur]:
            validClasses.remove(Verb)
        elif type(finalWord) in [Article,SingArt,PlurArt]:
            #validClasses.remove(Pronoun)
            validClasses.remove(Article)
            validClasses.remove(Verb)
            validClasses.remove(Adverb)
            validClasses.remove(Preposition)
        elif type(finalWord) == Preposition:
            validClasses.remove(Verb)
            validClasses.remove(Preposition)
            validClasses.remove(Adverb)
        elif type(finalWord) == Adverb:
            validClasses.remove(Adverb)



        # prevents more than one verb in a sentence and more than one article before a verb
        for i in sentence:
            if type(i) in [Noun,Masculine,Feminine,NeuterA,NeuterAn,Plural,ProperNoun,Pronoun,HeHim,SheHer,ItIts,TheyThem]:
                nounPresent = True
            elif type(i) in [Verb,IntransSing,IntransPlur,TransSing,TransPlur]:
                verbPresent = True
            if type(i) in [IntransSing,IntransPlur,TransSing,TransPlur] and Verb in validClasses:
                validClasses.remove(Verb)
            elif nounPresent == False and Verb in validClasses:
                validClasses.remove(Verb)
            if verbPresent == False and Article in validClasses:
                validClasses.remove(Article)

        nounClasses = [Masculine,Feminine,NeuterA,NeuterAn,Plural]
        verbClasses = [IntransSing,IntransPlur,TransSing,TransPlur]
        articleClasses = [SingArt,PlurArt]
        pronounClasses = [HeHim,SheHer,TheyThem,ItIts]

        singularClasses = [Masculine,Feminine,NeuterA,NeuterAn,IntransSing,TransSing,SingArt] # add pronouns here!
        pluralClasses = [Plural,IntransPlur, TransPlur,PlurArt] # once again add pronouns





        # converting into subclasses

        for classKey in classSubclassEquivalence:
            if classKey in validClasses:
                validClasses.remove(classKey)
                validClasses.extend(classSubclassEquivalence[classKey])

        # removing based on singular and plural
        if type(finalWord) not in [Adverb,Preposition]:
            if finalWord.plural == Number.SINGULAR:
                for classKey in pluralClasses:
                    if classKey in validClasses and classKey not in articleClasses:
                        validClasses.remove(classKey)

                if finalWord.base == "a":
                    if NeuterAn in validClasses:
                        validClasses.remove(NeuterAn)
                elif finalWord.base == "an":
                    for classKey in singularClasses:
                        if classKey in validClasses and classKey != NeuterAn:
                            validClasses.remove(classKey)


            else:
                for classKey in singularClasses:
                    if classKey in validClasses and classKey not in articleClasses:
                        validClasses.remove(classKey)
        if type(finalWord) in [Adverb,Preposition]:
            for classKey in singularClasses:
                if classKey in validClasses and classKey not in [ProperNoun, SingArt]:
                    validClasses.remove(classKey)
        
        # <NEED TO FIX TO LOGIC>
        
        """
        if type(finalWord) in [HeHim,SheHer,TheyThem,ItIts]:
            if finalWord.case == Case.ACCUSATIVE:
                if ProperNoun in validClasses:
                    validClasses.remove(ProperNoun)
        """
        # removing based on gender (WILL HAPPEN ONCE PRONOUNS IMPLEMENTED)


        # verb stuff

        # general verb removage

        if type(finalWord) in [IntransSing,IntransPlur,TransSing,TransPlur]:
            for classKey in singularClasses:
                if classKey in validClasses and classKey not in articleClasses:
                    validClasses.remove(classKey)
            if finalWord.transitive == Transitivity.INTRANS:
                validClasses = []
                # ADD BACK ADVERBS AND PREPOSITIONS

        



        # Based on the previous words
        if validClasses == []:
            sentenceContinue = False
            break
        else:
            wordClass = random.choice(validClasses)

            word = WordChoosing(wordClass)
            if type(word) == list:
                classedWord = ProperNounChoosing(word)
            else:
                classedWord = wordClass(word)

            sentence.append(classedWord)



        if type(finalWord) in [Noun,Masculine,Feminine,NeuterA,NeuterAn,Plural,ProperNoun,Pronoun,HeHim,SheHer,ItIts,TheyThem]:
            nounPresent = True
        elif type(finalWord) in [Verb,IntransSing,IntransPlur,TransSing,TransPlur]:
            verbPresent = True

        # Ending a sentence: if minimum requirements are in sentence and sentence[-1].closer == True, allow to end sentence

        if verbPresent and type(finalWord) not in nonclosers:
            if random.choice([0,1]) == 1:
                sentenceContinue == False
                break
            
        # additionally if no possible following words, force end sentence


        sentenceString = ""
        for i in sentence:
            sentenceString += str(i)
            sentenceString += " "


    sentenceString = ""
    sentenceString = " ".join([str(i) for i in sentence])
    sentenceString += "."

    fullText+= sentenceString
    fullText+= " "
print(fullText)





"""
TO DO/FIX:

- implement the concept of subject for longer distance verb agreement
- implement pronouns
- fix to logic
- fix verb priorities -- it seems possible that verb needs to exist  before or at position 3 (0 indexed)
"""
