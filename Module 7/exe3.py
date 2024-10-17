airport_dict = {}

def add_airport():
    name = input ("Enter your airport name:")
    icao_code = input("Enter the icao code:")

    if icao_code in airport_dict:
        print("this airport is already added to the databse.")
    else:
        airport_dict[icao_code] = name
        print(f"Airport {name} and ICAO code {icao_code} have been added.")

def fetch_the_airport():
    icao_code = input("Input the Airport's ICAO code:")

    if icao_code in airport_dict:
        print(f"The name of the Airport and ICAO code {icao_code} is: {airport_dict[icao_code]}")
    else:
        print("This ICAO code is not available.")

def main():
    while True:
        print("Choose an option:")
        print("(1). Enter a new airport")
        print("(2). Fetch the information of an airport")
        print("(3). Quit")

        number = int(input("Enter the number (1,2,3):"))
        if number == 1:
            add_airport()
        elif number == 2:
            fetch_the_airport()
        elif number == 3:
            print("Quit")
            break

main()
