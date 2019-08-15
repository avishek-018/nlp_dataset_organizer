
# coding: utf-8

# In[32]:


import os       #for directory handling
import shutil   #for copying file
import datetime #get the current datetime
import re       #for pattern matching in string


# In[33]:


# do not use / \ < > ? " * | symbols in class names => eg: don't use [[Road/Rail]]
class_names = [
           "Road-Rail",
           "Water", 
           "Air", 
           "Fire", 
           "Suicide", 
           "Others"
        ]


# In[34]:


classes = ["[["+c+"]]" for c in class_names]


# In[35]:


fn = "data.txt"
try:
    file = open(fn, 'r', encoding="utf8") # open existing file in R&W mode
except IOError:
    file = open(fn, 'w', encoding="utf8") 
    for c in classes:
        file.write(c+"\n"*3)
    file.close()
    file = open(fn,"r", encoding="utf8") 


# In[36]:


lines = file.readlines()
file.close()


# In[37]:


for dr in class_names:
    if not os.path.exists("data/"+dr):
        os.makedirs("data/" + dr)
    else:
        print(dr, " Already exists")


# In[38]:


for line in lines:
    if line[:-1] in classes:
        path = "data/"+line[2:-3]
        
    elif len(line) < 20:
        continue
        
    else:
        data_count = len(os.listdir(path))
        f = open(path + "/" + str(data_count+1) +".txt", "w", encoding="utf8")
        f.write(line)
        f.close()
        
        


# In[39]:


backup_path = "backup_raw_data/"
c = 0
flag = 1
if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        flag = 0
        
date = datetime.date.today()


for tx in os.listdir(backup_path):
    x = re.search(str(date), tx)
    if x:
        c+=1

if c == 0:
    backup_name = str(date) + "_" + fn
else:
    backup_name = str(date) + "_"  + "(" +str(c) + ")_" + fn


if flag:
    shutil.copy2(fn, backup_path+backup_name)
    flag = 1


# In[40]:


file = open(fn, 'w', encoding="utf8")
file.truncate(0)
for c in classes:
        file.write(c+"\n"*3)
file.close()

