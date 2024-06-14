#input string to check its content:
class string():
    def __init__(self):
        self.vowels = 0
        self.consonants = 0
        self.space =0
        self.lowercase = 0
        self.uppercase= 0
        self.string = input("Enter the string: ")
    def count_uppercase(self):
        for letter in self.string:
            if(letter.isupper()):
                self.uppercase += 1
        print("Total number of uppercase:",self.uppercase)

    def count_lowercase(self):
        for letter in self.string:
            if(letter.islower()):
                self.lowercase += 1
        print("Total number of lowercase",self.lowercase)
    def count_vowels(self):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i in self.string:
            if i in vowel:
                self.vowels +=1
            else:
                continue
        print("Total number of vowels:",self.vowels)

    def count_consonants(self):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i in self.string:
            if i not in vowel:
                self.consonants += 1
        print("Total number of consonants:",self.consonants)

    def count_spaces(self):
        for i in self.string:
            if i == " ":
                self.space +=1
        print("Total number of spaces:",self.space)
s = string()
s.count_consonants()
s.count_vowels()
s.count_lowercase()
s.count_uppercase()
s.count_spaces()

