#Inheritance in python

from chef import chef #importing class chef
from chinesechef import chinesechef #importing class chinesechef

mychef = chef()
mychef.make_chicken()

mychinesechef = chinesechef() #creating object of chinesechef
mychinesechef.make_salad() #accessing function make salad from chinese chef