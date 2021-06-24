# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:38:08 2021

@author: rofun
"""
import random


class Animal:
    
    def __init__(self, name, age, health=10, happiness=10):
        self.name = name
        
        self.age = age
        self.health = health
        self.happiness = happiness
        
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
        
        
        #raise NotImplementedError
        
    def display_info(self):
        print(f"{self.name} de subspecie {self.sub} edad: {self.age}, su salud es {self.health} y su felicidad es {self.happiness}")
        return self
        

class Reptile(Animal):
    
    def __init__(self, name, age, sub, health=25, happiness=20, temp=30):
        super().__init__(name, age, health, happiness)
        self.temp = temp
        self.sub = sub
    
    def feed(self):
        self.health += 10
        self.happiness += 5
        
        return self

             
    
    def activity(self):
        self.temp = random.randint(25, 38)
        print(f"la {self.sub}  {self.name} tiene una temperatura de {self.temp} C")
        
        if self.temp < 26:
            print(f"la {self.sub}  {self.name} tiene una temperatura de {self.temp} C subiremos su temperatura para que este mas comoda")
            self.temp += 3
            self.happiness + 5
            
        if self.temp > 37:
            print(f"la {self.sub}  {self.name} tiene una temperatura de {self.temp} C bajaremos su temperatura para que este mas comoda")
            self.temp -= 3
            
            self.happiness + 5
        
        return self
        
    def display_info(self):
        print(f"{self.name} de subspecie {self.sub} edad: {self.age}, su salud es {self.health}, su felicidad es {self.happiness} y su temp es :{self.temp} C")
        return self
    
    def __repr__(self):
        return self.name


class Feline(Animal):
    
    def __init__(self, name, age, sub, health=25, happiness=10):
        super().__init__(name, age, health, happiness)
        self.sub = sub
    
    def feed(self):
        self.health += 5
        self.happiness += 5
    
    def activity(self):
        print(f"{self.name} comienza a jugar con el juguete que le diste")
        self.happiness += 10
        
    def display_info(self):
        print(f"{self.name} de subspecie {self.sub} edad: {self.age}, su salud es {self.health} y su felicidad es {self.happiness}")
        return self
    
    def __repr__(self):
        return self.name
    

class Bird(Animal):
    
    def __init__(self, name, age, sub, health=10, happiness=10):
        super().__init__(name, age, health, happiness)
        self.sub = sub
    
    def feed(self):
        self.health += 10
        self.happiness += 15
        return self
    
    def activity(self):
        print(f"{self.name} juega y recibe carino de su cuidador asignado :)")
        self.happiness += 10
        
    def display_info(self):
        print(f"{self.name} de subspecie {self.sub} edad: {self.age}, su salud es {self.health} y su felicidad es {self.happiness}")
        return self
    
    def __repr__(self):
        return self.name
    
    
class Zoo():
    
    def __init__(self,name):
        self.name = name
        self.animals = []
        
   
    def add_feline(self, name, age, sub):
        self.animals.append(Feline(name, age, sub))
        return self
    
    def add_reptile(self, name, age, sub):
        self.animals.append(Reptile(name, age, sub))
        return self
   
    def add_bird(self, name, age, sub):
        self.animals.append(Bird(name, age, sub))
        return self
    
    def see_animals(self):
        for animal in self.animals:
            animal.display_info()
        return self
    
    def __repr__(self):
        return self.name


Zooint = Zoo("Buin")    



while True:
    
    
    resultado = input("que desea hacer (1:crear un ave) (2:crear un felino) (3: crear un reptil) (4:alimentar un animal) (5: ver lista de animales) (6: actividades especificas para animales) (0: para salir):\n")
    
    if resultado == "1":
        
        sub = input("escriba que tipo de ave desea:\n")
        name = input("el nombre de su ave:\n")
        age = random.randint(0, 5)
        
        Zooint.add_bird(name,age,sub)
        print("creando ave")
    
    elif resultado == "2":
        
        sub = input("escriba el tipo de felino que sea:\n")
        name = input("el nombre de su felino:\n")
        age = random.randint(0, 20)
        Zooint.add_feline(name,age,sub)
        print("creando un felino")
        
    elif resultado == "3":
        
        sub = input("escriba el tipo de reptil:\n")
        name = input("el nombre de su reptil:\n")
        age = random.randint(0,80)
        Zooint.add_reptile(name,age,sub)
        print("creando reptil")
        
    elif resultado == "4":
        
        if Zooint.animals == []:
            print("porfavor crea un animal o mas para poder alimentar")
        
        else:
            print(Zooint.see_animals())
            animalfeed = input("cual de sus animales desea alimentar? ingrese su nombre:\n")
            
            chosen = next((a for a in Zooint.animals if a.name == animalfeed), None)
            
            if chosen is None:
                print('ese animal no existe, porfavor revisa el nombre de tu animal')
                continue
            else:
                chosen.feed()
                print(chosen.display_info())
            
    elif resultado == "6":
        
        if Zooint.animals == []:
            print("porfavor crea un animal o mas")
        
        else:
            print(Zooint.see_animals())
            activity = input("con que animal deseas tener una actividad, ingresa su nombre:\n")
            
            chosen2 = next((a for a in Zooint.animals if a.name == activity), None)    
        
            if chosen2 is None:
                print('ese animal no existe, porfavor revisa el nombre de tu animal')
                continue
            else:
                chosen2.activity()
                
            
            
                                    
        
        
    elif resultado == "0":
        break
    
    elif resultado == "5":
        print(Zooint.see_animals())
    
    else:
        print("input invalido")
        
        
    