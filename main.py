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
 # Найти площадь прямоугольника, треугольника или круга

