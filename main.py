# math = {'lec':
#             {'Day':"D1" ,
#              "period":{"S_P":1 , "E_P":3}
#              }
#         }

material = {
'math' : { "Group":"G1" ,
        'lecture':dict(Day="D1", period={"S_P":1 , "E_P":3}) ,
        "section": dict(Day="D3" , period={"S_P":1 , "E_P":2}) } ,

'physics' : { "Group":"G1" ,
        'lecture':dict(Day="D1", period={"S_P":4 , "E_P":6}) ,
        "section": dict(Day="D3" , period={"S_P":3 , "E_P":4}) } ,

'english' :  { "Group":"G1" ,
        'lecture':dict(Day="D1", period=[4,5]) ,
        "section": dict(Day="D3" , period=[1,2]) }

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

for i in material.keys() :
        for day in days.keys() :
                #check day if found
            if i['lecture']['Day'] == day :
                #check period content for lecture
                lec_s_p = periods[i['lecture']['period']["S_P"]-1]
                lec_e_p = periods[i['lecture']['period']["E_P"]-1]
                if len(table[lec_s_p:lec_e_p]) == 0 :
                    table[lec_s_p:lec_e_p] = i
                #check day if found
            if i["section"]['Day'] == day :
                #check period content for Section
                sec_s_p = periods[i["section"]['period']["S_P"]-1]
                sec_e_p = periods[i["section"]['period']["E_P"]-1]
                if len(table[sec_s_p:sec_e_p]) == 0 :
                    table[sec_s_p:sec_e_p] = i
