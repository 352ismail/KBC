questions=[{'Question':'The International Literacy Day is observed on', 
            'Score':100000,
                    'Options':
                    {
                        'A:Sep 8','B:Nov 28','C:May 2','D:Sep 22'
                    }
                    ,'Answer':'D'
            },
            {'Question':'The language of Lakshadweep. a Union Territory of India, is', 
             'Score':500000,
                    'Options':
                    {
                        'A:Tamil','B:Hindi','C:Malayalam','D:Telugu'
                    },
                    'Answer':'B'
            },
            {'Question':'In which group of places the Kumbha Mela is held every twelve years?', 
             'Score':550000,
                    'Options':
                    {
                        'A:Ujjain. Purl; Prayag. Haridwar','B:Prayag. Haridwar, Ujjain,. Nasik','C:Rameshwaram. Purl, Badrinath. Dwarika','D:Chittakoot, Ujjain, Prayag,\'Haridwar'
                    },
                     'Answer':'C'
            },
            {'Question':'Bahubali festival is related to', 
             'Score':900000,
                    'Options':
                    {
                       'A:Islam','B:Hinduism','C:Buddhism','D:Jainism'
                    }
                     ,'Answer':'B'
            },
            {'Question':'Which day is observed as the World Standards  Day?', 
             'Score':2000000,
                    'Options':
                    {
                       'A:June 26','B:Oct 14','C:Nov 15','D:Dec 2'
                    }
                     ,'Answer':'D'
            }]

totalscore = 0

for question in questions:
    print(question["Question"] , "Options = ","\n", question["Options"] ,"\n")
    answer = input("Enter your answer: ")
    if(question["Answer"] == answer.upper()):
        score = question["Score"]
        print(f"Correct answer You have earned:{score}")
        totalscore = totalscore+question["Score"]
    else:
        print("Incorrect answer")

if totalscore > 0:
    print(f"Congratulations you have earned = {totalscore}")
else:
    print("Better Luck next time !")




# print(questions[0])