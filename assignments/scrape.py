import requests
import sys
import traceback
from selenium import webdriver as wd
import time
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def Parse_into_table(parse_string,myinput):
    alp = parse_string.find('21.3')
    
    #print(alp)
    lis = []
    #print(parse_string[189:194])
    #print(parse_string[194:])
    print("my input below")
    print(myinput)
    print(type(myinput))
    if myinput == 1:
        split_parsed_string = parse_string[196:].splitlines()
        print(split_parsed_string)
        sps = split_parsed_string
    elif myinput == 2:
        print("in numero 2")
        '''with open('input2.txt','r') as file:
            text = file.read()
            print(text)'''
        import input
        sps = input.my_list
        print(sps)

        #sys.exit(1)
    #for i in range(len(sps)):
    i = 0
    n = 0
    
    df = pd.DataFrame(columns=['first_name','lastname','Placing','country',
                               'continent','affiliate','age_and_or_height',
                              'points','21.1','21.1 time','21.2','21.2 time','21.3','21.3 time','21.4','weight'])
    matches = ['in','cm','lb','kg']
    while i+1 < len(sps):
        check = False
        checkTab = False
        if(sps[i+1] == '\t'):
            Place = sps[i] #first is rank
            print('rank is {}'.format(sps[i]))
            if i+1 < len(sps):i+=1 
            tab = sps[i]
            if i+1 < len(sps):i+=1
            first_name = sps[i]
            if i+1 < len(sps):i+=1
            last_name = sps[i]
            if i+1 < len(sps):i+=1
            print('the athlete is {} {}'.format(first_name,last_name))
            country = sps[i]
            if i+1 < len(sps):i+=1
            continent = sps[i]
            if i+1 < len(sps) and ('CrossFit' in sps[i+1] or 'Crossfit' in sps[i+1]):
                i+=1
                affiliate = sps[i]
                print('He has affiliate')
            elif i+1 < len(sps) and 'Age' not in sps[i+1]:
                i+=1
                affiliate = sps[i]     
            else:
                affiliate = None
                print('{} has no affiliate'.format(first_name))
                #i -= 1 #I think this is wrong
             
            if i+1 < len(sps):i+=1
            age = sps[i]
            print("age is {}".format(age))
            if i+1 < len(sps) and any(x in sps[i+1] for x in matches):#'cm' in sps[i+1] ||if 'in' in sps[i+1] || 'kg' in sps [i+1] || 'lbs'in sps[i+1]:
                i+=1
                age_and_or_height = sps[i]
                print("height and weight {}".format(age_and_or_height))
            else:
                age_and_or_height = None
            
            if i+1 < len(sps):i+=1
            vp = sps[i]
            if i+1 < len(sps):i+=1
            tab = sps[i]
            if i+1 < len(sps):i+=1
            points = sps[i]
            if i+1 < len(sps):i+=1
            tab = sps[i]
            
            if i+1 < len(sps):i+=1
            ###Maybe while loop start
            for j in range(4):
                checkTab=False
                WO = sps[i]
                print("workout is {}".format(WO))
                if j == 0:
                    firstWO = WO;
                    rept1 = None
                elif j == 1:
                    secondWO = WO;
                    rept2 = None
                elif j == 2: 
                    thirdWO = WO;
                    rept3 = None
                elif j == 3:
                    fourthWO = WO;
                    rept4 = None
                #print('workout score {} of workout no {}'.format(WO,j))
                
                if i+1 < len(sps):i+=1
                
                
                if 'front squats' in sps[i]:
                    #print("following is front squats")
                    #print(sps[i])
                    while i+1 < len(sps) and 'Tiebreak'not in sps[i+1]:
                        i+=1
                    if i+1 < len(sps):i+=1
                elif 'snatches' in sps[i]:
                    #print("following is snatches")
                    #print(sps[i])
                    while i+1 < len(sps) and 'Tiebreak'not in sps[i+1]:
                        i+=1
                    if i+1 < len(sps):i+=1
                elif 'wall walk' in sps[i]:
                    #print("following is wall walk")
                    #print(sps[i])
                    while i+1 < len(sps) and 'Tiebreak'not in sps[i+1]:
                        i+=1
                    if i+1 < len(sps):i+=1
                elif 'bear crawl' in sps[i]:
                    while i+1 < len(sps) and 'Tiebreak'not in sps[i+1]:
                        i+=1
                    if i+1 < len(sps):i+=1
                
                elif '--'in WO:
                    print("User DID NOT log workout {} placinb is Next Line".format(j))
                    rep_or_time = WO
                    if j == 0:
                        rept1 = None
                        #firstWO = None
                    elif j == 1:
                        rept2 = None
                        #secondWO = None
                    elif j == 2:
                        rept3 = None
                        #thirdWO = None
                    elif j == 3:
                        rept4 = None
                        #fourth = None
                    print(rep_or_time)
                
                    #while i+1 < len(sps) and not(sps[i].isnumeric()):
                     #   l = 12
                        #print("{} is not numeric so keep going".format(sps[i]))
                                        
                    while i+1 < len(sps) and ('\t' != sps[i] and sps[i] != ''):
                        print("while in while loop or -- sps[i] = {}".format(sps[i]))
                        if sps[i] == '\t':
                            print("it is tab")
                        if sps[i] == '':
                            print(" it is a empty string")
                        i+=1
                    #print("sps now before empty string check {}".format(sps[i]))
                   
                        
                    if i+1 < len(sps) and sps[i] == '':
                        while i+1 < len(sps) and not(sps[i].isnumeric()):
                            print("{} is not numeric so keep going".format(sps[i]))
                            checkTab = True
                            i+=1
                        if i+1 < len(sps) and (checkTab == True and sps[i+1] == '\t'):
                            i+=1
                        '''print("in -- I got a nul char \n")

                        if i+1 < len(sps) and (sps[i]=='' and sps[i+1]!=''):
                            ############
                            if i+1 < len(sps) and'Judged by' in sps[i+1]:
                                print('following is judged by in (--) {}'.format(sps[i+1]))
                                i+=1
                            if i+1 < len(sps) and '\t' in sps[i+1]:
                        #print(sps[i])
                                checkTab = True
                                if i+3 < len(sps):i+=3
                            elif i+1 < len(sps) and ''==sps[i+1]:
                                checkTab = True
                                print("empty spce after judged by in (--) {}".format(sps[i+3]))
                                if i+4 < len(sps):i+=4
                            ###########
                        elif i+3 < len(sps) and sps[i+3] == '': #if there are 4 consecutive empty strings
                            checkTab=True
                            i+=5

                        elif i+2 < len(sps) and sps[i+2] == '': #if there are three consecutive empyt strings
                            checkTab = True
                            i+=4
                            print("the next 2 one is {}".format(sps[i]))
                        else:
                            checkTab = True
                            i+=3
                            print("the next one is {}".format(sps[i]))

                        

                    #if 'reps' in sps[i]:
                     #   if i+1 < len(sps): i+=1
                    #if 'Tiebreak' in sps[i]:
                     #   if i+1 < len(sps): i+=1'''

                    if i+1 < len(sps):
                        i-=1
                        print("subtracting sps[i]= {} sps[i-1]={} sps[i+1]={}".format(sps[i],sps[i-1],sps[i+1]))
                        if i+3 < len(sps): print("sps[i+2] ={} sps[i+3] = {}".format(sps[i+2],sps[i+3]))


                elif 'squats' in sps[i]:
                    while i+1 < len(sps) and 'Tiebreak'not in sps[i+1]:
                        i+=1
                    if i+1 < len(sps):i+=1
                   
                elif i+1 < len(sps) and 'Tiebreak' in sps[i]: #if i get rid of this tie break will be the score i think
                   # print('if this tie break {} and folliwng below'.format(sps[i]))
                    #i+=1
                    TieBreak_wkot3 = sps[i]
                    #print(sps[i])
                else:
                   # print('workout {} was completed there score is below'.format(j))
                    rep_or_time = sps[i]
                    if j == 0:
                        rept1 = rep_or_time
                        #firstWO = None
                    elif j == 1:
                        rept2 = rep_or_time
                        #secondWO = None
                    elif j == 2:
                        rept3 = rep_or_time
                        #thirdWO = None
                    elif j == 3:
                        rept4 = rep_or_time
                        #fourth = None
                    #print(rep_or_time)
                    if i+1 < len(sps) and 'Tiebreak' in sps[i+1]:
                        #print("tiebreak after completion")
                        i+=1
                    #if i+1 < len(sps):print('this is what followed after the score: {} for workout {}'.format(sps[i+1],j))
                if i+1 < len(sps) and'Judged by' in sps[i+1]:
                    #print('following is judged by 1')
                    i+=1
                    #print(sps[i])

                    if i+1 < len(sps) and '\t' in sps[i+1]:
                        #print(sps[i])
                        if i+2 < len(sps):i+=2
                        
                    elif i+1 < len(sps) and ''==sps[i+1]:
                        if i+3 < len(sps):i+=3

                elif (i+1 < len(sps) and '\t' == sps[i+1]) or ('\t'==sps[i] and '- s' in WO):
                    print("initial tab but check false \n")
                    
                    if checkTab == False: #'Judged by' not in sps [i+1]:
                        if '\t'==sps[i] and '- s' in WO:
                            i-=1
                        print('there was an initial tab and a false')
                        tab = '\t'
                        if i+2 < len(sps):i+=2
                    
                elif i+1 < len(sps) and ''== sps[i+1]:
                    if check == True:
                        print("the check was true \n")
                    if check == False:
                        print('I got a supposed three space')
                        if i+3 < len(sps):i+=3
                
            
            print('last thing captured in for loop before added to list {}'.format(sps[i]))
            mylist = [first_name,last_name,Place,country,continent,age,affiliate,age_and_or_height,
                      points,firstWO,rept1,secondWO,rept2,thirdWO,rept3,fourthWO,rept4] 
            #df.loc[len(df)] = mylist
            lis.append(mylist)
            #print('{} first name {} last name {}'.format(first_name,last_name,firstWO) )
            #print(j)
            #n+=1
            #if n == 3:
            #    print('returnning')
        #print("last thing captured {}".format(sps[i]))
    return lis


