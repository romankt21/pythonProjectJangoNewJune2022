import os


# print(os.environ)
# print(os.getcwd())

# print(os.listdir())     # покаже файли і папки на  1 рівні в списку   ['.git', '.idea', 'test.py']

# os.mkdir('first')       # створює папку
# os.mkdir('second')

# print(os.path.join('folder', '222', '1.txt'))    # join прирівнює / або\ в різних ОС рез folder\222\1.txt.
                                                # # Повертає слеші відповідно до ОС

# os.rename('test.py', 'test2.py')               # перейменувати файл з test.py на test2.py  або перенести файл

# os.rename('test2.py',  os.path.join('first', 'test.py'))      # файл test2.py перенести файл в папку first і

                                                            # перейменувати на test.py


# for item in os.walk('.'):                 # перебирання папок
#     print(item)                         #  ('.', ['.git', '.idea', 'first', 'second'], ['test.py'])

# for root, folder, files in os.walk('.'):
#     print(f'{root=}{folder=}{files=}')      # root='.'folder=['.git', '.idea', 'first', 'second']files=['test.py']
#                                             #  спочатку виводить корінь, потім папки, а потім файли



