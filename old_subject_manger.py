class Subject_Checker :
    def __init__(self):
        import json
        with open(r"DB/materials.json") as material_db:
            self.material = json.load(material_db)

        self.lecture_result = ""
        self.sections_result = ""
        self.lec_day = ""
        self.sec_day = ""
        self.lec_index = 0
        self.sec_index = 0


        self.subject = ""

        self.days = ["D1", "D2", "D3", "D4", "D5"]

        self.periods = ["p1", "p2", "p3", "p4", "p5", "p6", 'p7', "p8"]

        self.table = {"D1": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D2": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D3": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D4": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''},
                 "D5": {"p1": '', "p2": '', "p3": '', "p4": '', "p5": '', "p6": '', 'p7': '', "p8": ''}}



    def sub_checker(self):
        for subject in self.material.keys():
            self.lec_day = self.material[subject]['lecture']['Day']
            for lec_index in range(self.material[subject]['lecture']['period']["S_P"] - 1,
                                   self.material[subject]['lecture']['period']["E_P"], 1):
                self.lec_index = lec_index
                lec_checker = []
                if len(self.table[self.lec_day][self.periods[lec_index]]) == 0:
                    lec_checker.append(True)
                    try:
                        if lec_checker[0] == True and lec_checker[1] == True and lec_checker[2] == True:
                            continue

                    except:
                        pass
                    finally:
                        self.lecture_result = True

            self.sec_day = self.material[self.subject]['section']['Day']

            for sec_index in range(self.material[subject]['section']['period']["S_P"] - 1,
                                        self.material[subject]['section']['period']["E_P"], 1):
                self.sec_index = sec_index
                sec_checker = []
                if len(self.table[self.sec_day][self.periods[sec_index]]) == 0:
                    sec_checker.append(True)
                    try:
                        if sec_checker[0] == True and sec_checker[1] == True and sec_checker[2] == True:
                            continue
                    except:
                        pass
                    finally:
                        self.sections_result = True




    def table_fill(self):
        #subjects = Subject_Checker().sub_checker()
        # check day if found
        try :
            if self.lecture_result == True and self.sections_result == True :
                pass
        except :
            print("failed")

        finally:
            self.table[self.lec_day][self.periods[self.lec_index]] = self.subject , self.material[self.subject]["Group"]
            self.table[self.sec_day][self.periods[self.sec_index]] = self.subject , self.material[self.subject]["Group"]

        return  self.table