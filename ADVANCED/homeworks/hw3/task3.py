# В большой текстовой строке подсчитать количество встречаемых слов 
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

txt = input("введите строку: ")
WORDS = 10
punctuation = "+-—.,;:!?,'"""

for char in punctuation:
    txt = txt.replace(char, " ")

words = (txt.lower()).split()
all_words_set = set(words)
word_dict = {}

for word in all_words_set:
    word_dict[word] = words.count(word)

for i in range(WORDS):
    max_count = 0
    current_key = ""

    for word in all_words_set:
        if word_dict.get(word) > max_count:
            max_count = word_dict.get(word)
            current_key = word

    print(f"{i+1} место часто встречающихся слов '{current_key}', {word_dict.get(current_key)} раз")
    del word_dict[current_key]
    all_words_set.remove(current_key)

"""
для копирования
Комаров лежит на диване и смотрит телевизор. В руке у него пульт. На экране девушка с ясными глазами рассказывает последние новости. Палец нажимает кнопку. Девушка пропадает. Какой-то старик вскапывает огород. Палец на кнопку. По льду носятся вспотевшие хоккеисты. Кнопка. Две женщины плачут. Одна утешает другую словами: «Он обязательно вернётся». Кнопка. Какие-то англичане учат ловить большую рыбу в Северном море. Кнопка. Стрельба. К раненному подбегает красотка. Кнопка. Опять новости. Но уже с другой бабой. Кнопка. Мультфильмы. Кнопка. Рекламируют средство от диареи. Кнопка. Афроамериканка с большими грудью и губами ритмично танцуепоёт. Кнопка. Старый чёрно-белый фильм с носатыми и курчавыми итальянцами. Кнопка… Комаров вместе с диваном и пультом пропадает. Вспышка и его нет. Вместо него на экране спортсмены бегут марафон. Петраков сжимает в правой руке пульт и ему кажется, что он управляет эфиром. Окно телевизора светится. Листающему каналы Петракову кажется, что он сейчас решает, что ему покажут. Кнопка. Вспышка. Рецепт салата со сладким перцем. Кнопка. Кино про пришельцев. Среди марсиан испуганный Комаров показывает кому-то пульт, как паспорт. На его лице паника, начало истерики и развитие ужаса. Петраков его толком не разглядел. Опять кнопка. Война в пустыне. Из БТР пытается высунуть голову Комаров и позвать на помощь. Не успевает. Кнопка. Вспышка. Телевизор превращается в шкап морга. Диван с Петраковым и пультом превращается в группу криминалистов. Идёт отличный детективный сериал. Комаров его переключать не собирается. К Комарову на диван подсаживается девушка-диктор с ясными глазами и ласково что-то шепчет на ухо. Пахнет хоккейным потом. Девушка открывает форточку. В комнату заваливают чёрно-белые курчавые итальянцы, плачущие бабы, английские рыбаки, мускулистые марафонцы, груди и губы танцуепоющей афроамериканки, раненный боец, красотка, смешарики, дед с лопатой и кулинар с перцем. У каждого из них в каждой руке по пульту. Вспышка. Присутствующие не замечают, как хозяин комнаты пропал, зато замечают, что включился телевизор, на экране которого боксёры. Боксёр в синих трусах очень похож на Комарова, в красных – вылитая копия Петракова. Бьют они друг друга безжалостно. Компания перед экраном улюлюкает, визжит и кричит, болея за спортсменов.  Приносят пиво. Болельщики перед телевизором неистовствуют. Боксёры безмолвствуют. Удар в челюсть. Нокаут! Свет гаснет. Электричество совсем кончилось.
"""