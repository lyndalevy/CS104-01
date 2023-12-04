def main():
    names = []
    i = 0
    for i in range(10):
        name = input("Enter a name: ")
        names.append(name)
    print(names)
    i = 0
    for i in range(10):
        print(names.pop(i))
        print(i)

main()
        
    
