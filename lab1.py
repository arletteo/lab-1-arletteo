#* Section 1 (Git)
  #persnickety
#* Section 2 (Data Definitions)

#* 1)
#celcius is a measurement of temperature in degrees celcius
#farenheit is a measurement of temperature in degrees farenheit
def convert_celcius_to_farenheit(celcius):
    farenheit = (celcius *(9/5)) + 32
    return farenheit

#* 2)
#a Price is a number representing the price of an item in cents

#* 3)
#a PriceRecord is an object representing an item in a store
# a Name is a string representing the name of an item 
class PriceRecord:
      def __init__(self, name, price):
          self.name = name #a Name
          self.price = price # a Price
      def __repr__(self):
          return ("Item name: %r Item Price: %r" %(self.name, self.price))
      def __eq__(self, other):
          return self.name = other.name and self.price = other.price
#* 4)
#a Tab is an object that contains information about an open tab
#a URL is a string representing the URL of the website open in a a tab 
#a date is a string representing the most recent date the url was visited
class Tabs:
      def __init__(self, url, date):
          self.url = url #a URL
          self.date = date #a Date
      def __repr__(self):
          return ('Tab URL: %r Most recently visited on %r' %(url, date))
      def __eq__(self, other):
          return self.url = other.url and self.date = other.date

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)
# takes the price of an item as a parameter and returns the price plus tax
# float ---> float
def add_tax(price):
    tax = price* .875
    return price + tax

#* 2)
#takes the name of an item and returns the price of the item 
# string list --> float
def find_item_price(item_name, store_database):
    for item in store_database:
        if item_name == item.name:
           return item.price

#* 3)
#takes a region and calculates the average income of the region
#string list --> int 
def med_income(geo_region, database):
    pass 
    
#* 4)
#takes a region and returns a list of cities that overlap with the region
#string list --> list 
def overlaping_cities(region, database): 
    pass 

#* Section 4 (Test Cases)

#* 1)
import unittest

class TestCases (unittest):
      def test_1(self):
          self.assertEqual(second_largest(1,2,3), 2)
      def test_2(self):
          self.assertEqual(second_largest(2,2,2),2)
          
if __name__ == '__main__':
   unittest.main()

#* 2)
import unittest 

class TestCases(unittest):
      def test_1(self):
          self.assertTrue(no_capitals('blah'))
      def test_2(self):
          self.assertFalse(no_capitals('Fajnfej'))
if __name__ == '__main__':
   unittest.main()

#* 3)
import unittest

class TestCases(unittest):
      def test_1(self):
          self.assertEqual(northernmost('San Diego', 'Los Angeles'), 'Los Angeles')
      def test_2(self):
          self.assertEqual(northernmost('Tijuana', 'San Diego'), 'San Diego')
if __name__ == '__main__':
   unittest.main()


#* Section 5 (Whole Functions)

#* 1)
#takes a measurment in feet and returns the measurement in meters
#float --> float
def feet_to_meters(length):
    return length*0.3048

#* 2)
class MusicalNote:
    def __init__(self, frequency, duration):
         self.frequency = frequency
         self.duration = duration 
    def __repr__(self):
        return (('Frequency: %r Duration: %r) %(self.frequency, self.duration))
          

#* 3)
def up_an_octave(note):
    
    

#* 4)

