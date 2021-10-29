#importing required libraries
import requests
from tqdm import tqdm

#getting url
url = input("enter url: ")

file = url.split('/')[-1]                    #naming file
r = requests.get(url, stream=True, allow_redirects=True)                  #enabling downloads
total_size = int(r.headers.get('content-length'))                         #getting size of file
initial_pos = 0                                                           #initial position of progress bar
with open(file,'wb') as f:                                                #saving file/downloading file
    with tqdm(total=total_size, unit='byte', unit_scale=True,desc=file,initial=initial_pos, ascii=True) as pbar:        #showing progress bar
        for ch in r.iter_content(chunk_size=1024):                        #chunk size or ch represents chunk of data which is 1024 bytes
            if ch:                                                        #you can change chunk size if you want
                f.write(ch) 
                pbar.update(len(ch))
