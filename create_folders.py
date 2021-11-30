import os
import shutil

folder_names = [f"day_{day:02d}" for day in range(1, 25)]

def create_folders():
    """ Create basic folder structure with placeholder files
    for solvers and challenge input """
    for folder in folder_names:
        if not os.path.exists(os.path.join(os.getcwd(), folder)):
            os.mkdir(folder)
            os.mkdir(f"{folder}/part_1")
            open(f"{folder}/part_1/solve.py", "w").close()
            open(f"{folder}/part_1/input.txt", "w").close()
            
            os.mkdir(f"{folder}/part_2")
            open(f"{folder}/part_2/solve.py", "w").close()
            open(f"{folder}/part_2/input.txt", "w").close()

def remove_folders():
    """ Remove all folders, useful during script creation """
    for folder in folder_names:
        shutil.rmtree(folder, ignore_errors=True)

#remove_folders()
create_folders()
