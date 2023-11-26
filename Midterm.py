import json
import os
import requests 
from bs4 import BeautifulSoup 

open_tab=[]
#****************************************************************************************

def insertionSort(): 
    
  border=1
  while border<len(open_tab): 
    current=border 
    while current>0 and open_tab[current]['title'].lower()<open_tab[current-1]['title'].lower(): 
        
       temp=open_tab[current]
       open_tab[current]=open_tab[current-1]
       open_tab[current-1]=temp
      
       current-=1
    border+=1
  print (open_tab)
#**************************************************************************************** 
def Open_New_Tab ():
    
   title = (input("Enter the Title of the website: ")).strip()
   url = input("Enter the URL: ")
   Is_String =title.isalpha()
    
   if Is_String == True and url !="":
     check_title = False   
     for tab in open_tab:
       if  tab["title"] == title :
          check_title = True
     if check_title == True:
        print("Title ALready exist!! ") 
     else:   
      tab = {"title": title, "url": url, "content":"","child_tabs" :{}}
      open_tab.append(tab)
      print("Tab "+title+" Opened Successfully.")
      print (open_tab)
   else:
      print("Try Again By Entering Letters Only NO Characters Not Empty. ")  
#*****************************************************************************************
def Close_Tab():
    
    
    print ("Enter An Index To Close, OtherWise Will Close the last opened tab.  ")
    index =input("Enter Here : ")
    
    if len(open_tab) > 0:
        
     if index == "":
        close_tabs = open_tab.pop() 
        print("Since No Index Enter The Last Tab Opened Will Closed : "+close_tabs['title'])
     else:
       if 0 <= int(index) < len(open_tab) :
         close_tabs =  open_tab.pop(int(index))
         print ("Closed Tab IS" +close_tabs['title']+"At Index : " + index )
       else:
         print("Index Not Valid Please Try Again.")
    
    else:
        print("Their Is No Tab Open")
          

   
#******************************************************************************************
def Display_All_Tabs():
    if len(open_tab) > 0:
     for i in range(len(open_tab)):
        tab =open_tab[i]
        print(str(i)+". "+tab['title'])
        for j in range(len(tab['child_tabs'])):
            tab_1=tab['child_tabs'][j]
            print(str(i)+"."+str(j)+". "+tab_1['title'])
    else:
      print("Their Is No Tab Open")
      
#*****************************************************************************************
def Open_Nested_Tab():
    if len(open_tab) > 0:
        parent_index = int(input("Enter the index of the parent tab: "))
        if 0 <= parent_index < len(open_tab):
            title = (input("Enter the Title of the website: ")).strip()
            url = input("Enter the URL: ") 
            child={"title": title, "url": url}
            tab = open_tab[parent_index]
            tab1 = tab['child_tabs']
            Is_String =title.isalpha()
            
            if Is_String ==True and url != "":    
                index_childtab = len(tab1)
                open_tab[parent_index]['child_tabs'][index_childtab]=child
                
            else:
             print("Try Again By Entering Letters Only NO Characters Not Empty. ") 
        else:
          print("Index Not Valid Please Try Again.")  
    else:
      print("Their Is No Tab Open")
    
#*****************************************************************************************

def Sort_Tabs():
    if len(open_tab) > 0: 
       insertionSort()
       print("Tabs Sorted successfully")
    else:
      print("Their Is No Tab Open")   

#***************************************************************************************
def Save_Tab():
    if len(open_tab) > 0: 
       print("\nEnter:")
       print("1. Add a New File. ")
       print("2. OverWrite On Existing File.")
       answer = (input("Your choice: "))  
        
       file_path = input("Enter the file path (must be .txt)to Save tabs from:")
       if file_path == "":
           print("File Path Is Empty Please Try Again")
           
       else: 
        exist = os.path.exists(file_path)   
        if answer == '1':
           if exist == False:
              f = open(file_path, "x") 
              json.dump(open_tab, f, indent = 2)
              f.close()
           else:
              print("You Choose Add New File And The File Is Exist Please Try Again.") 
        elif answer == '2':
            if exist == True:
               f = open(file_path, "w")
               json.dump(open_tab, f, indent = 2)
               f.close()
            else:
               print("You Choose OverWrite An Existing File And The File Is Not Found Please Try Again.")   
        else:
          print("Please Try Again And Choose A Chioce Between 1 or 2 Only!! ")  
    else:
      print("Their Is No Tab Open") 
    
#***************************************************************************************
def Switch_Tab() :
    print ("Enter An Index of the tab to switch and display, OtherWise Will switch and display the last opened tab.  ")
    index =int(input("Enter Here : "))
    
    if len(open_tab) > 0:
      
       if index == "":
          index = len(open_tab) - 1 
       else:
          if 0 <= int(index) < len(open_tab) :
             index=  index
          else:
             print("Index Not Valid Please Try Again.")    
      
       tab =  open_tab[index]
       r = requests.get(tab['url'] )
       if r.status_code == 200:
          x = BeautifulSoup(r.text, 'html.parser')
          print(x)
          open_tab[index]['content'] = str(x)
       else:
          print("An Error occurred!")
          
    else:
        print("Their Is No Tab Open")   

#*****************************************************************************************
def Import_Tab() :
    
    file_path = input("Enter the file path (must be .txt) to import tabs from:")
    
    if file_path == "":
       print("File Path Is Empty Please Try Again")
       
    else:
       exist = os.path.exists(file_path)
       if exist ==  True:
         file = open(file_path, "r") 
         print(file.read())
         file.seek(0)
         open_tab = json.load(file)
         print (open_tab)
       else:
         print("File Not Found") 
    
#****************************************************************************************
def mainMenu():
  choice=-99 # dummy value
  while choice != '9':
       
    print("\nMenu:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1' :
        Open_New_Tab ()
       
    if choice == '2' :
        Close_Tab()
   
    if choice == '3' :
        Switch_Tab() 
       
    if choice == '4' :
        Display_All_Tabs()
    
    if choice == '5' :
        Open_Nested_Tab()
    
    if choice == '6' :
        Sort_Tabs() 
    
    if choice == '7' :
        Save_Tab()
    
    if choice == '8' :
        Import_Tab()    
 
    if choice == '9' :
        print("NOW WILL EXIST, GOODBYE!!!")  

mainMenu()    
    