from csv_to_df import Csv_to_df
from  cliner import Cliner
from basic_modul import Basic_modul
from data_classifier import Classifier
from user_data import Getuser
from tester import Test
import os
class Maneser:
    def __init__(self):
        self.loder = None
        self.df = None
        self.big = None
        self.small = None
        self.dict_model = None
        self.dict_priors = None
    #@staticmethod
    def raner(self):

        list_files = os.listdir(r'C:\PycharmProjects\PycharmProjects\naive_base\data')
        for i in range(len(list_files)):
            print(f"for file {list_files[i]} enter {i + 1}")
        while True:
            choise = int(input(f"enter 1 -- {len(list_files)}\n"))
            if choise > 0 and choise <= len(list_files):
                break
        try:
            file_choise = list_files[choise - 1]
        except IndexError:
            print("not aloud choise")

        loder = Csv_to_df(f'data/{file_choise}' )
        #loder = Csv_to_df(r'C:\PycharmProjects\PycharmProjects\naive_base\data\buy_computer_data.csv')
        self.df = loder.csv_to_df()
        self.big = loder.big_part_of_df()
        self.small = loder.small_part_of_df()
        # print("all data frame")
        # print(df)
        # print("70% data frame")
        # print(big)
        # print("30% data frame")
        # print(small)
        basic_mod = Basic_modul()
        #basic_mod.func_dict(df)
        basic_mod.func_dict(self.big)
        #basic_mod.func_dict(small)

        self.dict_model = basic_mod.dict_model
        self.dict_priors = basic_mod.dict_priors
        # test = Test()
        print(Test.Check_30_70(self.small,self.dict_model,self.dict_priors))




        dict_user = Getuser.get_dict_col_value(self.dict_model)
        classifier = Classifier()
        print(classifier.classifier_data(dict_user,self.dict_model,self.dict_priors))




manser = Maneser()
manser.raner()
#print(manser.dict_model)