#count = 0
#word = "Hello World!"
#for i in word:
#  if i=="w":
#    count +=1
#print (count)

#isHasCar = True
#while isHasCar:
#  if input("Enter data: ") == "Stop":
#    isHasCar=False
#    print ("End of cycle")
#  else:
#    print("cycle go on")

#for i in range(1,11):
#    if i==5:
#      break
#    if i%2==00:
#      continue
#    print(i)  

#found = None
#for i in "hello":
#  if i=="l":
#    found = True
#    break
#  else:
#    found = False
#print(found)

#LIST
#nums = [5, 7, 2, 4, 7, True, "Hello", 6.7, [5, 7]]
#nums[0] = 50
#nums[5]=777
#print(nums[-1][1]) #[-1]обратный индекс, обращение к последнему элементу списка

#numbers = [5, 2, 7]
#numbers.append(100) #добавляет новый элемент в конец списка
#print(numbers)
#numbers.insert(1, True) #вставляет элемент на заданное место в списке, остальные элементы смещаются
#print(numbers)
#numbers.extend([9, 9, 9]) #вставляет новый список в конец существующего
#print(numbers)
#b = [0, 0, 0]
#numbers.extend(b)
#print(numbers)
#numbers.sort()
#print (numbers)
#numbers.reverse() # реверсирует элементы в списке
#print(numbers)
#numbers.pop (-7) #удаляет последний элемент, если значение не задано, если передать значение, то удалить элемент по индексу, при этом можно использовать отрицат индексы
#print(numbers)
#numbers.remove(True)
#numbers.clear () #удаляет элементы списка
#print(numbers)
#print(numbers.count(2)) #считает количество элементов что совпадают со значением, что передано в метод
#print(len(numbers)) #выводит длину списка

#nums = [5, 2, 7, "50", False ]
#i=0
#for el in nums:
# el*=2
# print (el)
# nums[i]=el
# i+=1
#print(nums)

#n=int(input("Enter length: "))
#user_list=[]
#i=0
#while i < n:
#  string = "Enter element #" + str(i+1) + ": "
#  user_list.append(input(string))
#  i+=1 
#print (user_list)

#STRING
#word = 'fooTThball, wollEYball, tEnnis'
#print(word)
#print (len(word))
#print(word.count('r'))
#print(word.upper())
#print(word.isupper())
#print(word.islower())
#print(word.capitalize())
#print(word.find('y')) #ищет символ и возвращает его индекс
#print(word.split(',')) #разбивает строку на список из элементов по отределенному символу
#переводит строку в список, потом привод каждый элемент списка к правилу каждый элемент с большой буквы, остальные маленькие, затем объединяет список в строку с разделениями ,
#hobby=word.split(', ')
#for i in range(len(hobby)):
#  hobby[i]=hobby[i].capitalize()
#print(hobby)
#result =', '.join(hobby)
#print(result)
#-------------------- end

#lis = [6, 4, "Stroka", True, 6.5]
#print(lis[2:])
#print (lis[::2])

# КОРТЕЖИ tuple
#data = (4, 6, 7, 3, 6, True, 5.6, 'HELLO')
# data [0]=5 !!!not right
#print(data [1:6])
#print(data.count(60))
#print(len(data))
#for el in data:
#  print(el)
#nums = [5, 7, 8]
#print(nums)
#new_data = tuple(nums) # список в кортеж
#print(new_data)
#word = 'Hello world'
#print(word)
#new_word=tuple(word) # word = tuple 'Hello world'
#print(new_word)
#-----------------------------------

#DICTIONARY
#country = {'code': 'UA', 'name': 'Ukraine', 'population': 44}
#country = dict (code='UA', name = 'Ukraine')
#print(country['name'])
#print (f"DICTIONARY{country}")
#print(country.items())
#for key, value in country.items():
#  print(key, " - ", value)
#print(country['code'])
#print(country.get('name'))
#country.clear() #очищает весь словарь
#country.pop('population') #удаляет определенный элемент по ключу
#country.popitem() #удаляет последний элемент
#print(country.keys())
#print(country.values())
#print (country)
#print (country.items())
#country['population'] = 30
#print(country.items())

#person = {
#  'user_1':{
#    'first_name': 'John',
#    'last_name': 'Marley',
#    'age': 45,
#    'address':('Kuev', 'street 1', '21'),
#    'grades': {'math':5, 'physics':3}
#  },
#  'user_2':{
#    'first_name': 'Volodimir'
#  } 
#}
#print (person['user_1']['address'][1])

# МНОЖЕСТВА = список без повторяющехся элементов
# data = set ("hello")
# print (data)
# data = {5, 7, 4, 3, 5}
# #data[0]=43 #!!!!НЕЛЬЗЯ
# data.add (32)
# data.update (["32", True, 4, 6])
# data.remove(True)
# data.pop()
# data.clear()
# print (data)
# nums = [5, 7, 3, 5, 5]
# nums = set (nums)
# print (nums)
# # Frousen set (mix set and tuple)
# new_data = frozenset([5, 7, 4, "32", True, 4, 6, 5, 7, 4, 3, 5])
# print(new_data)

#FUNCTION
# def test_func(): 
#   pass # nothing 
#   print ("HELLO", end="")
#   print ("!")
   
# test_func()

# def test_func(word): 
#   pass # nothing 
#   print (word, end="")
#   print ("!")
   
# test_func("Hi")
# test_func (5)

# def summa(a,b):
#   res = a+b
#   return (res)

# # summa (5, 7)
# print (summa ("Hi-", "hi"))

# res = summa (5.7, 7.5)
# print (res)

#FILE 
# w пишит в файл ( перезаписывает)  и если файла не сущ, то создает его, a добавляет новую инфо ( в дополнение к старой), r read если файла не сущ, то выдает ошибку
# запись данных
# data = input ("Enter text ")
# file = open ('text.txt', 'a')
# file.write("Hello!!!\n")
# file.write(data+"\n")
# file.close()

#считывание данных
#file = open('text.txt', 'r')
#print(file.read(1)) # read and print 1 symbol
#print(file.read()) # read and print all text in file
# for line in file:
#   print(line) # read string
# file.close()

#EXCEPT
# i = True
# while i:
#   try:
#     x = int(input ("Enter a number "))
#     x +=5
#     print(x)
#     i = False
#   except ValueError:
#     print ("Enter better a number")

# try:
#   x=5/1
#   x = int (input(">>> "))
# except ZeroDivisionError:
#   print ("ZeroDivisionError")
# except ValueError:
#   print ("You enter samth wrong")
# else:
#   print ("else")
# finally:
#   print("Finally")

# # WITH... as открывает и потом сразу закрывает файл, то есть file.close() не нужен
# try:
#   with open ('text.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
# except FileNotFoundError:
#   print ("File not found")


# create list and find min
# nums1 = [5, 7, 9, 2, 4]
# min = nums1[0]
# for el in nums1:
#   if el < min:
#     min = el
# print (min)

# nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
# min2 = nums2[0]
# for el in nums2:
#   if el < min2:
#     min2 = el
# print (min2)

# variant with Function
# def minimal (l):
#   min_num = l[0]
#   for el in l:
#     if el < min_num:
#       min_num = el
#   return min_num

# nums1 = [5, 7, 9, 2, 4]
# min1=minimal (nums1)
# nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
# min2= minimal (nums2)
# print (min1, min2)

#LAMBDA
# fun = lambda x, y:x*y
# print(fun (5, 2))


#-----------------------------------------------------

#  1 - Найти площадь и периметр прямоугольного треугольника
#import math
#a=input ("Enter katet 1 :")
#b= input ("Enter katet 2 :")
#s=float(a)*float (b)/2
#print (f"area of a right triangle = {s} sm")
#p=math.sqrt(float(a)*float(a)+float(b)*float(b))+float(a)+float(b)
#print (f"perimetr of a right triangle = {p} sm")

# 2 Обмен значений переменных
#a=input ("enter the value of variable 1: ")
#b = input("enter the value of variable 2: ")
#c = a
#a = b
#b = c
#print(f"Exchange of variable values: a = {a}, b = {b}")
#variant 2
#a=input ("enter the value of variable 1: ")
#b = input("enter the value of variable 2: ")
#c = input("enter the value of variable 3: ")
#a, b, c = c, b, a
#print(f"Exchange of variable values: a = {a}, b = {b}, c = {c}")

# 3 Сумма цифр трехзначного числа
#abc = int(input ("enter a three-digit number: "))
#c = abc%10
#abc=abc//10
#b = abc%10
#a = abc//10
#print(a + b + c)
# variant 2
#abc = int(input ("enter a three-digit number: "))
#c = abc%10
#b = abc%100//10
#a = abc//100
#print(a + b + c)
#variant 3
#abc = input ("enter a three-digit number: ")
#a = int (abc[0])
#b = int (abc[1])
#c = int (abc[2])
#print(a + b + c)

# 4 Найти корни квадратного уравнения
#import math
#a = float(input("Enter a(not egual 0): "))
#if a==0:
#  print ("ERROR a = 0 !!!!")
#else:
#  b = float(input("Enter b: "))
#  c = float(input("Enter c: "))
#  d=b**2 - 4*a*c 
#  if d<0:
#    print ("корней нет")
#  elif d==0:
#    x = (-b)/(2*a)
#    print (f"есть один корень x = {x}")
#  else:
#    x1 = (-b+math.sqrt(d))/(2*a)
#    x2 = (-b-math.sqrt(d))/(2*a)
#    print (f"есть два различных корня x1 = {x1} u x2 = {x2}")
  
  # Найти площадь прямоугольника, треугольника или круга
