import os



if __name__ == "__main__":
    print("Wellcome to ROBO Speaker 1.1 . Created By MA-Sani ")

    while True:
        x = input("Enter , Wahat you wants me to speaks about : ")
        if x == "q":
            os.system("says 'bye bye friends")
            break
        command = f"say {x}"
        os.system(command)