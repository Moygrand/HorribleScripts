import openpyxl
import shutil

ruta= ""
hab = "hab.xlsx"
cfg = "vTech-1265.cfg"
fichero = openpyxl.open(ruta+hab)

point = 1
while fichero["Faults"].cell(point,1).value is not None:
    sip = fichero["Faults"].cell(point,1).value
    configf = ruta+"vTech-"+str(sip)+".cfg"
    shutil.copy(ruta+cfg,configf)
    with open(configf,"r") as f:
        lineas = f.readlines()
    lineas[473]="profile.admin.access_password = 6.Techph0ne"+"\n"
    lineas[502]="sip_account.1.authentication_access_password = "+"11312340"+"\n"
    lineas[503]="sip_account.1.authentication_name = "+str(sip)+"\n"
    lineas[520]="sip_account.1.display_name = "+str(sip)+"\n"
    lineas[530]="sip_account.1.label = "+str(sip)+"\n"
    lineas[564]="sip_account.1.user_id = "+str(sip)+"\n"
    with open(configf,"w") as f:
        f.writelines(lineas)
    point+=1
