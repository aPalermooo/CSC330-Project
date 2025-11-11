import pickle

with open("info/schema_info_dump.pkl", "rb") as file:
    schema_info = pickle.load(file)

def list_schemas():
    for s in schema_info.keys():
        print(s)

def get_schema_info(t: str = ""):
    if t in schema_info.keys():
        print(t)
        print(schema_info[t])
        print()
    else:
        for t in schema_info.keys():
            get_schema_info(t)

with open("info/schema_columns_info_dump.pkl", "rb") as file:
    schema = pickle.load(file)