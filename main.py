import json

material = {
'math' : { "Group":"G1" ,
        'lecture':dict(Day="D1", period={"S_P":1 , "E_P":3}) ,
        "section": dict(Day="D3" , period={"S_P":1 , "E_P":2}) } ,

'physics' : { "Group":"G1" ,
        'lecture':dict(Day="D1", period={"S_P":4 , "E_P":6}) ,
        "section": dict(Day="D3" , period={"S_P":3 , "E_P":4}) } ,

'english' :  { "Group":"G1" ,
        'lecture':dict(Day="D1", period={"S_P":7 , "E_P":8}) ,
        "section": dict(Day="D3" , period={"S_P":5 , "E_P":6}) }

}

# days = {"D1":'',"D2":'',"D3":'',"D4":'',"D5":''}
days = ["D1","D2","D3","D4","D5"]

# periods = { "p1": '' , "p2":'' , "p3":'' ,
#          "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''}
periods = ["p1" , "p2" , "p3" , "p4" , "p5", "p6" , 'p7' , "p8"]

table = {"D1":{"p1": '' , "p2":'' , "p3":'' , "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''},
         "D2":{"p1": '' , "p2":'' , "p3":'' , "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''},
         "D3":{"p1": '' , "p2":'' , "p3":'' , "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''},
         "D4":{"p1": '' , "p2":'' , "p3":'' , "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''},
         "D5":{"p1": '' , "p2":'' , "p3":'' , "p4":'' , "p5":'' , "p6":'' , 'p7':'' , "p8":''}}


for subject in material.keys() :
        #check day if found
        lec_day =material[subject]['lecture']['Day']
        sec_day = material[subject]['section']['Day']
        #period content for lecture
        lec_s_p = periods[material[subject]['lecture']['period']["S_P"]-1]
        lec_e_p = periods[material[subject]['lecture']['period']["E_P"]-1]
        #  period content for Section
        sec_s_p = periods[material[subject]["section"]['period']["S_P"] - 1]
        sec_e_p = periods[material[subject]["section"]['period']["E_P"] - 1]

        for lec_index in range(material[subject]['lecture']['period']["S_P"]-1 , material[subject]['lecture']['period']["E_P"] , 1) :
            lec_checker = []
            if len(table[lec_day][periods[lec_index]]) == 0 :
                lec_checker.append(True)
                try :
                    if lec_checker[0] == True and lec_checker[1] == True and lec_checker[2] == True :
                        continue

                except :
                    pass
                finally:
                    table[lec_day][periods[lec_index]] = subject

                    #############################################
        for sec_index in range(material[subject]['section']['period']["S_P"]-1 , material[subject]['section']['period']["E_P"] , 1) :
            sec_checker = []
            if len(table[sec_day][periods[sec_index]]) == 0 :
                sec_checker.append(True)
                try :
                    if sec_checker[0] == True and sec_checker[1] == True and sec_checker[2] == True :
                        continue

                except :
                    pass
                finally:
                    table[sec_day][periods[sec_index]] = subject

print(json.dumps(table , indent=4))