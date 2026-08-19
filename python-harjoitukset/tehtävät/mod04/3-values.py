gender = input("Which gender are you? ")
gender = gender.lower()

value = int(input("What is your hemoglobin value? "))

if value >= 117 and value <= 155 and gender == "male":
    print ("Normal range")
elif value < 117 and gender == "male":
    print ("You have low hemoglobin.")
elif value > 155 and gender == "male":
    print ("You have high hemoglobin.")

if value >= 134 and value <= 167 and gender == "female":
    print ("Normal range")
elif value < 134 and gender == "female":
    print ("You have low hemoglobin.")
elif value > 167 and gender == "female":
    print ("You have high hemoglobin.")