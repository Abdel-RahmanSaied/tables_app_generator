class New_Subject_Manger():
    def __init__(self):
        pass

    def lecture_checker(self , subject_table_to_check:dict):
        #check lecture period availability in table
        periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]

        table = {"D1": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D2": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D3": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D4": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D5": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''}}

        for sub_name in subject_table_to_check.keys():
            group_name = subject_table_to_check[sub_name]["Groups"]
            start_lecture_period = subject_table_to_check[sub_name]["Groups"][group_name]["lecture"]["period"]["S_P"] - 1
            end_lecture_period = materials[group_name]['lecture']['period']["E_P"]
            lec_day = materials[group_name]['lecture']['Day']
            # return table of lectures  if available and pass it to section checker
            #return false if not available
        pass

    def section_checker(self , table_of_lectures:dict) :
        #check section period availabitiy in table
        #return table of lectures and sections if available
        #return false if not available
        pass

    def subject_generator(self):
        #take group of eatch of subject and pass it to lecture checker
        pass

    def table_viewer(self):
        #take table from section and put it in list
        #return list of success tables
        pass


