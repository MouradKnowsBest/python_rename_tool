import os
from os import walk
import shutil
import pandas as pd
import ctypes
from ctypes import wintypes
_GetShortPathNameW = ctypes.windll.kernel32.GetShortPathNameW
_GetShortPathNameW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
_GetShortPathNameW.restype = wintypes.DWORD
#print(list(set(ce_que_on_veut_copier) - set(les_fichiers)))
#dir, les_dossiers, les_fichiers = sortir_les_fichiers(r"E:\Feuil1")
#print(les_fichiers)
#print(len(les_fichiers))

#print(len(les_fichiers))

#print(list(set(second_column) - set(les_fichiers)))



#sheet = Feuil1

#Case_A = filename camera

#liste = ["Ukraine", "Allemagne", "UK"]
#creer_dossier(r"C:\Users\p094836\Desktop\Test", liste)

#a, b , les_fich = sortir_les_fichiers(r'E:\RWUP5_BJA_TJP_PostInj_TOTAL PARTIE_1')
#print(len(les_fich))

#couper_fichiers(, les_fich)





#for i in les_fich:
    #print(i[12:])
    #os.rename(r'E:\ce_qui_reste' + '//' + i, r'E:\ce_qui_reste' + '//' + i[12:])


# def creer_dossier(path, les_noms):
#     for o in les_noms:
#         #print(o)
#         path_complet = path + str(o)[:-5]
#         os.mkdir(path_complet)
#
# def copier_fichiers(path, files):
#     for z in files:
#         shutil.copy(path + z, path + z[:-5])
#
# def couper_fichiers(path, files):
#     for z in files:
#         shutil.move(path + z, path + z[:-5])
#
#
# def compare_between_two_lists(list_1, list_2):
#     la_diff = list(set(list_1) - set(list_2))
#     return la_diff
#
#
# dir, les_dossiers, les_fichiers = sortir_les_fichiers(r'E:\RWUP5_BJA_TJP_PostInj_part1')
#
# print(les_fichiers)
# print(len(les_fichiers))
#
# tous_les_fichiers = les_fichiers
#
# #print(tous_les_fichiers)
# with open('tous_les_fichiers.txt', 'w') as f:
#     for item in tous_les_fichiers[1:]:
#         f.write("%s\n" % item)
#
# dir_2, les_dossiers_2, les_fichiers_2 = sortir_les_fichiers(r'E:\RWUP5_BJA_TJP_PostInj_donne_a_moi')  # Put the right path !
#
# ce_que_moi_javais = les_fichiers_2
#
# la_diff = list(set(tous_les_fichiers) - set(ce_que_moi_javais))
# print(len(la_diff))
#
# with open('ce_qui_manque.txt', 'w') as f:
#     for item in la_diff:
#         f.write("%s\n" % item)
#
# def copier_fichiers_2(path, files):
#     path_jdid =r'E:\ce_qui_reste'
#     for z in files:
#         #print(path + z)
#         shutil.copy(path + '//'+z, path_jdid + z)
#
#
# copier_fichiers_2('E:\RWUP5_BJA_TJP_PostInj_part1', la_diff)
#print(les_dossiers)
#print(les_fichiers)

#les_noms = list(er)
#les_noms.pop(0)
#les_noms.pop(0)
#print(les_noms)

#t = [i for i in doublon_safia if i in dirnames]

#print(len(t))


#dirpath =r"E:\RWUP5_BJA_TJP_Resim112"
#dirpath ="C://Users//p094836//Desktop//Réunions//"


#dirpath = "E://Contenu_Disque//RWUP2-3-4_BJA_LKA_ReSim82_NewCalib//"

#dir, les_dossiers, les_fichiers = sortir_les_fichiers(dirpath)




#print(les_fichiers[1:])
#print(len(les_fichiers[1:]))

#print(les_fichiers.index('RWUP2_BJA_LKA_VALEO_BJA0980_20180421_022141_0006.emp4'))

#fr = les_fichiers[60:]

#les_fichiers.pop(0:57)
#les_fichiers.pop(0)
#print(les_fichiers)
# for i in les_fichiers:
#     #if i[8:] in les_noms:
#         print(i)
#         rename(dirpath + str(i), str(dirpath + str(i[:-4]))
#         #print('cest bon')



#for i in les_fichiers[1:]:
    #print(i)
    #print(i[:-4])
    #print(dirpath + "//" + i, dirpath + "//" + i[:-4] + "_Resim11p2.csv")
    #rename(dirpath + "//" + i, dirpath + "//" + i[:-4] + "_Resim11p2.csv")

#creer_dossier(dirpath, les_fichiers)

#copier_fichiers(dirpath, fr)

