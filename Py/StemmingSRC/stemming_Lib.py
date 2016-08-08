"""
__init__py
"""

"""
    stemmed_word = stem(word)
"""

from collections import defaultdict


# Conditions

def A(base):
    # A   No restrictions on stem
    return True

def B(base):
    # B  Minimum stem length = 3
    return len(base) > 2

def C(base):
    # C  Minimum stem length = 4
    return len(base) > 3

def D(base):
    # D  Minimum stem length = 5
    return len(base) > 4

def E(base):
    # E  Do not remove ending after e
    return base[-1] != "e"
    
def F(base):
    # F  Minimum stem length = 3 and do not remove ending after e
    return len(base) > 2 and base[-1] != "e"

def G(base):
    # G  Minimum stem length = 3 and remove ending only after f
    return len(base) > 2 and base[-1] == "f"

def H(base):
    # H  Remove ending only after t or ll
    c1, c2 = base[-2:]
    return c2 == "t" or (c2 == "l" and c1 == "l")
    
def I(base):
    # I  Do not remove ending after o or e
    c = base[-1]
    return c != "o" and c != "e"
    
def J(base):
    # J  Do not remove ending after a or e
    c = base[-1]
    return c != "a" and c != "e"
    
def K(base):
    # K  Minimum stem length = 3 and remove ending only after l, i or u*e
    c = base[-1]
    cc = base[-3]
    return len(base) > 2 and (c == "l" or c == "i" or (c == "e" and cc == "u"))
    
def L(base):
    # L  Do not remove ending after u, x or s, unless s follows o
    c1, c2 = base[-2:]
    return c2 != "u" and c2 != "x" and (c2 != "s" or c1 == "o")
    
def M(base):
    # M  Do not remove ending after a, c, e or m
    c = base[-1]
    return c != "a" and c!= "c" and c != "e" and c != "m"

def N(base):
    # N  Minimum stem length = 4 after s**, elsewhere = 3
    return len(base) > 3 or (len(base) == 3 and base[-1] != "s")

def O(base):
    # O  Remove ending only after l or i
    c = base[-1]
    return c == "l" or c == "i"
 
def P(base):
    # P  Do not remove ending after c
    return base[-1] != "c"
    
def Q(base):
    # Q  Minimum stem length = 3 and do not remove ending after l or n
    c = base[-1]
    return len(base) > 2 and (c != "l" and c != "n")

def R(base):
    # R  Remove ending only after n or r
    c = base[-1]
    return c == "n" or c == "r"

def S(base):
    # S  Remove ending only after dr or t, unless t follows t
    l2 = base[-2]
    return l2 == "rd" or (base[-1] == "t" and l2 != "tt")

def T(base):
    # T  Remove ending only after s or t, unless t follows o
    c1, c2 = base[-2:]
    return c2 == "s" or (c2 == "t" and c1 != "o")

def U(base):
    # U  Remove ending only after l, m, n or r
    c = base[-1]
    return c == "l" or c == "m" or c == "n" or c == "r"

def V(base):
    # V  Remove ending only after c
    return base[-1] == "c"

def W(base):
    # W  Do not remove ending after s or u
    c = base[-1]
    return c != "s" and c != "u"

def X(base):
    # X  Remove ending only after l, i or u*e
    c = base[-1]
    cc = base[-3]
    return c == "l" or c == "i" or (c == "e" and cc == "u")
    
def Y(base):
    # Y  Remove ending only after in
    return base[-2:] == "in"

def Z(base):
    # Z  Do not remove ending after f
    return base[-1] != "f"

def a(base):
    # a  Remove ending only after d, f, ph, th, l, er, or, es or t
    c = base[-1]
    l2 = base[-2:]
    return (c == "d" or c == "f" or l2 == "ph" or l2 == "th" or c == "l"
            or l2 == "er" or l2 == "or" or l2 == "es" or c == "t")
    
def b(base):
    # b  Minimum stem length = 3 and do not remove ending after met or ryst
    return len(base) > 2 and not (base.endswith("met")
                                  or base.endswith("ryst"))

def c(base):
    # c  Remove ending only after l
    return base[-1] == "l"

# Endings

m = [None] * 12

