import pandas as pd

excel_path = 'excel_file.xlsx'

df = pd.read_excel(excel_path)
print(df.head())

















# -----------------------------------
# df1 = df[df['Age']<35]
# print(df1.head())
# df1.to_excel('new_excel_file.xlsx')
# -----------------------------------

# -----------------------------------
# df_new = df.loc[0:2, 'Name':'Age']
# print(df_new.head())
# -----------------------------------

# -----------------------------------
# df_new = df.iloc[0:2, 0:3]
# print(df_new.head())
# -----------------------------------

# -----------------------------------
# print(df.loc[0, 'Name'])
# -----------------------------------

# -----------------------------------
# df_new.index = ['a', 'b', 'c', 'd', 'e', 'f']
# print(df_new.head())
# -----------------------------------


# -----------------------------------
# print(df.iloc[0, 1])
# -----------------------------------

# -----------------------------------
# name_age_df = df[['Name', 'Age']]
# print(name_age_df.head())
# -----------------------------------

# -----------------------------------
# songs = {
#   'Album': ['Thriller', 'Back In Back', 'The Dark Side Of The Moon', 'The Bodygaurd', 'Bat Out Of Hell'], 
#   'Released': [1982, 1980, 1973, 1992, 1977], 
#   'Length': ['10', '20', '30', '40', '50']
# }
# songs_frame = pd.DataFrame(songs)

# print(songs_frame.head())
# -------------------------------------

# -------------------------------------
# excel_path = './excel_file.xlsx'

# df = pd.read_excel(excel_path)
# print(df.head())
# -------------------------------------