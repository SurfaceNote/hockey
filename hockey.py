import os, errno
import zipfile
import shutil
from os import listdir
from os.path import isfile, join


def main():
    
    start = input("Введи 'начать' или 'завершить'? ").lower()

    if start != "начать" and start != "завершить":
        print("Введи слово правильно, пожалуйста.\n")
        print(start)
        main()

    if start == 'начать':
        link_folder = input('Укажи директорию файлов матча (Например: "E:/Работа/хоккей/Irbis - Reactor") ')
        link_folder = link_folder.replace("\\", '/')
        a = input("Сколько у тебя всего партов? (введи число): ")
        b = input("С какого парта? (введи число): ")


        for new_folder in range(int(a)):
            name = "part-" + str(b)
            os.chdir(link_folder)
            os.mkdir(name)
            os.chdir(link_folder + "/" + name)
            os.mkdir("final")
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
        a = input("Сколько у тебя всего партов? (введи число): ")
        b = input("С какого парта? (введи число): ")

        for n in range(int(a)):
            os.chdir(link_folder + "/result")
            final_name = name + str(b)
            zip_name1 = final_name + " " + club1 + " - " + club2 + ".zip"
            zip_name2 = final_name + " " + club1 + " - " + club2
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

            shutil.move(link_folder + "/result/" + final_name + "/" + str(zip_name1), link_folder + "/result/")

            b = int(b) + 1

if __name__ == '__main__':
    main()
