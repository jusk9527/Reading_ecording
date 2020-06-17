# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

import csv
path = "./stocks.csv"
with open(path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

# ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
# ['AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500']
# ['AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000']
# ['BA', '98.31', '6/11/2007', '9:36am', '+0.12', '104800']
# ['C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900']
# ['CAT', '78.29', '6/11/2007', '9:36am', '-0.23', '225400']


# better
from collections import namedtuple
with open(path) as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple("Row", headings)
    for r in f_csv:
        row = Row(*r)
        print(row)