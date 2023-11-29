print("------------------------")
product_name = input("Product name: ")

try:
    product_net_price = float(input("Product net price: "))
except:
    print("Process interrupted. Bad data type.")
    exit()


client_email = input("Client mail: ")

try:
    client_phone = int(input("Client phone: "))
except:
    print("Process interrupted. Bad data type.")
    exit()



tax = product_net_price * 23 / 100
gross_price = product_net_price - tax

print("------------------------")
print("Welcome in Michael’s store.")
print("Your basket: ", product_name, "\n", product_net_price, "\n", gross_price, "\n", client_email, "\n", client_phone)
print("------------------------")

