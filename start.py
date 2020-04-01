import os
import cotools
from cotools import search, text, abstract, texts, abstracts

# cotools todo:
# something with metadata see:
# https://pages.semanticscholar.org/coronavirus-research
# something with anti viral compounds (see above)

# redownload every update of cotools
# make sure your version is up to date!!!
# we are on 0.1.5
# there may be bugs in this so ping me or make a PR if this does anything
# unexpected, and always update cotools (pip install cord-19-tools)
downloaded = False  # set back to true because this takes a hot minute
if not downloaded:
    cotools.download("data")

print(os.listdir("data/"))

# start with comm_use as that contains pmc
# more info here
# https://pages.semanticscholar.org/coronavirus-research

comm_use = cotools.Paperset("data/comm_use_subset")

print(len(comm_use))

# basic tutorial on cotools.Paperset!

# indexing to access individual papers, output is a dict
print(comm_use[0])
print(type(comm_use[0]))

# indexing to access several papers, returns a list of dicts
print(comm_use[:15])
print(type(comm_use[:14]))


# apply to entire paperset(takes a minute, but memory light because of laziness)
print(comm_use.apply(len))

# get all text:
comm_use.texts()

# get all abstracts
comm_use.abstracts()

# get the text of a single paper
text(comm_use[0])
# or of multiple
texts(comm_use[4:15])

# same with abstracts
abstract(comm_use[0])
abstracts(comm_use[4:15])


# search for texts!
covid = search(comm_use, ["covid", "novel coronavirus"])  # returns a list

# refine the searches!
terms = ["ventilator", "cpap", "bipap"]
ventil = [
    x
    for x in covid
    if any(t in text(x).lower() for t in terms)
    or any(t in abstract(x).lower() for t in terms)
]

print(len(ventil))
