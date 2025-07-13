
from basic_modul import Basic_modul
class Classifier:
    @staticmethod
    def classifier_data(dictionary_choice,dictionary_basic_mod,dictionary_priors):
        dict_result = dictionary_priors
        #ריצה על מילון הבחירה
        for key_basic, value_basic in dictionary_basic_mod.items():
            for key_choice, value_choice in dictionary_choice.items():
                try:
                    num = dictionary_basic_mod[key_basic][key_choice][value_choice]
                except KeyError:
                    num = 1e-10

                dict_result[key_basic] *= num

        #print(dictionary_choice)
        #print(dict_result)
        return max(dict_result,key=dict_result.get)




