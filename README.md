# VacationFinder
Tool to search and find when new vacations have been added to a website. Sends a text notification to user when more vacations added detected.

## Python Version:  
- 3.9  
 
## Current supported emails:  
- gmail  
 
## Current supported phone carriers:  
- att  
- tmobile  
- verizon  
- sprint  
- virgin  
- boost  
- cricket  
- metro  
- us cellular  
- xfinity  

## One time setup:  
- add settings to config.ini  
- sign in to your gmail account  
- turn allow less secure apps to ON using the link below  
   https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NLknQ0n1ii0IaCeaXqFEZ1ros8GARoX3lNhSHDcnWE81APVGwMdVot0UQVbzPiz5XYrxtccBkVXJTXcDW0dCBphk4Svw
   
- open terminal -> cd into project directory -> pip3 install -r requirements.txt  

 
## How to use:  
- run main.py  

## Automatically run on raspberry pi:  
- copy VacationFinder folder to raspberry pi desktop  
- right click 'vacationfinder.sh' -> properties -> permissions tab -> set all permissions to 'anyone'  
- type 'crontab -e' in terminal  
- add '0,30 9-21 * * 5,6,0 /home/pi/Desktop/VacationFinder/src/vacationfinder.sh' to bottom  
- ctrl + s  
