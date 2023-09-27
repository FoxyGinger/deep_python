# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# file_path = "C:/Users/User/Documents/example.txt" -> ('C:/Users/User/Documents/', 'example', '.txt')
import pathlib


def get_file_info(file_path):
    file = pathlib.PurePosixPath(file_path.strip())
    path = file.parent.__str__()
    if path == '.':
        path = ''
    else:
        path += '/'

    file_name = file.stem.__str__()
    extension = file.suffix.__str__()

    if extension == '':
        extension, file_name = '.' + file_name, ''

    return path, file_name, extension


assert get_file_info('C:/Users/User/Documents/example.txt') == ('C:/Users/User/Documents/', 'example', '.txt'), get_file_info('C:/Users/User/Documents/example.txt')
assert get_file_info('/home/user/data/file') == ('/home/user/data/', '', '.file'), get_file_info('/home/user/data/file')
assert get_file_info('D:/myfile.txt') == ('D:/', 'myfile', '.txt'), get_file_info('D:/myfile.txt')
assert get_file_info('C:/Projects/project1/code/script.py') == ('C:/Projects/project1/code/', 'script', '.py'), get_file_info('C:/Projects/project1/code/script.py')
assert get_file_info('/home/user/docs/my.file.with.dots.txt') == ('/home/user/docs/', 'my.file.with.dots', '.txt'), get_file_info('/home/user/docs/my.file.with.dots.txt')
assert get_file_info('file_in_current_directory.txt') == ('', 'file_in_current_directory', '.txt'), get_file_info('file_in_current_directory.txt')