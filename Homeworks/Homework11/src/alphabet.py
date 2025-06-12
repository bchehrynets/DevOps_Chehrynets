import string

# Base Alphabet class
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print("Alphabet letters:", ' '.join(self.letters))

    def letters_num(self):
        return len(self.letters)

# Derived EngAlphabet class
class EngAlphabet(Alphabet):
    _letters_num = 26  # Static private attribute

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return EngAlphabet._letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."

# Main testing block
if __name__ == "__main__":
    eng_alphabet = EngAlphabet()

    # Print all letters
    eng_alphabet.print()

    # Print number of letters
    print("Number of letters:", eng_alphabet.letters_num())

    # Check if 'F' belongs to English alphabet
    print("'F' is in English alphabet:", eng_alphabet.is_en_letter('F'))

    # Check if 'Щ' belongs to English alphabet
    print("'Щ' is in English alphabet:", eng_alphabet.is_en_letter('Щ'))

    # Print example text
    print("Example text:", EngAlphabet.example())

