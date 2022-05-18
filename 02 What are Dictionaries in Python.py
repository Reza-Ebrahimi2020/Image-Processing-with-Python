# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:03:43 2022

@author: Reza
"""
life_sciences = {'Botany':'plants',
                 'Zoology':'animals',
                 'Cell_biology':'cells'}

life_sciences['Neuroscience'] = 'nervous_system'

d = list(life_sciences.keys()) #Save keys as a list
e = list(life_sciences.values())
print(d)
