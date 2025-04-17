# File Read & Write Challenge

# Step 1: Read from the original file
with open('example.txt', 'r') as file:
    content = file.read()

# Step 2: Modify the content (convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open('output.txt', 'w') as file:
    file.write(modified_content)

print("File has been read and modified content written to 'output.txt'")