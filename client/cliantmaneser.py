import requests
import json
class Client:
    def __init__(self):
        self.file = None
        self.dict_choise = None


    def chuse_file(self):
        response = requests.get("http://localhost:8001/csv_files")
        word_list = response.json()
        list_files = word_list["files"]

        # for file in list_files:
        #     print(file)
        #print(list_files)
        for i in range(len(list_files)):
            print(f"for file {list_files[i]} enter {i + 1}")
        while True:
            choise = int(input(f"enter 1 -- {len(list_files)}\n"))
            if  0 < choise <= len(list_files):
                break
        try:
            file_choise = list_files[choise - 1]
        except IndexError:
            print("not aloud choise")
        self.file = file_choise
        #print(file_choise)

    def make_df(self):
        response = requests.get(f"http://localhost:8001/put_file?file={self.file}")
        test_details = response.json()
        test_result = test_details["tester"]
        print(f"The test is raigt with {test_result}%")
        #print(response.json())

    def get_users_features(self):
        response = requests.get("http://localhost:8001/features")
        dicta = response.json()
        dict_mod = dicta["model"]
        for v in dict_mod.values():
            dict_choise = {}
            dict1 = {}
            for key, val in v.items():
                lis = []
                for k in val.keys():
                    lis.append(k)
                dict1[key] = lis


            for col,value in dict1.items():
                print(f"col: {col}")
                cass = 1
                for val in value:
                    print(f"for {val} enter {cass}:")
                    cass += 1
                while True:
                    ch = int(input(f"enter a nuber 1 -- {len(value)}.\n"))
                    if 0 < ch <= len(value):
                        break
                try:
                    dict_choise[col] = value[ch - 1]
                except IndexError:
                    print("not aloud choise")

            #print(dict_choise)
            self.dict_choise = dict_choise
            return

    def clas(self):
        dict_str = json.dumps(self.dict_choise)
        response = requests.get(f"http://localhost:8001/clas?dict_choise={dict_str}")
        anser_json = response.json()
        anser_dict = anser_json["anser"]["result"]
        anser = anser_json["anser"]["class"]
        print(f"the prosens arr {anser_dict}")
        print(f"yor anser is {anser} !!!")
