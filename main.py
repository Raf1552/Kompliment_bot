# -*- coding: utf-8 -*-
# Ну попробуем вспомнить что-то
import telebot
import random
random.random()
cpicok=['Ты всегда знаешь, как меня удивить.', 'Глядя на тебя, понимаешь, что спорт — это сила', 'Потрясающая фигура! Тебя легко принять за фитнес-тренера или спортсменку', 'Прости, засмотрелся на тебя и потерял мысль. Ты не могла бы повторить все еще раз?', 'Если быть красивой считается преступлением, то тебя объявят виновной.', 'Я вижу столько тепла в твоих глазах.', 'Не переставай улыбаться, твоя улыбка обворожительна!', 'Мне нравится твой стиль.', 'Это платье идеально сидит на тебе. Я ему даже завидую.', 'Ты очень вкусно пахнешь.', 'Твой смех очаровывает!', 'Я очень сильно ценю тебя.', 'Ты прекрасный слушатель.', 'Ты очень добра к людям вокруг тебя.', 'У тебя всегда самые лучшие идеи.', 'Ты очень талантливая и креативная девушка', 'Твой голос очень мелодичный и волнующий.', 'У тебя безукоризненные манеры.', 'Ты отлично владеешь искусством оказываться в нужное время в нужном месте!', 'Как тебе удается находить выход из безвыходных ситуаций?!', 'Я хотел бы встретить тебя еще в детстве.', 'Ты заслуживаешь объятия прямо сейчас.', 'Ты являешься прекрасным примером для других.', 'Ты всегда можешь подобрать правильные слова.', 'Мне очень нравятся твои причуды.', 'Мне нравится гулять с тобой.', 'С тобой я могу говорить обо всем.', 'С тобой мне всегда очень комфортно.', 'Я благодарен за то, что ты есть.', 'Ты всегда знаешь, как меня удивить.', 'Даже kогда ты рядом, мне кажется, что тебя не хватает.', 'Ты понимаешь меня настолько хорошо, как будто читаешь мои мысли.', 'Просто проводить время с умной, интеллигентной девушкой уже приносит незабываемые минуты радости.', 'Ты классная собеседница. Когда общаюсь с тобой, даже не замечаю, как пролетает время.', 'Невероятна, когда не боишься быть собой.', 'Твоя действия говорят больше, чем слова.', 'Меня поражает твоя открытость и искренность.', 'Я полностью обезоружен твоим остроумием.', 'У меня мурашки от тебя.', 'Ты как магнит притягиваешь к себе.', 'С тобой очень легко и приятно говорить, ты умеешь располагать к себе парней.', 'Вот смотрю на тебя и понимаю, что в человеке может быть прекрасна душа, тело и мысли.', 'Рядом с тобой я могу быть самим собой.', 'Ты важна для меня', 'Ты даришь мне вдохновение в жизни, которое ранее меня не посещало. Классно, что я встретил тебя, очаровательная муза!', 'Благодаря тебе я поверил в то, что действительно бывают родственные души.', 'Мне очень важно выслушать твое мнение', 'Обожаю твои милые странности', 'Ты потрясающий друг!', 'Ты – уникальная! В тебя нельзя не влюбиться.', 'Ты – мой антидепрессант!', 'Всякий раз, когда мне грустно, мысль о тебе сразу поднимает настроение.', 'Доверяю твоей интуиции.', 'Ты понимаешь меня лучше всех на свете.', 'Ты даешь мне уверенность в себе и всегда меня поддерживаешь. Ты моя надежда и любовь.', 'Ты удивительная девушка, которая может служить примером для всех остальных.' ,'Твой творческий потенциал кажется безграничным.', 'Ты на самом деле знаешь кто ты и чего хочешь.', 'Ты знаешь себе цену.', 'Ты всегда изучаешь новые вещи и пытаешься развиваться — это потрясающе.', 'Я не сумел бы завершить это дело без твоей помощи.', 'Много читаешь? Порекомендуешь что-нибудь? Мне почему-то кажется, что ты сразу же угадаешь книгу, которая мне понравится.']
cpicok1=['Тебе я готов рассказать всё о себе, потому что знаю, что ты надёжный!', 'Таких друзей как ты не сыскать на всём белом свете!', 'Я рад тому, то у меня есть такой друг как ты!', 'Быть другом это призвание и это призвание твоё!', 'А говорят настоящих друзей нет, но это не правда, ведь ты то есть!','Наша дружба для меня на вес золота!', 'Я постоянно удивляюсь тебе, какой же всё-таки ты хороший друг!', 'Благодарю тебя за всё что ты для меня делаешь, ты классный друг!', 'Я уверен, что если со мной случится беда, первым на помощь придёшь именно ты!', 'Какой же у тебя крепкий характер, словно сталь, молодец!', 'Лучшие комплименты другу', 'Ты всегда меня выручаешь, ценишь, уважаешь, и это взаимно, дружище!', 'Я искренне надеюсь на то, что наша дружба будет вечной!']
imenaG=['Влада', 'Елена', 'Ленушка', 'Лена', 'Леночка', 'Ленуся', 'Алёнка', 'Леся', 'Еленя', 'Еля', 'Ела', 'Елюша', 'Елюся', 'Люся', 'Еленка', 'Лёна', 'Лёся', 'Лёля', 'Ленуша', 'Алин', 'Элин', 'Эли', 'Элла', 'Хеля', 'Эленита', 'Лалла','Владлена', 'Александра', 'Марина', 'Маринка', 'Маринуша', 'Мариша', 'Маша', 'Марися', 'Маря', 'Мара', 'Маруся', 'Муся', 'Ина'  , 'Владленка', 'Александра', 'Владя', 'Ладя', 'Вадя', 'Леня', 'Александрушка' , 'Алексаня','Алексана', 'Саня', 'Санюра', 'Санюта', 'Санюха', 'Санюша', 'Алексаха', 'Алексаша', 'Саша', 'Сашуха', 'Сашуля' , 'Сашуня' , 'Сашута', 'Сашура', 'Шура', 'Шурёна', 'Шуруня', 'Шурка', 'Алекся', 'Алексюха', 'Алексюша', 'Аля', 'Ася', 'Лекса', 'Лексаня', 'Лексана', 'Лексаша']
imenaB=['Пётр','Гриша','Григорий ', 'Грег','Давидка', 'Давидок', 'Дава', 'Додя', 'Видя', 'Давыдка', 'Давыдок','Григорьюшка', 'Григоря', 'Григора', 'Гриха', 'Гриша', 'Гришко', 'Гришака', 'Гришука', 'Гришаня', 'Гришата', 'Гришоня', 'Гришуня', 'Гришута', 'Гришуха', 'Гриня', 'Гринюка', 'Гринюха', 'Гринюша', 'Грика', 'Горя', 'Гора','Давид','Алексей','Алексейка', 'Алёха', 'Лёха', 'Алёша', 'Лёша', 'Алёня', 'Лёня', 'Алёка', 'Алека', 'Лёка', 'Лека', 'Лёля', 'Аля', 'Алюня', 'Люня', 'Лексейка', 'Лекса', 'Лекся', 'Лёкса', 'Лёкся','Петр', 'Петя', 'Петро', 'Петруня', 'Петруся', 'Петруха', 'Петруша', 'Петря', 'Пета', 'Петраша', 'Петряй', 'Петряка', 'Петряня', 'Петрята', 'Петряха', 'Петряша', 'Петуня', 'Петуся', 'Петуха', 'Петуша', 'Петрушка', 'Петюка', 'Петюня', 'Петюся', 'Петюха', 'Петюша', 'Петяй', 'Петяйка', 'Петяня', 'Петян', 'Петяха', 'Петяша', 'Петька', 'Петрик', 'Петечка','Кирилл','Кирилка', 'Киря', 'Кира', 'Кирюха', 'Кируха', 'Кирюша', 'Кирюня', 'Кируня', 'Кируся', 'Киряха', 'Киряша','Павелка', 'Павлик',' Павлуня', 'Павлюня', 'Павлуся', 'Павлюся', 'Павлуха', 'Павлуша', 'Павля', 'Павлюка', 'Павлюкаша', 'Павша', 'Пава', 'Паха', 'Паша', 'Павел','Пашата', 'Пашуня', 'Пашута', 'Пашуха', 'Паня', 'Пана', 'Панюта', 'Панюха', 'Панюша', 'Паняша', 'Паля', 'Палюня', 'Палуня','Фёдорка', 'Федя', 'Федька', 'Федор', 'Фёдор', 'Феденька', 'Федюня', 'Федюся', 'Федуся', 'Федюха', 'Федюша', 'Федяйка', 'Федяка', 'Федяня', 'Федяша', ]
b=len(cpicok)-1
c=len(cpicok1)-1
bot=telebot.TeleBot('970360053:AAHmMP9VAuOO8kHvmk4jlvZcvteAI7rOAAo')
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши своё имя')
@bot.message_handler(content_types=['text'])

