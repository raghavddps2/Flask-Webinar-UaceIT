import os

# This gets the current working directory!
current_directory = os.getcwd() 

# This lists the files/folders in the directory and loops over them!
print("\nThe Files/Folders inside the current directory are: \n")

for entry in os.listdir(current_directory):
    print(entry)
    
print("---------------------------------------------------------")