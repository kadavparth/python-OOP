class Calorie:
    """Represents amount of calories calculated with
    BMR = 10*weight + 6.25*height -5*age + 5 - 10*temperature
    """
    def __init__(self,weight,height,age,temperature):
        self.temperature = temperature
        self.height = height
        self.age = age
        self.weight = weight

    def calculate(self):
        result = 10*self.weight + 6.25*self.height - \
                 5*self.age + 5 - 10*self.temperature
        return result

class Temperature:

    """
    Data collected from timeanddate.com/weather
    """

    def __init__(self,country,city):
        self.country = country
        self.city = city

    def get(self):
        temp = 13.0
        return temp

if __name__ == '__main__':
    temperature = Temperature('usa','kalamazoo').get()


