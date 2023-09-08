class Anagram :
    match_list = ["hello", "goodbye"]
    match_list2 = ["listen", "poison", "hello"]
    def __init__(self, word):
        self.word = word

    def word (self):
        return self.word    

    def match (self, new_word):
        if new_word in self.match_list :
            print (anagram.new_word)
            self.word = new_word
        else:
            print ([])    

    new_word = property(word, match,)

    def match_checker (self, new_list):
        for new_list in self.match_list2 :
            return new_list != self.word and sorted(new_list) == sorted(self.word)
            self.word = new_list
        
        

anagram = Anagram("men")  
print (anagram.word)
anagram.new_word= "hello"         
anagram.new_list