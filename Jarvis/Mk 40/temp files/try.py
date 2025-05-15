# import pandas as pd
#
# def find_employees(employee):
#     s1 = employee["salary"][0]
#     s2 = employee["salary"][1]
#     s3 = employee["salary"][2]
#     s4 = employee["salary"][3]
#
#     s1e = employee["name"][0]
#     s2e = employee["name"][1]
#     s3e = employee["name"][2]
#     s4e = employee["name"][3]
#     toreturn = ""
#     if s4>s2:
#         toreturn += f"{s4e} is earing more than manager {s2e}"
#     if s4 > s1:
#         toreturn += f"{s4e} is earing more than manager {s1e}"
#     if s3>s2:
#         toreturn += f"{s3e} is earing more than manager {s2e}"
#     if s3 > s1:
#         toreturn = f"{s3e} is earing more than manager {s1e}"
#
#     return
# table = {
#     "id": [1,2,3,4],
#     "name": ["joe","henry","sam","max"],
#     "salary": [70000,80000,60000,90000],
#     "managerId":[3,4]
# }
# output = find_employees(table)
# print(output)
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


def find_employees(employee):
    s1 = employee["salary"][0]
    s2 = employee["salary"][1]
    s3 = employee["salary"][2]
    s4 = employee["salary"][3]

    s1e = employee["name"][0]
    s2e = employee["name"][1]
    s3e = employee["name"][2]
    s4e = employee["name"][3]

    toreturn = {
        "employee":[]
    }

    if s4 > s2:
        toreturn["employee"].append(s4e)
    if s4 > s1:
        toreturn["employee"].append(s4e)
    if s3 > s2:
        toreturn["employee"].append(s3e)
    if s3 > s1:
        toreturn["employee"].append(s3e)
    dftoreturn = pd.DataFrame(toreturn)
    return dftoreturn


table = {
    "id": [1, 2, 3, 4],
    "name": ["joe", "henry", "sam", "max"],
    "salary": [70000, 80000, 60000, 90000],
    "managerId": [3, 4, 0,0]
}

df_table = pd.DataFrame(table)
# df_table.fillna()
output = find_employees(df_table)
print(output)

