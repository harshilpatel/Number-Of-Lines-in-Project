#/usr/bin/python
# harshil912@gmail.com 
import os, glob

count = 0
filetypes = set()
def get_folder_lines(path, count):
    global filetypes
    local_count = 0
    files_to_avoid = ['.png','.jpg','.jpeg','.min.js','.gz','.pyc','.gif','.sqlite3','.txt','.svg','.woff','auto']
    files_to_consider = ['.py','.js','.css']
    folders_to_avoid=['allauth','venv','www','.git','vendor']
    for file in os.listdir(path):
        if not os.path.isdir(os.path.join(path, file)):
            file_type_accept = [ftype for ftype in files_to_consider if ftype in file]
            file_type_avoid = [ftype for ftype in files_to_avoid if ftype in file]        
            if file_type_accept and not file_type_avoid :
                f = open(os.path.join(path, file),'r')
                data = f.read()
                count += data.count("\n")
                local_count += data.count("\n")
                f.close()
            # else:
                # filetypes.add(file_type[0])
        else:
            if file not in folders_to_avoid:
                count = get_folder_lines(os.path.join(path, file), count)
    # print path + " " +str(local_count)
    # print count
    return count 

home_path = os.getcwd()

print "Total lines: " + str(get_folder_lines(home_path, count))
# print filetypes
