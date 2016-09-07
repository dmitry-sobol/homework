__author__ = 'dmitry-sobol'

#vars init
i = 0
true_answers = 0

#questions and answers
question = ['Опишите одним словом вторую версию пайтона?', 
            'А третью?', 
            'Какая кодировка используется в python3 по умолчанию?',
            'Как инициировать git репозиторий?',
            'Как сделать коммит в git?']
answer = ['плохая', 
          'хорошая',
          'unicode',
          'git init',
          'git commit']

while i < len(question):
    print (question[i], ":")
    user_answer = input()
    if user_answer == (answer[i]):
        true_answers += 1
        print ("Ответ верный, верных ответов: ", true_answers, "\n")
    else:
        print ("Ответ неверный \n")
    i += 1