#couper_fichiers(dirpath, fr)

def creer_dossier(path, les_noms):
    # Crée des dossier dans le path spéficié et la liste des noms spécifiés
    for o in les_noms:
        #print(o)
        path_complet = path + "//" + str(o)
        if not os.path.exists(path_complet):
            os.mkdir(path_complet)

def rename(a, b):
    os.rename(a, b)
    return a, b

def sortir_les_fichiers(path):
    dir = []
    les_dossiers = []
    les_fichiers = []
    for (et, er, filenames) in walk(path):
        dir.extend(et)
        les_dossiers.extend(er)
        les_fichiers.extend(filenames)
        break
    return dir, les_dossiers, les_fichiers

def copier_fichiers(path, files):
    # Copie un ou ensmeble de fichiers d'un endroit à un autre
    for z in files:
        shutil.copy(path + z, path + z[:-5])

def get_short_path_name(long_name):
    """
    Gets the short path name of a given long path.
    http://stackoverflow.com/a/23598461/200291
    """
    output_buf_size = 0
    while True:
        output_buf = ctypes.create_unicode_buffer(output_buf_size)
        needed = _GetShortPathNameW(long_name, output_buf, output_buf_size)
        if output_buf_size >= needed:
            return output_buf.value
        else:
            output_buf_size = needed

def couper_fichiers(original_path, destination_path, ce_que_on_veut_copier, extension):
    """
    :param original_path: Path of the original data from which we are going to take data
    :param destination_path: Path to the destiniation where we are going to put the data
    :param ce_que_on_veut_copier: A list containing the data
    :param extension: The extension of the data
    :return: The number of data correctly/incorrectly processed
    """
    good_count = 0
    bad_count_1 = 0
    bad_count_2 = 0
    for z in list(ce_que_on_veut_copier):
            try:
                good_count += 1

                origi = str(original_path + z + "_4121_SW112_20181107" + extension)
                desti = str(destination_path + z + "_4121_SW112_20181107" + extension)

                shutil.move(origi, desti)
                print(str(origi))

                #shutil.copy(original_path + z + extension, destination_path + z + extension)
            except FileNotFoundError:
                bad_count_1 += 1
                print(str(origi))
                print("Fichier non trouvé, on le saute et on continue...")
                continue
            except TypeError:
                bad_count_2 += 1
                print(str(origi))
                #print(original_path + z + extension)
                print("Type ERROR, on le saute et on continue...")
                continue
    return good_count, bad_count_1, bad_count_2

def read_data_from_excel(path, sheet_number, title_of_column):
    """
    :path: Path to the Excel File
    :sheet_number: Number of the Excell sheet that contains the data
    :name_of_column: Name of the column we want to load the data from
    :return: A list that contains data
    """
    df = pd.read_excel(path, sheet_name=sheet_number)  # can also index sheet by name or fetch all sheets
    ce_que_on_veut_copier = df[str(title_of_column)].tolist()
    return ce_que_on_veut_copier


def main():
    les_pays = ['FR', 'FR-GR', 'FR-IT', 'FR-NL', 'FR-SP', 'GR', 'GR-FR', 'IT', 'NL', 'RO', 'SP', 'UK', 'UK-FR']

    creer_dossier(r"C:\Users\p094836\Desktop\Test", les_pays)

    #for pays in les_pays:

     #   data = read_data_from_excel(path=r"C:\Users\p094836\Desktop\data.xlsx",
       #                             sheet_number=0,
        #                            title_of_column=pays)

      #  couper_fichiers(original_path=r"F:\Donnees_SW7_resimules_en_SIL11p2" + "//",
          #              destination_path=r"F:\Donnees_SW7_resimules_en_SIL11p2" + "//" + str(pays) + "//",
         #              ce_que_on_veut_copier=data,
          #              extension=".mat")

# main()

source = r"E:\XFK\Fcam_Resim4\AEB_ziyada"

dir, les_dossiers, les_fichiers = sortir_les_fichiers(source)


for fichier in les_fichiers:
    rename(source + "//" + fichier,
           source + "//" + fichier.replace("CAN-IC", "FCam"))



# Create a folder where you will stock your data

#creer_dossier(, )

# Load the data that we want to transfer

#liste_des_pays = ["UK", "SP", "FR", "GR", "IR", "FR_SP", "FR_UK",	"FR_SP_IT",	"FR_BL", "UK_BL", "UK_FR",
#                 "UK_IR_FR",	"SP_FR", "SP_PR", "IR_FR", "IR_UK"]


#data_resim = read_data_from_excel(path=r"C:\Users\p094836\Desktop\Taille_des_capsules_presentes_en Resim_et_Brutes.xlsx",
 #                                                               sheet_number=0,
  #                                                              title_of_column="Nom Capsule")


