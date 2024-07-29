products = [    
    {
        "id" : 1,
        "name" : "Potteto",
        "price" : 150,
        'discount_price' : 120,
    },    
    {
        "id" : 2,
        "name" : "tometo",
        "price" : 160,
        'discount_price' : 150,
    },
    {
        "id" : 3,
        "name" : "drink",
        "price" : 100,
        'discount_price' : "",
    },
    {
        "id" : 4,
        "name" : "milk",
        "price" : 150,
        'discount_price' : "",
    },
    {
        "id" : 5,
        "name" : "oil",
        "price" : 170,
        'discount_price' : 165,
    },
]

for k in products:
   l = f"{k['id']} : {k['name']}"
   print(l)

card = []
i = 1 
while i <= len(products):
   select_product = input('Select your product id ')
   if select_product == "0":
      break
   else:
      card.append(select_product)
      i += 1

def get_total (*product):
   total = 1
   for y in product[-1]:
      for x in products:
        if x["id"] == int(y):
            if x['discount_price'] != "":
               total += x['discount_price']
            else:
               total += x['price']
   return total 
   
            
         
   
result = get_total (card)
print(result)