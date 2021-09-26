from  teeeeeeeeest import  New_Sub
import json

with open(r"DB/materials.json") as material_db:
    materials = json.load(material_db)
table = New_Sub().check_subject(materials)

print(json.dumps(table , indent=4))

