# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 10. Метод бутерброда')

# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |


phrase = input('Введите слово для шифрования: ')
# phrase = 'sandwich'
counter = 0  # Счетчик колличесвта букв
letter_counter = 0
First_part = ''
Second_part = ''

# Счетчик букв
for i in phrase:
  counter += 1

# Первая часть слова
for letter in phrase:
  letter_counter += 1
  if counter % 2 == 1:
    halfCounter = int((counter + 1) / 2)
  else:
    halfCounter = int(counter / 2)
  if letter_counter <= halfCounter:
    First_part += letter

# Проверка четности количесвта букв в слове
max = letter_counter
if letter_counter % 2 == 1:
  letter_counter += 2 
else:
  max = letter_counter

# Вторая часть слова
while True:
  if max <= letter_counter / 2:
    break
  letter_counter2 = 0
  for letter2 in phrase:
    letter_counter2 += 1
    if letter_counter2 == max:
      Second_part += letter2
      max -= 1

letter_counter = 0 # обнуление переменной

# Проверка
#print ('Новая фраза 1 = ', First_part)
#print ('Новая фраза 2 = ', Second_part)
#print('\n' + '=' * 20, '\n')

print('\n')

# Cмешивание двух частей
print('Введеное слово:          ', phrase)
print('Зашифрованное слово:      ', end = '')

for number in range(counter):
  if number % 2 == 0:
    letter_count = -2
    for letter1 in First_part:
      letter_count += 2
      if letter_count == number:
        print(letter1, end = '')
        break
  elif number % 2 == 1:
    letter_count = -1
    for letter2 in Second_part:
      letter_count += 2
      if letter_count == number:
        print(letter2, end = '')
        break
