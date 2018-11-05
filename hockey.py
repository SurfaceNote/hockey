import os, errno
import zipfile
import shutil
from os import listdir
from os.path import isfile, join


def main():
    
    start = input("'Начать' или 'завершить'?")
    start.lower()

    if start == 'начать':
        link_folder = input('Укажи директорию файлов матча (Например: "E:/Работа/хоккей") ')
        link_folder = link_folder.replace("\\", '/')
        a = input("Сколько у тебя всего партов?")
        b = input("С какого парта?")


        for new_folder in range(int(a)):
            name = "part-" + str(b)
            os.chdir(link_folder)
            os.mkdir(name)
            b = int(b) + 1

    if start == 'завершить':

        link_folder = input('Укажи директорию файлов матча (Например: "E:/Работа/хоккей/Irbis - Reactor") ')
        os.chdir(link_folder)
        print(link_folder)
        link_folder = link_folder.replace("\\", '/')
        print (link_folder)
        os.mkdir("result")
        os.chdir(link_folder +"/result")

        name = "part-"
        club1 = input("Домашняя команда: ")
        club2 = input("Гостевая команда: ")
        a = input("Сколько у тебя всего партов?")
        b = input("С какого парта?")

        for n in range(int(a)):
            os.chdir(link_folder + "/result")
            final_name = name + str(b)
            zip_name1 = final_name + " " + club1 + " - " + club2 + ".zip"
            shutil.copytree(link_folder + '/' + str(final_name) + '/final/', str(final_name))
            shutil.copytree(link_folder + '/' + str(final_name) + '/embedded/index', str(final_name) + '/index')



            os.chdir(link_folder + '/result/' + str(final_name) + '/')


            all_files = [f for f in listdir(link_folder + '/result/' + str(final_name) + '/') if isfile(join(link_folder + '/result/' + str(final_name) + '/',f))]
            csv_file =[]
            for t in all_files:
                if '.csv' in t:
                    csv_file.append(t)


            zipfile.ZipFile(zip_name1, "w", zipfile.ZIP_DEFLATED)
            with zipfile.ZipFile(zip_name1, 'a') as myzip:
                myzip.write(csv_file[0])
                myzip.write('index/autosave.csv')

            b = int(b) + 1

if __name__ == '__main__':
    main()
