
def to_dict():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]
    
    dict_ = {}
    for item in d:
        dict_[item[0]]=item[1]

    new_dict = {}
    for key, value in dict_.items():
        if new_dict.get(value) is None:
            new_dict[value]=key
        else:
            new_dict.update({value: f"{new_dict.get(value)} {key}"})
    
    sorted_list = sorted(new_dict.items())
    for key, value in sorted_list:
        print(f"{key} : {value}")
        

if __name__ == "__main__":
    to_dict()
