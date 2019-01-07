import ml.py

conference = input("Please enter the name of conference: ")
company = input("Please enter the name of conference: ")

file = open("name.txt",w)
file.write(conference)
file.close()

print(ml.flag())
