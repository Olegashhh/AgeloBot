# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAP
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
!pip install pyTelegramBotAPI

from telebot import TeleBot, types
import random

bot = TeleBot(token='5994359949:AAHz-0cRmQHCKJe7xhdzhkYfqSyHavSyfV0', parse_mode='html') # создание бота

# объект клавиаутры
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keybaord.row(
   types.KeyboardButton(text='Избранные новинки'),
    types.KeyboardButton(text='Выбор редакции'),
)
# второй ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='Книга + кино'),
    types.KeyboardButton(text='приободряшка'),
)


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе с выбором подкаста\nВыбери желаемый вариант:', # текст сообщения
        reply_markup=card_type_keybaord,
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # проверяем текст сообщения на совпадение с текстом какой либо из кнопок
    # в зависимости от типа карты присваем занчение переменной 'card_type'
    if message.text == 'Избранные новинки':
       bot.send_message(message.from_user.id, 'Посмотри главные выпуски недели на любой вкус.\n \nПодробнее ознакомься по ' + '[ссылке](https://music.yandex.ru/users/yamusic-podcast/playlists/1019)', parse_mode='Markdown')
    elif message.text == 'Выбор редакции':
        bot.send_message(message.from_user.id, 'Посмотреть выбор редакции ты можешь по ' + '[ссылке](https://music.yandex.ru/non-music/editorial/album/podcast_editorial_main)', parse_mode='Markdown')
    elif message.text == 'Книга + кино':
        bot.send_message(message.from_user.id, 'Не каждый фильм может ппохвастаться детальным повествованием книги. Можешь послушать подкасты по книгам по ' + '[ссылке](https://music.yandex.ru/non-music/editorial/album/audiobooks_films2022)', parse_mode='Markdown')
    elif message.text == 'приободряшка':
        bot.send_message(message.from_user.id, 'Отвлекись от серьезных дел, дай мозгу передохнуть вместе с ' + '[stand up](https://music.yandex.ru/album/13779940/track/80638271)', parse_mode='Markdown')
    else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()