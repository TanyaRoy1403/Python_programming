# JSON--> IT IS OBJECT NOTATION
# IT IS USE FOR SORTING AND TRANSFERING DATA BETWEEN BROWSER AND SERVER
# json formate--> '{sting,number,null,boolean,object,array,object}'

import json
# d={
#     "course_name":"python",
#     "fees":"5000"
# }                     # object convert into json
# f=json.dumps(d)
# print(f)

# print(type(f))
# #convert json into python object
# # syntax-->json.loads()
# d='{ "course_name":"python","fees":"500"}'
# y= json.loads(d)
# print(y)
# print(type(y))
file = open("posts.json","r")
x= file.read()
print(json.loads(x))