m[11] = dict((
        ("alistically", B),
        ("arizability", A),
        ("izationally", B)))
m[10] = dict((
        ("antialness", A),
        ("arisations", A),
        ("arizations", A),
        ("entialness", A)))
m[9] = dict((
        ("allically", C),
        ("antaneous", A),
        ("antiality", A),
        ("arisation", A),
        ("arization", A),
        ("ationally", B),
        ("ativeness", A),
        ("eableness", E),
        ("entations", A),
        ("entiality", A),
        ("entialize", A),
        ("entiation", A),
        ("ionalness", A),
        ("istically", A),
        ("itousness", A),
        ("izability", A),
        ("izational", A)))
m[8] = dict((
        ("ableness", A),
        ("arizable", A),
        ("entation", A),
        ("entially", A),
        ("eousness", A),
        ("ibleness", A),
        ("icalness", A),
        ("ionalism", A),
        ("ionality", A),
        ("ionalize", A),
        ("iousness", A),
        ("izations", A),
        ("lessness", A)))
m[7] = dict((
        ("ability", A),
        ("aically", A),
        ("alistic", B),
        ("alities", A),
        ("ariness", E),
        ("aristic", A),
        ("arizing", A),
        ("ateness", A),
        ("atingly", A),
        ("ational", B),
        ("atively", A),
        ("ativism", A),
        ("elihood", E),
        ("encible", A),
        ("entally", A),
        ("entials", A),
        ("entiate", A),
        ("entness", A),
        ("fulness", A),
        ("ibility", A),
        ("icalism", A),
        ("icalist", A),
        ("icality", A),
        ("icalize", A),
        ("ication", G),
        ("icianry", A),
        ("ination", A),
        ("ingness", A),
        ("ionally", A),
        ("isation", A),
        ("ishness", A),
        ("istical", A),
        ("iteness", A),
        ("iveness", A),
        ("ivistic", A),
        ("ivities", A),
        ("ization", F),
        ("izement", A),
        ("oidally", A),
        ("ousness", A)))
m[6] = dict((
        ("aceous", A),
        ("acious", B),
        ("action", G),
        ("alness", A),
        ("ancial", A),
        ("ancies", A),
        ("ancing", B),
        ("ariser", A),
        ("arized", A),
        ("arizer", A),
        ("atable", A),
        ("ations", B),
        ("atives", A),
        ("eature", Z),
        ("efully", A),
        ("encies", A),
        ("encing", A),
        ("ential", A),
        ("enting", C),
        ("entist", A),
        ("eously", A),
        ("ialist", A),
        ("iality", A),
        ("ialize", A),
        ("ically", A),
        ("icance", A),
        ("icians", A),
        ("icists", A),
        ("ifully", A),
        ("ionals", A),
        ("ionate", D),
        ("ioning", A),
        ("ionist", A),
        ("iously", A),
        ("istics", A),
        ("izable", E),
        ("lessly", A),
        ("nesses", A),
        ("oidism", A)))
m[5] = dict((
        ("acies", A),
        ("acity", A),
        ("aging", B),
        ("aical", A),
        ("alist", A),
        ("alism", B),
        ("ality", A),
        ("alize", A),
        ("allic", b),
        ("anced", B),
        ("ances", B),
        ("antic", C),
        ("arial", A),
        ("aries", A),
        ("arily", A),
        ("arity", B),
        ("arize", A),
        ("aroid", A),
        ("ately", A),
        ("ating", I),
        ("ation", B),
        ("ative", A),
        ("ators", A),
        ("atory", A),
        ("ature", E),
        ("early", Y),
        ("ehood", A),
        ("eless", A),
        ("elily", A),
        ("ement", A),
        ("enced", A),
        ("ences", A),
        ("eness", E),
        ("ening", E),
        ("ental", A),
        ("ented", C),
        ("ently", A),
        ("fully", A),
        ("ially", A),
        ("icant", A),
        ("ician", A),
        ("icide", A),
        ("icism", A),
        ("icist", A),
        ("icity", A),
        ("idine", I),
        ("iedly", A),
        ("ihood", A),
        ("inate", A),
        ("iness", A),
        ("ingly", B),
        ("inism", J),
        ("inity", c),
        ("ional", A),
        ("ioned", A),
        ("ished", A),
        ("istic", A),
        ("ities", A),
        ("itous", A),
        ("ively", A),
        ("ivity", A),
        ("izers", F),
        ("izing", F),
        ("oidal", A),
        ("oides", A),
        ("otide", A),
        ("ously", A)))
