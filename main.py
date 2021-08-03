import pandas as pd
import session
import user

NUMBER_OF_USERS = 50
NUMBER_OF_ARGS = 8

filename = "kub.xlsx"
xl = pd.ExcelFile(filename)

sheet_names = xl.sheet_names
del sheet_names[1]

# Make session queries:

# sheet_names[0] = "2_30.07"
# sheet_names[1] = "2_31.07"

# for sheet in sheet_names:
#     print(sheet)
#     print(session.Session(sheet).make_insert_query())


# Make user and share queries:

for sheet in range(len(sheet_names)):
    print(sheet)
    df = xl.parse(sheet_names[sheet])
    for item in range(1):

        array = df.loc[item, :].array[0:NUMBER_OF_ARGS]
        # user query
        # print(user.User(array[0], array[1], sheet + 1).make_insert_query())
        # share query
        print(array)
# Большой КУШ | Клин-клином	| КлУШа | КуКУШка | КУШать подано | Лягушка-кваКУШка
