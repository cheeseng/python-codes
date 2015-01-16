#! /usr/bin/python
"""
Code to split html tables to make one table per row
Used for kindle where large tables are partially omitted
"""
from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='File', help='path of html file')
args = parser.parse_args()
 
f = open(args.file)
arr = f.read()
f.close()
soup = BeautifulSoup(arr)
tl = soup.find_all('table')
for t in tl:
    tr = t.find_all('tr')
    temp = []
    for row in tr[1:]:
        temp.append(row.extract())
    temp.reverse()
    for row in temp:
        st = BeautifulSoup(str(t))
        l = st.find_all('caption')
        for c in l:
            c.extract()
        st.tr.replaceWith(row)
        t.insert_after(st.table)
f = open(args.file, 'w')
f.write(str(soup))
f.close()
