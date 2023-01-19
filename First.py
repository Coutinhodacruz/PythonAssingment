
print("Wellcome to quiz game !!")
print('if your spelling is incorrect then you are wrong answer')
score = 0

question_no = 0
playing = input('Do you want to play ? ').lower()

if playing == 'yes':

    question_no = 1
    ques = input(f'\n (question_no) b.spell boy? ')
    if ques == 'boy':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Boy')

    question_no += 1
    ques = input(f'\n(question_no).Spell girl? ')
    
    if ques == 'Girl':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Girl')


    question_no += 1
    ques = input(f'\n(question_no). Spell Government? ')
    
    if ques == 'Government':
        score +=1
        print('correct! you got 1 point')
    else:
        print('Incorrect!')
        print(f'current answer is ---> Gorvernment')


   