def average_score():
    school_total_scores = 0
    counter = 0
    
    scores_lists = [
    {'school_class': '4"A"', 'scores': [3,4,4,5,2]}, 
    {'school_class': '4"B"', 'scores': [3,3,3,4,5]}, 
    {'school_class': '5"V"', 'scores': [4,4,4,5,3]}, 
    {'school_class': '4"V"', 'scores': [5,5,5,5,4]}, 
    {'school_class': '5"B"', 'scores': [3,3,3,5,3]}
]
    for school_class in scores_lists:
        scores = school_class['scores']
        
        total_scores = 0
        for i in scores:
            counter = counter + 1
            total_scores = total_scores + i
            
        scores_avg = total_scores / len(scores)
        Grade = school_class['school_class']

        print(f"Class average score in grade {Grade} is - {scores_avg}")
        
        school_total_scores = school_total_scores + total_scores
        
    school_total_aver_score = school_total_scores / counter  
    print('School total average score is - ', school_total_aver_score)
        
if __name__=='__main__':     
    average_score()