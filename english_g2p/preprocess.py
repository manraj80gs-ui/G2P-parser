from pathlib import Path
import json
import re


class DictionaryParser:

    def __init__(self, dictionary_file):
        self.dictionary_file = Path(dictionary_file)

    def parse(self):

        pronunciation = {}

        with open(self.dictionary_file, encoding="utf8") as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                if "(set! wordstruct" not in line:
                    continue

                # Extract word
                word = line.split("(set!")[0].strip()

                # Extract phones
                phones = re.findall(r'"([^"]+)"', line)

                pronunciation[word] = phones

        return pronunciation


def main():

    ROOT = Path(__file__).resolve().parent.parent

    dictionary = ROOT / "data" / "IE_dict_9Jan2023"

    parser = DictionaryParser(dictionary)

    pronunciation = parser.parse()

    output = ROOT / "data" / "pronunciation.json"

    with open(output, "w", encoding="utf8") as f:
        json.dump(pronunciation, f, indent=2)

    print(f"Parsed {len(pronunciation):,} words")
    print("Saved pronunciation.json")


if __name__ == "__main__":
    main()
