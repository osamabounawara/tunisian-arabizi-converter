# Arabizi Converter

Converts Tunisian Arabizi to Arabic script, in Python.

```
3aslema → عسلامة
sa7bi   → صاحبي
barcha  → برشا
```

## What is Arabizi?

Arabizi is Arabic written with Latin letters and digits. In Tunisia, it's how most people write darija online: on Facebook, Messenger, SMS, in comments and group chats.

It appeared in the late 1990s and 2000s, when phones and computers often had no Arabic keyboard. People wrote Arabic with the Latin keys they had, and used digits for the sounds that Latin letters can't express, picking the digit that **looks like** the Arabic letter:

| Digit | Letter | Example |
|---|---|---|
| 2 | ء | 2na |
| 3 | ع | 3aslema |
| 5 | خ | 5obz |
| 7 | ح | 7aja |
| 8 | غ | 8ali |
| 9 | ق | 9ahwa |

Arabizi has no official spelling (`barcha`, `barsha`, `barcha2`…), and very few tools can read it.

## How it works

```bash
python3 converter.py
```

1. **Lexicon first:** if the word is known, return its correct spelling (`sa7bi` → صاحبي).
2. **Otherwise, rules:** two-letter combinations first (`ch` → ش, `kh` → خ), then digits, then single letters.

## Results

**3 / 10** test words converted perfectly. Test words are never added to the lexicon, so the score stays honest.

Most errors come from information that simply isn't in the Arabizi spelling:

- **Final `a`:** `7aja` → حاجة but `barcha` → برشا. Same ending, different letter.
- **Short or long vowels:** the `a` in `9ahwa` isn't written in Arabic, the one in `5sara` is.
- **The Tunisian `e`:** in `mte3i` → متاعي, the `e` stands for a long ا (imala).
- **`s` → س or ص:** `sa7bi` needs ص, and nothing in the spelling says so.

Rules can't solve these. A larger lexicon helps, and learning from real data is the next step.

## Next steps

- [ ] 50 test cases, run with pytest
- [ ] Convert a word from the command line: `python3 converter.py 3aslema`
- [ ] Arabic → Arabizi
