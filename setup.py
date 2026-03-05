from core.paths import Paths
from core.files import Folder

paths={
    '\\app\\',
    '\\admins\\',
    '\\bills\\',
    '\\students\\',
    '\\seats\\'
}



def Setup():
    
    for f in paths:
        Folder().create(Paths().sys_path+f)
        print(f'making files for: {f}')