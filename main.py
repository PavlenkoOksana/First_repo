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