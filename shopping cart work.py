def cart():
    list=[]
    while True:
        list_item = input ("Enter Your shopping list or type 'n' for next step ")
        if list_item == 'n':
            break
        else: 
            list.append(list_item)
            
       
    while True:    
        next=input("Enter your next step add/show/delete/quit ")  
        if next == 'quit':
            print("Thanks for Shopping") 
        elif next =="add":
            adding = input("what you want to add ")
            list.append(adding)
            print(f"you have following items in your new list {list} ")
        elif next == "delete":
            del_item = input("Enter item you want to delete ")    
            for i in list:
                if i == del_item:
                   list.remove(i) 
            print(f"you have following items in your new list {list} ")
        elif next=="show":
            print(f"you have following items in the list {list} ")

cart()        





