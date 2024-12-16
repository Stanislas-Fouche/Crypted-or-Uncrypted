import os

#Script to rename a dataset of files with different extensions to a dataset of files with the same extension but sorted to be able to use them more efficiently later

file_paths = [os.path.join('dataset/non_chiffre', file) for file in os.listdir('dataset/non_chiffre')]

txt = 0
csv = 0
jpg = 0
png = 0
pdf = 0

dir_path = "dataset/non_chiffre/"
offset = 0

for file in file_paths:
    if   file[-4:] == ".txt":
        os.rename(file, dir_path + (str((txt + offset ) )) + ".txt")
        txt += 1
        print(txt)
    elif file[-4:] == ".csv":
        os.rename(file, dir_path + (str((csv + offset ))) + ".csv")
        csv += 1
    elif file[-4:] == ".jpg":
        os.rename(file, dir_path + (str( (jpg + offset )) + ".jpg"))
        jpg += 1
    elif file[-4:] == ".png":
        os.rename(file, dir_path + (str( (png + offset )) + ".png"))
        png += 1
    elif file[-4:] == ".pdf":
        os.rename(file, dir_path + (str( (pdf + offset )) + ".pdf"))
        pdf += 1

# csv txt jpg png pdf 
