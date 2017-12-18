#created by Matthew Walsh
#created for ics3u
#created on dec 2017
#address program

from enum import Enum

Street = Enum('ST', 'DR', 'AVE', 'CRES', 'GRV')

class Address():
      def __init__(self, house_number, street_name, street_type):
          
          self.house_number = house_number
          self.street_name = street_name               
          self.street_type = street_type  
      
      def street_address(self):
          
          self.street_name = (address.house_number + ' ' + address.street_name + ' ' + address.street_type)
          
          return self.street_name                                                                          
           
house_number = raw_input("What is their house number? ")
house_number = house_number.upper()      
street_name = raw_input("What is the name of the street? ")
street_name = street_name.upper()    
street_type = raw_input("What is their street type? ")  
street_type = street_type.upper()  
while street_type not in Street:
    street_type = raw_input("Please enter their street type. (ex: Dr) ")     
    street_type = street_type.upper()
            
address = Address(house_number, street_name, street_type)

print(address.street_address())                
