import os
import glob
import re
import shutil

def sed(pattern, replace, source, dest=None, count=0):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    Args:
        pattern (str): pattern to match (can be re.pattern)
        replace (str): replacement str
        source  (str): input filename
        count (int): number of occurrences to replace
        dest (str):   destination filename, if not given, source will be over written.
    Source: https://stackoverflow.com/questions/12714415/python-equivalent-to-sed
    """
    fin = open(source, 'r', encoding='utf-8')
    num_replaced = count
    if dest:
        fout = open(dest, 'w', encoding='utf-8')
    else:
        name = os.path.join(source, "tmp.txt")
        fout = open(name, 'w', encoding='utf-8')
    for line in fin:
        out = re.sub(pattern, replace, line)
        fout.write(out)
        if out != line:
            num_replaced += 1
        if count and num_replaced > count:
            break
    try:
        fout.writelines(fin.readlines())
    except Exception as E:
        raise E
    fin.close()
    fout.close()
    if not dest:
        shutil.move(name, source) 
    return

if __name__ == "__main__":
    gamePath = r"E:\Jeux\Steam\SteamApps\workshop\content\799600"

    modlistID = [
        r"2882082274",
        r'2879940121',
        r'2879478059',
        r'2880166908',
    ]

    for fo in modlistID:
        rules = glob.glob(os.path.join(gamePath, fo, '**/**/*.rules'), recursive = True) 
        for rule in rules:
	    # Replace an empty buff list: problem if a script already has a rule or if it doesn't exist in the rule file
            sed('ReceivableBuffs \[\]', 'ReceivableBuffs \[PowerPlacebo\]', rule) 
