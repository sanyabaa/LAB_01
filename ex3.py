"""Напишіть програму для друку літери Л висотою 5 рядків
 за допомогою введеного користувачем символу.

 ||| курс, Бритвич Олександр Володимирович (ПІБ)"""

a = input('Натисни * та ENTER ')

b = """       ^_----^
      //     |
     //      |
    //       |
   //        |"""
# Перевіряється, чи користувач ввів символ '*'
if a == '*':

    # Якщо умова виконується, виводяться рядки для виводу літери Л в 5 рядків
    print(b)

# Якщо умова не виконується, виводиться повідомлення про введення неправильного символу
else:
    print('Введіть * !!!')
