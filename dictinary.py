# syntax-->{"key":value}
this_dic={"brand":"ford","model":"mustang","year":"1964","year":"2020"}
print(this_dic["brand"])   #to  excess value we print key
print(this_dic) #same itmes does not allow to store
print(this_dic.get("brand"))  # also to excess the itmes of dic
print(this_dic.keys())  # to access all keys of dic
print(this_dic.values()) # to acess all values of dic
this_dic["color"]="white"  # to add  new key
this_dic["year"]= 2018  # to change the existing item value  
this_dic.update({"year":"2018"}) # other way to change value ,also use to add item
print(this_dic)
print(this_dic.items())  # to get all key with their respective value
(this_dic.pop("model"))  # to remove items of dic
this_dic.popitem() # remove the last item of dic
print(this_dic)
del this_dic["model"] # remove the item 
print(this_dic)
this_dic.clear()  # empty the dic
print(this_dic)

# loop in dic
for x in this_dic:  # using for loop return only keys
    print(x)
for x in this_dic:
    print(this_dic[x])  # this will return all value of dic

for x,y in this_dic.items():  # this will all key and values
    print(x,y)
print(this_dic.copy()) # to copy dic
print(dict(this_dic))  #to copy dic
myfamily={"child1":{"name":"emil","year":"2004"},
          "child2":{"name":"tobias","year":"2007"},
          "child3":{"name":"linus","year":"2011"}
}
print(myfamily["child1"]["name"])  #to acess the item of nested dic
