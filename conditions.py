# CS104

# Lynda Levy

# conditions.py

def main():
    temp = eval(input("Please enter the current tempurature: "))
    if temp > 90:
        print("Wear shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jaket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay inside")

main()
    
