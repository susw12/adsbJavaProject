import ml

conference = input("Please enter the name of conference: ")

file = open("name.txt",w)
file.write(conference)
file.close()

print(ml.kowalski())