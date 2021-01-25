import os
import re


def main():
    srcPath = 'Source directory goes here'
    dstPath = 'Destination directory goes here (can be the same as srcPath)'
    dirElements = os.listdir(srcPath)           # Listing all elements under srcPath


    # Creating lists for the extraction of strings corresponding to sequence numbers and datestamps of the filenames
    spltSD = [str(i).split("_")[1:] for i in dirElements]     # Modify filename prefix as needed

    # Final managed lists containing every file's sequence number and datestamp, respectively
    spltS = [spltSD[spltSD.index(i)][1] for i in spltSD]
    spltD = [spltSD[spltSD.index(i)][0] for i in spltSD]

    # Empty list to contain the full modified filenames
    fullName = []


    for seq in spltX:
        for date in spltD:
            fullName.append("CI4GERIC_ASMAT_000000" + seq + "_" + date) # Populating fullName list. Change depending upon criteria

    for file, name in zip(dirElements, fullName):
        os.rename(os.path.join(srcPath, file), os.path.join(dstPath, name)) # Renaming files


if __name__ == '__main__':
    main()
