# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:54:52 2021

@author: liora
"""
def WhatsApp(input_chat):
    import json
    input_chat=input_chat+".txt"
    
    fi=open(input_chat ,'r' , encoding=('utf-8'))
    file=fi.readlines()
    fi.close()
    idd=dict()
    full_list=list()
    i=1
    first_row=file[1]
    for line in file[5:]:
        if line[4:8]=='2021':
            start=line.find('-')
            end=line.find(':',start)
            result=line[start+1:end]
            if result not in idd:
                idd[result]=i
                i=i+1
        if line[4:8]=='2021':
            datetime=line[:start]
            num= idd[result]
            text= line[end:]
            help_dict={'datetime' : datetime ,'id': num ,'text': text.strip()}
            full_list.append(help_dict)
        else:
            full_list[-1]['text']=full_list[-1]['text']+line.strip()
    
    
    creation_date=first_row[:first_row.find('-')]
    start2=first_row.find('"')+1
    end2=first_row.find('"',start2)
    chat_name=first_row[start2:end2]
    yedy=first_row.find('ידי')
    creator=first_row[first_row.find(' ',yedy):]
    num_of_participants=len(idd)
    meta_dict={'creation_date' : creation_date,'chat_name': chat_name , 'creator' : creator.strip() , 'num_of_participants' : num_of_participants}
    
    total_dict={'messages':full_list, 'metadata':meta_dict}

    return_json = json.dumps(total_dict , ensure_ascii=False)
    with open(chat_name,'w',encoding=('utf8')) as open_text:
        open_text.writelines(return_json)
        open_text.close()

WhatsApp('WhatsApp_friend')
