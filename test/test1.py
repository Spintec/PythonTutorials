def group_by_owners(files):
    dictt=dict()
    for keys,valuez in files.items():
        if valuez not in dictt:
            dictt[valuez]=[]
        dictt[valuez].append(keys)
    return dictt





if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))