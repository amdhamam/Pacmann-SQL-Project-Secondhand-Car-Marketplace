# Import the os module
import os

# Define the path to the scripts folder
path = "C:\\Users\\(replace with your username)\\OneDrive\\Documents\\GitHub\\pacmann_sql_project_secondhand_car_marketplace\\py scripts" ## path example

# Create a list of files to execute
files_to_execute = [file for file in os.listdir(path) if file.endswith(".py")]

# Loop until the list is empty
while files_to_execute:
    # Get the first file from the list
    file = files_to_execute.pop(0)
    # Print the file name
    print(file)
    # Execute the script using os.system
    full_path = os.path.join(path, file)
    exit_code = os.system(f'python "{full_path}"')
    # Check if the script ran successfully
    if exit_code == 0:
        # Continue to the next file
        continue
    else:
        # Catch any error and append the file back to the list
        print(f"Error executing {file}")
        files_to_execute.append(file)
