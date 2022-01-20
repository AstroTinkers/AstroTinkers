proverka = set()
while True:
    vhod = input("Input(Press q to exit):")
    if vhod == "q":
        if len(proverka) == 0:
            break
        else:
            final = list(proverka)
            final.sort()
            textfile = open("Results.txt", "w")
            for elements in final:
                textfile.write(elements + "\n")
            textfile.close()
            print(final)
        break
    elif vhod in proverka:
        print("You already got one.")
    else:
        proverka.add(vhod)
        print("Item added to checklist.")
