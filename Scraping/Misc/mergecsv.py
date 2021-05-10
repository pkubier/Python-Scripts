import glob, os
import pandas as pd

from pandas import DataFrame, ExcelWriter

writer = ExcelWriter("C:/Users/patrick/Downloads/csv/compiled.xlsx")

for filename in glob.glob("C:/Users/patrick/Downloads/csv/*.csv"):
    df_csv = pd.read_csv(filename)

    (_, f_name) = os.path.split(filename)
    (f_shortname, _) = os.path.splitext(f_name)

    df_csv.to_excel(writer, f_shortname, index=False)

writer.save()