#import math
#v = float(input ("Площадь какой фигуры вы хотите найти? Введите 1 если прямоугольника, 2 если треугольника, 3 если круга: "))
#if v==1:
# a=float(input("введите сторону а: "))
# b=float(input("введите сторону b: "))
# s=a*b
# if s > 0:
#  print ("Площадь прямоугольника =  %.2f"%s)
# else:
#  print ("Такого прямоугольника не существует")
#elif v==2:
# a=float(input("введите сторону а: "))
# b=float(input("введите сторону b: "))
# c=float(input("введите сторону c: "))
# s=math.sqrt(((a+b+c)/2)*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))
# if s>0:
#  print ("Площадь треугольника =  %.2f"%s)
# else:
#  print ("Такого треугольника не существует") 
#elif v==3:
# r=float(input("введите радиус круга: "))
# s=math.pi*r**2
# if s>0:
#  print ("Площадь круга =  %.2f"%s)
# else:
#  print ("Такого круга не существует") 
#else:
# print ("введено неверное значение")


#Определить существование треугольника по трем сторонам
#print ("Для определения существования треугольника введите его стороны: ")
#a=float(input("сторона а: "))
#b=float(input("сторона b: "))
#c=float(input("сторона c: "))
#if a<b+c and b<a+c and c<a+b:
#  print ("Треуголник с заданными сторонами существует %c"%9655)
#else:
#  print("Треуголник с заданными сторонами НЕ существует %c"%9760)


# variant 2
#print ("Для определения существования треугольника введите его стороны: ")
#a=float(input("сторона а: "))
#b=float(input("сторона b: "))
#c=float(input("сторона c: "))
#if a>=(b+c):
#  print ("Треуголник с заданными сторонами НЕ существует %c"%9760, ": сторона \"а\" больше или равна сумме двух других")
#elif b>=(a+c):  
#  print ("Треуголник с заданными сторонами НЕ существует %c"%9760, ": сторона \"b\" больше или равна сумме двух других")
#elif c>=(a+b):
#  print ("Треуголник с заданными сторонами НЕ существует %c"%9760, ": сторона \"c\" больше или равна сумме двух других")
#else:
#  print ("Треугольник с заданными сторонами существует %c"%9655)


#Принадлежит ли точка кругу?  
#import math
#x=float(input("Чтобы определить принадлежит ли точка с координатами кругу радиуса R с центром в начале координат, введите значение координаты точки по оси Х: "))
#y = float(input("введите значение координаты точки по оси Y: "))
#r = float(input("введите радиус круга: ")) 
#if (x**2+y**2)<=r**2:
#  print ("YES")
#else:
#  print("NO") 

# Перевернуть число
#num=int(input("enter an integer: "))
#mun=0
#while num>0:
#  d = num%10
#  num=num//10
#  mun=mun*10
#  mun=mun+d
#print ("inverted number = ", mun)

# Перевернуть список
#str = input("введите строку для реверсии: ")
#str_list = list(str)
#str_list.reverse()   
#str2="".join(str_list)
#print ("перевернутое значение :", str2)

#variant2
#str=input("введите строку для реверсии: ")
#str1 = str[::-1]
#print (str1)

#variant3
#from random import randint
#n1 = randint(5000, 1000000) 
#print("Исходное число:", n1)
#n1 = str(n1)
#n2 = n1[::-1]
#n2 = int(n2)
#print('"Обратное" ему число:', n2)

#Возведение чисел в степень до заданного предела
#p=int(input("Введите степень числа: "))
#n = int(input("Введите число, которое нельзя превосходить: "))
#i=1
#while i**p <= n:
#  print (i**p, end=' ')
#  i+=1
#print ("Последнее число, возведенное в степень: ", i-1)

#Сумма и произведение цифр числа
#n = abs(int(input("Enter the number: "))) 
#sum = 0
#mult = 1
#if n==0:
#  mult=0
#else:
#  while n>0:
#   if (n%10)!=0:       #доп условие: если в числе встречается цифра 0, то мы ее не учитываем при сумме и умножении; (n%10)!=0 можно заменить на n%10, так как если это равно нулу, то это ложь
#     sum = sum + n%10
#     mult=mult*(n%10)
#   n=n//10
#print("Sum of digits of a given number = ", sum, "; Product of the digits of a given number =", mult)  


#Посчитать четные и нечетные цифры числа
#n = int(input("Enter the number: "))
#even = 0
#odd = 0
#while n>0:
#  if n%2==0:
#    even+=1
#    n=n//10
#  else:
#    odd+=1
#    n=n//10
#print ("even =", even, " odd = ", odd)

# variant 2
#a=input("Enter the number: ")
#even=0
#odd=0
#for i in a:
#  i= int(i)
#  if i%2==0:
#    even+=1
#  else:
#    odd+=1
#print ("even =", even, " odd = ", odd)

#variant 3
#a = input("Enter the number: ")
#d="02468"
#even=0
#odd=0
#for i in a:
#  if i in d:
#    even+=1
#  else:
#    odd+=1
#print ("even =", even, " odd = ", odd)

#Программа "Простейший калькулятор"
#print("0 в качестве знака операции завершит работу программы\n")
#while True:
#  c = input("Enter computational operation (+, -, *, /) ")
#  if c=="0":
#    print ("End")
#    break
#  if c in "+-/*":
#    a = float(input("Enter the number 1: "))
#    b = float(input("Enter the number 2: "))
#    if c == "+": 
#     print ("Result: ", a+b)
#    if c=="-":
#     print ("Result: ", a-b)
#    if c=="*":
#     print ("Result: ", a*b)
#    if c=="/":
#     if b!=0:
#       print ("Result: ", a/b)
#     else:
#       print ("Division by zero!")
#  else:
#    print ("Invalid operation sign!")

#Вычисление факториала
#n = input("Enter the number: ")
#factorial = 1
#if n.isdigit():
#  n1 = int(n)
#  while n1 > 0:
#   factorial=factorial*n1
#   n1=n1-1
#  print (f"Factorial of a number {n} = {factorial}")
#else:
#  print ("input error, you entered the wrong number")

#variant 3
#n = input("Enter the number: ")
#factorial = 1
#if n.isdigit():
#  for i in range (2, int(n)+1):
#    factorial=factorial*i
#  print (f"Factorial of a number {n} = {factorial}")
#else:
#  print ("input error, you entered the wrong number")

#Числа Фибоначчи: циклом и рекурсией
#n = input ("Enter the serial number of the Fibonacci number: ")
#fib1=1
#fib2=1
#fib_str=[fib1, fib2]
#i=3
#if n.isdigit ():
#  if int(n) ==1:
#    fib=fib1
#  elif int(n)==2:
#    fib=fib1
#  else:
#    while i<=int(n):
#     fib=fib1+fib2
#     fib1=fib2
#     fib2=fib
#     i+=1
#     fib_str.append(fib)
#  print(f"Number of the Fibonacci digit {n}: {fib}")
#  print(f"Fibonacci sequence up to digit {n}: {fib_str}")
#else: 
#  print("input error, you entered the wrong number")


  #variant 2

#n = input ("Enter the serial number of the Fibonacci number: ")
#fib1=1
#fib2=1
#fib_str=[fib1, fib2]
#i=0
#if n.isdigit ():
#  while i<(int(n)-2):
#   fib=fib1+fib2
#   fib1=fib2
#   fib2=fib
#   i+=1
#   fib_str.append(fib)
#  print(f"Number of the Fibonacci digit {n}: {fib2}")
#  print(f"Fibonacci sequence up to digit {n}: {fib_str}")
#else: 
#  print("input error, you entered the wrong number")

#variant 3 с помощью цикла for
#n = int(input ("Enter the serial number of the Fibonacci number: "))
#fib1=fib2=1
#print ("Fibonacci sequence ", fib1, fib2, end=' ')
#for i in range (2, n):
#  fib=fib1+fib2
#  fib1=fib2
#  fib2=fib
#  print (fib2, end=' ')
#print(f"\nNumber of the Fibonacci digit {n}: {fib2}")

# variant 4 рекурсия
# def fibonacci(n):
#   if n==0:
#     return 0
#   if n in (1, 2):
#     return 1
#   return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(6))

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# Винятки у Python
# val = input ("Enter number: ")
# try:
#   val=int(val)
# except ValueError:
#   print ("This is not a number")
# else: 
#   print (val>0)
# finally:
#   print ("This will be printed anyway")

# age = input("How old are you? ")
# try:
#   age = int(age)
#   if age >= 18:
#     print(">=18")
#   else:
#     print ("Kinder")
# except ValueError:
#   print ("This is not a number") 
# finally:
#   print("This is the end")

# is_active = bool(input("Is the user active? "))
# is_admin = bool(input("Is the user administrator? "))
# is_permission = bool(input("Does the user have access? "))
# print (is_active, is_admin, is_permission)
# print (type(is_active), type (is_admin), type (is_permission) )
# access = is_admin or (is_permission and is_active)
# print (access)

# У Python також існує короткий варіант тернарного оператора.
# some_data = None
# message = some_data or "Not data"
# print(message)

# ЗАВДАННЯ: НАЙБІЛЬШИЙ СПІЛЬНИЙ ДІЛЬНИК
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = first if first <= second else second
# while first%gcd != 0 or second%gcd != 0:
#     gcd = gcd-1
# print (gcd)


# num = int(input("Enter integer (0 for output): "))
# sum = 0
# for i in range (0, num + 1):
#   sum = sum + i
# while num !=0:
#   num = int (input("Enter integer (0 for output): "))
#   for i in range (0, num + 1):
#     sum = sum + i
# print (sum)    

              # #  message = input("Enter a message: ")
              # #  offset = int(input("Enter the offset: "))
              # #  encoded_message = ""
              # #  for ch in message:
    
#ЗАВДАННЯ: КОД ЦЕЗАРЯ
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# encoded_list = list()
# for ch in message:
#     if ch.isalpha() and ch.islower():
#         pos = ord(ch) - ord('a')  
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a")) 
#         encoded_list.append(new_char)
#     elif ch.isalpha() and ch.isupper():
#         pos = ord(ch) - ord('A')  
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A")) 
#         encoded_list.append(new_char)
#     else:
#         encoded_list.append(ch)  
# encoded_message = ''.join(encoded_list)
# print(encoded_message)

#Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, приймаючи від користувача операнди (числа) та оператор.

# result = None
# operand = None
# operator = None
# prew_num = None
# wait_for_number = True

# while True:
#   v = input(">>> ")
#   if v == "=":
#     print (result)
#     break
#   elif wait_for_number == True: 
#          try:
#              operand = int(v)
#          except ValueError:
#              print (f"{v} is not a number. Try again")
#          else:
#             print("Sie haben eine Zahl eingegeben")
#             wait_for_number = False
#             if result != None:
#                 if operator == "+":
#                     result = result+operand
#                 elif operator == "-":
#                     result = result-operand
#                 elif operator == "*":
#                     result = result*operand
#                 elif operator == "/":
#                     result = result/operand    
#             elif result == None:
#                 result = operand
                       
#   elif wait_for_number == False:
#         if v in "+-/*": 
#           wait_for_number = True
#           print("Sie haben eine Aktion eingegeben")
#           operator = v
#         else:
#           print (f"{v} is not a math operator")
           
# Перевод из десятичной системы счисления в двоичную
# bin_str=""
# while True:
#    decimal_num = input("Enter decimal number: >>>  ")
#    try:
#       decimal_num = int(decimal_num)
#    except ValueError:
#       print(f"!!!{decimal_num} is not a number. Try again") 
#    else:
#       while decimal_num >0:
#         bin_str = str (decimal_num%2) + bin_str
#         decimal_num = decimal_num//2
#       print (bin_str)
#       break
      
# # variant 2 with list
# bin_list = []
# while True:
#   decimal_num = input("Enter decimal number: >>>  ")
#   try:
#       decimal_num = int(decimal_num)
#   except ValueError:
#       print (f"!!!{decimal_num} is not a number. Try again") 
#   else: 
#      while decimal_num > 0:
#          bin_list.append(decimal_num%2)
#          decimal_num = decimal_num//2
         
#      bin_list.reverse()
#      for i in bin_list:
#         print (i, end="")
#      break

# number = int(input (">>> "))
# for i in range (number):
#   if i%2==1:
#     print (i, "Number is odd")
#   else:
#     print (i, "Number is NOT odd") 

# name = input ("Enter name: ")
# res=""
# for char in range (len(name)):
#   if char%2==1:
#     res=res+name[char].upper()
#   #  continue
#   # else:
#   res=res+name[char]
# print (res)
    
# def total(a=5, *numbers, **phone_book):
#     print('a', a)
#     # прохід по всіх елементах кортежу
#     for single_item in numbers:
#         print('single_item', single_item)

#     #прохід по всіх елементах словника
#     for first_part, second_part in phone_book.items():
#         print(first_part,second_part)

# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         nonlocal discount
#         price = price - price*discount
#     print (price) # цена до вызова функции apply_discount()
#     apply_discount()
#     print (price) # цена после вызова функции apply_discount()
#     return price 
        
# print ("Price with discount: ", discount_price(100, 0.1))

# def get_fullname (first_name, last_name, middle_name=""):
#   if middle_name=="":
#     return first_name + " " +last_name
#   else:
#     return first_name + " " + middle_name + " " + last_name
#print (get_fullname("Oksana", "Pavlenko", "Oleksandrivna"))    

# def format_string(string, length):
#   d = (int (length) - len(string))//2
#   if len(string) >= int (length):
#     return string
#   else: 
#     return " "*d + string
  
# print(format_string(length=15, string='abaa'))
# def first(size, *arg):
#     return int(size)+len(arg) 

# print (first(5, "first", "second", "third"))
# print (first(1, "Alex", "Boris"))

# def second(size, **kl_arg):
#      return int(size)+len(kl_arg) 

# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))

# def cost_delivery(quantity, *product, discount=0):
#     if int(quantity) == 1:
#         return 5 - 5*discount
#     elif int(quantity) >= 2:
#         return 5 + 2*(int(quantity)-1)- (5 + 2*(int(quantity)-1))*discount

# print (cost_delivery(5, discount=0.5))

#рядки документації
# def fun(a, b=2, c=3):
#     """Знаходить суму трьох параметрів.

#      Перший параметр обов'язковий, два інших за замовчанням дорівнюють 2 і 3"""
#     return a + b * c

# print(fun.__doc__)

# Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень C= n! / ((n - k)! · k!) де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

# def factorial(n):
#   if n < 2:
#     return 1
#   else:
#     return n*factorial(n-1)

# def number_of_groups(n, k):
#   return int(factorial(n)/(factorial(n - k)* factorial(k)))

#Алгоритм Евклида - нахождение наибольшего общего делителя
# aa = input ("Enter a first number: ")
# bb = input ("Enter a second number: ")
# nod= None
# try:
#   a = int(aa)
#   b = int (bb)
# except ValueError:
#   print ("a or/and b are not a number. Try again")
# else:
#   while True:
#    if a>=b:
#     if a%b==0:
#       nod = b
#       break
#     else:
#       a = a%b
#    else:
#     if b%a==0:
#       nod=a
#       break
#     else:
#       b = b%a
# print (f"greatest common divisor {aa} and {bb} = ", nod)

# variant 2
# a = int(input ("Enter a first number: "))
# b = int(input ("Enter a second number: "))
# while a!=0 and b !=0:
#   if a>b:
#     a= a%b
#   else:
#     b=b%a
# print (f"greatest common divisor = ", a+b)

# variant 3 Алгоритм нахождения НОД вычитанием
# a = int(input ("Enter a first number: "))
# b = int(input ("Enter a second number: "))
# while a!=b:
#   if a>b:
#     a = a-b
#   else:
#     b=b-a

# print (f"greatest common divisor = ", a)

# # variant 4 Функция, вычисляющая НОД
# def nod (a, b):
#   while a!=b:
#    if a>b:
#      a = a-b
#    else:
#      b=b-a
#   return a   

# while True:
#   aa = input ("Enter a first number: ")
#   bb = input ("Enter a second number: ")
#   try:
#     aa=int(aa)
#     bb=int(bb)
#   except ValueError:
#     print ("a or/and b are not a number. Try again")
#   else:
#     print(f"greatest common divisor = ", nod(aa, bb))
#     break

# Проверка простоты числа перебором делителей
# from math import sqrt
# a = int(input ("Enter a number: "))
# prime = True
# for i in range(2, int(sqrt(a)+1)):
#   if a%i == 0:
#     prime = False
#     break
#   else:
#     i+=1
# if prime: 
#   print(f"number {a} is a prime number")
# else:
#   print(f"number {a} is a composite number")

#varian function   
# from math import sqrt
# def is_prime (n):
#   i=2
#   while i<=int(sqrt(n)):
#     if n%i ==0:
#       return False
#     i+=1
#   if n>1:
#     return True

# k = int(input(">>> "))
# print (is_prime (k))
               
#Проверить уникальность элементов списка
# data = [5, 7, 4, 3, 5]
# for i in range(0, 5):
#   for j in range (i+1, 5):
#     if data[i]==data[j]:
#       print("No unic")
#       quit()
# print (type(data))
# print ("unic")

#variant 2
# data = [5, 7, 4, 3, 6]
# setarr=set(data)
# if len(setarr)!=len (data):
#   print("No unic")
# else: 
#   print ("unic")

#variant 3
# data = [5, 7, 1, 3, 2]
# for item in data:
#   if data.count(item)>1:
#      print("No unic")
#      break
# else: # В программе выше ветка else цикла for срабатывает только в случае, если работа цикла не была прервана с помощью оператора break.
#     print("unic")

#variant 4 определить неуникальные элементы
# data = [5, 7, 1, 3, 2, 7, 7, 5, 8, 0]
# for item in data:
#   count = data.count(item)
#   if count>1:
#     print (f"element {item} meet {count} time")

#Чтобы исключить из перебора повторы значений, мы можем преобразовать список во множество. После этого перебирать в цикле элементы множества, которые уникальны.
# data = [5, 7, 1, 3, 2, 7, 7, 5, 8, 0]
# setdata=set(data)
# for item in setdata:
#   count = data.count(item)
#   if count>1:
#     print (f"element {item} meet {count} time")

#Удаление элементов списка по условию
# data = [96, 72, 44, 22, 35, 29, 97, 69, 25, 12]
# del_data = []
# i=0
# while i < len (data):
#     if 20 < data[i] < 90:
#         del_data.append(data[i])
#         del data[i]
#     else:
#         i+=1
 
# print("data =", data)
# print("del_data =", del_data)

#Пересечение списков, совпадающие элементы двух списков
# l1 = [0, 3, 8, True, [1, 2], 'a']
# l2 = ['b', [1, 2], 8, True, 2, 5, 122, 'a']
# l3=[]
# for it1 in l1:
#   for it2 in l2:
#     if it1==it2:
#       l3.append(it1)
#       break
# print (l3)

#variant 2
# l1 = [0, 3, 8, 3, 3, True, [1, 2], 'a', 3]
# l2 = ['b', [1, 2], 8, 3, True, 2, 3, 5, 3, 122, 'a']
# l3=[]
# for it1 in l1:
#   if it1 in l2 and it1 not in l3:
#       l3.append(it1)
# print (l3)

# variant 3 Пусть если в обоих списках есть по несколько одинаковых значений, они должны попадать в список совпадающих элементов в том количестве, в котором встречаются в списке, где их меньше. 
# l1 = [5, 2, 4, 'r', 4, 'ee', 1, 1,  4]
# l2 = [4, 1, 'we', 'ee', 'r', 4, 1, 1]
# l3=[]
# for it1 in l1:
#   if it1 not in l3:
#      t = l1.count(it1) if l1.count(it1) < l2.count(it1) else l2.count(it1)
#      #l3 += [it1] * t так тоже можно добавить элемент it1 в список t раз
#      for i in range(t):
#        l3.append(it1)
# print (l3)

