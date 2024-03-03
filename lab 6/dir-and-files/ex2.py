import os

def check_access(path):
    print(f"let`s check for access to a specified path: {path}")
    print(f"Path exists: {os.access(path, os.F_OK)}.")
    print(f"Path is readible: {os.access(path, os.R_OK)}.")
    print(f"Path is writeable: {os.access(path, os.W_OK)}.")
    print(f"Path is executable: {os.access(path, os.X_OK)}.")

path = os.getcwd()
check_access(path)
