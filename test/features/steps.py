# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Factorial import Factorial

@step(u'Given I have the number (\d+)')
def given_i_have_the_number_0(step, number):
    world.number = int(number)

@step(u'When I compute its factorial')
def when_i_compute_its_factorial(step):
	fact=Factorial()
	world.number = fact.get_factorial(world.number)
	
@step(u'Then I see the number (\d+)')
def then_i_see_the_number_1(step, expected):
    assert world.number == int(expected)
