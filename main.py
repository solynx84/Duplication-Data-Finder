# Duplicate Data Finder Project

print("===== DUPLICATE DATA FINDER =====")


filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        data = file.readlines()

    
    data = [x.rstrip("\n\r") for x in data]

    
    data = [x for x in data if x.strip()]

    if len(data) == 0:
        print("File is empty. Nothing to check.")

    else:
        print("\n1. Exact Match")
        print("2. Ignore Case and Extra Spaces")

        choice = input("Enter your choice: ")

        if choice == "1":
            entries = data

        elif choice == "2":
            entries = [x.strip().lower() for x in data]

        else:
            print("Invalid choice!")
            exit()

        
        unique = set(entries)

        
        print("\nTotal items:", len(data))
        print("Unique items:", len(unique))

        found = False

        for item in unique:
            count = entries.count(item)

            if count > 1:
                print("Duplicate:", item,
                      "(", count, "times )")
                found = True

        if found == False:
            print("No duplicates found.")


        unique_list = []

        for i in range(len(data)):
            if entries[i] not in unique:
                continue

            if entries[i] not in [
                entries[j] for j in range(i)
            ]:
                unique_list.append(data[i])

        with open("unique.txt", "w") as file:
            for item in unique_list:
                file.write(item + "\n")

        print("Unique list saved to unique.txt")

except FileNotFoundError:
    print("File", filename,
          "not found. Please enter a valid file name.")