def get_answer(question):
	answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех', 'Пока': 'Увидимся'}
	return answers[question]
question=input('введите привет,как дела,пока')
print (get_answer(question))
