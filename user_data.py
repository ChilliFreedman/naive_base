
from basic_modul import Basic_modul
from csv_to_df import Csv_to_df
basic_mod  = Basic_modul()
#print(func_dict('buy_computer_data.csv'))
class Getuser:
    @staticmethod
    def get_dict_col_value(dict_mod):

        for v in dict_mod.values():
            dict_choise = {}
            dict1 = {}
            for key, val in v.items():
                lis = []
                for k in val.keys():
                    lis.append(k)
                dict1[key] = lis

                #
            for col,value in dict1.items():
                print(f"col: {col}")
                cass = 1
                for val in value:
                    print(f"for {val} enter {cass}:")
                    cass += 1
                while True:
                    ch = int(input(f"enter a nuber 1 -- {len(value)}.\n"))
                    if ch > 0 and ch <= len(value):
                        break
                try:
                    dict_choise[col] = value[ch - 1]
                except IndexError:
                    print("not aloud choise")

            print(dict_choise)
            return dict_choise
