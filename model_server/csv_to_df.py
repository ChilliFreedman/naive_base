import pandas as pd

class Csv_to_df:
    def __init__(self,csv_file):
        self.csv_file = csv_file




    def csv_to_df(self):

        df = pd.read_csv(self.csv_file)

        for col in df.columns:
            if df[col].dtype == 'bool':
                df[col] = df[col].astype('str')
        return df



    def big_part_of_df(self):
        df = self.csv_to_df()
        seventi_present = int(len(df) * 0.7)
        big = df.head(seventi_present)

        return big

    def small_part_of_df(self):
        df = self.csv_to_df()
        therti_present = int(len(df) * 0.3)
        small = df.tail(therti_present)

        return small



