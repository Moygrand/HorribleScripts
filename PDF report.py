from PyPDF2 import PdfReader
import pandas as pd

path = "SimphonyPriceRecords.pdf"
reader = PdfReader(path)
doc = reader.pages

def MasterRecords(doc):
    lista = []
    df = pd.DataFrame(columns=["#","Name","Zone/Location","Inheritance Type","Major Group","Family Group","Master Group","Report Group","Options"])
    for page in doc:
        lista=page.extract_text().split('\n')
        finalist = [lista[i:i+9] for i in range(0,len(lista),9)]
        tempdf = pd.DataFrame(finalist,columns=df.columns)
        df = pd.concat([df,tempdf], ignore_index=True)
        lista=[]
        finalist=[]

    df.to_excel("masterRecords.xlsx")

def DefinitionRecords():
#For A4 PDF
    df =pd.DataFrame(columns=["#","Def Seq",
                            "First Name",
                            "Zone/Location","Inheritance Type",
                            "Menu Item Class","Print Class Override",
                            "Main Level","Sub Level","SLU","SLU 2",
                            "SLU 3","SLU 4","SLU 5","SLU 6","SLU 7",
                            "SLU 8","SLU Sort Prior","NLU Group","NLU Number",
                            "Tare Weight","Surcharge",
                            "Quantity","Allergen Class Override",
                            "Major Group","Family Group"])

    lista =[]
    df = pd.DataFrame()
    for itemlist in range(0,len(doc),7):
        
        lista= doc[itemlist].extract_text().split('\n')
        df1 = pd.DataFrame([lista[i:i+6] for i in range(0,len(lista),6)],columns=["#","Def Seq",
                            "First Name","Zone/Location","Inheritance Type",
                            "Menu Item Class"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df2 = pd.DataFrame([lista[i:i+8] for i in range(0,len(lista),8)],columns=["#","Def Seq",
                            "First Name","Print Class Override",
                            "Main Level","Sub Level","SLU","SLU 2"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df3 = pd.DataFrame([lista[i:i+7] for i in range(0,len(lista),7)],columns=["#","Def Seq",
                            "First Name","SLU 3","SLU 4","SLU 5","SLU 6"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df4 = pd.DataFrame([lista[i:i+8] for i in range(0,len(lista),8)],columns=["#","Def Seq",
                            "First Name","SLU 7",
                            "SLU 8","SLU Sort Prior","NLU Group","NLU Number"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df5 = pd.DataFrame([lista[i:i+6] for i in range(0,len(lista),6)],columns=["#","Def Seq",
                            "First Name","Tare Weight","Surcharge","Quantity"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df6 = pd.DataFrame([lista[i:i+6] for i in range(0,len(lista),6)],columns=["#","Def Seq",
                            "First Name","Allergen Class Override",
                            "Major Group","Family Group"])
        
        itemlist+=1
        lista= doc[itemlist].extract_text().split('\n')
        df7 = pd.DataFrame([lista[i:i+3] for i in range(0,len(lista),3)])
        
        dfs=[df2,df3,df4,df5,df6]

        for data in dfs:
            df1 = pd.merge(df1,data,on=["#","Def Seq",
                            "First Name"])
        df = pd.concat([df,df1],ignore_index=True)


    pd.DataFrame.to_excel(df,"SimphonyDefinitionRecords.xlsx")

#PriceRecords
def PriceRecords():
    lista=[]
    df = pd.DataFrame()
    for itemlist in range(0,len(doc),2):
        lista=doc[itemlist].extract_text().split('\n')
        df1 = pd.DataFrame([lista[i:i+13] for i in range(0,len(lista),13)],columns=["#","Def Seq",
                                "Definition Name","Price Seq #","Price","Zone/Location","Inheritance Type","Prep Cost","Tax Class Override","Condiment Parent","Service Charge group","Active on level","Options"])
        itemlist+=1

        lista=doc[itemlist].extract_text().split('\n')
        df2 = pd.DataFrame([lista[i:i+8] for i in range(0,len(lista),8)],columns=["#","Def Seq",
                                "Definition Name","Price Seq #","Effectivity Group", "Effectivity Status","Major Group","Family Group"])
        df1 = pd.merge(df1,df2,on=["#","Def Seq",
                                "Definition Name","Price Seq #"])
        df=pd.concat([df,df1],ignore_index=True)

    pd.DataFrame.to_excel(df,"SimphonyPriceRecords.xlsx")