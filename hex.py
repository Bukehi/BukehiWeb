import sys
import os

files=sys.argv[1:]
for filepath in files:
    file=os.path.split(filepath)
    
    filename='B_'+file[1]
    filepath_B=os.path.join(file[0],filename)
    with open(filepath,'rb') as f:
        data=f.read()
    data=data.removeprefix(b'\xff\xff\xff')
    
    with open(filepath_B,'wb') as f:
        f.write(data)

