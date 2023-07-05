# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:10:40 2023

@author: Gustavo
"""

stats = {'key1':20, 'key2':35, 'key3': 44}
max_key = max(stats.items(), key=operator.itemgetter(1))[0]
print(max_key)