import propernouns
from enum import Enum 
# Nouns

class Basis(Enum):
    BOY = 0
    GIRL = 1
    BUMPUS = 2
    CAT = 3 
    DOG = 4

### use a tsv to store all the data and initialize the objects from there

neutera = ["box","bumpus","cat","dog","fence","flower","house","rock","store","tree"]
neuteran = ["apple"]
malea = ["boy"]
femalea = ["girl"]
pluralnoun = ["apples", "boxes", "boys", "bumpuses", "cats", "dogs", "fences", "flowers", "girls", "houses", "rocks", "stores", "trees"]

intransSingVerb = ["dances","goes","hops","jumps","runs","sings","walks"]
intransPlurVerb = ["dance","go","hop","jump","run","sing","walk"]
transSingVerb = ["zots","eats","kisses"]
transPlurVerb = ["zot","eat","kiss"]

mascPronouns = ["he","him","his"]
femPronouns = ["she","her","her"]
neuterPronouns = ["it", "its","its"]
pluralPronouns = ["they","them","their"]


articleSingular = ["a","an","the","that","this"]
articlePlural = ["the","those","these","some"]

properNouns = [[propernouns.BOYNAME,"M",Basis.BOY],[propernouns.GIRLNAME,"F",Basis.GIRL],[propernouns.BUMPUSNAME,"N",Basis.BUMPUS],[propernouns.CATNAME,"N",Basis.CAT],[propernouns.DOGNAME,"N",Basis.DOG]]
assignedproperNouns = []
for i in properNouns:
    if i[0] != None:
        assignedproperNouns.append(i)


adverbs = ["now","soon","sometimes","later"]

prepositions = ["near","to"]