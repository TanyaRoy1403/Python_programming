# file = open("new.text")
# contents = file.read()
# print(contents)
#
# with open("/users/Asus/Desktop/new.text") as file:  #absolute file path
#     content = file.read()
#     print(content)
with open("../../Desktop/new.text") as file:  #relative file path
    content = file.read()
    print(content)