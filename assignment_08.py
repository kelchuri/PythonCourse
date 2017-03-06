__author__ = 'Kalyan'

from placeholders import *

# write a class Person with attributes name, age, weight (kgs), height (ft) and takes
# them through the constructor and exposes a method get_bmi_result()
# which returns one of "underweight", "healthy", "obese"
# http://en.wikipedia.org/wiki/Body_mass_index

class Person:

  def __init__(self,name,age,height,weight):
       self.name=name
       self.age=age
       self.height=(height)
       self.weight=weight

  def get_bmi_result(self):
         a=int(self.height)
         b=int(self.weight)
         d=float(a*0.3048)
         e=d**2
         bmi=float(b/e)
         if (bmi<18.5):
             return "underweight"
         elif (bmi>25):
               return "obese"
         else:
             return "healthy"





def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()


three_things_i_learnt = """
-using constructors for initializing the values
-accessing the values in other functions
-performing various operations on the arguments
"""

time_taken_minutes = 30