m[4] = dict((
        ("able", A),
        ("ably", A),
        ("ages", B),
        ("ally", B),
        ("ance", B),
        ("ancy", B),
        ("ants", B),
        ("aric", A),
        ("arly", K),
        ("ated", I),
        ("ates", A),
        ("atic", B),
        ("ator", A),
        ("ealy", Y),
        ("edly", E),
        ("eful", A),
        ("eity", A),
        ("ence", A),
        ("ency", A),
        ("ened", E),
        ("enly", E),
        ("eous", A),
        ("hood", A),
        ("ials", A),
        ("ians", A),
        ("ible", A),
        ("ibly", A),
        ("ical", A),
        ("ides", L),
        ("iers", A),
        ("iful", A),
        ("ines", M),
        ("ings", N),
        ("ions", B),
        ("ious", A),
        ("isms", B),
        ("ists", A),
        ("itic", H),
        ("ized", F),
        ("izer", F),
        ("less", A),
        ("lily", A),
        ("ness", A),
        ("ogen", A),
        ("ward", A),
        ("wise", A),
        ("ying", B),
        ("yish", A)))
m[3] = dict((
        ("acy", A),
        ("age", B),
        ("aic", A),
        ("als", b),
        ("ant", B),
        ("ars", O),
        ("ary", F),
        ("ata", A),
        ("ate", A),
        ("eal", Y),
        ("ear", Y),
        ("ely", E),
        ("ene", E),
        ("ent", C),
        ("ery", E),
        ("ese", A),
        ("ful", A),
        ("ial", A),
        ("ian", A),
        ("ics", A),
        ("ide", L),
        ("ied", A),
        ("ier", A),
        ("ies", P),
        ("ily", A),
        ("ine", M),
        ("ing", N),
        ("ion", Q),
        ("ish", C),
        ("ism", B),
        ("ist", A),
        ("ite", a),
        ("ity", A),
        ("ium", A),
        ("ive", A),
        ("ize", F),
        ("oid", A),
        ("one", R),
        ("ous", A)))
m[2] = dict((
        ("ae", A),
        ("al", b),
        ("ar", X),
        ("as", B),
        ("ed", E),
        ("en", F),
        ("es", E),
        ("ia", A),
        ("ic", A),
        ("is", A),
        ("ly", B),
        ("on", S),
        ("or", T),
        ("um", U),
        ("us", V),
        ("yl", R),
        ("s'", A),
        ("'s", A)))
m[1] = dict((
        ("a", A),
        ("e", A),
        ("i", A),
        ("o", A),
        ("s", W),
        ("y", B)))


def remove_ending(word):
    length = len(word)
    el = 11
    while el > 0:
        if length - el > 1:
            ending = word[length-el:]
            cond = m[el].get(ending)
            if cond:
                base = word[:length-el]
                if cond(base):
                    return base
        el -= 1
    return word


_endings = (("iev", "ief"),
            ("uct", "uc"),
            ("iev", "ief"),
            ("uct", "uc"),
            ("umpt", "um"),
            ("rpt", "rb"),
            ("urs", "ur"),
            ("istr", "ister"),
            ("metr", "meter"),
            ("olv", "olut"),
            ("ul", "l", "aoi"),
            ("bex", "bic"),
            ("dex", "dic"),
            ("pex", "pic"),
            ("tex", "tic"),
            ("ax", "ac"),
            ("ex", "ec"),
            ("ix", "ic"),
            ("lux", "luc"),
            ("uad", "uas"),
            ("vad", "vas"),
            ("cid", "cis"),
            ("lid", "lis"),
            ("erid", "eris"),
            ("pand", "pans"),
            ("end", "ens", "s"),
            ("ond", "ons"),
            ("lud", "lus"),
            ("rud", "rus"),
            ("her", "hes", "pt"),
            ("mit", "mis"),
            ("ent", "ens", "m"),
            ("ert", "ers"),
            ("et", "es", "n"),
            ("yt", "ys"),
            ("yz", "ys"))

