def get_int(prompt):
    """Utility to safely retrieve integer input."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter an integer.")


def get_int_list(prompt):
    """Utility to safely retrieve a space-separated list of integers."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Input cannot be empty. Please enter numbers.")
            continue
        try:
            return [int(x) for x in raw.split()]
        except ValueError:
            print("Invalid input! Make sure all values are integers separated by spaces.")


def input_data():
    print("\n1. One-Dimensional List")
    print("2. Two-Dimensional List")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        data = get_int_list("Enter numbers separated by spaces: ")
        return data, "1"

    elif choice == "2":
        rows = get_int("Enter number of rows: ")
        while rows <= 0:
            print("Number of rows must be at least 1.")
            rows = get_int("Enter number of rows: ")

        data = []
        for i in range(rows):
            row = get_int_list(f"Enter numbers for row {i + 1}: ")
            data.append(row)
        return data, "2"

    else:
        print("Invalid choice! Data was not updated.")
        return None, None


def flatten(data, choice):
    """Helper function to extract all numbers into a single list."""
    if choice == "2":
        return [num for row in data for num in row]
    return list(data)


def display_summary(data, choice):
    if not data:
        print("No data available! Please input data first.")
        return

    numbers = flatten(data, choice)
    if not numbers:
        print("Dataset contains no elements.")
        return

    print("\n--- Data Summary ---")
    print("Total elements:", len(numbers))
    print("Minimum value:", min(numbers))
    print("Maximum value:", max(numbers))
    print("Sum:", sum(numbers))
    print("Average:", round(sum(numbers) / len(numbers), 2))
    print("Unique values:", sorted(set(numbers)))


def factorial(n):
    """Iterative factorial to prevent recursion stack overflow."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def filter_and_double(data, choice):
    if not data:
        print("No data available! Please input data first.")
        return

    numbers = flatten(data, choice)
    limit = get_int("Enter threshold value: ")

    filtered = [num for num in numbers if num >= limit]
    doubled = [num * 2 for num in filtered]

    print("Filtered numbers (>= threshold):", filtered)
    print("Doubled numbers:", doubled)


def sort_data(data, choice):
    if not data:
        print("No data available! Please input data first.")
        return

    print("1. Ascending order")
    print("2. Descending order")
    order = input("Enter your choice: ").strip()

    if order not in ("1", "2"):
        print("Invalid sorting choice!")
        return

    reverse_order = (order == "2")

    if choice == "1":
        sorted_list = sorted(data, reverse=reverse_order)
        print("Sorted list:", sorted_list)

    elif choice == "2":
        sorted_2d = [sorted(row, reverse=reverse_order) for row in data]
        print("Sorted 2D list (row-by-row):")
        for row in sorted_2d:
            print(row)


def main():
    data = []
    choice = "1"

    while True:
        print("\n===== DATA ANALYZER =====")
        print("1. Input Data")
        print("2. Display Summary")
        print("3. Calculate Factorial")
        print("4. Filter and Double")
        print("5. Sort Data")
        print("6. Exit")

        option = input("Enter your choice: ").strip()

        if option == "1":
            new_data, new_choice = input_data()
            if new_data is not None:
                data, choice = new_data, new_choice

        elif option == "2":
            display_summary(data, choice)

        elif option == "3":
            num = get_int("Enter a non-negative integer: ")
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {num}:", factorial(num))

        elif option == "4":
            filter_and_double(data, choice)

        elif option == "5":
            sort_data(data, choice)

        elif option == "6":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid option! Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
