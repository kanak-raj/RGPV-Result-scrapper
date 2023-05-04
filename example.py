'''
This file demonstrates the usage of the tool.
'''

import rgpvscrape as r

r.scrape(college_code='0157',
         branch='CS',
         year=19,
         roll_num_range=(1000, 1150),
         sem=7)
