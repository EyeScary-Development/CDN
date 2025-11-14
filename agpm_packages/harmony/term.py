import os
def main():
        while True:
            command=input("enter a command for your terminal (q to quit): ")
            if command != "q":
                os.system(command)
            else:
                break