# variant - вариант с переводом списков во множества, не работает, если список содержит в кач-ве элемента другие списки 
# l1 = [0, 3, 8, True, 'a']
# l2 = ['b', 8, True, 2, 5, 122, 'a']
# print (list(set(l1) & set(l2)))

# #Двоичный, или бинарный, поиск элемента
# l1 = [5, 2, 4, 26, 35, 28, 11, 19, 34]
# l2 =[]
# #l1.sort() # функция по сортировке списка
# for i in range (len(l1)):
#   for j in range (i, len (l1)):
#     if l1[i]>l1[j]:
#       tr = l1[i]
#       l1[i] = l1[j]
#       l1[j] = tr
# print (l1)
# value = int(input (">>> "))
# low=0
# high = len(l1) - 1
# mid = len(l1)//2
# while l1[mid] != value and low <= high:
#   if value > l1[mid]:
#     low = mid + 1
#   else:
#     high = mid - 1
#   mid = (low + high)//2
# if low > high:
#   print ("No value")
# else:
#   print ("ID= ", mid)   

#Function
# def pr (n, str="Default value"): # definition визначення, все после def называется сигнатурой функции (название, параметры)
#   for _ in range(n):
#     print (str)

# pr(2) # call, callable
# #pr (n=2, str = "Hello world")
   
#функция считает кол во слов в тексте
# def count_words (text):
#   words = text.split ()
#   print(words)
#   return len(words)
#   # n=0
#   # for _ in text

# res= count_words ("hfhfj jdjdj djdjjf djdjf")
# print (res)

# def add(*args):
#   total=0
#   for i in args:
#     total+=i
#   print (type(args))
#   return total
# res=add (1,2,3,4)
# print ("sum is: ", res)

# def fib_recursive (n):
#   if n<=1:
#     return n
#   else:
#     return fib_recursive(n-1)+fib_recursive(n-2)

# def fib_iter(n):
#   if n==1:
#     return [1]
#   if n==2:
#     return [1,1]
#   fibs = [1, 1]
#   for _ in range (2, n):
#     fibs.append(fibs[-1]+fibs[-2])
#   return fibs

#print(fib_recursive(5))

# from pathlib import Path

# p = Path('C:/Users/kompik/Downloads')    # p Вказує на папку /home/user/Downloads
# for i in p.iterdir():
#      print(i.name)   # Виведе у циклі імена всіх папок та файлів у /home/user/Downloads

# print(p.exists())

#payment = [100, -1, 1200, 800, -100]

# def prepare_data(data):
#   min = data[0]
#   max = data[0]
#   for el in data:
#      if el < min:
#         min=el
#      if el>max:
#         max=el
#   data.remove(min)
#   data.remove(max)
#   return sorted(data)

# print(prepare_data([100, -1, 1200, 800, -100]))

# def format_ingredients(items):
#   st=""
#   if len (items) ==1:
#     return items[0]
#   elif len(items) ==0:
#     return "" 
#   else:
#     for i in range(len(items)-2):
#         st = st + items[i] + ", "
#     st = st + items[-2] + " and " +  items[-1]
#   return st

# print(format_ingredients(["2 eggs", "1 liter sugar"]))

# lang = {"Python": 1991, "Java": 1995}
# java = lang.get("Java", 1991)  # 1995
# js = lang.get("JS", "NO JS")  # 1995
# pascal = lang.get("Pascal")  # None

# print(java)
# print (js)
# print(pascal)

# person = {
#  'user_1':{
#    'first_name': 'John',
#    'last_name': 'Marley',
#    'age': 45,
#    'address':('Kuev', 'street 1', '21'),
#    'grades': {'math':5, 'physics':3}
#  },
#  'user_2':{
#    'first_name': 'Volodimir'
#  } 
# }
# #print (person['user_1']['address'][1])
# print(person['user_1']['last_name'])

# rating_system = {
#   'F':{
#     'Rating': 1,
#     'Explanation': 'Unsatisfactorily'
#   },
#   'FX':{
#     'Rating': 2,
#     'Explanation': 'Unsatisfactorily'
#   },
#   'E':{
#     'Rating': 3,
#     'Explanation': 'Enough'
#   },
#   'D':{
#     'Rating': 3,
#     'Explanation': 'Satisfactorily'
#   },
#   'C':{
#     'Rating': 4,
#     'Explanation': 'Good'
#   },
#   'B':{
#     'Rating': 5,
#     'Explanation': 'Very good'
#   },
#   'A':{
#     'Rating': 5,
#     'Explanation': 'Perfectly'
#   }
# }

# def get_grade(key):
#    if rating_system.get(key) != None:
#      return rating_system [key]['Rating']
#    else:
#     return 'None'

# def get_description(key):
#   if rating_system.get(key) != None:
#     return rating_system [key]['Explanation']
#   else:
#     return 'None'

# print(get_grade('AA'))
# print(get_description('AA'))

# def lookup_key(data, value):
#   key_list = []
#   for k, val in data.items():
#     if val == value:
#       key_list.append (k)
#   return key_list

# print(lookup_key({"Python": 1991, "Java": 1995, "JS": 1995}, 1990))    

# def split_list(grade):
#   less_average = list()
#   more_average = list()
#   sum=0
#   if grade == []:
#     return [], []
#   for el in grade:
#     sum = sum + el
#   sum = sum/(len(grade))
#   for el in grade:
#     if el <= sum:
#       less_average.append(el)
#     else:
#       more_average.append(el)
#   less_tuple = tuple(less_average)
#   more_tuple = tuple(more_average)
#   # print (type(less_average), type(more_average))
#   # print (type(less_tuple), type(more_tuple))
#   # print(less_average)
#   return less_average, more_average
  
# print (split_list([1, 12, 3, 24, 5]))

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }

# def calculate_distance(coordinates):
#   sum=0
#   for i in range(len(coordinates)-1):
#     if coordinates[i] > coordinates[i+1]:
#       kor = (coordinates[i+1], coordinates[i])
#       for key in points:
#         if key==kor:
#           sum = sum + points[kor]      
#     else:
#       kor = (coordinates[i], coordinates[i+1])
#       for key in points:
#         if key==kor:
#           sum = sum + points[kor]  

#   return sum    
 
# print(calculate_distance([0, 1, 3, 2, 0]))

# def game(terra, power):
#   for i in terra:
#     for j in i:
#       if j<=power:
#         power = power + j
#       else:
#         break
#   return power
#print (game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))

# def is_valid_pin_codes(pin_codes):
#   valid = True
#   num = '0123456789'
#   if pin_codes != []:
#      if len(pin_codes) == len(set(pin_codes)):
#        for i in pin_codes:
#          if (type(i)==str) and (len(i)==4):
#            for j in i:
#             if j not in num:
#              valid = False
#          else:
#            valid = False
#      else:
#        valid = False
#   else:
#     valid = False
#   return valid

# print(is_valid_pin_codes([]))

# from random import randint
# str_pass = ''
# print(len(str_pass))

# def get_random_password():
#   global str_pass
#   for i in range(8):
#     str_pass = str_pass + chr(randint(40, 126))
#   print(len(str_pass))  
#   return str_pass

# print (get_random_password())

#---------------------------
#Генерация надежного пароля
# from random import randint
# def get_random_password():
#   str_pas = ''
#   for _ in range(8):
#     random_num = randint(40, 126)
#     str_pas = str_pas + chr(random_num)
#   return str_pas
# r = get_random_password() 
# print(r)
# n = get_random_password()
# print(n)
# print (get_random_password())    
# print (get_random_password()) 
    
# def is_valid_password(password):
#   valid = False
#   capital_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   small_let = 'abcdefghijklmnopqrstuvwxyz'
#   numbers = '0123456789'
#   is_cap = False
#   is_small= False
#   is_number=False
#   for el in password:
#       if el in capital_let:
#         is_cap = True
#       elif el in small_let:
#         is_small = True
#       elif el in numbers:
#         is_number = True
#   if (len(password)==8) and is_cap and is_small and is_number:
#     valid = True
#   return valid

# def get_password():
#   p = ""
#   i=0
#   while i<= 0:
#     p = get_random_password()
#     i+=1
#     if is_valid_password(p):
#       return p

# print (get_password())  

#--------------------------------------------------------
# from pathlib import Path
# def parse_folder(path):
#     files = []
#     folders = []
#     p = Path(path)
#     for i in p.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         elif i.is_file():
#             files.append(i.name)      
#     return files, folders

# print(parse_folder('C:/Users/kompik/Downloads'))

# from pathlib import Path
# def parse_folder(path):
#     files = []
#     folders = []
#     for i in path.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         elif i.is_file():
#             files.append(i.name)      
#     return files, folders

# print(parse_folder(Path('C:/Users/kompik/Downloads')))

# функция, в которую предается другая функция в качестве аргумента
# def another_func():
#   print("Hello")

# def func(another_func):
#   another_func()
#   print ("world")

# print(type(another_func))
# print (func(another_func))

# def is_polindrom(text):
#   rev = text[::-1]
#   print(rev)
#   return rev ==text

# print(is_polindrom([1, 2, 2, 1, 12, 134]))

#считает элем списка, которые повторяются больше чем к раз
# a = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# k=3
# print ("original ist: ", a)
# res = list()
# for i in a:
#   freg = a.count(i)
#   if freg >= k and i not in res:
#     res.append(i)
  
# print(res)

# a = [1, [1, 2, [1, 2, 3, [1, 23]]]]
# print(a)
# print (a[1][2][3][1])

# circle{
#   (0, 0): "centr",
#   (1, 0): "360",
#   (0, 1): "90",
#   (-1,0): "180",
#   (0,-1): "270"
# }

# a = (0, 0)

# info = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New York"
# }
# info.update ({"street": "street N", "email": "kelly@gmail.com"})

