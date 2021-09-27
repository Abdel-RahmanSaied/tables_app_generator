import itertools as it
import json
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
            group_name = subject_table_to_check[sub_name]
            for group_num in group_name.keys() :
                start_lecture_period = group_name[group_num]["lecture"]["period"]["S_P"] - 1
                end_lecture_period = group_name[group_num]["lecture"]["period"]["E_P"]
                lec_day = group_name[group_num]['lecture']['Day']
                ##################################
                lec_checker = []
                avilability_checker = False
                for lec_index in range(start_lecture_period, end_lecture_period, 1):
                    if len(table[lec_day][periods[lec_index]]) == 0:
                        lec_checker.append(True)
                        try:
                            if lec_checker[0] == True and lec_checker[1] == True and lec_checker[2] == True:
                                table[lec_day][periods[lec_index]] = sub_name, group_num
                                avilability_checker = True
                        except:
                            return avilability_checker
                        else:
                            return table
                # return table of lectures  if available and pass it to section checker
                #return false if not available

    def section_checker(self, subject_table_to_check:dict ,table_of_lectures:dict  ):
        #check section period availabitiy in table
        periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]
        for sub_name in subject_table_to_check.keys():
            group_name = subject_table_to_check[sub_name]
            for group_num in group_name.keys() :
                start_section_period = group_name[group_num]["section"]["period"]["S_P"] - 1
                end_section_period = group_name[group_num]["section"]["period"]["E_P"]
                lec_day = group_name[group_num]['section']['Day']
                ##################################
                sec_checker = []
                avilability_checker = False
                for lec_index in range(start_section_period, end_section_period, 1):
                    if len(table_of_lectures[lec_day][table_of_lectures[lec_index]]) == 0:
                        sec_checker.append(True)
                        try:
                            if sec_checker[0] == True and sec_checker[1] == True and sec_checker[2] == True:
                                table_of_lectures[lec_day][periods[lec_index]] = sub_name, group_num
                                avilability_checker = True
                        except:
                            return avilability_checker
                        else:
                            return table_of_lectures

                #return table of lectures and sections if available
                #return false if not available

    def subject_generator(self,material):
        #take group of eatch of subject and pass it to lecture checker

        sub_list = []
        all_sub_list = []
        groups_count = {}
        for sub_name in material.keys():
            group_name = material[sub_name]["Groups"]
            counter = 0
            for group_num in group_name.keys():
                sub_list_material = {sub_name: {group_num: group_name[group_num]}}
                sub_list.append(sub_list_material)
                counter += 1
            groups_count[sub_name] = counter
        last_index = 0
        for all_sub_index in groups_count.keys():
            all_sub_list.append(sub_list[last_index:last_index + groups_count[all_sub_index]])
            last_index += groups_count[all_sub_index]

        combinations = it.product(*all_sub_list)
        result = list(combinations)
        return result

    def table_viewer(self):
        #take table from section and put it in list
        #return list of success tables
        pass


