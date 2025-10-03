"""
Day 30 - Exception Handling
This project demonstrates exception handling with try/except/else/finally blocks
"""
import json
import os


def read_data():
    """Read data from JSON file with error handling"""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Data file not found. Creating a new one...")
        return {}
    except json.JSONDecodeError:
        print("Error: Data file is corrupted. Starting fresh...")
        return {}
    else:
        print("Data loaded successfully!")
        return data


def write_data(data):
    """Write data to JSON file with error handling"""
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
    else:
        print("Data saved successfully!")


def add_entry():
    """Add a new entry to the data"""
    website = input("Enter website name: ")
    email = input("Enter email/username: ")
    password = input("Enter password: ")
    
    if not website or not email or not password:
        print("Error: All fields are required!")
        return
    
    data = read_data()
    data[website] = {
        "email": email,
        "password": password
    }
    write_data(data)


def search_entry():
    """Search for an entry in the data"""
    website = input("Enter website name to search: ")
    
    if not website:
        print("Error: Website name is required!")
        return
    
    data = read_data()
    
    try:
        entry = data[website]
    except KeyError:
        print(f"No entry found for {website}")
    else:
        print(f"\nWebsite: {website}")
        print(f"Email: {entry['email']}")
        print(f"Password: {entry['password']}\n")


def list_all_entries():
    """List all stored entries"""
    data = read_data()
    
    if not data:
        print("No entries found!")
        return
    
    print("\n=== All Stored Entries ===")
    for website, details in data.items():
        print(f"\nWebsite: {website}")
        print(f"Email: {details['email']}")
        print(f"Password: {details['password']}")
    print("\n")


def main():
    """Main function with exception handling demonstration"""
    print("=" * 50)
    print("Day 30 - Exception Handling Challenge")
    print("Password Manager (Command Line Version)")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add new entry")
        print("2. Search entry")
        print("3. List all entries")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                add_entry()
            elif choice == "2":
                search_entry()
            elif choice == "3":
                list_all_entries()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-4.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
