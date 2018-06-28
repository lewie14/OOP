#----------------data types ----------------------------


print(type(5))

my_dict ={}

print(type(my_dict))

my_list = []

print(type(my_list))

#--------------Define a class ------------------------
class Facade:
  pass
  
facade_1 = Facade()

facade_1_type = type(facade_1)

print(facade_1_type)

# --------------Class Variables-------------------------
class Grade:
  minimum_passing = 65
  
  
#-------------------Methods-------------------------------
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
    
#-------------------Methods with arguments-------------------------------

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)

#-------------------Constructors------------------------------

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

class Shouterr:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouterr("shout")
# prints "SHOUT"

shout2 = Shouterr("shout")
# prints "SHOUT"

shout3 = Shouterr("let it all out")
# prints "LET IT ALL OUT"

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

#-------------------Instance Variables------------------------------

class FakeDict:
  pass
  
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#-------------------Attribute Functions------------------------------

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value


#For every element in the list, check if the element has the attribute count. 
#If so, count the number of times the string "s" appears in the element. Print this number.

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))


#-------------------Self------------------------------
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#----------Everything is an Object------------------
print()
print(dir(5))
print()

def this_function_is_an_object(first,second):
	return first
print(dir(this_function_is_an_object))
print()

class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))

print()
print("--------------------")

fun_list = [10, "string", {'abc': True}]

print(type(fun_list))
# Prints <class 'list'>

print(dir(fun_list))

#-------------String representation----------------
print()

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

#-------------review-----------------------
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
