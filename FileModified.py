import pathlib 
from datetime import datetime

fname = pathlib.Path('thenewFile.txt')

if fname.exists(): 
    mtime = datetime.fromtimestamp(fname.stat().st_mtime)
    mtimeString = datetime.strftime(mtime,'%Y-%m-%d')
    nowtimeString = datetime.strftime(datetime.now(),'%Y-%m-%d')
    if mtimeString != nowtimeString:
        print('Sending Phish URL Request')
    else:
        print('Using already downloaded URL\'s')
else:
    print("Sending Request and creating the URL file")


# print("some random words for file")
