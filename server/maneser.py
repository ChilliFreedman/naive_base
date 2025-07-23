from server.csv_to_df import Csv_to_df
#from  cliner import Cliner
from server.basic_modul import Basic_modul
from server.data_classifier import Classifier

from server.tester import Test
import os
class Maneser:
    def __init__(self):
        self.loder = None
        self.df = None
        self.big = None
        self.small = None
        self.dict_model = None
        self.dict_priors = None


    def get_os_files(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.abspath(os.path.join(base_path, '..', 'data'))

        files = os.listdir(data_path)
        # list_files = os.listdir(r'../data')
        return files
    def create_df(self,file):
        try:
            path = os.path.abspath(f'./data/{file}')
            #print(f"Trying to read: {path}")

            loder = Csv_to_df(path)

            self.df = loder.csv_to_df()
            #print("DataFrame loaded successfully:")
            #print(self.df.head())
            #loder = Csv_to_df(f'../data/{file}')
            #self.df = loder.csv_to_df()
            self.big = loder.big_part_of_df()
            self.small = loder.small_part_of_df()
            return self.df
        except Exception as a:
            #return a
            print(f"Error in create_df: {a}")
            raise

    def run_model(self):
        try:
            basic_mod = Basic_modul()
            basic_mod.func_dict(self.big, self.df)
            self.dict_model = basic_mod.dict_model
            self.dict_priors = basic_mod.dict_priors
        except Exception as a:
            return a



    def run_tester(self):
        return Test.Check_30_70(self.small, self.dict_model, self.dict_priors)

    def get_from_user(self,dict_user):
        return Classifier.classifier_data(dict_user, self.dict_model, self.dict_priors)