# data_croatie = read_data_from_excel(path=r"C:\Users\p094836\Desktop\Liste_Croitie_Serbie_Roumanie_Resim.xlsx",
#                                                                  sheet_number=0,
#                                                                  title_of_column="filename camera")
#
# data_roumanie = read_data_from_excel(path=r"C:\Users\p094836\Desktop\Liste_Croitie_Serbie_Roumanie_Resim.xlsx",
#                                                                  sheet_number=1,
#                                                                  title_of_column="filename camera")
#
# data_serbie = read_data_from_excel(path=r"C:\Users\p094836\Desktop\Liste_Croitie_Serbie_Roumanie_Resim.xlsx",
#                                                                  sheet_number=2,
#                                                                 title_of_column="filename camera")

# dir, les_dossiers, les_fichiers_croatie = sortir_les_fichiers(r"E:\Capsule_avec_diff_inf5_RESIM\CROATIE")
# dir, les_dossiers, les_fichiers_roumanie = sortir_les_fichiers(r"E:\Capsule_avec_diff_inf5_RESIM\ROUMANIE")
# dir, les_dossiers, les_fichiers_serbie = sortir_les_fichiers(r"E:\Capsule_avec_diff_inf5_RESIM\SERBIE")
#
# #print(data)
# # Transfer the data into the destination path
#
# #couper_fichiers(original_path=r"E:\RWUP5_BJA_TJP_Resim112_fichier_pmat" + "//",  # original_path=r"E:\par_pays\UK_BL" + "//"
#  #                destination_path=r"E:\Capsule_avec_diff_inf5_RESIM" + "//",
#   #              ce_que_on_veut_copier=data_resim,
#    #               extension=".mat")
#
# les_fichiers_croatie_safia = [i[:-14] for i in les_fichiers_croatie]
# les_fichiers_roumanie_safia = [i[:-14] for i in les_fichiers_roumanie]
# les_fichiers_serbie_safia = [i[:-14] for i in les_fichiers_serbie]
#
#
# resim_diff_croatie = list(set(data_croatie) - set(les_fichiers_croatie_safia))
# resim_diff_roumanie = list(set(data_roumanie) - set(les_fichiers_roumanie_safia))
# resim_diff_serbie = list(set(data_serbie) - set(les_fichiers_serbie_safia))
#
#
# print(resim_diff_croatie)
# print(len(resim_diff_croatie))
#
# print(resim_diff_roumanie)
# print(len(resim_diff_roumanie))
#
# print(resim_diff_serbie)
# print(len(resim_diff_serbie))
#
# with open(r'C:\Users\p094836\Desktop\resim_diff_croatie.txt', 'w') as f:
#     for item in resim_diff_croatie:

#         f.write("%s\n" % item)
#
# with open(r'C:\Users\p094836\Desktop\resim_diff_roumanie.txt', 'w') as f:
#     for item in resim_diff_roumanie:
#         f.write("%s\n" % item)
#
# with open(r'C:\Users\p094836\Desktop\resim_diff_serbie.txt', 'w') as f:
#     for item in resim_diff_serbie:
#         f.write("%s\n" % item)
#
# couper_fichiers(original_path=r"E:\Enregistrement_mat_Info_RoadType" + "//",  # original_path=r"E:\par_pays\UK_BL" + "//"
#                    destination_path=r"E:\Enregistrement_mat_Info_RoadType\CROATIE" + "//",
#                   ce_que_on_veut_copier=data_croatie,
#                     extension=".mat")
#
#
#
# couper_fichiers(original_path=r"E:\Enregistrement_mat_Info_RoadType" + "//",  # original_path=r"E:\par_pays\UK_BL" + "//"
#                    destination_path=r"E:\Enregistrement_mat_Info_RoadType\ROUMANIE" + "//",
#                   ce_que_on_veut_copier=data_roumanie,
#                     extension=".mat")
#
# couper_fichiers(original_path=r"E:\Enregistrement_mat_Info_RoadType" + "//",  # original_path=r"E:\par_pays\UK_BL" + "//"
#                    destination_path=r"E:\Enregistrement_mat_Info_RoadType\SERBIE" + "//",
#                   ce_que_on_veut_copier=data_serbie,
#                     extension=".mat")
#
# print("data_croatie : {}".format(len(data_croatie)))
# print("data_roumanie : {}".format(len(data_roumanie)))
# print("data_serbie : {}".format(len(data_serbie)))

#dir, les_dossiers, les_fichiers = sortir_les_fichiers(r"E:\Roulage_RWUP5_TJP_pmat_postinj\Liste_CommentaireLCA_3690")