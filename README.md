# Lottery Generator

## Description/ Motivation
This program was created to solidify python concepts such as web crawling and working with large datasets. Powerball numbers were selected for this as they have been documented since January of 2000 on the Idaho lottery website, providing a large, free, tabulated dataset to work with. In addition to web crawling this program was intended to reinforce other concepts such as compiling tabulated data, applying basic statistical analysis, and working with Excel and text documents. 

## How does it work 
The program, once ran, prompts the user on how many potential winning combinations to generate, and makes sure that a valid numeric input is entered. It will then scrape the Idaho lottery website's winning numbers for the Powerball, truncate any unwanted data (winning date), and separate individual ball values into columns from the original dataset using the *pandas* module. An excel sheet is then created using the *openpyxl* module and the created table is written into this. This lets the user perform any additional statistical analysis if desired. Basic statistical analysis is performed on each column of the created table (average and 1 sigma analysis), which is then used as bounds in a random number generator for each index value for winning number outputs. The potential winning number is then compared to all previous winning numbers to see if it has occured in the past and if so a new number is generated. Finally the number of combinations that was inputed at the beginninng of the program are inputed into a text file and shown to the user. 

## How to run it. 

Install pandas, numpy, openpyxl, and lxml using pip

```cmd
python lotteryNumbers.py
```
Provide user input on number of combinations desired
