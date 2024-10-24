import json
Team1="Osu"
Team1score = [{"a":2, "b":3},{"a":2, "b":3}]
outFile = open("demo.txt", "w")
json.dump(Team1score, outFile, indent=4)

List=[('OU', 1418), ('TOL', 1381)]
for i in range(i<12):
    print("a")
    
print(List[0][0][0])
Dictionary = {Team1:Team1score}
print(Dictionary)
for key in Team1score[1].keys():
    print(key)