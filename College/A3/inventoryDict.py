def dataBase():#creating a data base funciton that returns the default data base that i can call in main()
    inventoryDB = { 
            'F01':["Orange", "Fruit", 2.99, 1000],
            'F02':["Apple", "Fruit", 1.99, 5000],
            'F03': ["Banana", "Fruit", 1.99, 490],
            'D01':["Milk", "Dairy", 7.5, 500],
            'D02':["Cheese", "Dairy", 15, 840],
            'D03':["Yogurt", "Dairy", 5.5, 700],
            'V01':["Carrot", "Vegetable", 3.8, 890],
            'V02':["Celery", "Vegetable", 3.99, 890],
            'V03':["Bean", "Vegetable", 4.5, 1500],
            'V04':["Potato", "Vegtable", 6, 1000]
        }#end of inventory (With Default Values)
    return inventoryDB#rturning the values 
categoryList = ["fruit", "dairy", "vegetable"]

