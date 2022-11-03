import sys
import json
import datetime
#This program is not multiprocessed.. that will be the homework


class mapper():
    
    def __init__(self, ):
        pass
        
    def map_reviews(self, reviews):
        
        output = []
        for review in reviews:
            output.append({review['movie']: review['rating']})
            
        return output
            
        
class reducer():

    def __init__(self):
        pass
        
    def sort(self, mapped_reviews):
        
        # SORT
        sorted_reviews = {}
        for mapped_review in mapped_reviews:  # mapped_reviews = [{'War Dogs':4}, {'Top Gun':5}, ...]
            for key, value in mapped_review.items(): # key = review, value = rating
                if key not in sorted_reviews:
                    sorted_reviews[key] = [value]
                else:
                    sorted_reviews[key].append(value)
                
        return sorted_reviews
        
    def reduce(self, sorted_reviews):
        
        output = {}
        for key, value in sorted_reviews.items():
            output[key] = sum(value) / len(value)
            
        return output
        
if __name__ == "__main__":
    
    startTime = datetime.datetime.now()

    print()
    
    data = None
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    
    print(data)

    mapper = mapper()
    reducer = reducer()
    
    mapped_reviews = mapper.map_reviews(data)
    print('Mapped Words')
    print(mapped_reviews)
    print()

#sorts to combine reviews into one long list
    sorted_reviews = reducer.sort(mapped_reviews)
    print('Sorted Reviews')
    print(sorted_reviews)
    print()
    
    #finds average review for each movie
    review_avg = reducer.reduce(sorted_reviews)
    print('Reduced Output')
    print(review_avg)
    print()
    
    endtime = datetime.datetime.now() - startTime
    print(endtime)