# for i in info.values():
#   print(i)

# for i, j in info.items():
#   print(i, j)

# A = {"math": 92, "eng": 80, "fisik": 99, "social": 89}
# B = {"math": 77, "eng": 56, "fisik": 58, "social": 99}
# res = list()
# for key in A:
#   if A[key]>80:
#     print (f"Key : {key} = {A[key]}")
#     res.append(A[key]) 

# print ("res: ", res)
# A["English"] = A.pop("eng")    
# print(A)

# s1 = {"red", "green", "blue"}
# print (s1, type(s1))
# s2 = set (s1)
# print ("set ", type(s2), s2)
# s3 = str(s1)
# print ("str ", type(s3), s3)

# import sys
# print(sys.argv)

# for arg in sys.argv:
#   print ("arg: ", arg)

# from pathlib import Path
# p = Path('C:/Users/kompik/Downloads')
# print(p.parent)
# print(p.name)
# print(p.suffix)
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())

# def parse_folder(path):
#   for el in path.iterdir():
#     if el.is_dir():
#       print (f"This is folder: {el}")
#     else:
#       print(f"This is file; {el}")

# def parse_file(path):
#   for el in path.iterdir():
#     if el.is_dir():
#       print (f"This is folder: {el}")
#       parse_file(el)
#     else:
#       print(f"This is file; {el}") 

# parse_folder(p)
# parse_file (p)

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q"))  # -1
# print(s.index("er", start, end)) # 5
# (s.index("q"))  # -1

# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))

# s =  "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
# print(s)  # 'Bob' Dilan

#print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111
#print('pi: {:0.5}'.format(3.14159265358979323846))
#print('"{}" "{:+}" "{}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"
#print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|
# import re
# s = "I am 25 years old."
# age = re.search('\d+', s)
# print(age)
# print(type(age))
# print(age.group())  # 25
# print(type(age.group))

# def real_len(text):
#   res = ""
#   #ks =  ["\n", "\f", "\r", "\t", "\v"]
#   for i in range(len(text)-1):
#     if text[i]!='\''and (text[i+1]!="n" or text[i+1]!="f" or text[i+1]!="r" or text[i+1]!="t" or text[i+1]!="v"):
#         res = res + text[i]
#   res=res+text[-1]
#   print(res)
#   return len(res)

# print(real_len("Oksana\nPavlenko"))

# def real_len(text):
#   if text.find("\n")> -1:
#     text = text.replace("\n", "")
#   if text.find("\f")> -1:
#     text = text.replace("\f", "")    
#   if text.find("\r")> -1:
#     text = text.replace("\r", "") 
#   if text.find("\t")> -1:
#     text = text.replace("\t", "")   
#   if text.find("\v")> -1:
#     text = text.replace("\v", "") 
#   print(text)
#   return len(text)

# print(real_len('Al\nKdf\ne23\t\v.\r'))
# print('AlKdfe23.')    

# def real_len(text):
#   text = text.replace("\n", "")
#   text = text.replace("\f", "")    
#   text = text.replace("\r", "") 
#   text = text.replace("\t", "")   
#   text = text.replace("\v", "") 
#   print(text)
#   return len(text)

# print(real_len('Al\nKdf\ne23\t\v.\r'))
# print('AlKdfe23.')    

# message = "У темній кімнаті всі кішки чорні (мабуть)"
# square_brackets = message.replace("(", "[").replace(")", "]")
# clear_brackets = message.replace("(", "").replace(")", "")

# print(square_brackets)  # У темній кімнаті всі кішки чорні [мабуть]
# print(clear_brackets)  # У темній кімнаті всі кішки чорні мабуть

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

# def find_articles(key, letter_case=False):
#   res = list()
#   if letter_case:
#     print("letter_case=True")
#     for i in range(len(articles_dict)):
#       if (key in articles_dict[i]["title"]) or (key in articles_dict[i]["author"]):
#         res.append(articles_dict[i])
#   else:
#     print("letter_case=False")
#     key = key.lower()
#     for i in range(len(articles_dict)):
#       if (key in articles_dict[i]["title"].lower()) or (key in articles_dict[i]["author"].lower()):
#         res.append(articles_dict[i])
#     print(key)
#   return(res)
      
# print(find_articles ("ocean"))

# print(articles_dict[0]["title"])
# l.append(articles_dict[0])
# l.append(articles_dict[1])
# print(l)

# def sanitize_phone_number(phone):
#     san_phone=""
#     san_phone=phone.replace(")","")
#     san_phone=san_phone.replace("(","")
#     san_phone=san_phone.replace(" ","")
#     san_phone=san_phone.replace("-","")
#     san_phone=san_phone.replace("+","")
#     return san_phone 
# print(sanitize_phone_number("    +38(050)123-32-34"))
# variant другой с другой формой записи 
# def sanitize_phone_number(phone):
#     san_phone=(
#         phone.replace(")","")
#         .replace("(","")
#         .replace(" ","")
#         .replace("-","")
#         .replace("+","")
#     )
#     return san_phone 
# print(sanitize_phone_number("    +38(050)123-32-34"))


# def is_check_name(fullname, first_name):
#   pref = fullname.startswith(first_name)
#   return pref
# print(is_check_name ("OksanaPavlenko", "Oksana"))

# country_cod = {"JP":"+81", "SG":"+65", "TW":"+886", "UA":"+380"}

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
#    tel_cod ={"UA":[], "JP":[], "TW":[], "SG":[]}
#    #tel_list = list()
#    for tel in list_phones:
#        tel1 = sanitize_phone_number(tel)
#        #tel_list.append(tel1)
#        if tel1.startswith("380"):
#            tel_cod["UA"].append(tel1)
#        elif tel1.startswith("81"):
#            tel_cod["JP"].append(tel1)
#        elif tel1.startswith("886"):
#            tel_cod["TW"].append(tel1)
#        elif tel1.startswith("65"):
#            tel_cod["SG"].append(tel1)
#        else:
#            tel_cod["UA"].append(tel1)
      
#    return (tel_cod)

# print(get_phone_numbers_for_countries(["    +38(050)123-32-34", "+  88612458 (444)-1", "     0503451234", "    65(111) 23-22-15", "+ 81 121 14444 78885", "(050)8889900", "8102456","38050-111-22-22", "38050 111 22 11   "]))

#ЗАВДАННЯ: ВАЛІДАЦІЯ ПОВІДОМЛЕННЯ НА НАЯВНІСТЬ СПАМ СЛІВ
# def is_spam_words(text, spam_words, space_around=False):
#   r = True
#   if space_around:
#       for el_spam_words in spam_words:
#           n = text.lower().find(el_spam_words.lower()) 
#           if not (text.lower().startswith(el_spam_words.lower())) and text.lower()[n-1]!=" " and text.lower()[n+len(el_spam_words)-1]!=" " and text.lower()[n+len(el_spam_words)-1]!=".":
#               print("строка НЕ начинается со спама")
#               r = False
#           else:
#               print("строка начинается со спама")
#               r = True
#               break
  
    
#   else:
#       for el_spam_words in spam_words:
#           if el_spam_words.lower() not in text.lower():
#               r = False
#           else:
#               r = True
#   return r

# print(is_spam_words("Молох", ["лох"], True))

# str = "Hello, i have wondefull news - Putin is dead"
# sp = "Putin"
# res = sp in str
# print(res)

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# def translate(name):
#     for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#         TRANS[ord(c)] = l
#         TRANS[ord(c.upper())] = l.upper()    
#     return name.translate(TRANS)


# print(translate("Олекса Івасюк"))

   
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# def formatted_grades(students): 
#   i = 1
#   grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#   res = list()
#   for k, val in students.items():
#     res.append("")
#     res[i-1]=("{:>4}|{:<10}|{:^5}|{:^5}".format(i, (str(k)), str(students.get(k)), str(grades.get(students.get(k)))))
#     i = i + 1
#   return(res)


# for el in formatted_grades(students):
#     print(el)

# def formatted_numbers():
#     res = list()
#     res.append("")
#     res[0]=("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
#     for i in range(1, 17):
#         res.append("")
#         res[i]=("|{:<10d}|{:^10x}|{:>10b}|".format(i-1, i-1, i-1))
#     return(res)    

# for el in formatted_numbers():
#     print(el)

# import re


# def find_word(text, word):
#     dict_s = {
#         'result': '',
#         'first_index': '',
#         'last_index': '',
#         'search_string': '',
#         'string': ''
# }
#     res = re.search(word, text)
#     if res:
#        dict_s['result'] = True
#        dict_s['first_index'] = res.start()
#        dict_s['last_index'] = res.end()
#        dict_s['search_string'] = word
#        dict_s['string'] = text
#     else:
#        dict_s['result'] = False
#        dict_s['first_index'] = None
#        dict_s['last_index'] = None
#        dict_s['search_string'] = word
#        dict_s['string'] = text
#     return dict_s

# print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))

# import re

# def find_all_words(text, word):
#   numbers = re.findall(word, text, flags=re.IGNORECASE)
#   return numbers

# print(find_all_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as PYthon 0.9.0.", "Python"))

# import re
# def replace_spam_words(text, spam_words):
#   p=text
#   for sp in spam_words:
#     n = "*"*len(sp)
#     p = re.sub(sp, n, p, flags=re.IGNORECASE)
#   return(p) 

# print(replace_spam_words("Guido yyy van Rossum began cccc working on Python in the late 1980s, ddddd as a successor to the ABC programming language, and first released it in 1991 as PYthon 0.9.0.", ["yyy", "cccc", "DDDDD"]))

# cars =  [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]      

# def get_key(element):
#   return element['car']

# print(cars)
# cars.sort(key = get_key)
# cars.sort(key = get_key, reverse=True)
# print (f"sorted: {cars}")
# ============================

