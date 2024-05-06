# import OS module
import os, glob
import geopandas
# Get the list of all files and directories
path = "C:\Luis\Data\eqr\*.shp"
#dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
#print(dir_list)
#for file in dir_list:
#    print(file)

dirLuis = glob.glob(path)

for file in dirLuis:
    dirName = os.path.dirname(file)
    baseName = os.path.basename(file)
    baseNameNoExt = baseName.split(".")[0]
    jsonName = dirName + "\\" + baseNameNoExt + ".json"
    mySahpeFile = geopandas.read_file(file)
    mySahpeFile.to_file(jsonName,driver="GeoJSON")
    print(file)
