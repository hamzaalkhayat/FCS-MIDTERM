def Open_New_Tab (Order_OpenTabs):
    Open_Tabs = Order_OpenTabs
    title = input("Enter the Title of the website: ")
    url = input("Enter the URL: ")
   
    if title == "" or url == "":
       print("Title OR Url is Empty Please Try Again ") 
    else:
     check_title = False   
     for tab in Open_Tabs:
       if  tab["title"] == title :
          check_title = True
     if check_title == True:
       print("Title ALready exist!! ") 
     else:   
      tab={"title": title, "url": url}
      Open_Tabs.append(tab)
      print("Tab "+title+" Opened Successfully.")
    return Open_Tabs

def mainMenu():
  Order_OpenTabs=[] 
    
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
    
    if choice == '1':
      Order_OpenTabs = Open_New_Tab (Order_OpenTabs)
mainMenu()    
    