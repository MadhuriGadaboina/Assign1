#!/usr/bin/env python
# coding: utf-8

# In[58]:


#Question1
#list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sorting the list ages(default)
ages.sort()
print("Sorted Ages=",ages)

#Min age from the list ages
min_age=min(ages)
print("Minimum_age:",min_age)

#Max age from the list ages
max_age=max(ages)
print("Maximum_age:",max_age)

#Add min age and max age to the list ages
ages.append(min_age) 
ages.append(max_age)
print("Updated ages List:",ages)


mid=len(ages)//2
#Median age of the list ages
Med_age = (ages[mid] + ages[~mid]) / 2
print("Median of ages:",Med_age)

#Average age of the list ages
avg=sum(ages) / len(ages)
print("Average age:",avg)

#Range of the list ages
range=max(ages)-min(ages)
print("Range:",range)


# In[59]:


#Question2
#Created empty dog dictionary
dog={}

#dog dictionary with keys and values
dog={'name':'charlie', 'color':'golden', 'breed':'goldenretriever', 'legs':'4', 'age':'5'}
print("Dog dictionary:",dog)

#Created Student dictionary
student = {
    'first_name':'Madhuri',
    'last_name':'Gadaboina',
    'gender':'Female',
    'age':'22',
    'country':'USA',
    'city':'overland park',
    'marital status':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print("Student Dictionary:",student)

#length of Student Dictionary
print("Length of Student Dictionary:",len(student))

#Getting the value of skills
print("value of skills:",student['skills'])

#checking its data type
print("Datatype of Skills:",type(student['skills']))

#Added Values to Skills
student['skills'].append('HTML')

keys = student.keys()
print("Student_Keys:",keys) 
values = student.values()
print("Student_Values:",values)


# In[60]:


#Question3 
#Tuple of Sisters
sisters=('sheetal','shweta','vyshu','abhi')
print("My Sister:",sisters)

#Tuple of Brothers
brothers=('sathi','kartik','sunny','lucky','bittu','chikkuru')
print("My Brothers:",brothers)

#Join Brothers and Sisters and Assign to Siblings
siblings=sisters+brothers
print("My siblings :",siblings)

#Length of Siblings Tuple
print("Numbers of Siblings:",len(siblings))

#Adding Father Name and Mother name to siblings and assigning it to Family members
family_members=siblings+('Ramesh kumar','ramadevi')
print("My Family Members:",family_members)


# In[61]:


#Question4

#sets of it_companies,A and B
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#list of ages
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of set it_companies
print("length of it_companies:",len(it_companies))

#Added Twitter to it_companies
it_companies.add( 'Twitter')
print("it_companies after adding Twitter:",it_companies)
#inserted Multiple IT companies to bthe set
it_companies.update( ['TCS','Wipro','Cognizant'])
print("updated it_companies:",it_companies)
#removed one of the it_companies
it_companies.remove('Google')
print(it_companies)

#Join of A and B
print("Join of A and B:",A.union(B))

#intersection of A and B
print("intersection of A and B:",A.intersection(B))

#finding A subset of B
print("A subset of B:",A.issubset(B))

#finding A and B are Disjoint Sets
print("A and B are Disjoint Sets:",A.isdisjoint(B))

#Finding Symmetric Difference
print("Symmetric Difference:",A.symmetric_difference(B))

#Deleting all the sets
del A,B,it_companies

#converting list to set anf finding their lengths
ages=set(age)
print(ages)
print("Length of set ages:",len(ages))
print("Length of list age:",len(age))


# In[62]:


#Question5
import math as M  

#radius as user input
Radius = float (input ("Please enter the radius of the given circle: "))  

#area of circle
_area_of_the_circle_ = M.pi* Radius * Radius  
print (" The area of the given circle  = %.2f " % _area_of_the_circle_)  

#Circumference of the circle
_circum_of_circle_= 2 * M.pi * radius
print(" Circumference Of a Circle = %.2f" %_circum_of_circle_)


# In[63]:


#Question6
string = "I am a teacher and I love to inspire and teach people"
# Use split method to separate the words and set to get the unique values
uniq=set(string.split(" "))
print("Unique Words:",uniq)
print ("Length:",len(uniq))


# In[64]:


#Question7
#used escape Sequence tab
 
print("Name\t Age\tCountry\tCity\t\nAsabeneh 250\tFinland\tHelsinki")


# In[65]:


#Question8
#Using String format method
print(f'radius = 10')
print(f'area = 3.14*radius**2')
print(f'"The area of circle with radius {r} is {3.14*r*r} meters square"')


# In[66]:


#Question9
#Creating a list(L1) for weights(lbs) of N students
L1=[int(num) for num in input().split(" ")]
#Creating another list called W_kg
W_kg=[] 
#Using for loop to iterate the values and appending the list
for i in L1:
 W_kg.append(round(i/2.205,2))
#Displaying the values in kgs after conversion
print ("Values are:",W_kg)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




