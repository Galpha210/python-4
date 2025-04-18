filename = input("Enter the filename you want to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")

except PermissionError:
    print(f"❌ Error: You don't have permission to read '{filename}'.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")