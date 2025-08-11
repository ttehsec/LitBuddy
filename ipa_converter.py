import pronouncing
import json
# import time  # Uncomment if using speak_chunk

# ✅ Manual override for tricky words
custom_phonemes = {
    "chicken": ["CH", "IH", "K", "IH", "N"],
    "elephant": ["EH", "L", "AH", "F", "AH", "N", "T"],
    "school": ["S", "K", "UW", "L"],
    "yellow": ["Y", "EH", "L", "OW"]
}

# ✅ CMU phoneme to IPA
cmu_to_ipa = {
    "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ",
    "EY": "eɪ", "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i",
    "JH": "dʒ", "K": "k", "L": "l", "M": "m", "N": "n", "NG": "ŋ",
    "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "ɹ", "S": "s", "SH": "ʃ",
    "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u", "V": "v", "W": "w",
    "Y": "j", "Z": "z", "ZH": "ʒ"
}


def clean_phonemes(phoneme_list):
    return [p.strip("0123456789") for p in phoneme_list]


def phonemes_to_ipa(phonemes):
    return [cmu_to_ipa.get(p, p.lower()) for p in phonemes]


def group_phonemes(phonemes):
    vowels = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
    chunks = []
    current_chunk = []

    for phoneme in phonemes:
        current_chunk.append(phoneme)
        if phoneme in vowels:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def breakdown_phonemes(phonemes):
    vowels = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
    consonants = {
        "B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L", "M", "N", "NG",
        "P", "R", "S", "SH", "T", "TH", "V", "W", "Y", "Z", "ZH"
    }

    cleaned = clean_phonemes(phonemes)

    for i, p in enumerate(cleaned):
        if p in vowels:
            prefix = cleaned[:i]
            vowel = [p]
            suffix = cleaned[i+1:]

            return {
                "prefix": phonemes_to_ipa(prefix),
                "vowel": phonemes_to_ipa(vowel),
                "suffix": phonemes_to_ipa(suffix),
                "consonants": phonemes_to_ipa([ph for ph in cleaned if ph in consonants])
            }

    return {
        "prefix": phonemes_to_ipa(cleaned),
        "vowel": [],
        "suffix": [],
        "consonants": phonemes_to_ipa([ph for ph in cleaned if ph in consonants])
    }


def generate_data(wordlist, speak=False):
    data = {}
    missing_words = []

    for word in wordlist:
        word = word.lower()

        # Get ARPAbet phonemes
        if word in custom_phonemes:
            arpabet = custom_phonemes[word]
        else:
            phones = pronouncing.phones_for_word(word)
            if not phones:
                arpabet = []
                missing_words.append(word)
            else:
                arpabet = clean_phonemes(phones[0].split())

        # Convert to IPA
        ipa = phonemes_to_ipa(arpabet)

        # Group ARPAbet and IPA chunks
        arpabet_chunks = group_phonemes(arpabet)
        ipa_chunks = ["".join(phonemes_to_ipa(chunk.split())) for chunk in arpabet_chunks]

        # Structural breakdown
        structure = breakdown_phonemes(arpabet)

        # Optional: Speak each chunk
        if speak:
            for chunk in ipa_chunks:
                print(f"🔊 {chunk}")
                speak_chunk(chunk)  # You must define this function
                time.sleep(0.3)

        # Store data
        data[word] = {
            "arpabet": arpabet,
            "ipa": ipa,
            "chunks": ipa_chunks,
            "syllables": ipa_chunks,
            "structure": structure
        }

    if missing_words:
        print(f"⚠️ Missing phonemes for: {', '.join(missing_words)}")

    return data