# Hash the ending rules by the last letter of the target ending
_endingrules = defaultdict(list)
for rule in _endings:
    _endingrules[rule[0][-1]].append(rule)

_doubles = frozenset(("dd", "gg", "ll", "mm", "nn", "pp", "rr", "ss", "tt"))


def fix_ending(word):
    if word[-2:] in _doubles:
        word = word[:-1]
    
    for endingrule in _endingrules[word[-1]]:
        target, newend = endingrule[:2]
        if word.endswith(target):
            if len(endingrule) > 2:
                exceptafter = endingrule[2]
                c = word[0-(len(target)+1)]
                if c in exceptafter: return word
            
            return word[:0-len(target)] + newend
    
    return word


def stem(word):
    """Returns the stemmed version of the argument string.
    """
    return fix_ending(remove_ending(word))


"""Paice-Husk stemming
algorithm.

    stemmer = PaiceHuskStemmer(my_rules_string)
    stemmed_word = stemmer.stem(word)
"""

import re
from collections import defaultdict


class PaiceHuskStemmer(object):
    """Implements the Paice-Husk stemming algorithm.
    """
    
    rule_expr = re.compile(r"""
    ^(?P<ending>\w+)
    (?P<intact>[*]?)
    (?P<num>\d+)
    (?P<append>\w*)
    (?P<cont>[.>])
    """, re.UNICODE | re.VERBOSE)
    
    stem_expr = re.compile("^\w+", re.UNICODE)
    
    def __init__(self, ruletable):
        """
        :param ruletable: a string containing the rule data, separated
            by newlines.
        """
        self.rules = defaultdict(list)
        self.read_rules(ruletable)
    
    def read_rules(self, ruletable):
        rule_expr = self.rule_expr
        rules = self.rules
        
        for line in ruletable.split("\n"):
            line = line.strip()
            if not line:
                continue
            
            match = rule_expr.match(line)
            if match:
                ending = match.group("ending")[::-1]
                lastchar = ending[-1]
                intact = match.group("intact") == "*"
                num = int(match.group("num"))
                append = match.group("append")
                cont = match.group("cont") == ">"
                
                rules[lastchar].append((ending, intact, num, append, cont))
            else:
                raise Exception("Bad rule: %r" % line)

    def first_vowel(self, word):
        vp = min([p for p in [word.find(v) for v in "aeiou"]
                  if p > -1])
        yp = word.find("y")
        if yp > 0 and yp < vp:
            return yp
        return vp

    def strip_prefix(self, word):
        for prefix in ("kilo", "micro", "milli", "intra", "ultra", "mega",
                       "nano", "pico", "pseudo"):
            if word.startswith(prefix):
                return word[len(prefix):]
        return word

    def stem(self, word):
        """Returns a stemmed version of the argument string.
        """
        
        rules = self.rules
        match = self.stem_expr.match(word)
        if not match: return word
        stem = self.strip_prefix(match.group(0))
        
        is_intact = True
        continuing = True
        while continuing:
            pfv = self.first_vowel(stem)
            rulelist = rules.get(stem[-1])
            if not rulelist: break
            
            continuing = False
            for ending, intact, num, append, cont in rulelist:
                if stem.endswith(ending):
                    if intact and not is_intact: continue
                    newlen = len(stem) - num + len(append)
                    
                    if ((pfv == 0 and newlen < 2)
                        or (pfv > 0 and newlen < 3)):
                        # If word starts with vowel, minimum stem length is 2.
                        # If word starts with consonant, minimum stem length is
                        # 3.
                            continue
                    
                    is_intact = False
                    stem = stem[:0-num] + append
                    
                    continuing = cont
                    break
        
        return stem

# The default rules for the Paice-Husk stemming algorithm

