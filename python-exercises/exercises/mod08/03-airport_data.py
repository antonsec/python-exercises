airport = {
    "EFHK":"Helsinki-Vantaa Airport"
}

while True:
    option = int(input("Selct options: 1. Enter new aiport 2. Get info on existing airport 3. Quit program\n"))

    if option == 3:
        print ("Ending program..")
        break

    elif option == 1:
        icao = input("Enter ICAO code of the new airport: ")
        airport_name = input("Enter the new airports name: ")
        airport[icao] = airport_name

    elif option == 2:
        old_icao = input("Enter given ICAO code: ")

        if old_icao in airport:
            print (airport[old_icao])
        else:
            print (f"{old_icao} doesn't exist.")