# comp = lambda element:element["car"]
# is_prime = lambda x: x%2==0
# is_sguare = lambda x: x**2

# print("lambda >>>>>>>>>", is_prime(3))
# print("lambda>>>>>>", is_sguare(2))



# a =[1,2,3,52,1,31,88]
# a.sort()
# print (a)

#--------------
# d={
#   "a" : 1,
#   "b" : 2,
#   "c" : 3,
#   "d" : 1,
#   "h" : 2,
#   "w" : 256
# }
# def lookup_key (data, value):
#   keys=list()
#   for key, number in data.items():
#     if number == value:
#       keys.append(key) 
#   return(keys)

# print(lookup_key(d, 1))

#------

# numbers = ["123", "456", "1000", "800", "dhdsj"]
# def sanitize(numbers):
#   res_numb = list()
#   for num in numbers:
#     if isinstance(num, str) and num.isdigit():
#       res_numb.append(num) 
#   return res_numb

# def trans_int(numbers):
#   res_num = list()
#   for num in numbers:
#     res_num.append(int(num))
#   return res_num  
# def avarage(numbers):
#   return sum(numbers) / len(numbers)


# san = sanitize(numbers)
# print(san)
# sani = trans_int(san)
# print(sani)
# res = avarage(sani)
# print(res)
# print(trans_int(sanitize(numbers)))
# print(sanitize(numbers))

# words = ["ad", "bd", "aaab", "baa", "badab"]
# allowed="ab"
# words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
# allowed="abc"
# def countCons(allowed, words):
#   count = 0
#   allowed = set(allowed)
#   res = list()
#   for el in words:
#     if set(el).issubset(allowed):
#       count+=1
#       res.append(el)
#   return count, res

# print(countCons(allowed, words))

# def factorial(n):
#   if n>=2:
#     return factorial(n-1)*n
#   else:
#     return 1
  
# print(factorial(3))

#buble sort
#---------
# l = [1, 42, 423, 5, 86, -6, 0, -12]
# def buble_sort(array):
#   for i in range(0, len(array)-1):
#      for j in range (0, len(array)-1-i):
#         if array[j]>array[j+1]:
#            array[j], array [j+1] = array[j+1], array[j]
#   return(array)

# print(buble_sort(l))

# =========================
# import re

# def find_all_emails(text):
#     result = re.findall(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'", text, flags=re.IGNORECASE)
#     return result    
        
# print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' ))   
# ============================

# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print(result)

# result = re.findall(r'[a-zA-Z]\w{0,}\.{0,}\w{0,}\.{0,}\w+@\w+\.\w{2,}', 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net')
# print(result)

# import re


# def find_all_phones(text):
#     result = re.findall(r"[+]\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}|[+]\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}", text) 
#     return result

# import re
# s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
# print(re.findall("(\d){3}", s))  # ['0']
# print(re.findall("[\d]{3}", s))  # ['110']
# print(re.findall("\d{3}", s))    # ['110']

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(4)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# fh.close()

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)

# fh.close()

# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!')

# position = fh.tell()
# print(position) # 6

# fh.seek(1)
# position = fh.tell()
# print(position) # 1

# fh.read(2)
# position = fh.tell()
# print(position) # 3

# fh.read(102)
# position = fh.tell()
# print(position) # 3

# fh.close()

# byte_str = 'some text'.encode()
# print (byte_str)

# numbers = [127, 255, 156]
# byte_numbers = bytes(numbers)
# print (byte_numbers)
# print(hex(255))

# s = "Привіт!"

# utf8 = s.encode()
# print(utf8) # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

# utf16 = s.encode('utf-16')
# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)  # True

# byte_array = bytearray(b'Kill Bill')
# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array) # bytearray(b'Bill Kill')

# import shutil
# archive_name = shutil.make_archive('backup', 'zip')

# import shutil
# archive_name = shutil.make_archive('backup', 'zip', 'd:\Projects')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')

# import shutil

# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))

# fh = open('test.txt', 'w')
# fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')
# fh.close()

# def total_salary(path):
#   sal_list = ''
#   sum = float(0)
#   fr=open(path, 'r')
#   while True:
#     line = fr.readline()
#     for l in line:
#        if l.isdigit():
#           sal_list=sal_list + l
#     sal = float(sal_list)
#     print("sal", sal)
#     sum = sum + sal
#     print("sum", sum)
#     sal_list = '0'
#     if not line:
#         break
#   fr.close()  
#   return sum

# print(total_salary('D:/Projects/test.txt'))

# l='12.3'
# print(float(l)*2)
# print(l)

# def write_employees_to_file(employee_list, path):
#     f = open(path, 'w')
#     for i in range(len(employee_list)):
#         for el in employee_list[i]:
#             f.write(el + "\n")
#     f.close()


# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'D:/Projects/test.txt')

# def read_employees_from_file(path):
#   list_employees = []
#   f = open(path, 'r')
#   while True:
#     line = f.readline()    
#     if line!='':
#            line = line.replace("\n", "")
#            list_employees.append(line)           
#     if not line:
#          break
#   f.close()
#   return list_employees

# print(read_employees_from_file('D:/Projects/test.txt'))

# def add_employee_to_file(record, path):
#   f = open(path, 'a')
#   f.write(record + "\n")

#   f.close()

# add_employee_to_file('Oksana Pavlenko,43', 'D:/Projects/test.txt')

# def get_cats_info(path):
#    cats_dict = []
#    k=0
#    with open(path, 'r') as f:
#      while True:
#        line = f.readline()
#        line1 = line.replace("\n", "")
#        if(len(line1) == 0):
#         break
#        cats_dict.append ({"id": "", "name": "", "age": ""})
#        #if len(line1)!=0:
#        str_res = ''
#        cats_list = []
#        for i in range(len(line1)):
#          if line1[i]!=',':
#            str_res = str_res + line1[i]
#          else:
#            if str_res!='':
#              cats_list.append(str_res)
#            str_res=''
#        if str_res!=0:
#          cats_list.append(str_res)       
#        print(cats_list)
#        cats_dict[k]['id']=cats_list[0]
#        cats_dict[k]['name']=cats_list[1]
#        cats_dict[k]['age']=cats_list[2]
#        k=k+1
#        if not line:
#          break   
           
#    return cats_dict

# get_cats_info('D:/Projects/test.txt')




# str="abc83 cde7 1 b 24"
# res=[]
# str_res=''
# for i in range(len(str)):
#   if str[i].isdigit():
#     str_res = str_res + str[i]
#   else:
#     if str_res != "":
#       res.append(str_res)
#     str_res = ''
# if str_res != '':
#   res.append(str_res)
#print(res)

# str = 'ae1,Tayson,3'
# list_res =[]
# str_res = ''
# for i in range(len(str)):
#   if str[i]!=',':
#     str_res = str_res + str[i]
#   else:
#     if str_res!='':
#       list_res.append(str_res)
#     str_res=''
# if str_res!=0:
#   list_res.append(str_res)

# print(list_res)

# def get_recipe(path, search_id):
#   is_found = False
#   res = {
#     "id": "",
#     "name": "",
#     "ingredients": []
#     }
#   with open(path, 'r') as f:
#     while True:      
#       str_MongoDB=''
#       str_name=''
#       line = f.readline()
#       line1 = line.replace('\n','')
#       for i in range(len(line1)):
#         if line1[i] == ',':
#           break
#         str_MongoDB=str_MongoDB+line1[i]
#       if str_MongoDB == search_id:
#         print ("wir find!!!")
#         is_found = True        
#         res["id"]=str_MongoDB
#         for i in range(25, len(line1)):
#           if line1[i]!=',':
#             str_name = str_name + line1[i]
#           else: 
#             if str_name!='':
#               res["name"]=str_name
#               str_name = ''
#               k=i
#               break        
#         for i in range(k+1, len(line1)):
#             if line1[i]!=',':
#               str_name = str_name + line1[i]
#             else:
#               if str_name!='':
#                 res["ingredients"].append(str_name)
#                 str_name=''   
#         if str_name!='':
#           res["ingredients"].append(str_name)
#       str_MongoDB=''  
       

#       if not line:
#         break 
#     if is_found:
#       return(res)
#     else:
#       return None   
# print(get_recipe("recept.txt", "60b90c2413067a15887e1"))

# def sanitize_file(source, output):
#   with open(source, 'r') as s_file:
#     text=s_file.read()
#     for int in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#       text=text.replace(int,'')        
#     print(text)
#     with open(output,'w') as out_file:
#       out_file.write(text) 
# sanitize_file('test.txt', 'sanit_file.txt')

# def save_applicant_data(source, output):
#   k=0
#   res = []
#   res_line=''
#   with open(source, 'r') as source_file:
#     l = source_file.readlines()
#     for line in l:
#       if "name" in line:
#         #res_line=res_line + line.strip()
#         res.append(line.strip())
#         l.remove(line)
#         k=k+1
#     for j in range(k):
#       for line in l:
#         if "specialty" in line: 
#           l.remove(line)
#           res[j] = res[j] + line.replace(' ','')
#           break
#     for j in range(k):
#       for line in l:
#         if "math" in line: 
#           l.remove(line)
#           res[j] = res[j] + line.replace(' ','')
#           break
#     for j in range(k):
#       for line in l:
#         if "lang" in line: 
#           l.remove(line)
#           res[j] = res[j] + line.replace(' ','')
#           break  
#     for j in range(k):
#       for line in l:
#         if "eng" in line: 
#           l.remove(line)
#           res[j] = res[j] + line.replace(',','').replace(' ','')
#           break  
#   with open(output,'w') as output_file:
#     for el in res:
#       el=el.replace("name",'')
#       el=el.replace("specialty",'') 
#       el=el.replace("math",'')
#       el=el.replace("lang",'') 
#       el=el.replace("eng",'')    
#       el=el.replace('"','')
#       el=el.replace(':','')
#       el=el.replace('\n','')
           
#       output_file.writelines(el+'\n')
    
