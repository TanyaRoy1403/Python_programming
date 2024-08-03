#new_dict={new_key:new_value for (key,value) in dict.items()}
#new_dict={new_key:new_value for (key,value) in dict.items() if test}
# names=["alexa","tanya","beth","jhon","neha","dave"]
# import random
# scores={student:random.randint(1,100) for student in names }
# print(scores)

sent = "what is the airspeed velocity of an unladen swallow?"
new_dict = {word: len(word)for word in sent.split()}
print(new_dict)

weather_c={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}
weather_f={day :(temp_c *9/5)+32 for (day,temp_c) in weather_c.items()}
print(weather_f)