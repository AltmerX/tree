#!/usr/bin/env python3
import subprocess
import sys
import os



def display(path):
    global totalDirCount
    global totalFileCount  
    tree(path,1,"")
    if totalDirCount!=0 or totalFileCount!=0:
        print(".")
    print("\n",totalDirCount," directories, ",totalFileCount," files",sep='')

def tree(path,level,indent):
    global totalDirCount
    global totalFileCount
    content=sorted(os.listdir(path))
    count=0
    for entry in content:
        if os.path.isfile(path+"/"+entry):
            totalFileCount+=1
            if count==len(content)-1:
                temp=indent+"└── "
                print(temp+entry)
            else:
                temp=indent+"├── "
                print(temp+entry)
        else:
            totalDirCount+=1
            if count==len(content)-1:
                temp=indent+"└── "
                print(temp+entry)
                indent=indent+"    "
                tree(path+"/"+entry,level+1,indent)
            else:
                print(indent+"├── "+entry)
                tree(path+"/"+entry,level+1,indent+"│   ")
        count=count+1
        
if __name__ == '__main__':
    # just for demo
    path="."
    totalDirCount=0
    totalFileCount=0
    if len(sys.argv)==2:
        path=sys.argv[1]
    display(path)
    