# save_applicant_data('test.txt', 'sanit_file.txt')


# li = ['hfjkskj,','jflkdjsakl,','jfkjsdlksd,']
# res=''
# for el in li:
#   for i in range(len(el)-1):
#     res = res + el[i]
#   el = res 
# print(li)
      
# a = ' One     two      three'
# arr=a.split()  # удаляет лишние пробелы
# print(arr)

# def camel_to_snake(s):
#   res = ''
#   for char in s:
#     if char.isupper():
#       res=res+'_'+char.lower()
#     else:
#       res+=char
#   return res  #для вывода всего кроме первого символа res[1:]

# print(camel_to_snake("getNumbersFromString"))  

# def decompose(dna_string):
#   frame =""
#   res = []
#   res.append(dna_string[0:2])
#   for i in range(2, len(dna_string), 3):
#     res.append(dna_string[i:i+3])
#   frame = " ".join(res)
#   return(frame)

# print(decompose("AGGTGACACCGCAAGCCTTATATTAGC"))

# def poker(catds):
#   res = set()
#   for card in catds:
#     last = card[-1]
#     res.add(last)
#   return len(res)==1

# print(poker(["AS", "3S", "10S", "KS", "4S"]))

# def len_vowels_1(text):
#   vowels ="aeiou"
#   for char in text:
#     if char not in vowels:
#       text = text.replace(char, ".")
#   l=text.split(".")
#   lenghts = list()
#   for elem in l:
#     lenghts.append(len(elem))
#   print(lenghts)
#   return max(lenghts)

# print(len_vowels_1("asfdaaeioafafdaeea"))
# import re

# def len_vowels_2(text):
#   res=re.findall(r'[aeiou]+', text)
#   max_el=max(res, key=len)
#   return len(max_el)

# print(len_vowels_2("asfdaaeioafafdaeea"))
# morze_dict={
  
# }
# def morze(text):



# print(morze("Hello, how are you"))
# import re

# def dadFilter(text):
#   return re.sub(r',+', ',',text).rstrip(',')
# print(dadFilter("Hello,,,,,,, it is me,,,"))



# def save_applicant_data(source, output):
#   data=""
#   with open(source) as source:
#     for person in source:
#       data=data+",".join(str(val) for val in person.value())
# ===========================

# def is_equal_string(utf8_string, utf16_string):
#   return utf8_string.decode('utf-8')==utf16_string.decode('utf-16')

# print(is_equal_string(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!', b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00')) 
# print(is_equal_string(b'Hello, how are you', b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00h\x00o\x00w\x00 \x00a\x00r\x00e\x00 \x00y\x00o\x00u\x01'))

# s = "Привет"

# utf8 = s.encode()
# print("utf8",utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

# utf16 = s.encode('utf-16')
# print("utf16",utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)  # True

# str = "Привет"

# print('==========================')
# print("utf8", str.encode('utf-8').decode('utf-8'))
# print("utf16", str.encode('utf-16').decode('utf-16'))
# print("utf32", str.encode('utf-32').decode('utf-32'))

# h = 'utf8 b'Hello, how are you'
# utf16 b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00h\x00o\x00w\x00 \x00a\x00r\x00e\x00 \x00y\x00o\x00u\x00'
# utf32 b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00,\x00\x00\x00 \x00\x00\x00h\x00\x00\x00o\x00\x00\x00w\x00\x00\x00 \x00\x00\x00a\x00\x00\x00r\x00\x00\x00e\x00\x00\x00 \x00\x00\x00y\x00\x00\x00o\x00\x00\x00u\x00\x00\x00''

# def save_credentials_users(path, users_info):
#   str_user=''
#   with open(path, 'wb') as file:
#     for key, value in users_info.items():
#       file.write((key +":" + value +'\n').encode())

# save_credentials_users('byte-test.txt',{'andry':'uyro18890D', 'steve':'oppjM13LL9e'})

# def get_credentials_users(path):
#   res=[]
#   with open(path, 'rb') as file:
#     while True:
#       line = file.readline()
#       line = line.decode()
#       line = line.replace('\n','')
#       res.append(line)
#       if not line:
#         break
#   res.pop(-1)
#   return res
# print(get_credentials_users('byte-test.txt'))

# import base64

# message = 'aladdin:opensesame'
# message_bytes = message.encode("utf-8")
# print(message_bytes)
# base64_bytes = base64.b64encode(message_bytes)
# print(base64_bytes)
# base64_message = base64_bytes.decode("utf-8")
# print(base64_message)


# import base64
# def encode_data_to_base64(data):
#   res=[]
#   for el in data:
#     el_bytes=el.encode('utf-8')
#     base64_el=base64.b64encode(el_bytes)
#     res.append(base64_el.decode('utf-8'))
#   return res  

# print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))

# import shutil

# archive_name = shutil.make_archive('backup', 'zip')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')
# import shutil

# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))



# def save_applicant_data(source, output):
#     data = ""
#     for person in source:
#         data += ','.join([str(v) for v in person.values()])
#         data += '\n'
#     with open(output, 'w') as output_file:
#         output_file.write(data)

# save_applicant_data('test.txt', 'sanit_file.txt')


# import shutil

# def create_backup(path, file_name, employee_residence):
#   with open (path + '/' + file_name, 'wb') as ff:
#              for key, value in employee_residence.items():
#                   str = (key + " " + value + "\n").encode()
#                   ff.write(str) 
        
#   archive_name = shutil.make_archive('backup_folder', 'zip', path) 
#   return archive_name

# print(create_backup('d:\Projects','create_backup.txt',{'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}))

# import shutil

# def unpack(archive_path, path_to_unpack):
#   shutil.unpack_archive(archive_path, path_to_unpack)    
# unpack('111.zip', '111-unpack')

# def is_integer(s):
#     res = True
#     if len(s) == 0:
#         res = False
#         return res
#     else:
#         s=s.strip()
#         if len(s)>=1:
#             if s[0]=='+' or s[0]=='-'or s[0].isdigit():
#                 # print(s)
#                 # print(s[0]=='+' or s[0]=='-'or s[0].isdigit())               
#                 for i in range(1, len(s)):
#                     if not s[i].isdigit():
#                         res = False
#             else:
#                 res=False
              
#         else:
#             res=False   
#     return res 
# print(is_integer("    +12511177   ")) 

# def capital_text(s):
#   punctuation_mark='!?.' 
#   i=1
#   index_first_symb=0
#   wait = False
#   if s[0] != " ":
#     s=s.replace(s[0], s[0].upper())
#   else:
#     while i <= len (s)-1:
#       if s[i-1]==" " and s[i].isalpha():
#         s=s.replace(s[i], s[i].upper())
#         index_first_symb=i
#         print("index_first_symb",i)
#         break
#       i+=1
# #============================================
#   for i in range(index_first_symb+1, len(s)):
#     if s[i] in punctuation_mark:
#       wait = True
#       for j in range (i+1, len(s)):
#         if s[j].isalpha() and wait == True:
#           print (f"s[j].isalpha() and wait == True, i= {i}, j = {j}, wait = {wait}")
#           s=s[:j] + s[j].upper() + s[j+1:]
#           wait = False
#           break
#   return s
# print(capital_text("      i go to! no? yes. of course  "))




# def capital_text(s):
#   punctuation_mark='!?.' 
#   wait = True
#   for i in range(len(s)):
#     if wait == True and s[i].isalpha():
#       s = s[:i] + s[i].upper() + s[i+1:]
#       wait = False
#     elif s[i] in punctuation_mark:
#       wait = True
#   return s
# print(capital_text("      i go to! no? yes. of course  "))

# s = "22 hhfhdj534 dd1jfdk 5 jldk78"
# res = []
#i=0

# while i<len(s):
#   str_res=''
#   while i<len(s) and s[i] in "0123456789":
#     str_res = str_res + s[i]
#     i+=1
#   i+=1
#   if str_res!="":
#     res.append(str_res)  
# print(res)  

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     word=''
#     if not reverse:
#         for i in range(len(riddle)):
#             if riddle[i]==start_letter:
#                 word=riddle[i:i+word_length]
#                 break
#     else:
#         riddle = riddle[::-1]
#         for i in range(len(riddle)):
#             if riddle[i]==start_letter:
#                 word=riddle[i:i+word_length]
      
#     return word

# print(solve_riddle('mi1powerpret', 5, 'p'))
# print(solve_riddle('mi1rewopret',5,'p',reverse=True))
# print(solve_riddle('mi1powerret',5,'p'))

# def data_preparation(list_data):
#   res=[]
#   min_el=None
#   max_el=None
#   for list in list_data:
#     if len(list)>2:
#       min_el=list[0]
#       max_el=list[0]
#       for el in list:
#         if el>max_el:
#           max_el=el
#         if el<min_el:
#           min_el=el
#       list.remove(min_el)
#       list.remove(max_el)
#       for el in list:
#           res.append(el)
#     else:  
#       for el in list:
#         res.append(el)  
#   res.sort(reverse=True)
#   return res    
# print(data_preparation([[1,2,3],[3,4],[5,6]]))  

# def token_parser(s):
#   operator = "+-/*)()"
#   res = []
#   number_str=''
#   i=0
#   while i< len(s):
#     if s[i]!=" " and s[i] not in operator:
#           number_str = ""
#           while i<len(s) and s[i] in "0123456789":
#             number_str = number_str + s[i]
#             i+=1
#           i-=1
#           if number_str !="":
#               res.append(number_str)
#     elif s[i] in operator:
#       res.append(s[i])
#     i+=1  
#   return res
# print("result>>>> ",token_parser("2+ 347 + 11111 -5 * 3"))

# def all_sub_lists(data):
#   out = [[]]
#   for i in range(len(data)):
#     for j in range(len(data)-i):
#       out.append(data[j:j+i+1])
#   return out 
# print(all_sub_lists([1, 2, 3, 4]))

