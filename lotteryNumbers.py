#lotteryNumbers

import pandas as pd 
import numpy as np
import openpyxl, os, random, pprint
from pathlib import Path

#get user input on how many combinations they want, validate integer input
while True:
    print("How many combinations would you like?")
    num_comb = input()
    try: 
        num_comb = int(num_comb)
    except:
        print("Please use numeric digits.")
        continue
    break
# Access Idaho Lottery website
print('accessing files')
url = "https://www.idaholottery.com/games/winning-numbers-history/powerball" 

#Acess and exctract the numbers on the first page and insert into nested list
df = pd.read_html(url, index_col= 0)
df= df[0] # converts from list of Dataset to actual dataset

#separate values into columns and trim the unwated values(MP: #), drop origin column
print("Converting Data")
new = df["Winning Numbers"].str.split(" ", n = 6, expand = True) 

df["First Number"] = new[0]
df["Second Number"] = new[1]
df['Third Number'] = new[2]
df['Fourth Number'] = new[3]
df['Fifth Number'] = new[4]
df["PowerBall"] = new[5]
df.drop(columns = ["Winning Numbers"], inplace = True)

#convert dataframe object (str) to int values
df["First Number"] = pd.to_numeric(df["First Number"])
df["Second Number"] = pd.to_numeric(df["Second Number"])
df['Third Number'] = pd.to_numeric(df["Third Number"])
df['Fourth Number'] = pd.to_numeric(df["Fourth Number"])
df['Fifth Number'] = pd.to_numeric(df["Fifth Number"])
df["PowerBall"] = pd.to_numeric(df["PowerBall"])


#Create a new Excel Spreadsheet 
wb = openpyxl.Workbook()
wb.sheetnames
sheet = wb.active
sheet.title = 'Lottery Statistics'
wb.save('Lottery_Generator.xlsx')
# Insert Combinations into Excell, One number/cell, One Combination/ Row

df.to_excel('Lottery_Generator.xlsx', index = False, header = True)
wb.close()

#Designate Other Cells for Statistical Processes If needed Using further Excell Processing
print("Tabulating Winning Numbers")





# find and apply statistical data for each number
av_col = df.mean(axis=0)
std_col = df.std(axis=0)  
av_sig = []
for i in range(df.shape[1]):
    av_sig.append([round(av_col[i]), round(std_col[i])])

#loop with random number generator applying conditions: Must be within each bound, current combination
#  != any previous combination, for (user input) amount of cycles/ outputs 
print("Generating Numbers")

row_count = len(df.index)
combs_out = []
for i in range(num_comb):
    b = True
    while b:
        num_temp = []
        for k in range(len(av_sig)):
            #random combination stored in temporary var to compare to df
            num_temp.append(random.randint((av_sig[k][0] - av_sig[k][1]), (av_sig[k][0] + av_sig[k][1])))
        
        # check to see if the num-temp list matches any row in the dataframe
        if (num_temp[0] == df.iloc[i][1]) and (num_temp[1] == df.iloc[i][2]) and (num_temp[2] == df.iloc[i][3]) \
            and (num_temp[3] == df.iloc[i][4]) and (num_temp[4] == df.iloc[i][5]) and (num_temp[5] == df.iloc[6]):
            continue
        else:
            combs_out.append(num_temp)
            b = False
        

#Print Results for user into a text file, one combo/line
print("Opening file")
p = open('lottery_number_output.txt', 'w')
p.write("Possible Combinations" + "\n")
p.close()
p = open("lottery_number_output.txt", 'a')
for i in range(len(combs_out)):
    line_out = []
    line_out = combs_out[i]
    line_out = str(line_out)
    p.write(line_out + "\n")
p.close()
os.startfile("lottery_number_output.txt")