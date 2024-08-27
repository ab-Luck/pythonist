# class Vehicle():
#     def __init__(self,name,speed,milage,model):
#         self.name=name 
#         self.speed=speed
#         self.milage=milage
#         self.model=model 
#     def tyres(self,tyres):
#         return f'{self.name} has {tyres} tyres'
#     def color(self,color):
#         return f'{self.name} has {color} color'
# class Mini(Vehicle):
#     def __init__(self,name):
#         self.name=name        
# v=Vehicle('honda civic',280,'5500km',2023)
# print(f'car name: {v.name.title()} model is: {v.model} and its speed is: {v.speed} with milage: {v.milage.title()} {v.color("silver")}')    
# m=Mini('minicivic')
# print(f'{m.name} is actually belongs to the family {v.name.title()} but it does not mean that its speed is {v.speed}')

class Vehicle:
    def __init__(self, name, staff, capacity):
        self.name = name
        self.staff = staff
        self.capacity = capacity

    def fare(self):
        return self.capacity * 1200
    def expense(self):
        return f/self.staff
        

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 3, 46)
f=bus.fare()
print(f'total fare is: {f}')
be=bus.expense()
print(f'expenses are {be}')
tf=f-be
print(f'Profit: {tf}')
