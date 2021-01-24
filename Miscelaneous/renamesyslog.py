import os
import re


def main():
    srcPath = 'Source directory goes here'
    dstPath = 'Destination directory goes here (can be the same as srcPath)'
    dirElements = os.listdir(srcPath)           # Listing all elements under srcPath


    # Creating lists for the extraction of strings corresponding to sequence numbers and datestamps of the filenames
    spltXD = [str(i).split("ASPPSGW01_")[1:] for i in dirElements]

    spltX = [str(i).split("_")[1:] for i in spltXD]
    spltX = [str(i).split("'")[0] for i in spltX]
    spltX = [str(i).split('["')[1:] for i in spltX]

    spltD = [str(i).split("_")[0] for i in spltXD]
    spltD = [str(i).split("['")[1:] for i in spltD]

    # Final managed lists containing every file's sequence number and datestamp, respectively
    seqNum = [''.join(map(str, i)) for i in spltX]
    dateNum = [''.join(map(str, i)) for i in spltD]

    # Empty list to contain the full modified filenames
    fullName = []


    for seq in seqNum:
        for date in dateNum:
            fullName.append("CI4GERIC_ASMAT_000000" + seq + "_" + date) # Populating fullName list given criteria

    for file, name in zip(dirElements, compName):
        os.rename(os.path.join(srcPath, file), os.path.join(dstPath, name)) # Renaming files


if __name__ == '__main__':
    main()
