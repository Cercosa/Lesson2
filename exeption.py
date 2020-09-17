def ask_me():
    while True: 
        try:
            user_say = input('Ask me something: ')
            computers_answers = {"How are you?": "I'm fine",
                             "What are you doing?": "I'am coding",
                             "It's a good weather today?": "Yes, it is",
                             "Are you happy today?": "Yes, I am"}
            
            if computers_answers[user_say] == "I'm fine":
                print(computers_answers[user_say])
                break
        
            else:
                print(computers_answers[user_say])
        except KeyError:
            print('''I dont understand you, sorry try again. 
You can ask me only:
-How are you?
-What are you doing?
-It's a good weather today?
-Are you happy today?''')
        except KeyboardInterrupt:
            print("Bye!")    
            
if __name__=='__main__':     
    ask_me()