import os
import pickle
import shutil
import subprocess
from tkinter import messagebox
def checkBSPSRC(path: str):
    # try: 
    #     path.index("jar")
    # except ValueError:
    #     return messagebox.showerror("Couldn't get bspsrc",'Can\'t find bspsrc.jar \nPlease select the folder where "bspsrc.jar" is.')
    # else:
    print(path)
    newPath = r""+path
    print(newPath)
    bspsrc = newPath + "java -jar bspscr.jar -h"

    # Check if bspzip do exsits
    subprocess.call(bspsrc)


def MapToVMT():
    output_path_var = pickle.load(open("./cache/output-path.dat", "rb"))
    print(output_path_var)
    if output_path_var == "":
        return messagebox.showwarning("No folder...", "Please input the output folder")
    path = "./bspsrc/bspsrc.jar"
    newPath = os.path.split(path)[0]
    # command = newPath + " 
    # print(command)   
    # newPath, shell=True, args=["java -jar bspsrc.jar", f' -r "{output_path_var}" "{VMF_path_var}"'] 
    app = "java -jar bspsrc.jar"
    command = f'-r "{output_path_var}" "{output_path_var}"'
    subprocess.call(f'run-bspsrc.bat {newPath} {command}')
    return messagebox.showinfo("Map converted", 'Finished converting map')

    
    
