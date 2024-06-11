import pandas as pd

choice = 0
ch = "x"
while ch == "x":
    print("SUPER MARKET")
    print("MENU:")
    print("1.  Insert Product Data")
    print("2.  Create Table of Data")
    print("3.  Display Numbers of Rows from the Table")
    print("4.  Delete Data from the Table")
    print("5.  Save the Table")
    print("6.  Add or Delete Data")
    print("7.  Read the Saved Table")
    print("8.  Display Numbers of Rows from the Saved Data")
    print("9.  Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter Number of Products: "))
        p_id = []
        p_type = []
        p_name = []
        p_quantity = []
        price = []
        for i in range(n):
            pid = input("Enter the ID of the Product : ")
            protype = input("Enter the type of the Product : ")
            pname = input("Enter the Name of the Product : ")
            quant = input("Enter Quantity : ")
            pri = input("Enter Price (In AED) : ")
            p_id.append(pid)
            p_type.append(protype)
            p_name.append(pname)
            p_quantity.append(quant)
            price.append(pri)
        dict = {' Product ID ': p_id, 'Product Type ': p_type, 'Product Name ': p_name,
                'Quantity ': p_quantity, 'Price ': price}
        print('Your Data is Successfully Inserted: ', dict)
    elif choice == 2:
        print('Your Table of Product Data is Successfully Created: ')
        print("\t\t\tSUPER MARKET")
        df = pd.DataFrame(dict)
        print(df)
    elif choice == 3:
        choice1 = 0
        ch1 = "y"
        while ch1 == "y":
            print("OPTIONS: ")
            print("1. To Display Rows from the Start of the Table of Product Data")
            print("2. To Display Rows from the Last of the Table of Product Data")
            print("3. Back")
            choice1 = int(input("Enter your choice: "))
            if choice1 == 1:
                print(df.head(int(input("Enter the number of rows you want to display from the start: "))))
            elif choice1 == 2:
                print(df.tail(int(input("Enter the number of rows you want to display from the start: "))))
            elif choice1 == 3:
                break
            else:
                print("ERROR")
    elif choice == 4:
        print(df)
        df = df.drop(int(input("Enter index of the row: ")), axis=0)
        print("Changed Table of Data: ")
        print(df)
    elif choice == 5:
        df.to_csv('Super Market', index=False)
        print("Your Data has been successfully Saved")
    elif choice == 6:
        choice2 = 0
        ch2 = "z"
        while ch2 == "z":
            print("MENU:")
            print("1.  Add")
            print("2.  Delete")
            print("3.  Back")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                n = int(input("Enter Number of Products:"))
                p_id = []
                p_type = []
                p_name = []
                p_quantity = []
                price = []
                for i in range(n):
                    pid = input("Enter the ID of the Product : ")
                    protype = input("Enter the type of the Product : ")
                    pname = input("Enter the Name of the Product : ")
                    quant = input("Enter Quantity : ")
                    pri = input("Enter Price (In AED) : ")
                    p_id.append(pid)
                    p_type.append(protype)
                    p_name.append(pname)
                    p_quantity.append(quant)
                    price.append(pri)
                dict2 = {' Product ID ': p_id, ' Product Type': p_type, ' Product Name ': p_name,
                         ' Quantity ': p_quantity, ' Price ': price}
                df2 = pd.DataFrame(dict2)
                print('Your Table of Product Data is Successfully Created: ')
                print("\t\t\tSUPER MARKET")
                print(df2)
                df2.to_csv('Super Market', index=False, mode='a', header=False)
                print('Your Data has been Successfully edited.')
            elif choice2 == 2:
                df = pd.read_csv('Super Market')
                print(df)
                df = df.drop(int(input("Enter index of the row: ")), axis=0)
                df.to_csv('Super Market', index=False)
                print('Your Data has been Successfully edited.')
            elif choice2 == 3:
                break
            else:
                print("ERROR")
    elif choice == 7:
        CSV = pd.read_csv('Super Market')
        print(CSV)
    elif choice == 8:
        csv1 = pd.read_csv('Super Market', nrows=int(input("Enter No of rows to be displayed: ")))
        print(csv1)
    elif choice == 9:
        print('Ending the program ...')
        quit()
    else:
        print('Error: INVALID CHOICE')
