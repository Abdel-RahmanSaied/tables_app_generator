import itertools as it
import json
class Subject_Manger():

    def __init__(self):
        pass

    def lecture_checker(self , subject_table_to_check:dict):
        # get table in dictionary
        periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]
        table = {"D1": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D2": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D3": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D4": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D5": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''}}
        #check lecture period availability in table

        for subject_name in subject_table_to_check.keys() :
            group_name = subject_table_to_check[subject_name][subject_name]
            for group_num in group_name.keys() :
                lec_day = group_name[group_num]['lecture']['Day']
                start_lecture_period = group_name[group_num]["lecture"]["period"]["S_P"] - 1
                end_lecture_period = group_name[group_num]["lecture"]["period"]["E_P"]
                period_availabity_checker = []

                #############################################
                for period_check in range(start_lecture_period,end_lecture_period):
                    if table[lec_day][periods[period_check]] != "" :
                        period_availabity_checker.append(False)
                        #print(period_availabity_checker)
                        # table[lec_day][periods[period_check]] = subject_name, group_num
                    else:
                        period_availabity_checker.append(True)

                try:
                    if False in period_availabity_checker:
                        return False
                        break
                    else:
                        for fill_sub in range(start_lecture_period, end_lecture_period):
                            table[lec_day][periods[fill_sub]] = subject_name, group_num
                except:
                    print("something went wrong")

    def section_checker(self, subject_table_to_check:dict ):
        periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]
        table = {"D1": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D2": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D3": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D4": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D5": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''}}
        #main variables
        # for subject_name in subject_table_to_check.keys() :
        #     group_name = subject_table_to_check[subject_name][subject_name]
        #     for group_num in group_name.keys() :
        #         lec_day = group_name[group_num]['lecture']['Day']
        #         start_lecture_period = group_name[group_num]["lecture"]["period"]["S_P"] - 1
        #         end_lecture_period = group_name[group_num]["lecture"]["period"]["E_P"]
        # # fill lecture period  in table
        # ##############################################################
        # for fill_sub in range(start_lecture_period, end_lecture_period):
        #     table[lec_day][periods[fill_sub]] = subject_name, group_num
        ###############################################################
        for subject_name_section in subject_table_to_check.keys() :
            group_name_section = subject_table_to_check[subject_name_section][subject_name_section]
            for group_num_section in group_name_section.keys() :
                sec_day = group_name_section[group_num_section]['section']['Day']
                start_section_period = group_name_section[group_num_section]["section"]["period"]["S_P"] - 1
                end_sectione_period = group_name_section[group_num_section]["section"]["period"]["E_P"]
                period_availabity_checker = []

                #############################################
                for period_check_section in range(start_section_period,end_sectione_period):
                    if table[sec_day][periods[period_check_section]] != "" :
                        period_availabity_checker.append(False)
                        #print(period_availabity_checker)
                        # table[lec_day][periods[period_check]] = subject_name, group_num
                    else:
                        period_availabity_checker.append(True)

                try:
                    if False in period_availabity_checker:
                        return False
                        break
                    else:
                        for fill_sub_section in range(start_section_period, end_sectione_period):
                            table[sec_day][periods[fill_sub_section]] = subject_name_section, group_num_section
                except:
                    print("something went wrong")




        #check section period availabitiy in table
        #return table of lectures and sections if available
        #return false if not available
        pass

    def subject_generator(self, material: dict):
        # take group of eatch of subject and pass it to lecture checker
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
        # take table from section and put it in list
        # return list of success tables
        ##########
        #fill table in lectures
        #fill table in sections
        #save in new list by (table+counter) -> table 1 , table 2 , .....

        pass

    # def convert_syntax(self, materials: dict):
    #     sub_material = Subject_Manger().subject_generator(materials)
    #     for mat_counter in range(len(sub_material)):
    #         new_mat = {}
    #         for mat_counter in list(sub_material[mat_counter]):
    #             r = str(mat_counter.keys()).split("'")[1]
    #             new_mat[r] = mat_counter





