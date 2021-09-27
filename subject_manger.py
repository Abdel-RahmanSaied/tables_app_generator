class Subject_Checker():
    def __init__(self):
        pass
    def check_subject(self , materials:dict):
        # return true or false
        # days = ["D1", "D2", "D3", "D4", "D5"]
        periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]

        table = {"D1": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D2": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D3": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D4": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D5": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''}}

        lecture_result = ''
        section_result = ''
        table_result = []



        for group_name in materials.keys():
            print(group_name)
            start_lecture_period = materials[group_name]["lecture"]["period"]["S_P"] -1
            end_lecture_period = materials[group_name]['lecture']['period']["E_P"]
            lec_day = materials[group_name]['lecture']['Day']
            print("start lec part")
            lec_checker = []
            for lec_index in range(start_lecture_period , end_lecture_period, 1):
                if len(table[lec_day][periods[lec_index]]) == 0:
                    lec_checker.append(True)
                    try:
                        if lec_checker[0] == True and lec_checker[1] == True and lec_checker[2] == True:
                            print("lec checker success")

                    except:
                        print("error in lec")
                    else:
                        lecture_result = True
                        print(f"{lecture_result} lect of {group_name}" )
                    finally:
                        print("end of lec part")
                else:
                    lec_checker.append(False)

            start_section_period = materials[group_name]['section']['period']["S_P"]-1
            end_sections_period = materials[group_name]['section']['period']["E_P"]
            sec_day = materials[group_name]['section']['Day']
            sec_checker = []
            print("start sec part")
            for sec_index in range(start_section_period , end_sections_period, 1):
                if len(table[sec_day][periods[sec_index]]) == 0:
                    sec_checker.append(True)
                    try:
                        if sec_checker[0] == True and sec_checker[1] == True  and sec_checker[2] == True :
                            print("sec checker successful")

                    except:
                        print("error in sec")
                    else:
                        section_result = True
                        # print(f"{section_result} sect of {group_name}")
                    finally:
                        print("end of sec part")

                try:
                    if lecture_result == "True" and section_result == "True":
                        print("table checker successful")
                except:
                    print("failed")
                else:
                    table_result.append(True)

            else:
                sec_checker.append(False)
# condition error >> the function always return true :(
            table_result_counter = len(table_result)
            table_result_checker = True
            for index in range(table_result_counter):
                if table_result[index] == True:
                    table_result_checker = True
                else:
                    table_result_checker = False


            print(table_result)
            #print(table_result_checker)
            return table_result_checker




def all_subjects_options(subjects: list):
        # return list of all posiple options
        # [m1,m2,m3]
        # [e1,e2,e3]
        # output
        # [[m1,e1][m1,e2][m1,e3][m2,e1][m2,e2][m2,e3],etc]
        pass