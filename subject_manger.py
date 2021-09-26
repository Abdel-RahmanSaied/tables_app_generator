class New_Sub():
    def __init__(self):
        pass
    def check_subject( materials: dict):
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

        for group_name in materials.keys():

            start_lecture_period = group_name['lecture']['period']["S_P"]
            end_lecture_period = group_name['lecture']['period']["E_P"]
            lec_day = group_name['lecture']['Day']
            for lec_index in range(start_lecture_period - 1, end_lecture_period, 1):
                lec_checker = []
                if len(table[lec_day][periods[lec_index]]) == 0:
                    lec_checker.append(True)
                    try:
                        if lec_checker[0] == True and lec_checker[1] == True and lec_checker[2] == True:
                            pass
                    except:
                        pass
                    finally:
                        lecture_result = True

                start_section_period = group_name['section']['period']["S_P"]
                end_sections_period = group_name['section']['period']["E_P"]
                sec_day = group_name['section']['Day']

                for sec_index in range(start_section_period - 1, end_sections_period, 1):
                    sec_checker = []
                    if len(table[sec_day][periods[sec_index]]) == 0:
                        sec_checker.append(True)
                        try:
                            if sec_checker[0] == True and sec_checker[1] == True and sec_checker[2] == True:
                                continue
                        except:
                            pass
                        finally:
                            section_result = True

            try:
                if lecture_result == True and section_result == True:
                    continue
            except:
                print("failed")
            finally:
                return True

    def all_subjects_options(subjects: list):
        # return list of all posiple options
        # [m1,m2,m3]
        # [e1,e2,e3]
        # output
        # [[m1,e1][m1,e2][m1,e3][m2,e1][m2,e2][m2,e3],etc]
        pass