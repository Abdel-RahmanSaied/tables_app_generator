from final_subject_manger import Subject_Manger
import json
# take group of eatch of subject and pass it to lecture checker

with open(r"DB/materials.json") as material_db:
    materials = json.load(material_db)


sub_material = Subject_Manger().subject_generator(materials)

print(len(sub_material))

for mat_counter in range(len(sub_material)):
    new_mat = {}
    for mat_counter in list(sub_material[mat_counter]):
        r = str(mat_counter.keys()).split("'")[1]
        new_mat[r] = mat_counter
    lec_check = Subject_Manger().lecture_checker(new_mat)
    if lec_check == None:

        print(True)
    else:
        print(False)
    # print(lec_check)
