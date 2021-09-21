# GoogleMapsScrapper
 A google maps search scrapper algorithm uses python selenium and bs4

# Author : [Efe Akaröz](https://github.com/KentelDevelopment)

# Setup
- Download and install [python3](https://www.python.org/)
- Download the chromedriver and put it in the path

       #Don't forget to put this path in to when query pops up
- And run command at cmd or bash 

           python3 main.py

# How to use
        [?] Use default files or enter filename[y/*]:
- Just enter "y" for using default txt files(2) or if you want to put in a different one just hit enter and wait for other inputs

When you hit "y"
----------------
It wil automatically open the files which is in folder 
        cities.txt
        keywords.txt
        
When you hit except "y"
----------------------
It will ask for filenames
         [?]Enter Filename for 'cities' :
         [?]Enter Filename for 'keywords' :
You can put in just filename before .txt as "*" or if you want you can write "*.txt"

        [?] Country Name :
- Put in a country name for cities

Algorithm will search for "{city} {keyword} {country}"

        [?] Enter the output filename:
- Just put in the output like this: "*.xlsx" you gonna enter just "*"

       [?]Chrome driver path:
-Enter the chromedriver path if you put the driver into the folder you need to put in "./<driver_filename>" to the query

        [?] Do you want to see the output[y/*]
- If you want to see window and print exctracted data just put in "y" else put in any chars



