import shutil
import os
import pickle
import subprocess
from tkinter import messagebox
def checkBSPZIP(path: str):
    try: 
        path.index("bin")
    except ValueError:
        return messagebox.showerror("Couldn't get bspzip",'Can\'t find bspzip.exe. \nPlease select the "bin" folder from any valve source games')
    else:
        print(path)
        newPath = r""+path
        print(newPath)
        bspzip = newPath + "/bspzip.exe"
        print(bspzip)
        # Check if bspzip do exsits

        try: 
            subprocess.call(bspzip)
        except Exception as E:
            return messagebox.showerror("Couldn't get bspzip",'Can\'t find bspzip.exe. \nPlease select the "bin" folder from any valve source games')



def extractMap(map: str):

        
    
    output_path_var = pickle.load(open("./cache/output-path.dat", "rb"))
    print(output_path_var)
    if output_path_var == "":
        return messagebox.showwarning("No folder...", "Please input the output folder")
    
    mapFileName = os.path.split(map)[1]
    print(mapFileName)
    try:
        shutil.copy(map, output_path_var)
    except Exception: 
        return messagebox.showerror("No map found!", "Please input the needed files and folders")
    path = pickle.load(open("./cache/bspzip-path.dat", "rb"))
    if path == "":
        return messagebox.showwarning("No bspzip found", "Please input the bspzip")
    output = output_path_var + f"\\{mapFileName}"

    command = path + "/bspzip" + f' -repack "{output}"'

    print(command)
    try:
        mapFileName.index("bsp")
    except ValueError:
        return messagebox.showerror("Can't load map",'BSPZIP can\'t load the map. \nDid you input the correct map?')
    else:    
        subprocess.call(command)
        return messagebox.showinfo(f"Repacked {mapFileName}", f'Repacked map')

    

