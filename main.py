
phrase = 'sandwich'
#phrase = 'abecofi'
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
  if counter % 2 == 1:
    halfCounter = int((counter + 1) / 2)
  else:
    halfCounter = int(counter / 2)
  if letter_counter <= halfCounter:
    First_part += letter
print(First_part) # help

print ('letter_counter = ', letter_counter)

max = letter_counter
# letter_counter2 = 0


while True:
  if max <= 0:
    break
  print('test') # help
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

