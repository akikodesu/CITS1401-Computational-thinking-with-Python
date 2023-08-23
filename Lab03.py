#Q1: Write a function my_abs(value) that returns the string mentioning whether the value is positive, negative or zero. The three possible outputs are "positive", "negative" or "zero". Remember the outputs are case sensitive. 
def my_abs(value):
    if value > 0:
        return 'positive'
    elif value < 0:
        return 'negative'
    else:
        return 'zero'
    

#Q2: Write a boolean function is_odd(number) that takes an integer parameter number and returns True if and only if number is odd. (Hint: consider the mod operator %).
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False
    

#Q3: Write a function bmi_risk(bmi, age) that takes two positive numeric arguments as parameters bmi and age and returns a string Low, Medium, or High according to the following table:
"""
                    Under 45    45 or over
BMI less than 22    Low         Medium
BMI 22 or more      Medium      High
"""
def bmi_risk(bmi, age):
    if age < 45:
        if bmi < 22:
            return 'Low'
        else:
            return 'Medium'
    else:
        if bmi < 22:
            return 'Medium'
        else:
            return 'High'
        

#Q4: Write a function buy_goods(cost, savings) that takes two positive numeric arguments as parameters cost and savings and returns a Boolean type True only if the cost of the item is less than 5% of the savings, otherwise false.
def buy_goods(cost, savings):
    if cost < (savings * 0.05):
        return True
    else:
        return False
    

#Q5: Rewrite the function record_check(age, gender, location) below so that only a single if-else statement is used. Your function does not need to return anything.
"""
def record_check(age, gender, location):
    """ Function to find a male person depending on their age, gender and location """
    if age > 18:
        if gender == "M":
            if location == "Perth":
                print("Found him!")
            elif location == "Sydney":
                print("Found him!")
            else:
                print("Did not find him.")
        else:
            print("Did not find him.")
    else:
        print("Did not find him.")

"""
def record_check(age, gender, location):
    if age > 18 and ((location == "Perth") or (location == "Sydney")):
        print("Found him!")
    else:
        print("Did not find him.")


#Q5: Write a function balance_list(items) that takes a list items which contains integers and returns the provided list if the number of items in the list is even, otherwise it returns the list but with its last item repeated (in order to make the number of items in the list even).
def balance_list(items):
    if len(items) % 2 == 0:
        return items
    else:
        items.append(items[-1])
        return items
    

#Q6: Write a function double_list(items) that takes a list items and returns a list that has been duplicated (see the examples below) if the number of items in the list is even, otherwise it returns a list that is the same as items but with only the last item repeated.
def double_list(items):
    if len(items) % 2 == 0:
        return items * 2
    else:
        items.append(items[-1])
        return items
    

#Q7: Two words are anagrams if they contains exactly the same letters but in a different order. Write a function are_anagrams(word1, word2) which returns True if the two parameters are anagrams.
"""
BIG HINTS:
    1. You can convert a word into a list of the letters in that word.
    2. Lists of strings can be sorted into alphabetical order using the list.sort() method.
    3. The equality operator '==' works on lists.
    4. Two identical words are not anagrams.
"""
def are_anagrams(word1, word2):
    
    sorted_word1 = sorted(list(word1))
    sorted_word2 = sorted(list(word2))
    
    return sorted_word1 == sorted_word2 and word1 != word2


#Q8: A list of people's ages and names are provided in two separate lists age_list and name_list, and they are indexed for each person (e.g. person 1's information is at age_list[1] and name_list[1]). 
#Write a function locate_person(age_list, name_list, age, name) which returns the index of the first person that has age equal to age and the name equal to name. You can assume there is always a person that matches the description, and names in the name_list are unique.
def locate_person(age_list, name_list, age, name):
    for index in range(len(age_list)):
        if age_list[index] == age and name_list[index] == name:
            return index
        

#Q9: A hunter takes n bullets to hunt. On a sunny day, his accuracy is high so it only takes 1 bullet to hunt a rabbit, and 2 bullets to hunt a deer. But on a rainy day, his accuracy drops and takes 2 bullets to hunt a rabbit and 3 bullets to hunt a deer. 
"""
Write a function hunting_animals(weather, animal, n) which returns the number of animal he successfully caught on that day.
weather values are either "sunny" or "rainy".
animal values are either "rabbit" or "deer"
n value is a positive integer 0 < n < 100.
"""
def hunting_animals(weather, animal, n):
    if weather == "sunny":
        if animal == "rabbit":
            return int(n)
        else:
            return int(n / 2)
    else:
        if animal == "rabbit":
            return int(n / 2)
        else:
            return int(n / 3)
        

#Q10: Write a boolean function check_temperature(temperature, limit) that takes floats temperature and limit, where temperature is in degrees Celsius and limit is in Fahrenheit, and returns True if limit is greater than the temperature in the same metric, else returns False. You may find the equation below useful.
#fahrenheit = celsius x 9 / 5 + 32
def check_temperature(temperature, limit):
    c_to_f = temperature * 9 / 5 + 32
    if limit > c_to_f:
        return True
    else:
        return False


#Q11: Write a function compare_strings(string1, string2) which returns the larger string based on the length of the string if their first letters are the same (e.g. "band" and "bread" as inputs, "bread" will be returned because the length is longer), if their lengths are the same, then the function returns "error". On the other hand, if their first letters are different, then their last letters are compared and the string with the character that will appear later in the dictionary is returned (e.g. with "sky" and "cloud" as inputs, "sky" will be returned because 'y' comes after 'd' in the dictionary). One exception to the second case is that, if the last letters of each string are the same, then the function is to return "error".
def compare_strings(string1, string2):
    if string1[0] == string2[0]:
        if len(string1) > len(string2):
            return string1
        elif len(string1) < len(string2):
            return string2
        else:
            return "error"
    else:
        if string1[0] != string2[0]:
            if string1[-1] < string2[-1]:
                return string2
            elif string1[-1] > string2[-1]:
                return string1
            else:
                return "error"
            

#Q12: We are in a long jump competition with various athletes. Some athletes are injured so their performance can be affected. These are the variables used:
"""
speed is the running speed in m/s (float value greater than 0).
power is the strength to jump (float value between 0 and 1). 
name is the jumper's name (string).
injured is whether the jumper is injured or not (boolean). If injured, the distance the jumper will jump is decreased by 20%.

For example, if Brian is running at 9m/s with a strength of 0.6 without any injuries, he can jump 0.6 * 9 = 5.40m.
For example, if Morrison is running at 9m/s with a strength of 0.6 but with an injury, he can jump 0.8 * 0.6 * 9 = 4.32m.

Write a function can_jump(speed, power, name, injured) which returns a string "[name] can jump [distance]m!", where "distance" is formatted to 2 decimal places. However, if the jumper jumps less than a metre, then the function is to return the string "[name] made a false attempt!"
"""
def can_jump(speed, power, name, injured):
    if speed * power > 1:
        if injured == False:
            distance = float(speed) * float(power)
            return name + " can jump " + "{:.2f}".format(distance) + "m!"
        else:
            distance = float(speed) * float(power) * 0.8
            return name + " can jump " + "{:.2f}".format(distance) + "m!"
    else:
        return name + " made a false attempt!"