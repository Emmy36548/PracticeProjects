items = []
while True:
	print("--------------Welcome to the SuperMarket--------------")
	print("1.View items \n2.Add items \n3.Purchase items \n4.Search items \n5.Edit items \n6.Exit")
	choice=int(input("Enter the number of your choice: "))
	if choice==1:
		print("-------View Items-------")
		print("The number of items in the inventory are: %d" %len(items))
		if len(items)!=0:
			print("Here are all the items available in the supermarket")
			for item in items:
				for key,value in item.items():
					print("%s : %s" %(key,value))
	elif choice==2:
		print("---------Add items---------")
		print("To add an item fill in the form")
		item={}
		item["name"]=input("item name: ")
		while True:
			try:
				item["quantity"]=int(input("Item quantity"))
				break
			except ValueError:
				print("Quantity should only be digits")
		while True:
			try:
				item["price"]=int(input("Price $: "))
				break
			except ValueError:
				print("Price should only be in digits")
		print("Item has been successfully added")
		item.append(item)

	elif choice==3:
		print("-----------Purchase items------------")
		print(items)
		purchase_item= input("Which item do you want to purchase? Enter name: ")
		purchase_quantity= int(input("Enter the quantity needed"))
		for item in items:
			if purchase_item.lower()==item["name"].lower():
				if item["quantity"]!=0:
					if purchase_quantity <= item["quantity"]:
						print("Pay %d at checkout counter" %(item["price"]*purchase_quantity))
						item["quantity"]-=purchase_quantity
					else:
						print("Quantity required is not available")
				else:
					print("Item out of stock")
	elif choice==4:
		print("-----------Search items-------------")
		print(items)
		search_item=input("Which item do you want to search for? Enter name: ")
		for item in items:
			if item["name"].lower() == search_item.lower():
				print("The item named" + search_item + "is displayed below with its details")
				print(item)
			else:
				print("item not found")
	elif choice==5:
		print("------------Edit items--------------")
		item_name=input("Enter the name of the item you want to edit: ")
		for item in items:
			if item_name.lower()==item["name"].lower():
				print("Here are the current details of " + item_name)
				print(item)
				item["name"]=input("item name: ")
				while True:
					try:
						item["quantity"]=int(input("item quantity"))
						break
					except ValueError:
						print("quantity should only be in digits")
				while True:
					try:
						item["price"]=int(input("Item price"))
						break
					except ValueError:
						print("Price should only be in digits")
				print(item)
			else:
				print("item not found")
	elif choice==6:
		print("---------------Exit---------------")
		break
	else:
		print("you entered an invalid input")




















































