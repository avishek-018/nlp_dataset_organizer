
# coding: utf-8

# In[10]:


import os       #for directory handling
import shutil   #for copying file
import datetime #get the current datetime
import re       #for pattern matching in string


# In[11]:


# do not use / \ < > ? " * | symbols in class names => eg: don't use [[Road/Rail]]

cls_file = open("classes.txt", 'r')
class_names = cls_file.read().splitlines()
class_names = [cn for cn in class_names if len(cn)> 0]
class_names


# In[12]:


classes = ["[["+c+"]]" for c in class_names]


# In[13]:


base = "nlp/"
if not os.path.exists(base[:-1]):
        os.makedirs(base[:-1])

fn = "data.txt"

data_path = base+fn
try:
    file = open(data_path, 'r', encoding="utf8") # open existing file in R&W mode
except IOError:
    file = open(data_path, 'w', encoding="utf8") 
    for c in classes:
        file.write(c+"\n"*3)
    file.close()
    file = open(data_path,"r", encoding="utf8") 


# In[14]:


lines = file.readlines()
file.close()


# In[15]:


for dr in class_names:
    if not os.path.exists(base + "data/" + dr):
        os.makedirs(base + "data/" + dr)
    else:
        print(dr, " Already exists")


# In[16]:


for line in lines:
    if line[:-1] in classes:
        path = base+"data/"+line[2:-3]
        
    elif len(line) < 10:
        continue
        
    else:
        data_count = len(os.listdir(path))
        f = open(path + "/" + str(data_count+1) +".txt", "w", encoding="utf8")
        f.write(line)
        f.close()
        
        


# In[17]:


backup_path = base+"backup_raw_data/"
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
    shutil.copy2(data_path, backup_path+backup_name)
    flag = 1


# In[18]:


file = open(data_path, 'w', encoding="utf8")
file.truncate(0)
for c in classes:
        file.write(c+"\n"*3)
file.close()

