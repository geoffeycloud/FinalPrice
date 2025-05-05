# Function to read a file and return its content
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' can't be read.")
        return None

# Function to write content to a new file
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to '{filename}'")
    except IOError:
        print(f"Error: The file '{filename}' can't be written.")

# Function to modify the content (for this example, we'll convert all text to uppercase)
def modify_content(content):
    return content.upper()

# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

# Read the content of the file
file_content = read_file(filename)

# If the file was read successfully, modify and write the content to a new file
if file_content is not None:
    modified_content = modify_content(file_content)
    new_filename = input("Enter the name of the new file to write: ")
    write_file(new_filename, modified_content)