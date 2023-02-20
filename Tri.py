import pandas as pd
from datetime import datetime

class TriCsv():

        
    def OpenFile(fileName):
        
        data = pd.read_csv(fileName)
        
        return data


    def empty(data, filename):
        
        vide = data.isnull()
        
        for title in vide:
            for i in range(len(vide[title])):
                if vide[title][i] == True:
                    data[title][i] = 'VIDE'
                    
        data.to_csv(filename, index=False)


    def duplicate(data, filename):
        
        data['email'] = data['email'].apply(lambda x: x.split(',', 1)[0])
        data = data.drop_duplicates(subset=['email'], keep='first')
        
        data.to_csv(filename, index=False)
        
        
    def pays(data, filename):
        
        for i in range(len(data['pays'])):
            if data['pays'][i].isdigit():
                data["pays"][i] = 'ERROR'
                
        data.to_csv(filename, index=False)


    def date(data, filename):
        
        month_dict = {
            'janv.': 'Jan',
            'févr.': 'Beb',
            'mars': 'Mar',
            'avr.': 'Apr',
            'mai': 'May',
            'juin': 'Jun',
            'juil.': 'Jul',
            'aout': 'Aug',
            'sept.': 'Sep',
            'oct.': 'Oct',
            'nov.': 'Nov',
            'déc.': 'Dec'                                                           #je me suis fait un ptit kiff là, même si c'est useless
        }
                                                                                    
        for index, row in data.iterrows():
            date_str = row['date_naissance']
            try:
                
                for k, v in month_dict.items():
                    date_str = date_str.replace(k, v)
                date_obj = datetime.strptime(date_str, '%d %b %Y')
                date_formatted = date_obj.strftime('%d/%m/%Y')
                data.at[index, 'date_naissance'] = date_formatted

            except ValueError:
                continue

        data.to_csv(filename, index=False)


    def size(data, filename):
        
        for i in range(len(data['taille'])):
            if "cm" in data['taille'][i]:
                cm_value = int(data['taille'][i].replace("cm", ""))
                m_value = cm_value / 100
                formatted_value = str(m_value) + "m"
                data['taille'][i] = formatted_value
 
        data.to_csv(filename, index=False)
        





# exemple d'utilisation :

# ---------------------------------------------------------------------------------------------------------------------------->
# from Tri import TriCsv
filename = 'personnes.csv'
data = TriCsv.OpenFile(filename)
TriCsv.empty(data, filename)
TriCsv.pays(data, filename)
TriCsv.date(data, filename)
TriCsv.size(data, filename)
TriCsv.duplicate(data, filename)
# ---------------------------------------------------------------------------------------------------------------------------->

