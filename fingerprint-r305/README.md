R305 UART Fingerprint Module Python Code
========================================
This is a simple script to use R305 UART fingerprint module. 
This code is especially useful for raspberry pi where direct UART pins are 
available, though I have tested on my PC with PL2303 converter.

Enroll
------
For enroll script, there is a variable `id` which assigns id to enrolled print.
Change that code to dynamically assign id.

Search
------
In search code, only ids from 0 to 5 are searched. change last four entries 
(16 bit int) in `data` list in search function to change it.
