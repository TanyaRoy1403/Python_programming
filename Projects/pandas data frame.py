student_dictt={
    "student":["tanya","rohit","lily"],
    "score":[56,76,89]
}
# for(key,value) in student_dictt.items():
#     print(value)
#     print(key)

import pandas
student_data_frame= pandas.DataFrame(student_dictt)
# print(student_data_frame)


for(index,row) in student_data_frame.iterrows():
    print(row)
    