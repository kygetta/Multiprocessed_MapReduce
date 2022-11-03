import sys

class mapper():
    
    def __init__(self, ):
        pass
        
    def map_words(self, words):
        
        #Takes input of words from text file and creates an array with a key value pair
        output = []
        for word in words:
            output.append({word: 1})
            
        return output #output is an array of dictionary with key value pairs
            
        
class reducer():

    def __init__(self):
        pass
        
    def sort(self, mapped_words):
        
        # SORT
        sorted_words = {}
        for mapped_word in mapped_words:  # mapped_word = {'the':1}, {'brown':1}, {'fox':1}, etc..
            for key, value in mapped_word.items(): # key = word, value = 1
                if key not in sorted_words:
                    sorted_words[key] = [value]
                else:
                    sorted_words[key].append(value) #if key is already in there then append the value to the array
                
        return sorted_words
        
    def reduce(self, sorted_words): #loop through sorted words (each key-val pair) and setting up each array that we have. Sum up the array
        
        output = {}
        for key, value in sorted_words.items():
            output[key] = sum(value)
            
        return output
        
if __name__ == "__main__":
    
    print()
    
    data = None
    with open('word.txt', 'r') as f:
        data = f.readlines()
    
    data = data[0].split(' ')
    
    mapper = mapper()
    reducer = reducer()
    
    mapped_words = mapper.map_words(data)
    print('Mapped Words') 
    print(mapped_words)
    print()
    
    sorted_words = reducer.sort(mapped_words)
    print('Sorted Words')
    print(sorted_words)
    print()
    
    reduced_word_count = reducer.reduce(sorted_words)
    print('Reduced Output')
    print(reduced_word_count)
    print()