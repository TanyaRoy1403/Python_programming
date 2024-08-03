# Exception is runtime error
# to handle it --> try:, except:, else:, finally: use

# type of error
# file not found
# with open("date.txt") as file:
#     file.read()

# key error
# dict = {"key": "value"}
# value = dict["key is not specified"]

# Index error
try:
    file = open("a_file.txt")
    print("this is an exception.")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("hello")
    print("this is handling")
else:      # this will execute if there  is no exception in try block
    print("this is the else block")
finally:
    print("this is the final block")

