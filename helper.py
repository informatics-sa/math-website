from lib import *
from lib.utils import *



def update_participations():
    members = get_members()
    with open('./root/data/participations.old.json') as f:
        parts_str = f.read()
    for uid in members:
        if 'iid' in members[uid]:
            oid = members[uid]['id']
            iid = members[uid]['iid']
            parts_str = parts_str.replace(f'"{oid}"', f'"{iid}"')
            print("replaced", oid, "with", iid)
    write_text('./root/data/participations.json', parts_str)

def update_exams():
    members = get_members()
    with open('./root/data/exams.json') as f:
        parts_str = f.read()
    for k, v in members.items():
        id = v['id']
        iid = v['iid']
        parts_str = parts_str.replace(f'"{id}"', f'"{iid}"')
    write_text('./exams.2.json', parts_str)


def check_distinct_ids():
    participations = load_json('participations.old')
    unique_names = set()
    for par in participations:
        for user in par['participants']:
            unique_names.add(user.lower().replace(' ', '_'))
    names = sorted(list(unique_names))
    for i in names:
        print(i)

def generate_members():
    participations = load_json('participations.old')
    unique_names = set()
    for par in participations:
        for user in par['participants']:
            user = str(user).lower()
            unique_names.add(user.lower())
    names = sorted(list(unique_names))
    data = []
    idx = 1
    for n in names:
        data.append({
            'iid': idx,
            'id': n,
            'arname': n,
            'enname': n
        })
        idx += 1
    write_text('./root/data/people.json', json.dumps(data))



def generate_members_names():
    members = load_json('people')
    for p in members:
        p['enname'] = p['id']
        p['arname'] = p['id']
    write_text('./root/data/people.json', json.dumps(members))

def sort_by_date(date_format="%Y/%m/%d"):
    # Read JSON file
    from datetime import datetime
    with open('./root/data/participations.json', 'r') as f:
        data = json.load(f)
    
    # Sort objects by start date
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['start'], date_format), reverse=True)
    
    # Write sorted data to output file
    with open('./root/data/participations.json', 'w') as f:
        json.dump(sorted_data, f, indent=4)

#generate_members_names()
# check_distinct_ids()
# exit(1)
#update_exams()
generate_members()
update_participations()
sort_by_date()