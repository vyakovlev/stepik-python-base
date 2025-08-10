rem @echo off
for /L %%i in (1,1,11) DO type %%i.txt | python 5.6.4.py
