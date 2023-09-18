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
word = 'fooTThball, wollEYball, tEnnis'
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