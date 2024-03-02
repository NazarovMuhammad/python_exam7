# ### 5 Question
# Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

# Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
# ```
# class Nobel:
#     pass

# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)

# class Nobel:
    
#     def __init__(self,category,year,name):
#         self.category = category
#         self.year = year
#         self.name = name
        
#     def __str__(self):
#          return f"{self.category},{self.year}, {self.name}"
     
# np2007 = Nobel('Peace',2007,'Muhammad Nazarov')
# print(np2007)









# ### 6 Question
# Write a program to create a child class Teacher that will inherit the properties and methods from the parent class Staff. Staff class has role, departament and salary attributes.
# Напишите программу для создания дочернего класса Teacher, который будет наследовать свойства и методы родительского класса Staff. Класс Staff имеет атрибуты role, departament и salary.     
# class Staff:
    
#     def __init__(self,role,departament,salary):
#         self.role = role
#         self.departament = departament
#         self.salary = salary
           
#     def __str__(self):
#       return f"{self.role},{self.departament}, {self.salary}"
  
# class Teacher(Staff):
#     pass

# S = Staff('developer Python','Oficce',15000)
# print(S)
# T = Teacher('Programist','School',10000)  
# print(T)











# ### 8 Question
# Given an integer n, return a string array answer (1-indexed) where:
#     answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     answer[i] == "Fizz" if i is divisible by 3.
#     answer[i] == "Buzz" if i is divisible by 5.
#     answer[i] == i (as a string) if none of the above conditions are true.

# Учитывая целое число n, верните ответ в виде массива строк (с индексом 1), где:
#      ответ[i] == "FizzBuzz", если i делится на 3 и 5.
#      ответ[i] == "Шипение", если i делится на 3.
#      ответ[i] == "Buzz", если i делится на 5.
#      ответ[i] == i (как строка), если ни одно из вышеуказанных условий не верно.

# #### Example 1:
#     Input: n = 3
#     Output: ["1","2","Fizz"]

# #### Example 2:
#     Input: n = 5
#     Output: ["1","2","Fizz","4","Buzz"]

# #### Example 3:
#     Input: n = 15
#     Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]



# a = int(input())
# fb = []
# for i in range(1,a):
#     if i%3 == 0 and 1%5 == 0:
#         fb.append("fizzbuzz")
#     elif i%3 == 0:
#         fb.append("Fizz") 
#     elif i%5 == 0:
#         fb.append("Buzz")
#     else:
#         fb.append(i)
        
# print(fb)



# ### 9 Question
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#     1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     3. Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Напишите алгоритм, определяющий, является ли число n счастливым.

# Счастливое число — это число, определяемое следующим процессом:
#      1. Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.
#      2. Повторяйте процесс до тех пор, пока число не станет равным 1 (где оно и останется), или пока он не зациклится в цикле, не включающем 1.
#      3. Счастливыми являются те числа, для которых этот процесс заканчивается на 1.

# Возвращайте true, если n — счастливое число, и false, если нет.

# #### Example 1:
#     Input: n = 19
#     Output: true
#     Explanation:
#         1**2 + 9**2 = 82
#         8**2 + 2**2 = 68
#         6**2 + 8**2 = 100
#         1**2 + 0**2 + 0**2 = 1

# #### Example 2:
#     Input: n = 2
#     Output: false   

a = int(input())
if a >10:
   b = a/10
   c = a%10
   while True:
       d = b**2 + c**2
       if d < 
       v = 
       if d == 0:
            print("True")
            break
       else:
           print('False')
           break    
        
 