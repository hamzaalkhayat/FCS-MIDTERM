open_tab=[]


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
      tab = {"title": title, "url": url, "nested_tabs": []}
      open_tab.append(tab)
      print("Tab "+title+" Opened Successfully.")
  

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
mainMenu()    
    