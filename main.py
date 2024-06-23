from dfa_builder import DFABuilder
from sentence_parser import PushdownParser
import json

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.upper().split()

    with open('dfa_config.json') as f:
        config = json.load(f)

    subject_dfa = DFABuilder.from_config(config["subjek"])
    predicate_dfa = DFABuilder.from_config(config["predikat"])
    object_dfa = DFABuilder.from_config(config["objek"])
    adverb_dfa = DFABuilder.from_config(config["keterangan"])

    tokens = []
    for word in words:
        if subject_dfa.simulate(word):
            tokens.append('S')
        elif predicate_dfa.simulate(word):
            tokens.append('P')
        elif object_dfa.simulate(word):
            tokens.append('O')
        elif adverb_dfa.simulate(word):
            tokens.append('K')
        else:
            print(f"Unknown word: {word}")
            return

    parser = PushdownParser()
    is_valid = parser.parse(tokens)

    if is_valid:
        print("The sentence is valid.")
    else:
        print("The sentence is invalid.")

if __name__ == "__main__":
    main()
