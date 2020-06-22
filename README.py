# PY3Programming-Course
Solution of PY3Programming Course 1 to 4

# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

# Hard-coded answers will receive no credit.



rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"                    
b=rainfall_mi.split(',')
rainfall_mi=0
count=0
for i in b:
    if (float(i) > 3.0):
        count=count+1
    else:
        pass
num_rainy_months=count    





# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

# Hard-coded answers will receive no credit.



sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count=0
for i in sentence.split(' '):
    if i[0]==i[-1]:
        same_letter_count+=1








# Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

# HINT 1: Use the accumulation pattern!

# HINT 2: the in operator checks whether a substring is present in a string.

# Hard-coded answers will receive no credit.






items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if 'w' in i:
        acc_num += 1

print(acc_num)







# Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

# Note 1: be sure to not double-count words that contain both an a and an e.

# HINT 1: Use the in operator.

# HINT 2: You can either use or or elif.

# Hard-coded answers will receive no credit.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
b=sentence.split()
num_a_or_e = 0
for i in b:
    if ('a' in i) or ('e' in i):
        num_a_or_e += 1

print(num_a_or_e)





 # Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels. 



s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
count,num_vowels=0,0
for i in s:
    if i in vowels:
        count=count+1

num_vowels=count











# Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners. 

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.reverse()
z_winners=winners
print(z_winners)





# Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z. 

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']                       
winners.sort()





# Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method. 

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
i="Guadalajara"
trav_dest.append(i)





# Write code to take ‘London’ out of the list trav_dest. 


trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove("London")




# Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports. 

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, 'horseback riding')







# Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars. 

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars=[]
for i in str1:
    chars.append(i)
    







# For each character in the string saved in ael, append that character to a list that should be saved in a variable app. 

ael = "python!"
app = []
for w in ael:
    app.append(w)
print(app)









 # For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds. 
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = [word + "ed" for word in wrds]
print(past_wrds)










# Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores. 

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores_split = scores.split(" ")
a_scores = 0
for x in scores_split:
    x = float(x)
    if x >= 90:
        a_scores += 1

print(a_scores)







# 	 Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”. 

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

stopwords = set(w.upper() for w in stopwords)
acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)











# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”. 


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = "The water earth and air are vital"

acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
print(acro)
















# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work. 


p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]














# Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    item_desc, number, cost = item.split(", ")
    print("The store has {} {}, each for {} USD.".format(number, item_desc, cost))





#  Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1. 


class BankAccount():
    def __init__(self, name , amt):
        self.name=name
        self.amt=amt
    def getname(self):
        return self.name
    def getamt(self):
        return self.amt
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name,self.amt)

t1=BankAccount("Bob",100)









# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0. 


class Bike():
    def __init__(self,x,y):
        self.color=x
        self.price=y
    

testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)









# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!) 


class AppleBasket():
    def __init__(self,x,y):
        self.apple_color=x
        self.apple_quantity=y
    def increase(self):
        self.apple_quantity+=1
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)
        

p1=AppleBasket('red',3)
p2=AppleBasket('blue',49)





#The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

#Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.

#For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
      
    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

p1=Grass_Pokemon("Belle")






#Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.

#To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10.




class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    attack_boost=10
    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]


p2=Grass_Pokemon("Bulby")
p3=Grass_Pokemon("Pika")


#Ques 3

    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"
        
    def opponent(self):
        if(self.p_type=="Grass"):
            return ('Fire', 'Water')
        if(self.p_type=="Ghost"):
            return ('Dark','Psychic')
        if(self.p_type=="Fire"):
            return ("Water","Grass")
        if(self.p_type=="Flying"):
            return("Electric","Fighting")
                    
        
       
        

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