# def make_request(keys, values):
#   dict={}
#   if len(keys)!=len(values):
#     return dict
#   else:
#     for i in range(len(keys)):
#       dict[keys[i]]=values[i]
#   return dict


# print(make_request(["1", "2", "3", "4"],["one", "two", "three", "four"]))
    
#Напишіть функцію sequence_buttons, що показує послідовність кнопок, яку необхідно натиснути, щоб на екрані телефону з'явився текст, введений користувачем.
# def sequence_buttons(string):
#   string = string.lower()
#   print(string)
#   letters = {'1':'.,?!:','2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz','0':' '}
#   out=''
#   for s in string:   
#     for key in letters: 
#         if s in letters[key]:    
#             for x in letters[key]: 
#                 if x == s:
#                     out=out + key 
#                     break   
#                 else:
#                     out = out + key 
#   return out
# print(sequence_buttons("Hello, World!"))

# def file_operations(path, additional_info, start_pos, count_chars):
#   res_str=''
#   with open(path, 'a') as ff:
#     ff.write(additional_info)
#   with open(path, 'r') as ff:
#     ff.seek(start_pos)
#     res_str=ff.read(count_chars)
#   return res_str  
# print(file_operations('D:/Projects/test1.txt', 'additional_info', 10, 5))

# def get_employees_by_profession(path, profession):
#   res_list=[]
#   res_str=''
#   with open(path, 'r') as ff:
#     lines = ff.readlines()
#   for line in lines:
#     if line.find(profession)!=-1:
#       line=line.replace('\n','').replace(' ','').replace(profession,'')
#       res_list.append(line)
#   res_str = " ".join(res_list)
#   return res_str    
# print(get_employees_by_profession('D:/Projects/test1.txt', 'cook'))

# def to_indexed(source_file, output_file):
#   lines=[]
#   with open(source_file, 'r') as in_f:
#     lines = in_f.readlines()
#     for i in range(len(lines)):
#       lines[i] = str(i) + ': ' + lines[i]
#   with open(output_file, 'w') as out_f:
#          for line in lines:
#             out_f.write(line)
  
# to_indexed('D:/Projects/test1.txt', 'D:/Projects/out.txt')

# Выпрямление списков при помощи рекурсии

# def flatten(data):
#   if data == []:
#     return data
#   if isinstance(data[0], list):
#     return(flatten(data[0]) + flatten(data[1:]))
#   return(data[:1] + flatten(data[1:]))

# print(flatten([1, 2, [3, 4, [5, 6]], 7]))

#рекурсивну функцію decode для декодування списку, закодованого цим способом:Розберемо просту техніку кодування та декодування на основі серій. Наприклад, у нас є список із повторюваними спостереженнями якоїсь величини, вона може приймати значення X, Y або Z. Значення з'являються у довільному порядку та зберігаємо ми їх у списку ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] або рядку "XXXZZXXYYYZZ".Внаслідок чого ми можемо зменшити обсяг інформації, що зберігається? Стиснення можна досягти заміною групи повторюваних значень на одноразове значення та лічильник повторів: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

# def decode(data):
#     if not data:
#         return []
#     else:
#         return [data[0]] * int(data[1]) + decode(data[2:])
# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

#рекурсивну функцію encode для кодування списку або рядка. Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
# def encode(data):
#       count=0
#       if not data:
#         return []
#       else:
#           for i in range(len(data)):
#               if data[0]==data[i]:
#                   count+=1
#               else:
#                   break               
#           return [data[0]] + [count] + encode(data[count:])      
              
        
# print(encode(['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']))    



# def print_num_rec(num):
#   if num != 0:
#     print_num_rec(num-1)
#     print(num)
# print_num_rec(5)

# def func(n):
#     if n!=0:
#        return f"{n}, {func(n-1)}"
         
# n = int(input("Введите число: "))
# print(func(n))

# def count(a, b):    
#     if a<b:
#         count(a, b - 1)
#         print(b)
#     elif a>b:
#         print(a)
#         count(a - 1, b)
#     else:
#         print(a)
# a = int(input())
# b = int(input())
# count (a, b)

# def count (a,b):
#   if a<b:
#     count(a, b-1)
#     print (b)
#   elif a>b:
#     print(a)
#     count(a-1,b)
#   else:
#     print(a)
# count (9,2)

# def rec(num):
#   print(num)
#   if num <4:
#     rec(num+1)
#   print(num)
# rec(1)

# def faktorial(n):
#   f=None
#   if n<=0: 
#     f=1
#   else:
#     f=n*faktorial(n-1)
#   return f
# print(faktorial(3))

#Точная степень двойки

# def st2(num):
#   if num == 1:
#     return ("Y")
#   elif num < 1:
#     return ("N")
#   else:
#     return st2(num/2)
     
# print (st2(9))

 #-------------------------заполняет рандомными данными людей, количества введенного с клавиатуры в файл, указанных на клаве, возвращает список словарей
# import argparse
# import json
# from mock import get_mocked_user

# parser = argparse.ArgumentParser(description="User data generation")
# parser.add_argument("--filename", help="JSON file", required=True)
# parser.add_argument("--amount", required=True)

# argument = vars(parser.parse_args())
# filename=argument.get("filename")
# amount = int(argument.get("amount"))

# print(filename, amount)

# with open(filename, 'w') as file:
#   users=list()
#   for i in range(amount):
#     user = get_mocked_user()
#     users.append(user)
#   string=json.dumps(users)
#   file.writelines(string)

  #-------------------------

# from pathlib import Path

# current_paht = Path('.')
# print(current_paht)
# print(current_paht.cwd()) # способо достать папку откуда запущен скрипт

# text_file = current_paht/"Temp"/"data.txt"
# print(text_file)
# print(text_file.parts)
# print(text_file.name)
# print(text_file.parent)

# from pathlib import Path
# print all files
# current_dir = Path('.')
# for el in current_dir.iterdir():
#   print(el.name)
#   print(el.is_dir())
#   print(el.is_file())

# from pathlib import Path
# current_dir=Path('main.py')
# statistics=current_dir.stat()
# print(statistics)

# parsing folder and file
# from pathlib import Path
# p = Path('.')
# def parse_folder(path):
#   for el in path.iterdir():
#     if el.is_dir():
#       print(f"This is folder: {el}")
#     else:
#       print(f"This is file: {el}")


# def parse_file(path):
#    for el in path.iterdir():
#      if el.is_dir():
#        print(f"This is folder: {el}")
#        parse_file(el)
#      else:
#        print(f"This is file: {el}")
       
# parse_folder(path=p)
#parse_file(path=p)
#------------------

# delete file 
# from pathlib import Path
# p=Path('test1.txt')
# if p.exists():
#   p.unlink()

#delete folder
# from pathlib import Path
# new_dir = Path("123")
# new_dir.mkdir(exist_ok=True)
# new_dir.rmdir() # delete not ampty folder

# from datetime import datetime

# current_datetime = datetime.now()

# future_month = (current_datetime.month % 12) + 1
# future_year = current_datetime.year + int(current_datetime.month / 12)
# future_datetime = datetime(future_year, future_month, 1)
# print(current_datetime.month % 12)
# print(int(current_datetime.month / 12))
# print(future_month)
# print (future_year)
# print(future_datetime)
# print(current_datetime < future_datetime)    # True

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0

# ts += 100_000
# print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.strftime('%A %d %B %Y')) # Tuesday 07 January 2020

# import random

# print(random.randint(1, 1000))
# print(random.random())
# fruits = ['apple', 'banana', 'orange']
# random.shuffle(fruits)
# print(fruits)   # ['banana', 'orange', 'apple']
# print(random.choice(fruits))   # 'banana'
# print(random.choices(fruits, k=4))   # ['banana', 'orange', 'orange', 'orange'] ибрати N випадкових елементів зі списку
# print(random.sample(fruits, k=2))   # ['banana', 'orange'] вибрати N елементів, що не повторюються, зі списку

# print(0.1 + 0.2 == 0.3)     # False
# print(0.1 + 0.2)            # 0.30000000000000004

# from decimal import Decimal, getcontext


# getcontext().prec = 6
# Decimal(1) / Decimal(7)  # Decimal('0.142857')

# getcontext().prec = 28
# Decimal(1) / Decimal(7) # Decimal('0.1428571428571428571428571429')

# getcontext().prec = 6
# print(float(Decimal(0.1) + Decimal(0.2)) == 0.3)   # True

# # обычное вычисление, существует погрешность
# a = 0.2+0.2+0.2-0.4 # a =   0.20000000000000007 - погрешность (???)
# print('a = ', a)

# # вычисление с помощью класса Decimal
# b = Decimal('0.2')+Decimal('0.2')+Decimal('0.2')-Decimal('0.4')
# print('b = ', b) # b = 0.2 - точный результат

# sq = []
# for i in range(1, 5+1):
#     sq.append(i**2)

# print(sq)   # [1, 4, 9, 16, 25]

# numbers = [i for i in range(1, 5+1)]
# print(numbers)
# sq = [i ** 2 for i in range(1, 5+1)]
# print(sq)
# numbers = [1, 4, 1, 3, 2, 5, 2, 6]
# sq = [i**2 for i in numbers]
# print(sq)
# sq1 = {i ** 2 for i in numbers}
# print(sq1)   # {1, 4, 36, 9, 16, 25}
# sq_dict = {i: i ** 2 for i in numbers}
# print(sq_dict)   # {1: 1, 4: 16, 3: 9, 2: 4, 5: 25, 6: 36}

# from datetime import datetime

# def get_days_from_today(date):
#   input_datetime=datetime.strptime(date, '%Y-%m-%d')
#   current_datetime = datetime.now()
#   print(input_datetime)
#   print(current_datetime)
#   difference = current_datetime - input_datetime
#   print(difference.days)
#   return difference.days  
# get_days_from_today('2020-10-09')

