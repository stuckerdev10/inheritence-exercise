#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Animal:
    def __init__(self, name, species_name, species_classification, weight):
        self.__name = name
        self.__species_name = species_name
        self.__species_classification = species_classification
        self.__weight = int(weight)
        
    @property
    def name(self):
        return self.__name
    
    @property
    def species_name(self):
        return self.__species_name
    
    @property
    def species_classification(self):
        return self.__species_classification
    
    @property
    def weight(self):
        self.__weight = int(self.__weight)
        return self.__weight
    
    def eat(self, food):
        print(f"You ate the {food}.")
        
    def move(self):
        print(f"You moved.")
   
    def die(self):
        print("You are dead.")
        
        


# In[24]:


class Fish(Animal):
    
    def __init__(name, species_name, species_classification, weight,                 water_body, sea_level):
        super().__init__(name, species_name, species_classification, weight)
        self.__water_body = water_body
        self.__sea_level = sea_level
        
    @property
    def water_body(self):
        return self.__water_body
    
    @property
    def sea_level(self):
        return self.__sea_level
    
    def swim(self):
        print("You are swimming")
        
    def bite(self):
        print("You bit at something")


# In[29]:


class Snake(Animal):
    def __init__(self, name, species_name, species_classification, weight,                location, venom_content, length):
        super().__init__(name, species_name, species_classification, weight)
        self.__location = location
        self.__venom_content = int(venom_content)
        self.__length = float(length)
    
    @property
    def location(self):
        return self.__location
    
    @property
    def venom_content(self):
        return self.__venom_content
    
    @property
    def length(self):
        return self.__length
    
    
    def bite(self):
        print("You took a bite")
    def shed(self):
        print("You shed your skin")


# In[49]:


class Human(Animal):
    def __init__(self, name, species_name, species_classification, weight,                height, location):
        super().__init__(self, name, species_name, species_classification, weight)
        self.__height = int(height)
        self.__location = location
      
    @property
    def height(self):
        return self.__height
    
    @property
    def location(self):
        return self.__location
    
    
    def run(self):
        print("You began to run")


# In[50]:


class Book:
    def __init__(self, title, author, page_length, year, publisher):
        self.__title = title
        self.__author = author
        self.__page_length = int(page_length)
        self.__year = year
        self.__publisher = publisher
        
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    
    @property
    def page_length(self):
        return self.__page_length
    
    @property
    def year(self):
        return self.__year
    
    @property
    def publisher(self):
        return self.__publisher
    
    
    
    def openBook(self):
        print("You opened the book")
        
    def closeBook(self):
        print("You closed the book")
        
    def pageForward(self):
        print("you went a page ahead")
        
    def pageBackwards(self):
        print("you went a page backwards")
        
    def readPage(self):
        print("You read a page")


# In[54]:


class Textbook(Book):
    def __init__(self, title, author, page_length, year, publisher,                topic, education_level):
        super().__init__(self, title, author, page_length, year, publisher)
        self.__topic = topic
        self.__education_level = education_level
        
    @property
    def topic(self):
        return self.__topic
    
    @property
    def education_level(self):
        return self.__education_level
    
    
    def quiz(self):
        print("You began a quiz from the textbook")


# In[58]:


class AddressBook(Book):
    def __init__(self, title, author, page_length, year, publisher,                location, address_types):
        super().__init__(self, title, author, page_length, year, publisher)
        self.__location = location
        self.__address_types = address_types
    
    @property
    def location(self):
        return self.__location

    @property
    def address_types(self):
        return self.__address_types

    def listAddresses(self):
        print("Here are the addresses:")


# In[59]:


class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    def accelerate(self):
        print("You began to accelerate")
    def decelerate(self):
        print("You began to decelerate")
    def forward(self):
        print("You shifted forward")
    def backwards(self):
        print("You shifted reverse")


# In[60]:


class Car(Vehicle):
    def __init__(self, make, model, year,                car_type, engine, mileage):
        super().__init__(self, make, model, year)
        self.__car_type = car_type
        self.__engine = engine
        self.__mileage = int(mileage)
        
    @property
    def car_type(self):
        return self.__car_type
    
    @property
    def engine(self):
        return self.__engine
    
    @property
    def mileage(self):
        return self.__mileage
    
    
    def start(self):
        print("You started the car")
    def stop(self):
        print("you stopped the engine")


# In[63]:


class Bicycle(Vehicle):
    def __init__(self, make, model, year,                speeds, bike_type):
        super().__init__(self, make, model, year)
        self.__speeds = int(speeds)
        self.__bike_type = bike_type
        
    @property
    def speeds(self):
        return self.__speeds
    
    @property
    def bike_type(self):
        return self.__bike_type
    
    def shift(self):
        print("You shifted up a gear")


# In[64]:


class Boat(Vehicle):
    def __init__(self, make, model, year,                boat_type):
        super().__init__(self, make, model, year)
        self.__boat_type = boat_type
        
    @property
    def boat_type(self):
        return self.__boat_type
    
    def sail():
        print("You began to sail")
        


# In[65]:


class HotAirBaloon(Vehicle):
    def __init__(self, make, model, year,                baloon_size):
        super().__init__(self, make, model, year)
        self.__baloon_size = baloon_size
        
    @property
    def baloon_size(self):
        return self.__baloon_size
    
    def elevate(self):
        print("The baloon went up")
    def de_elevate(self):
        print("The baloon went down")


# In[ ]:




