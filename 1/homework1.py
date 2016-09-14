__author__ = 'dmitry-sobol'

#vars init
i = 0
a = 0
true_answers = 0

#questions and answers
question = ['Опишите одним словом вторую версию пайтона? \n', 
            'А третью?', 
            'Какая кодировка используется в python3 по умолчанию?',
            'Как инициировать git репозиторий?',
            'Как сделать коммит в git?']
answer = ['плохая', 
          'хорошая',
          'unicode',
          'git init',
          'git commit']

for i in question:
    user_answer = input(i)
    if user_answer == (answer[a]):
        true_answers += 1
        print("Ответ верный, верных ответов: ", true_answers, "\n")
    else:
        print("Ответ неверный \n")
    a += 1