#print(sys.platform)
parse_this = ''
if sys.platform == "linux":
    PATH = "/home/branchmanager/Documents/MatPlotLib/chromedriver"
    secs = 5
else:
    PATH = "/Users/noahbranch/Documents/CodeAndDev.nosync/Chrome_Driver/chromedriver"
    secs = 20
#URL = 'https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=2284'
#URL = 'https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=1685'
#URL = 'https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=1625'    
#URL = 'https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=1077'   
#URL = 'https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=760'
URL="https://games.crossfit.com/leaderboard/open/2021"
#URL="https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=2361"
#URL="https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=2062"
#URL = "https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=482"
#URL="https://games.crossfit.com/leaderboard/open/2021?view=0&division=1&region=0&scaled=0&sort=0&page=760"

myinput = int(input("1. Scrape website \n2. Read file \n"))
if myinput == 1:
    driver = wd.Chrome(executable_path = PATH)


columns=['first_name','lastname','Placing','country',
                               'continent','Age','affiliate','Height and Weight',
                              'points','21.1','21.1 time','21.2','21.2 time','21.3','21.3 time','21.4','weight']

MyMainList = []
THE_list = []

if myinput == 1:
    driver.get(URL)

    time.sleep(secs)

try:
    
    #myinput = input("1. Scrape website \n 2. Read file")
    if myinput == 1:
        print(type(driver))
        close = driver.find_element_by_css_selector('.mc-closeModal')
        accept = driver.find_element_by_css_selector('.btn.btn-callout.btn-privacy-policy-accept')
        accept.click()
        close.click()
    

    i = 0
    for i in range(0,2750):
        print("index is now {}".format(i))
        if myinput == 1: 
            thirdDiv = driver.find_element_by_id('leaderboardSponsorVisible')
            table_class = thirdDiv.find_element_by_xpath("//table[@class='desktop athletes']")

        #print(thirdDiv.text)
        #print(table_class.get_attribute('innerText'))
            parse_this = table_class.get_attribute('innerText')
        MyMainList.extend(Parse_into_table(parse_this,myinput))

        print('I have ReTuNeD!')

        #if myinput == 2:
        #    sys.exit(1)
        #display(table)
        #df.append(table)
        #df1.append(df2)
        #display(df)
        #print(*MyMainList, sep = ", ") 
        if myinput == 1:
            footer = driver.find_element_by_css_selector('.desktop.footer')
            nums = footer.find_element_by_css_selector('.nums')
            active = nums.find_element_by_css_selector('.active')
            lets_look = active.get_attribute('innerText')
            if lets_look == '2750':
                break
            print(lets_look)

        if myinput == 1:
            time.sleep(5)
            button = driver.find_element_by_css_selector('.btn.next')

        #print(button.get_attribute('innerHTML'))
            button.click()
            time.sleep(5)
            print(driver.current_url)
    #df.loc[len(df)] = MyMainList
    THE_list.append(MyMainList)
    print(*THE_list,sep=", ")
    df = pd.DataFrame(MyMainList,columns=['first_name','lastname','Placing','country',
                               'continent','Age','affiliate','Height and Weight',
                              'points','21.1','21.1 time','21.2','21.2 time','21.3','21.3 time','21.4','weight'])
    df.to_csv("men_open_21.1.csv",columns = columns)
    if myinput == 2:
        sys.exit()
    #for i in MyMainList:
    #    if len(i) == 16:
     #       df.append(i)
     #       print("The length is {}".format(len(i)))
      #  else:
       #     print("NOT WORKING OUT")
        #    print(*i, sep = ", ") 
    display(df)
except Exception as e:
    e = sys.exc_info()
    print('Error Return Type: ', type(e))
    print('Error Class: ', e[0])
    print('Error Message: ', e[1])
    print('Error Traceback: ', traceback.format_tb(e[2]))
    if 'ERR_INTERNET_DISCONNECTED' in traceback.format_tb(e[2]):
        sys.exit(1)
    else:
        print('weon keepit spinin')
    
    #sys.exit(1)
        #print(webpage.text)
