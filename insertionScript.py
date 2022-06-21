import xlrd 
import openpyxl


#TODO : what i need 
#TODO : def a function to get team id from the division and team name and the groupe *
#TODO : for each , modify from att to id 


#! index starts at 1

#list of teams 

def get_teams():
    wookbook = openpyxl.load_workbook("./Finished/equipes.xlsx")
    ws = wookbook.active
    tmp_li = []
    for i in range(2, ws.max_row+1):
        tmp_li.append({
            "idEquipe":ws.cell(row=i,column=1).value,
            "sigle":ws.cell(row=i,column=2).value,
            "groupe":ws.cell(row=i,column=4).value,
            "division":ws.cell(row=i,column=5).value,
        })
    return tmp_li



def get_equipe_id(equipes,sigle):
    for eq in equipes:
        if eq["sigle"]==sigle :
            return eq["idEquipe"]
    raise Exception("Id team not found")


#adding equipe 
def insert_equipe_script():
    file = open('insert_equipe_script.sql', 'a',encoding="utf-8")
    wookbook = openpyxl.load_workbook("./Finished/equipes.xlsx")
    ws = wookbook.active
    for i in range(2, ws.max_row+1):
        file.write("INSERT INTO Equipe('idEquipe','sigle','nomComplet','division','anneeFondation','telephone','mobile','fax','location') VALUES ({a},'{b}','{c}','{d}',{e},{f},{g},{h},{i});\n".format(
            a=ws.cell(row=i,column=1).value,
            b=ws.cell(row=i,column=2).value.replace("'"," "),
            c=ws.cell(row=i,column=3).value.replace("'"," "),
            d=ws.cell(row=i,column=5).value,
            e=ws.cell(row=i,column=6).value or 'NULL',
            f=ws.cell(row=i,column=7).value or 'NULL',
            g=ws.cell(row=i,column=8).value or 'NULL', 
            h=ws.cell(row=i,column=9).value or 'NULL',
            i= "'{0}'".format(ws.cell(row=i,column=13).value.replace("'"," ")) if ws.cell(row=i,column=13).value != None else 'NULL'
        ))
    file.close()

#adding staff

def insert_staff_script(equipes):
    file1 = open('insert_staff_script.sql', 'a',encoding="utf-8")
    file2 = open('insert_occuper_script.sql', 'a',encoding="utf-8")
    wookbook = openpyxl.load_workbook("./Finished/staff.xlsx")
    ws = wookbook.active
    for i in range(2, ws.max_row+1):
        try:
            file1.write("INSERT INTO Staff('idStaff','prenom','nom','dateNaissance','lieuNaissance','wilayaNaissance') VALUES ({a},'{b}','{c}','{d}','{e}','{f}');\n".format(
                a=ws.cell(row=i,column=1).value,
                b=ws.cell(row=i,column=3).value.split(" ")[0].replace("'"," "),
                c=ws.cell(row=i,column=3).value.split(" ")[1].replace("'"," "),
                d=ws.cell(row=i,column=6).value,
                e=ws.cell(row=i,column=7).value.replace("'"," ") or 'NULL',
                f=ws.cell(row=i,column=8).value.replace("'"," ") or 'NULL',
            ))
            file2.write("INSERT INTO Occuper('idStaff','idEquipe','idSeason','position') VALUES ({a},{b},'2021/2022','{d}');\n".format(
                a=ws.cell(row=i,column=1).value,
                b=get_equipe_id(equipes,ws.cell(row=i,column=4).value),
                d=ws.cell(row=i,column=2).value.replace("'"," "),
            ))
        except:
            pass
        # print(ws.cell(row=i,column=1).value,"   -",ws.cell(row=i,column=4).value,"-")
        # print(ws.cell(row=i,column=1).value,"   -",get_equipe_id(equipes,ws.cell(row=i,column=4).value))
    file1.close()
    file2.close()


#adding entraineur 

def insert_entraineur_script(equipes):
    file1 = open('insert_entraineur_script.sql', 'a',encoding="utf-8")
    file2 = open('insert_entrainer_script.sql', 'a',encoding="utf-8")
    wookbook = openpyxl.load_workbook("./Finished/entraineurs.xlsx")
    ws = wookbook.active
    for i in range(2, ws.max_row+1):
        try:
            file1.write("INSERT INTO Entraineur('idEntraineur','nom','prenom','dateNaissance','lieuNaissance','wilayaNaissance') VALUES ({a},'{b}','{c}','{d}','{e}','{f}');\n".format(
                a=ws.cell(row=i,column=1).value,
                b=ws.cell(row=i,column=3).value.split(" ")[0].replace("'"," "),
                c=ws.cell(row=i,column=3).value.split(" ")[1].replace("'"," "),
                d=ws.cell(row=i,column=7).value,
                e=ws.cell(row=i,column=8).value.replace("'"," ") or 'NULL',
                f=ws.cell(row=i,column=9).value.replace("'"," ") or 'NULL',
            ))
            file2.write("INSERT INTO Entrainer('idEntraineur','idEquipe','idSeason','categorie','poste') VALUES ({a},{b},'2021/2022','{d}','{e}');\n".format(
                a=ws.cell(row=i,column=1).value,
                b=get_equipe_id(equipes,ws.cell(row=i,column=4).value),
                d=ws.cell(row=i,column=5).value.replace("'"," "),
                e=ws.cell(row=i,column=2).value.replace("'"," ")
            ))
        except:
            pass
        # print(ws.cell(row=i,column=1).value,"   -",ws.cell(row=i,column=4).value,"-")
        # print(ws.cell(row=i,column=1).value,"   -",get_equipe_id(equipes,ws.cell(row=i,column=4).value))
    file1.close()
    file2.close()

def create_insertion_script_staff(fileName,table,souceFile):
    file = open(fileName,'a')
    str= "INSERT INTO {table}(att1,att2) VALUES (val1,val2)".format(table=table)


# Import openyxl module

# Define variable to load the wookbook
wookbook = openpyxl.load_workbook("equipes.xlsx")

# Define variable to read the active sheet:
ws = wookbook.active

# Iterate the loop to read the cell values
# for i in range(0, ws.max_row):
#     for col in ws.iter_cols(1, ws.max_column):
#         print(col[i].value, end="\t\t")
#     print('')

# print(ws.cell(row=1,column=1).value)

tmp = get_teams()

# print(get_equipe_id(tmp,"J S B A B","Honneur","Groupe 1"))
insert_equipe_script()
insert_staff_script(tmp)
insert_entraineur_script(tmp)