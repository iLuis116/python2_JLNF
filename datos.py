DATA=[
    {"Name": "Facundo",
    "age": 72,
    "organization": "Platzi",
    "position": "Technical cuach",
    "organization": "Python",  
    },

    {"Name": "Luciana",
    "age": 33,
    "organization": "Globant",
    "position": "Designer",
    "organization": "Javascript",  
    },

    {"Name": "Hector",
    "age": 19,
    "organization": "Platzi",
    "position": "Associate",
    "organization": "ruby",  
    },

    {"Name": "Gabriel",
    "age": 20,
    "organization": "Platzi",
    "position": "Associate",
    "organization": "Javascript",  
    },

    {"Name": "Isabella",
    "age": 30,
    "organization": "Platzi",
    "position": "Manager",
    "organization": "Java",  
    },

    {"Name": "Karo",
    "age": 23,
    "organization": "Everis",
    "position": "Backend developer",
    "organization": "Python",  
    },

    {"Name": "Lorena",
    "age": 56,
    "organization": "Python organization",
    "position": "Language Maker",
    "organization": "Python",  
    },
    
]


def run():
    all_python_devs=[worker["Name"]for worker in DATA if worker["language"]=="python"]
    all_Platzi_workers=[worker["Name"] for worker in DATA if worker ["organization"]=="Platzi"]
    adults= list (filter(lambda worker: worker["age"]>18,DATA))
    adults= list (map(lambda worker:worker ["name"],adults))
    old_people= list(map(lambda worker:worker | {"old":worker["age"]>70},DATA))

    for worker in old_people:
        print(worker)


if __name__ =='__main__':
    run()