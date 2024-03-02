# EXAM FOR WEEK 5

## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

## RULES:
> No interner, no help to each other!

> Make one file and place all your work there (e.g. odina_kholiqov.py)

> Send the file at 

> You have 2 hours only

### 1 Question
Create Customers table with (CustomerID, FirstName, LastName, Email, Phone) and Orders table with (OrderID, CustomerID, OrderDate, TotalAmount) columns.
Relationship:
  1. Define a foreign key relationship between the CustomerID column in the Orders table and the CustomerID column in the Customers table.
  2. Ensure that when a customer is deleted from the Customers table, all associated orders are automatically deleted from the Orders table.
Filling table data:
  1. Insert three customers into the Customers table with sample data.
  2. Insert five orders into the Orders table, ensuring they are associated with existing customers.

### 2 Question
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA. The CITY table is described as follows: 

Запросите все столбцы для всех американских городов в таблице CITY с населением более 100 000 человек. Код страны для Америки — USA. Таблица CITY описывается следующим образом:

Sample table: CITY(ID, NAME, COUNTRY_CODE, ZIP_CODE)
| ID    |     NAME     |CODE |   POP   |
--------+--------------+-----+---------+
|  1    | New York     | USA | 8500000 |
|  2    | Los Angeles  | USA | 3990000 |
|  3    | Chicago      | USA | 2716000 |
|  4    | Houston      | USA | 2328000 |
|  5    | Phoenix      | USA | 1680000 |
|  6    | Philadelphia | USA | 1584000 |
|  7    | San Antonio  | USA | 1544000 |
|  8    | San Diego    | USA | 1407000 |
|  9    | Dallas       | USA | 1341000 |
|  10   | San Jose     | USA | 1035000 |

### 3 Question
Query a list of CITY and STATE from the STATION table. The STATION table is described as follows: 

Запросите список CITY и STATE из таблицы STATION. Таблица STATION описывается следующим образом:

Sample table: STATION(ID, CITY, STATE, ZIP_CODE)

| ID    |     CITY     |STATE |   ZIP_CODE   |
--------+--------------+------+--------------+
|  1    | New York     | NY   |    10001     |
|  2    | Los Angeles  | CA   |    90001     |
|  3    | Chicago      | IL   |    60601     |
|  4    | Houston      | TX   |    77001     |
|  5    | Phoenix      | AZ   |    85001     |
|  6    | Philadelphia | PA   |    19101     |
|  7    | San Antonio  | TX   |    78201     |
|  8    | San Diego    | CA   |    92101     |
|  9    | Dallas       | TX   |    75201     |
|  10   | San Jose     | CA   |    95101     |


### 4 Question
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer. The STATION table is described as follows:

Запросите список названий CITY у STATION для городов, имеющих четный идентификационный номер. Выведите результаты в любом порядке, но исключите из ответа дубликаты. Таблица STATION описывается следующим образом:

Sample table: STATION(ID, CITY, STATE, ZIP_CODE)

| ID    |     CITY     |STATE |   ZIP_CODE   |
--------+--------------+------+--------------+
|  1    | New York     | NY   |    10001     |
|  2    | Los Angeles  | CA   |    90001     |
|  3    | Chicago      | IL   |    60601     |
|  4    | Houston      | TX   |    77001     |
|  5    | Phoenix      | AZ   |    85001     |
|  6    | Philadelphia | PA   |    19101     |
|  7    | San Antonio  | TX   |    78201     |
|  8    | San Diego    | CA   |    92101     |
|  9    | Dallas       | TX   |    75201     |
|  10   | San Jose     | CA   |    95101     |


### 5 Question
Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
```
class Nobel:
    pass

np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)
```

### 6 Question
    Write a program to create a child class Teacher that will inherit the properties and methods from the parent class Staff. Staff class has role, departament and salary attributes.

Напишите программу для создания дочернего класса Teacher, который будет наследовать свойства и методы родительского класса Staff. Класс Staff имеет атрибуты role, departament и salary.

### 7 Question
Write a program to build a simple Student Management System using classes and containers (lists, dict). The system should perform the following operations:

    1. Accept: Method to enter new student details
    2. Display: Function to display student details
    3. Search: Search Function
    4. Delete
    5. Update

Напишите программу для построения простой системы управления студентами с использованием классов и контейнеров (list, dict). Система должна выполнять следующие операции:

     1. Принять: метод ввода данных о новом студенте.
     2. Дисплей: функция отображения сведений об ученике.
     3. Поиск: функция поиска.
     4. Удалить
     5. Обновление

### 8 Question
Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Учитывая целое число n, верните ответ в виде массива строк (с индексом 1), где:
     ответ[i] == "FizzBuzz", если i делится на 3 и 5.
     ответ[i] == "Шипение", если i делится на 3.
     ответ[i] == "Buzz", если i делится на 5.
     ответ[i] == i (как строка), если ни одно из вышеуказанных условий не верно.

#### Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

#### Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

#### Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


### 9 Question
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
    1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
    2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    3. Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Напишите алгоритм, определяющий, является ли число n счастливым.

Счастливое число — это число, определяемое следующим процессом:
     1. Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.
     2. Повторяйте процесс до тех пор, пока число не станет равным 1 (где оно и останется), или пока он не зациклится в цикле, не включающем 1.
     3. Счастливыми являются те числа, для которых этот процесс заканчивается на 1.

Возвращайте true, если n — счастливое число, и false, если нет.

#### Example 1:
    Input: n = 19
    Output: true
    Explanation:
        1**2 + 9**2 = 82
        8**2 + 2**2 = 68
        6**2 + 8**2 = 100
        1**2 + 0**2 + 0**2 = 1

#### Example 2:
    Input: n = 2
    Output: false


### 10 Question 
The database contains the following tables: "Users" (with information about users), "Movies" (with information about films),
"Ratings" (with information about the rating that users have given movies) and "Genres" (with information about film genres).
База данных содержит следующие таблицы: "Пользователи" (с информацией о пользователях), "Фильмы" (с информацией о фильмах), 
"Оценки" (с информацией о рейтинге, который пользователи поставили фильмам) и "Теги" (с информацией о тегах, присвоенных фильмам).

Tasks: Write a complex query that calculates the following statistics:

1. The average rating of each film, rounded to two decimal places, taking into account only those films with more than 30 ratings.
2. Top 5 most active users by number of ratings, including their total number of ratings and the average rating they gave.
3. The dynamics of the average rating of films over the past year (calculate the average rating for each month), as well as the total number of ratings for each month.

Задача: написать сложный запрос, который рассчитывает следующую статистику:
1. Средний рейтинг каждого фильма, округленный до двух знаков после запятой, с учетом только тех фильмов, у которых более 30 оценок.
2. Топ-5 самых активных пользователей по количеству оценок, включая их общее количество оценок и средний рейтинг, который они поставили.
3. Динамику среднего рейтинга фильмов за последний год (рассчитать средний рейтинг для каждого месяца), а также общее количество оценок за каждый месяц.