def konpliment(message):
    print(message.from_user.first_name+'   '+message.text)
    schetchik = 0
    for i in imenaG:
        if message.text == i:
            bot.send_message(message.chat.id, text=f"{message.text}"+'!'+' '+cpicok[random.randint(1,b)])
            schetchik=+1
            print(schetchik)
            continue
    for i in imenaB:
        if message.text == i:
            bot.send_message(message.chat.id, text=f"{message.text}" + '!' + ' ' + cpicok1[random.randint(1, c)])
            schetchik = +1
            print(schetchik)
            continue
    if schetchik==0:
        if message.text == 'Абзал':
            bot.send_message(message.chat.id, text='Абике, где этот бот учился, ты преподавал')
        elif message.text == 'Пероша':
            bot.send_message(message.chat.id, text='Тебя Пероша разве завут?')
        elif message.text== 'Раф' or message.text== 'Рафис':
            bot.send_message(message.chat.id, text='Не адманывай '+ message.from_user.first_name )
        elif message.text == 'Жамес':
            bot.send_message(message.chat.id, text='Тебя Жамес разве завут?')
        elif message.text == 'Эклерушка':
            bot.send_message(message.chat.id, text='Эх, Лена, Лена')
        else:
            bot.send_message(message.chat.id, text='таких имён не знаю, а знаю такое имя как '+ imenaG[random.randint(1, len(imenaG))]+', например, или '+imenaB[random.randint(1, len(imenaB))])



bot.polling()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/