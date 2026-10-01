# Tunisian Arabizi → Arabic mapping

# Digits
chiffres = {
    "2": "\u0627",   # ا  hamza, normalized to plain alif (same choice as the word counter)
    "3": "\u0639",   # ع  3lech -> علاش
    "5": "\u062E",   # خ  5sara -> خسارة
    "7": "\u062D",   # ح  7aja -> حاجة
    "8": "\u063A",   # غ  8ali -> غالي
    "9": "\u0642",   # ق  9ahwa -> قهوة
}

# Single letters (vowels are provisional: they'll be the hardest part)
lettres = {
    "a": "\u0627",   # ا
    "b": "\u0628",   # ب
    "t": "\u062A",   # ت
    "j": "\u062C",   # ج
    "d": "\u062F",   # د
    "r": "\u0631",   # ر
    "z": "\u0632",   # ز
    "s": "\u0633",   # س
    "f": "\u0641",   # ف
    "q": "\u0642",   # ق
    "k": "\u0643",   # ك
    "l": "\u0644",   # ل
    "m": "\u0645",   # م
    "n": "\u0646",   # ن
    "h": "\u0647",   # ه
    "w": "\u0648",   # و
    "y": "\u064A",   # ي
    "i": "\u064A",   # ي
    "o": "\u0648",   # و
    "u": "\u0648",   # و
    "g": "\u06A8",   # ڨ  Tunisian g
    "e": "",         # usually not written in Arabic: 3lech -> علاش
}

# Two-letter combinations (not used yet: they need special handling)
combinaisons = {
    "ch": "\u0634",  # ش
    "kh": "\u062E",  # خ
    "gh": "\u063A",  # غ
    "th": "\u062B",  # ث
    "dh": "\u0630",  # ذ
}

# Test cases: (arabizi, expected Arabic)
tests = [
    ("5sara", "خسارة"),
    ("2na", "انا"),
    ("3lech", "علاش"),
    ("8ali", "غالي"),
    ("9ahwa", "قهوة"),
    ("7aja", "حاجة"),
    ("barcha", "برشا"),
    ("chnowa", "شنوة"),
    ("bahi", "باهي"),
    ("mte3i", "متاعي"),
]


def convertir(mot):
    mot = mot.lower()
    resultat = ""
    i = 0
    while i < len(mot):
        deux = mot[i:i+2]              # the next two characters
        if deux in combinaisons:
            resultat += combinaisons[deux]
            i += 2                     # we used two characters
        else:
            c = mot[i]
            if c in chiffres:
                resultat += chiffres[c]
            elif c in lettres:
                resultat += lettres[c]
            else:
                resultat += c
            i += 1                     # we used one character
    return resultat


# Run all tests
reussis = 0
for arabizi, attendu in tests:
    obtenu = convertir(arabizi)
    if obtenu == attendu:
        print("OK  ", arabizi, "→", obtenu)
        reussis += 1
    else:
        print("FAIL", arabizi, "→", obtenu, "  attendu :", attendu)

print(reussis, "/", len(tests), "tests réussis")