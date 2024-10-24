import requests # import requests library for use
import pprint 
import math
opstr = 0.1
coeff = 400
kfact = 25
diff = 1
dstr = 0.4
rankings = {
}
year = (2000)
month = (8)
for y in range(2):
    for m in range(6):
        for d in range(31):
            if(int(int(month+m)/10)<1):
                date = str(int(str(year+y) + "0" + str(month+m) + "01") + d)
            else:
                if((month+m)>12):   
                    date = str(int(str(year+y+1) + "0" + str(month+m-12) + "01") + d)
                else:
                    date = str(int(str(year+y) + str(month+m) + "01") + d)
            api_result = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=" + date)
            api_result = api_result.json()
            # converts json to dicitonary

            events = api_result["events"]
            # grabs only the "data" element from the response
            if(events != []):
                for i in range(len(events)):
                    if(events[i] != {}):
                        if("winner" in (events[i]["competitions"][0]["competitors"][0])):
                            Team1 = (events[i]["competitions"][0]["competitors"][0]["team"]["abbreviation"])
                            Team1Win = (events[i]["competitions"][0]["competitors"][0]["winner"])
                            Team1Score = (events[i]["competitions"][0]["competitors"][0]["score"])
                            Team2 = (events[i]["competitions"][0]["competitors"][1]["team"]["abbreviation"])
                            Team2Score = (events[i]["competitions"][0]["competitors"][1]["score"])
                            if (Team1 not in rankings):
                                rankings[Team1]=1000
                            if(Team2 not in rankings):
                                rankings[Team2]=1000
                            if(Team1Win== True):
                                #print(Team1 + " " + Team1Score)
                                #print(Team2 + " " + Team2Score)
                                eloChange = kfact*(1-(1/(1+math.pow(10,((rankings[Team1]-rankings[Team2])/coeff)))))
                                eloChange = eloChange * math.log((int(Team1Score)-int(Team2Score))+1)
                                eloChange = round(eloChange, 2)
                                rankings[Team1]=rankings[Team1] + eloChange
                                rankings[Team2]=rankings[Team2] - eloChange
                            else:
                                #print(Team2 + " " +Team2Score)
                                #print(Team1 + " " + Team1Score)
                                eloChange = kfact*(1-((1/(1+math.pow(10,((rankings[Team1]-rankings[Team2])/coeff))))))
                                eloChange = eloChange * (dstr*math.log((int(Team2Score)+1-int(Team1Score))+1)+diff)
                                eloChange = round(eloChange, 2)
                                rankings[Team1]=rankings[Team1] - eloChange
                                rankings[Team2]=rankings[Team2] + eloChange
                                #print(Team2+" + "+str(eloChange))
                                #print(Team1+" - "+str(eloChange))
                        
                            #print()       
    print(str(year+y))                
    for i in range(len(rankings)):
        #finds the highest value in "rankings"
        Tempmax=max(zip(rankings.values(), rankings.keys()))[1]
        print(Tempmax + " " + str(round(rankings[Tempmax], 2)))

        #removes that highest value
        rankings.pop(Tempmax)
    
# item[1] represents the sorting based on value
# Sorted Dictionary



        





