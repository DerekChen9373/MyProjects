import sys

def add_data_for_name(name_data, year, rank, name):

    if name not in name_data:
        name_data[name] = {year: rank}
    else:
        if year in name_data[name]:
            rank1 = name_data[name][year]
            rank2 = rank
            if rank1 > rank2:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
def add_file(name_data, filename):

    with open(filename, "r") as f:
        count1=0
        for line in f:
            count1+=1
            if count1!=1:
                l=[]
                count=0
                for ch in line:
                    if ch==',':
                        l.append(count)
                    count+=1
                rank=line[:l[0]]
                name1=line[l[0]+1:l[1]]
                name2=line[l[1]+1:]
                rank=rank.strip()
                name1=name1.strip()
                name2=name2.strip()
            else:
                year=line
                year=year.strip()
            if count1>=2:
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)
def read_files(filenames):

    name_data={}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data

def search_names(name_data, target):

    names=[]
    for key in name_data:
        key1=key.lower()
        x=key1.find(target)
        if x!=-1:
            names.append(key)
    return names

def print_names(name_data):

    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))

def main():

    args = sys.argv[1:]
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]
    names = read_files(filenames)
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
