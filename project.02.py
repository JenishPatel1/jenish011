


while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Pattern Generator
    if choice == "1":
        print("\n--- Pattern Generator ---")

        while True:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))
                if rows <= 0:
                    print("Invalid input! Row count must be positive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")

        print("\nRight-Angled Triangle:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    # Option 2: Number Analyzer
    elif choice == "2":
        print("\n--- Number Analyzer ---")

        while True:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                if end <= start:
                    print("Invalid range! End number must be greater than start.")
                    continue
                break
            except ValueError:
                print("Please enter valid integers.")

        total = 0
        print("\odd and Even Numbers:")

        for number in range(start, end + 1):
            if number == 0:
                continue

            if number % 2 == 0:
                print("Number", number, "is Even")
            else:
                print("Number", number, "is Odd")

            total = total + number

        print("\nSum of all numbers from", start, "to", end, "is:", total)

    # Option 3: Exit
    elif choice == "3":
        print("\nExiting the program. Goodbye!")
        break

    # Invalid input handling
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print("\nThank you for using the Pattern Generator and Number Analyzer!")