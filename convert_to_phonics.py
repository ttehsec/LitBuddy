import json
import os
import pronouncing
import re

def simple_grapheme_split(word):
    # Basic mapping for common phonics chunks
    graphemes = ["ch", "sh", "th", "wh", "ph", "ck", "qu", "ng"]
    result = []
    i = 0
    while i < len(word):
        chunk = word[i:i+2]
        if chunk in graphemes:
            result.append(chunk)
            i += 2
        else:
            result.append(word[i])
            i += 1
    return result

def convert_word(word_obj):
    word = word_obj["word"]
    phones_list = pronouncing.phones_for_word(word)
    phonemes = phones_list[0].split() if phones_list else []
    graphemes = simple_grapheme_split(word.lower())
    word_obj["phonics"] = graphemes
    word_obj["phonemes"] = phonemes
    return word_obj

def convert_file(input_path, output_path):
    with open(input_path) as f:
        data = json.load(f)

    print(f"Loaded {len(data)} words from {input_path}")

    converted = []
    for word_obj in data:
        converted.append(convert_word(word_obj))

    with open(output_path, "w") as out:
        json.dump(converted, out, indent=2)
    print(f"✅ Saved {len(converted)} phonics-ready words to {output_path}")

# Example usage
if __name__ == "__main__":
    convert_file("wordlists/custom_words.json", "wordlists/custom_words_with_phonics.json")
