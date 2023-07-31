from random import choice

_diction = {}


def quest(question, answers, try_count):
    count = try_count + 1

    while try_count > 0:
        print(question)
        answer = input('Ваш ответ? >>> ').lower()
        if answer in answers:
            print(f'Бинго, отгадано за {count - try_count} попыток!')
            _diction[question] = f'{count - try_count} попыток(ка)'
            break
        else:
            print('Ответ неверный')
            try_count -= 1
    else:
        print('Попытки исчерпаны')


def list_quest(iters):
    quests = { \
        'Сколько ног у муравья?' : [str(i) for i in range(1, 7)],
        'Какого цвета огнетушитель?' : ['красный', 'синий', 'оранжевый'],
        'Сколько тебе было лет в детстве?' : [str(i) for i in range(19)],
        'Идут два крокодила, один зеленый, другой направо. Зачем мне холодильник, если я не курю?' : ['да', 'гладиолус', 'пежо']
        }
    for i in range(iters):
        temp = choice(list(quests.keys()))
        quest(temp, quests[temp], 3)


def how_many_answers():
    print(*(f'Загадака "{key[:15]}..." была отгадана за {value}' \
            for key, value in _diction.items()), sep='\n')

if __name__ == '__main__':
    list_quest(3)
    how_many_answers()