defaultrules = """
ai*2.     { -ia > -   if intact }
a*1.      { -a > -    if intact }
bb1.      { -bb > -b   }
city3s.   { -ytic > -ys }
ci2>      { -ic > -    }
cn1t>     { -nc > -nt  }
dd1.      { -dd > -d   }
dei3y>    { -ied > -y  }
deec2ss.  { -ceed > -cess }
dee1.     { -eed > -ee }
de2>      { -ed > -    }
dooh4>    { -hood > -  }
e1>       { -e > -     }
feil1v.   { -lief > -liev }
fi2>      { -if > -    }
gni3>     { -ing > -   }
gai3y.    { -iag > -y  }
ga2>      { -ag > -    }
gg1.      { -gg > -g   }
ht*2.     { -th > -   if intact }
hsiug5ct. { -guish > -ct }
hsi3>     { -ish > -   }
i*1.      { -i > -    if intact }
i1y>      { -i > -y    }
ji1d.     { -ij > -id   --  see nois4j> & vis3j> }
juf1s.    { -fuj > -fus }
ju1d.     { -uj > -ud  }
jo1d.     { -oj > -od  }
jeh1r.    { -hej > -her }
jrev1t.   { -verj > -vert }
jsim2t.   { -misj > -mit }
jn1d.     { -nj > -nd  }
j1s.      { -j > -s    }
lbaifi6.  { -ifiabl > - }
lbai4y.   { -iabl > -y }
lba3>     { -abl > -   }
lbi3.     { -ibl > -   }
lib2l>    { -bil > -bl }
lc1.      { -cl > c    }
lufi4y.   { -iful > -y }
luf3>     { -ful > -   }
lu2.      { -ul > -    }
lai3>     { -ial > -   }
lau3>     { -ual > -   }
la2>      { -al > -    }
ll1.      { -ll > -l   }
mui3.     { -ium > -   }
mu*2.     { -um > -   if intact }
msi3>     { -ism > -   }
mm1.      { -mm > -m   }
nois4j>   { -sion > -j }
noix4ct.  { -xion > -ct }
noi3>     { -ion > -   }
nai3>     { -ian > -   }
na2>      { -an > -    }
nee0.     { protect  -een }
ne2>      { -en > -    }
nn1.      { -nn > -n   }
pihs4>    { -ship > -  }
pp1.      { -pp > -p   }
re2>      { -er > -    }
rae0.     { protect  -ear }
ra2.      { -ar > -    }
ro2>      { -or > -    }
ru2>      { -ur > -    }
rr1.      { -rr > -r   }
rt1>      { -tr > -t   }
rei3y>    { -ier > -y  }
sei3y>    { -ies > -y  }
sis2.     { -sis > -s  }
si2>      { -is > -    }
ssen4>    { -ness > -  }
ss0.      { protect  -ss }
suo3>     { -ous > -   }
su*2.     { -us > -   if intact }
s*1>      { -s > -    if intact }
s0.       { -s > -s    }
tacilp4y. { -plicat > -ply }
ta2>      { -at > -    }
tnem4>    { -ment > -  }
tne3>     { -ent > -   }
tna3>     { -ant > -   }
tpir2b.   { -ript > -rib }
tpro2b.   { -orpt > -orb }
tcud1.    { -duct > -duc }
tpmus2.   { -sumpt > -sum }
tpec2iv.  { -cept > -ceiv }
tulo2v.   { -olut > -olv }
tsis0.    { protect  -sist }
tsi3>     { -ist > -   }
tt1.      { -tt > -t   }
uqi3.     { -iqu > -   } 
ugo1.     { -ogu > -og }
vis3j>    { -siv > -j  }
vie0.     { protect  -eiv }
vi2>      { -iv > -    }
ylb1>     { -bly > -bl }
yli3y>    { -ily > -y  }
ylp0.     { protect  -ply }
yl2>      { -ly > -    }
ygo1.     { -ogy > -og }
yhp1.     { -phy > -ph }
ymo1.     { -omy > -om }
ypo1.     { -opy > -op }
yti3>     { -ity > -   }
yte3>     { -ety > -   }
ytl2.     { -lty > -l  }
yrtsi5.   { -istry > - }
yra3>     { -ary > -   }
yro3>     { -ory > -   }
yfi3.     { -ify > -   }
ycn2t>    { -ncy > -nt }
yca3>     { -acy > -   }
zi2>      { -iz > -    }
zy1s.     { -yz > -ys  }
"""

