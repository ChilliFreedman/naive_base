import pandas
from data_classifier import Classifier
#from main import Maneser

from csv_to_df import Csv_to_df
#classifier:Classifier,small_df:pandas.DataFrame
class Test:
    @staticmethod
    def Check_30_70(small_df,dict_mod,dict_priors):
        # manser = Maneser()
        # manser.raner()


        correct = 0
        not_corect = 0
        num = 0
        total = len(small_df)
        target_col = small_df.columns[-1]
        for _, row in small_df.iterrows():
            dict_row = row.drop(target_col).to_dict()
            corect_tar_val = row[target_col]

            # print(dict_row)
            # print(corect_tar_val)
            # print(Classifier.classifier_data(dict_row,manser.dict_model,manser.dict_priors))
            # print(f"num {num}")
            # print(f"correct {correct}")
            # print(f"not_corect{not_corect}")


            if Classifier.classifier_data(dict_row,dict_mod,dict_priors) == corect_tar_val:
                correct += 1
            else:
                not_corect += 1
            num += 1
        return f"The test is raigt with {correct / total * 100}%"

