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



phrase = 'abecof'
counter = 0
new_phrase = ''
letter_counter = 0
nCounter = 0
a = 0
num = 1000
First_part = ''
Second_part = ''

for i in phrase:
  counter += 1

print ('Counter = ', counter)

for letter in phrase:
  letter_counter += 1
  if letter_counter % 2 == 1:
    First_part += letter
# print(new_phrase, end = '')


max = letter_counter
# letter_counter2 = 0


while True:
  if max <= 0:
    break
  print('test')
  letter_counter2 = 0
  for letter2 in phrase:
    letter_counter2 += 1
    if max % 2 == 1:
      max -= 1
    if letter_counter2 == max:
      Second_part += letter2
      max -= 2
      print(Second_part)

print('\n' * 2)

letter_counter = 0
last1 = 0
last2 = 0
# letter1_count = -2

for number in range(counter):
  if number % 2 == 0:
    letter_count = -2
    for letter1 in First_part:
      letter_count += 2
      if letter_count == number:
        print(letter1, end = '')
        last1 += 1
        break
  elif number % 2 == 1:
    letter_count = -1
    for letter2 in Second_part:
      letter_count += 2
      if letter_count == number:
        print(letter2, end = '')
        last2 += 1
        break

print('\n' * 2)


print ('Новая фраза = ', First_part)
print ('Новая фраза = ', Second_part)

print('\n' + '=' * 20, '\n')

