#Q1: Write a function to_celsius(fahrenheit) that takes a float temperature in degrees fahrenheit and returns the equivalent temperature in degrees celsius. The formula is:
#degrees_celsius = (fahrenheit - 32) * (5 / 9)
def to_celsius(fahrenheit):
    """Return the given fahrenheit temperature in degrees celsius"""
    degrees = float((fahrenheit - 32) * (5 / 9))
    return degrees


#Q2: Write a function days_in_years(number_of_years)that returns the number of days in the given number of years. You may assume that there are exactly 365 days in every year and that the numbers of years will always be a whole number.
def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    # Your code goes here
    days = int(number_of_years * 365)
    return days


#Q3: Write a function calculate_cartons(eggs)for a small local farm that takes a number of eggs and returns the number of egg cartons that will be needed to pack these eggs, assuming 12 eggs fit into a carton.
def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    cartons = eggs // 12
    return cartons


#Q4: Create a function dinner_calculator(meal_cost, drinks_cost)that calculates and returns the total cost of the meal for a small restaurant during happy hour
#The function takes two values, the cost of the meals and drinks before GST
#Before GST is applied, a 30% discount needs to be applied to the drinks cost.
#Goods and services tax needs to be added to the meal and drinks cost, GST is set to 15%.
#The function should return the total cost.
def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    drinks_cost = drinks_cost * 0.7
    GST = (meal_cost + drinks_cost) * 0.15
    total_cost = meal_cost + drinks_cost + GST
    return total_cost


#Q05: Write a function odd_finder(a,b,c,d,e,f,g,h,i,j) which takes 10 integers as inputs and returns the count of positive odd integers.
def odd_finder(a,b,c,d,e,f,g,h,i,j):
    numbers = [a,b,c,d,e,f,g,h,i,j]
    count = 0

    for num in numbers:
        if num > 0 and num % 2 != 0:
            count += 1
    return count


#Q6: A local biologist needs a program to predict virus population growth. The inputs would be
#the initial number of virus infected persons (num)
#the rate of growth (a real number greater than 0) (rate)
#the number of hours it takes to achieve this rate (hour)
#and a number of hours during which the virus population grows (time)
#Write a function virus_growth that takes these inputs and returns a prediction of the total population.
def virus_growth(num, rate, hour, time):
    total_times = time / hour
    total_population = num * (rate ** total_times)
    return total_population


#Q7: Write a function dseries(n_terms) to calculate the first n terms of the following series
#1^2 + 2^2 + 3^2 + 4^2 + 5^2 + ...
def dseries(n_terms):
    sum = 0
    for term in range(1, n_terms + 1):
        sum += term ** 2
    return sum
