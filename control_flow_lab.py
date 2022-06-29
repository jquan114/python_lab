 # exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
from calendar import c


letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
if letter in ' a e i o u':
    print(f'the letter{letter} is a vowel')
else:
    print(f'the letter{letter} is a consonant')



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
phrase = ''
while phrase != quit:
    phrase = input ('please enter a word or phrase: ')
    print(f' what you entered is {len(phrase)} characters long')


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
human_years = int(input("Input a dog's age in human years: "))
if human_years < 3:
    dog_years = human_years * 10
else:
    dog_years = 20 +(human_years -2) * 7
print(f"the dog's age in dog years is {dog_years}")





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
print('enter the length of three sides of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b and b == c:
    print(f'a triangle with sides of {a},{b} and {c} is equalateral triangle')
elif a != b and  a != c and b != c:
    print(f'a triangle with sides of {a},{b} and {c} is a scalene triangle')
else:
    print(f' a triangle with side of {a},{b} and {c} is a isosceles')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
term = 0 
a = 0
b = 1
while term < 50:
    if term < 2:
        print(f'term:{term} / number:{term}')
    else:
        num = a + b
        print(f'term{term} / number:{num}')
        a = b 
        b = num
    term += 1



# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('Enter the month of the season (Jan - Dec): ')
day = int(input('enter the day of the month:'))
if month  in ('Jan','Feb','Mar'):
    season = 'winter'
elif month in ('Apr','May','Jun'):
    season = 'spring'
elif month in ('Jul', 'Aug','Sep'):
    season = 'summer'
else:
    season ='Fall'
if month =='Mar' and day >19:
    season = 'Spring'
elif month == 'June' and day > 20:
    season = 'Summer'
elif month == 'Sep' and day > 21:
    season = "Fall"
elif month == "Dec" and day > 20:
    season ="Winter"
print(f'{month} {day} is in{season}')