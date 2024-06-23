from dfa_builder import DFABuilder
from sentence_parser import PushdownParser
import json

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.upper().split()

    with open('dfa_config.json') as f:
        config = json.load(f)

    subjek_dfa = DFABuilder.from_config(config["subjek"])
    predikat_dfa = DFABuilder.from_config(config["predikat"])
    objek_dfa = DFABuilder.from_config(config["objek"])
    keterangan_dfa = DFABuilder.from_config(config["keterangan"])
    
    tokens = []
    for word in words:
        if subjek_dfa.simulate(word):
            tokens.append('S')
        elif predikat_dfa.simulate(word):
            tokens.append('P')
        elif objek_dfa.simulate(word):
            tokens.append('O')
        elif keterangan_dfa.simulate(word):
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
