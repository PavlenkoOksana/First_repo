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


