fish = float(input("What is the length of the zander?\n"))

if fish < 42:
    print(f"You must release the fish. The zander is {round(42 - fish)}cm below the size limit.")
else:
    print ("Nice catch!")