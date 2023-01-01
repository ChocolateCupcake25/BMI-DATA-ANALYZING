#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : Ziyah Virani//Firece Bird")
print("This is a CSV of more than 1300 rows which has bmi data.")
print("The task is to find out what is the percentage of people who are underweight and healthy. And plot a pie chart around it")
print("Another task is to find out what is the percentage of male and female who are underweight and healthy. And plot a pie chart around it")


# In[2]:


#BMI Data

#predefine code
import pandas as pd
import matplotlib .pyplot as plt

dataframe = pd.read_csv("bmi.csv")
df = dataframe.dropna()
bmi = df['bmi']
df


# In[13]:


#Task 1
#How many people are underweight and create a dataframe out of it
uw_df=df.loc[bmi>18.5]['gender'].reset_index(name='gender')
print(uw_df)
uw_count=uw_df['index'].count()
print(uw_count)


# In[29]:


#Task 2
#How many people have normal weight and create a dataframe out of it
hw_df=df.loc[(bmi>18.5) & (bmi<24.9)]['gender'].reset_index(name="gender")
print(hw_df)
hw_count=hw_df['index'].count()
print(hw_count)


# In[34]:


#Task 3
#Plot a pie chart as per the percentage of people who are underweight and healthy. 
print("The percentage of people who are underweight and healthy.")
percentage = [uw_count,hw_count]
print(percentage)
percenatge_labels = ['Underweight%','Healthy%']
print(percenatge_labels)
value=percentage
label=percenatge_labels
plt.pie(value,labels=label,autopct="%0.1f%%",radius=2)
plt.show()


# In[35]:


#Task 4
#Group by the gender from underweight dataframe and create another data frame out of it
group_underweight=uw_df.groupby('gender')['gender'].count().reset_index(name='number')
print(group_underweight)


# In[36]:


#Task 5
#Plot a pie chart as per the percentage of male and female who are underweight
value=group_underweight['number']
label=group_underweight['gender']
plt.pie(value,labels=label,autopct="%0.1f%%",radius=2)
plt.show()


# In[37]:


#Task 6
#Group by the gender from healthy weight dataframe and create another data frame out of it
group_healthy_people = hw_df.groupby('gender')['gender'].count().reset_index(name='number')
print(group_healthy_people)


# In[38]:


#Task 7
#Plot a pie chart as per the percentage of male and female who are healthy
value=group_healthy_people['number']
label=group_healthy_people['gender']
plt.pie(value,labels=label,autopct="%0.1f%%",radius=2)
plt.show()


# In[ ]:




