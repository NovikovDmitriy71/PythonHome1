#__________________________________________________
# Монеты на столе (орел, решка) Необходимо определить минимальное
# количество монет которое требуется перевернуть, чтоб все моненты 
# лежали одной стороной (орлом или решкой)
# ______________________________________________________

# n=int(input('n =  ')) # Количество монет
# eagle_coin = tails_coin = 0 # (eagle - орел, tails - решка)
# for i in range(n):
#     x=int(input()) # Ввод: орел - 1, решка - 0
#     if x==1:
#         eagle_coin +=1
#     else:
#         tails_coin +=1
# if eagle_coin < tails_coin:
#     print(f'требуется перевернуть {eagle_coin} монет с орлом, их меньше')
# elif eagle_coin > tails_coin:
#     print(f'требуется перевернуть {tails_coin} монет с решкой, их меньше')
# else:
#     print('количество монет с орлом и решкой одинаково')

# ___________________________________________________

#Загадали два натуральных числа, необходимо найти числа если известна 
#сумма и произведение этих чисел

# a = int(input( 'Введите сумму 2х чисел  '))
# b = int(input('Введите произведение 2х чисел '))
# # D=int(((-a)**2 - 4*b)**0.5) дискриминант, проверка
# # print(D)
# y=int((a-((-a)**2 - 4*b)**0.5)/2)
# x=a-y
# print(f'Загаданные числа {x} и {y}   ')
#__________________________________________________

# Требуется вывести все целые степени двойки (т.е числа в виде 2К),
# не превосходящие  числа N

n=int(input('Введите число  '))
i=0
for i in range(n):
    if 2**i<n :  
        print(2**i)