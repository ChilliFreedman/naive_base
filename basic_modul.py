import pandas as pd


class Basic_modul:
    def __init__(self):
        self.dict_model = {}
        self.dict_priors  = {}
    # טוען את הנתונים
    def func_dict(self,df):
        #df = pd.read_csv(csv)

        # עמודת היעד
        target_col = df.columns[-1]

        # יוצרים את מבנה המילון
        result = {}

        # מקבלים את כל הערכים האפשריים בעמודת היעד
        target_values = df[target_col].unique()

        # לכל ערך ביעד (yes, no)
        for val in target_values:
            # סינון הטבלה לפי ערך זה
            subset = df[df[target_col] == val]
            self.dict_priors[val] = len(subset) / len(df)
            # print(len(subset))
            # print(len(df))

            # יצירת מילון פנימי
            inner_dict = {}

            for col in df.columns[:-1]:

                # ערכים ייחודיים בעמודה זו
                unique_vals = df[col].unique()
                #מקבל את כמות השורות של כל טבלה שמחולקת לפי הערכים בעמודה האחרונה ומוסיף את כמות הערכים של כל עמודה לפי מה שיש לה
                total = len(subset) + len(unique_vals)
                # מאותחל ב-1 +  כמות הפעמים שמופיע ומחולק במספר השורות פלוס מספר הערכים שכל עמודה משתנה בפני עצמה (Laplace smoothing)

                value_counts = {k: (1 + (subset[col] == k).sum()) / total for k in unique_vals}

                inner_dict[col] = value_counts

            result[val] = inner_dict
            self.dict_model = result
        return result
        # הדפסת התוצאה
        # import pprint
        #
        # pprint.pprint(result, width=120)
# if __name__ == "__main__":
#     a = Basic_modul()
#
#     aaa = a.func_dict()
#     for k, v in aaa.items():
#         print(k, v)
#     print(a.dict)
