#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:49:37 2018

@author: kritika 
"""

import string
import statistics
import ijson


#counting registered years

def User_each_year():

    count_yr={}

    with open('users-1.json', 'rb') as data:
        for obj in ijson.items(data, 'item'):
            if (obj['registered'][0:4]) not in count_yr:
                count_yr[(obj['registered'][0:4])] = 1
            else:
                count_yr[(obj['registered'][0:4])] +=1

    return count_yr



#Median for Number of Friends

def Median_num_frnd():

    frnd = []
    with open('users-1.json', 'rb') as data:
        for obj in ijson.items(data, 'item'):
            frnd.append(len(obj['friends']))
    median_frnd = statistics.median(frnd)
    return median_frnd



#age for users and their median

def Median_age():

    age_user =  []
    with open('users-1.json', 'rb') as data:
        for obj in ijson.items(data, 'item'):
            age_user.append((obj['age']))
    median2= statistics.median(age_user)

    return median2



#balance amount and their mean

def bal_mean():

    bal = []
    with open('users-1.json', 'rb') as data:
        for obj in ijson.items(data, 'item'):
            bal.append((obj['balance']))


    for k in range(len(bal)):
        for c in string.punctuation:
            if c == ',':
                bal[k]= bal[k].replace(c,"")
                bal[k]= bal[k][1:]

    #mean amount
    amt=[]
    for i in range(len(bal)):
        amt.append(float(bal[i]))
        mean_amt = round(sum(amt)/len(bal),2)

    return mean_amt



# Mean for number of Unread messages for Active females

def Mean_unrd_msg():

    unread_msg_act_fe = []
    with open('users-1.json', 'rb') as data:
        for obj in ijson.items(data, 'item'):
            if (obj['gender']) == 'female' and (obj['isActive']) == True:
                unread_msg_act_fe.append(int((obj['greeting']).split()[-3]))
        mean_unread_msg = round(sum(unread_msg_act_fe)/len(unread_msg_act_fe),2)

    return mean_unread_msg



def print_summary():
    x = User_each_year()
    y = Median_num_frnd()
    z = Median_age()
    q = bal_mean()
    w = Mean_unrd_msg()
    print("user registered in each year", x)
    print("meadian for numbr of frnds", y)
    print("median age for users", z)
    print("mean balance amount", q)
    print("mean for numbr of unread msg for active females", w)
    
    


