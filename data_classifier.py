
#from basic_modul import Basic_modul
class Classifier:
    @staticmethod
    def classifier_data(dictionary_choice,dictionary_basic_mod,dictionary_priors):
        num = 0
        dict_result = dictionary_priors.copy()
        # print("asdf dfff ghh hhjj ")
        # print(dict_result)
        #ריצה על מילון הבחירה
        for key_basic, value_basic in dictionary_basic_mod.items():
            for key_choice, value_choice in dictionary_choice.items():
                try:
                    num = dictionary_basic_mod[key_basic][key_choice][value_choice]
                    #print(num)
                except KeyError:
                    #print("aaa")
                    #בגדול זה לא נצרך כי זה כבר כוסה בבייסיק מודול בכל סיטואציה גם שלא קיים ב70%
                    num = 1e-10

                dict_result[key_basic] *= num
            #print(dict_result[key_basic])

        #print(dictionary_choice)
        print(dict_result)
        return max(dict_result,key=dict_result.get)




