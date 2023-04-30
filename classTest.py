from forDataBase import DataBase
name=input('Введите свое имя\n')
age=input('Введите свой возраст\n')
desc=input('Введите описание профиля\n')
profileList=[name,age,desc]
userProfile=DataBase('dataBase')
userProfile.create_table('userProfile','name TEXT, age INTEGER, description TEXT')
userProfile.insert_into('userProfile','?, ?, ?',profileList)
print(userProfile.request('SELECT * FROM userProfile')[0])

req=input('введи deleteProfile если хочешь заполнить профиль заново\n')
if req == 'deleteProfile':
    userProfile.delete_table('userProfile')