# Make the standard rules available as a module-level function

stem = PaiceHuskStemmer(defaultrules).stem

"""
Porter stemming algorithm 
"""

import re

# Suffix replacement lists

_step2list = {
              "ational": "ate",
              "tional": "tion",
              "enci": "ence",
              "anci": "ance",
              "izer": "ize",
              "bli": "ble",
              "alli": "al",
              "entli": "ent",
              "eli": "e",
              "ousli": "ous",
              "ization": "ize",
              "ation": "ate",
              "ator": "ate",
              "alism": "al",
              "iveness": "ive",
              "fulness": "ful",
              "ousness": "ous",
              "aliti": "al",
              "iviti": "ive",
              "biliti": "ble",
              "logi": "log",          
              }

_step3list = {
              "icate": "ic",
              "ative": "",
              "alize": "al",
              "iciti": "ic",
              "ical": "ic",
              "ful": "",
              "ness": "",          
              }


_cons = "[^aeiou]"
_vowel = "[aeiouy]"
_cons_seq = "[^aeiouy]+"
_vowel_seq = "[aeiou]+"

# m > 0
_mgr0 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq)
# m == 0
_meq1 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq + "(" + _vowel_seq + ")?$")
# m > 1
_mgr1 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq + _vowel_seq + _cons_seq)
# vowel in stem
_s_v = re.compile("^(" + _cons_seq + ")?" + _vowel)
# ???
_c_v = re.compile("^" + _cons_seq + _vowel + "[^aeiouwxy]$")

# Patterns used in the rules

_ed_ing = re.compile("^(.*)(ed|ing)$")
_at_bl_iz = re.compile("(at|bl|iz)$")
_step1b = re.compile("([^aeiouylsz])\\1$")
_step2 = re.compile("^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$")
_step3 = re.compile("^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$")
_step4_1 = re.compile("^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$")
_step4_2 = re.compile("^(.+?)(s|t)(ion)$")
_step5 = re.compile("^(.+?)e$")

# Stemming function

def stem(w):
    """Uses the Porter stemming algorithm to remove suffixes from English
    words.
    
    >>> stem("fundamentally")
    "fundament"
    """
    
    if len(w) < 3: return w
    
    first_is_y = w[0] == "y"
    if first_is_y:
        w = "Y" + w[1:]
        
    # Step 1a
    if w.endswith("s"):
        if w.endswith("sses"):
            w = w[:-2]
        elif w.endswith("ies"):
            w = w[:-2]
        elif w[-2] != "s":
            w = w[:-1]
    
    # Step 1b
    
    if w.endswith("eed"):
        s = w[:-3]
        if _mgr0.match(s):
            w = w[:-1]
    else:
        m = _ed_ing.match(w)
        if m:
            stem = m.group(1)
            if _s_v.match(stem):
                w = stem
                if _at_bl_iz.match(w):
                    w += "e"
                elif _step1b.match(w):
                    w = w[:-1]
                elif _c_v.match(w):
                    w += "e"
            
    # Step 1c
    
    if w.endswith("y"):
        stem = w[:-1]
        if _s_v.match(stem):
            w = stem + "i"
            
    # Step 2
    
    m = _step2.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _mgr0.match(stem):
            w = stem + _step2list[suffix]
            
    # Step 3
    
    m = _step3.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _mgr0.match(stem):
            w = stem + _step3list[suffix]

    # Step 4
    
    m = _step4_1.match(w)
    if m:
        stem = m.group(1)
        if _mgr1.match(stem):
            w = stem
    else:
        m = _step4_2.match(w)
        if m:
            stem = m.group(1) + m.group(2)
            if _mgr1.match(stem):
                w = stem
    
    # Step 5
    
    m = _step5.match(w)
    if m:
        stem = m.group(1)
        if _mgr1.match(stem) or (_meq1.match(stem) and not _c_v.match(stem)):
            w = stem
    
    if w.endswith("ll") and _mgr1.match(w):
        w = w[:-1]
    
    if first_is_y:
        w = "y" + w[1:]

    return w

if __name__ == '__main__':
    print stem("fundamentally")
    
