#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


dict1={}
dict1 = {"TOI": [3, 3, 3, 3, 3, 5, 6],
         "Hindu" : [2.5, 2.5 ,2.5 ,2.5 ,2.5, 4 ,4],
         "ET":[4, 4 ,4 ,4 ,4 ,4,10],
         "BM":[1.5 ,1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
         "HT":[2 ,2 ,2 ,2 ,2 ,4, 4]
        }


# In[4]:





# In[5]:



def CalculateSubscription(NewspaperName):
    WeeklyPrice = []
    WeeklyPrice = dict1[NewspaperName]
    TotalAmount=0
    for i in WeeklyPrice:
        TotalAmount += i
    return TotalAmount


# In[6]:


SubscriptionDict = {}
SubscriptionDict["Hindu"] = CalculateSubscription("Hindu")
SubscriptionDict["TOI"]=CalculateSubscription("TOI")
SubscriptionDict["ET"]=CalculateSubscription("ET")
SubscriptionDict["BM"]=CalculateSubscription("BM")
SubscriptionDict["HT"]=CalculateSubscription("HT")


# In[ ]:


SubscriptionDict
Inputdata = int(input("Enter The Amount"))
list1 = []
for data in SubscriptionDict:
    tempdata = 0
    while  tempdata<SubscriptionDict[data]:
        if(SubscriptionDict[data] < Inputdata) :
            list1.append(data)
            tempdata= Inputdata - SubscriptionDict[data]
        
    print(list1)
        
    

    


# In[11]:





# In[13]:





# In[ ]:




