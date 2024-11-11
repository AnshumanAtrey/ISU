#Develop a program to read, write, and append a text file.
# File Operations Program
def write_to_file(filename):
    """Write user input to a file."""
    with open(filename, 'w') as file:
        content = input("Enter text to write to the file: ")
        file.write(content)
    print("Content written to file successfully.")

def append_to_file(filename):
    """Append user input to a file."""
    with open(filename, 'a') as file:
        content = input("Enter text to append to the file: ")
        file.write(content + '\n')  # Add a newline for better formatting
    print("Content appended to file successfully.")

def read_from_file(filename):
    """Read and display the content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist. Please write to the file first.")

def main():
    """Main function to run the file operations program."""
    filename = "example.txt"  # Name of the file to operate on

    while True:
        print("\nFile Operations Menu:")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read from file")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            write_to_file(filename)
        elif choice == '2':
            append_to_file(filename)
        elif choice == '3':
            read_from_file(filename)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()