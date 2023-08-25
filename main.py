from players import Player
from utils import load_random_word

print('Введите имя игрока')
name_user = input()
player = Player(name_user)
print(f'Привет, {name_user}!')
word = load_random_word()

print(f'Составьте {word.count_subwords()} слов из слова {word.word.upper()}')
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Поехали, ваше первое слово?')

guessed_words = 0

while guessed_words != word.count_subwords():
    word_user = input().lower()

    if word_user == 'stop' or word_user == 'стоп':
        break
    if len(word_user) < 3:
        print('слишком короткое слово')
        continue
    if not word.check_subwords(word_user):
        print('неверно')
        continue
    if player.word_usage_check(word_user):
        print('уже использовано')
        continue

    player.plus_used_words(word_user)
    print('Верно')
    guessed_words += 1

print(f'Игра завершена, вы угадали {player.count_words_user()} слов!')
