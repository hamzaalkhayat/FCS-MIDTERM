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
    
    title = input("Enter the Title of the website: ")
    url = input("Enter the URL: ")
   
    if title == "" or url == "":
       print("Title OR Url is Empty Please Try Again ") 
    else:
     check_title = False   
     for tab in open_tab:
       if  tab["title"] == title :
          check_title = True
     if check_title == True:
        print("Title ALready exist!! ") 
     else:   
      tab = {"title": title, "url": url, "child_tabs" :{}}
      open_tab.append(tab)
      print("Tab "+title+" Opened Successfully.")
      print (open_tab)

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
            title = input("Enter the Title of the website: ")
            url = input("Enter the URL: ") 
            child={"title": title, "url": url}
            tab = open_tab[parent_index]
            tab1 = tab['child_tabs']
            index_childtab = len(tab1)
            open_tab[parent_index]['child_tabs'][index_childtab]=child
        else:
          print("Index Not Valid Please Try Again.")  
    else:
      print("Their Is No Tab Open")
    print (open_tab)
#*****************************************************************************************

def Sort_Tabs():
    insertionSort()
    print("Tabs Sorted successfully")

#***************************************************************************************
def Switch_Tab() :
    print ("Enter An Index of the tab to switch and display, OtherWise Will switch and display the last opened tab.  ")
    index =input("Enter Here : ")
    
    if len(open_tab) > 0:
       import requests 
       from bs4 import BeautifulSoup 
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
          print(BeautifulSoup(r.text, 'html.parser'))
       else:
          print("An Error occurred!")
          
    else:
        print("Their Is No Tab Open")   
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


mainMenu()    
    