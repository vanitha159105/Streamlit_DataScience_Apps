
# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 

# Data Pkgs
import pandas as pd 
import numpy as np


from collections import OrderedDict

from faker import Faker


# Utils
import base64
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")

scores = {'Zone': ['North','South','South',
                   'East','East','West','West','West','West'], 
          'School': ['Rushmore','Bayside','Rydell',
                     'Shermer','Shermer','Ridgemont',
                     'Hogwarts','Hogwarts','North Shore'],             
          'Name': ['Jonny','Joe','Jakob', 
                   'Jimmy','Erik','Lam','Yip','Chen','Jim'], 
          'Math': [78,76,56,67,89,100,55,76,79],
          'Science': [70,68,90,45,66,89,32,98,70]}
df = pd.DataFrame(scores, columns = 
                  ['Zone', 'School', 'Name', 
                   'Science', 'Math'])
df
	        
		
		


		

if __name__ == '__main__':
	main()



