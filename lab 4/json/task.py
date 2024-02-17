import json

file = open("sample-data.json")
db = json.load(file)

print("Interface Status")
print("=" * 120)
print(f"{'DN':<60} {'Description':<25} {'Speed':<15} {'MTU':<8}")
print("-" * 120)

for i in db["imdata"]:
    l1_phys_if = i["l1PhysIf"]["attributes"]
    dn = l1_phys_if["dn"]
    descr = l1_phys_if["descr"]
    speed = l1_phys_if["speed"]
    mtu = l1_phys_if["mtu"]
    print(f"{dn:<60} {descr:<25} {speed:<15} {mtu:<8}")
