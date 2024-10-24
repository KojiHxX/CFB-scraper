#bigfile structure:
#[year
#   [rank
#       [Tuple
#           Team, 
#           final ELo,
#           [week
#               {dictionary
#                   Score:
#                   Winner: (bool)
#                   Opponent
#                   CurrentElo
#                   Elochange:
#               }
#           ]
#       ]
#   ]
#]  
import pprint 
import math
import json
with open("CFBteams.json", "r") as cfb:   
    cfb=cfb.read()
    cfb=json.loads(cfb)
with open("demo3.json", "r") as bigfile:   
    bigfile=bigfile.read()
    bigfile=json.loads(bigfile)
    
    #print(bigfile[21][8][2])
#    for year in range(len(bigfile)):
#        print(year+1980)     
#        print(bigfile[year][0][0] +" elo: "+str(round(bigfile[year][0][1],2)))
#        print(bigfile[year][1][0] +" elo: "+str(round(bigfile[year][1][1],2)))
#        print(bigfile[year][2][0] +" elo: "+str(round(bigfile[year][2][1],2)))
    
file = open("output.html", "w")

# Write HTML content
file.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expandable Table Rows</title>
    <style>
        .center{margin-left: 
           auto;margin-right: 
           auto;
        }
        table {width: 80%;
           border-collapse: collapse;
        }
        tr:hover {background-color: 
           #D6EEEE;
        }
        th, td {font-family:"Arial";font-weight: 
           700;border: 2px solid #000000;padding: 
           8px;text-align: 
           left;cursor: 
           pointer;
        }
        th {
           background-color: #f2f2f2;
           font-family:"Arial";
           font-weight: 1000;
           font-size: 50px;
        }
        .hidden {display: none;}
        .toggle {cursor: pointer;font-size: 24px; /* Adjust size as needed */}
    </style>
</head>
<body>
    <table id="dataTable" class="center"><tbody>""")
for year in range(len(bigfile)):
    
    file.write("""
        <tr class="grandparent" onclick="toggleRow(this)">
		    <td style="text-align: center; vertical-align: middle;" colspan="2">
                """+str(1980+year)+
        """:
            </td>
	    </tr>
        """)
    for team in range(len(bigfile[year])):
        file.write("""
            <tr class="hidden parent" onclick="toggleRow(this)">
                <td width=70%>
                <img src=\""""+(bigfile[year][team][1])+
                """\" alt="Logo" width=50 height=50 style="vertical-align: middle; margin-right: 8px;">
                <span style="margin-left: 10px; font-size:60; font-weight:800;">#"""+str(team+1)+" "+bigfile[year][team][0]+
                """</span></td>
                <td colspan="2"; style="font-size:60; font-weight:800;">"""+str(round((bigfile[year][team][2]),2))+"""</div></td>
            </tr>
                """)
        for week in range(len(bigfile[year][team][3])):
            
            if((bigfile[year][team][3][week]["Winner"])==True):
                file.write("""
                    <tr class="hidden child">
                        <td width=70%% style="vertical-align: middle; text-align: left; height: 100%;">Beat """+bigfile[year][team][3][week]["Opponent"]+" "+bigfile[year][team][3][week]["Score"]+
                        "<img src=\""+bigfile[year][team][3][week]["OpponentLogo"]+"\" width=30 height=30 style=\"vertical-align: middle; margin-right: 8px; margin-left: 20px;\">"
                       "</td>")
                file.write("<td width=30% style=\"color:ForestGreen\"><div style=\"color:Black\">"+str(round((bigfile[year][team][3][week]["CurrentElo"]),2))+"</div> + "+str(round((bigfile[year][team][3][week]["Elochange"]),2))+"""</td>
                    </tr>
                       """)
            else:
                file.write("""
                    <tr class="hidden child">
                        <td width=70%% style="vertical-align: middle; text-align: left; height: 100%;">Lost to """+bigfile[year][team][3][week]["Opponent"]+" "+bigfile[year][team][3][week]["Score"]+
                        "<img src=\""+bigfile[year][team][3][week]["OpponentLogo"]+"\" width=30 height=30 style=\"vertical-align: middle; margin-right: 8px; margin-left: 20px;\">"
                       "</td>")
                file.write("<td width=30% style=\"color:FireBrick\"><div style=\"color:Black\">"+str(round((bigfile[year][team][3][week]["CurrentElo"]),2))+"</div> - "+str(round((bigfile[year][team][3][week]["Elochange"]),2))+"""</td>
                    </tr>
                       """)
file.write("""
    </tbody>
    </table>
    <script>
        function toggleRow(clickedRow) {
            let nextRow = clickedRow.nextElementSibling;

            // Check if the clicked row is a parent (i.e., UNC or BYU)
            if (clickedRow.classList.contains('parent')) {
                                
                // Toggle only the direct child rows
                while (nextRow && !nextRow.classList.contains('parent')) {
                    nextRow.classList.toggle('hidden');
                    nextRow = nextRow.nextElementSibling;
                }
            } else {
                // If it's a row like 1980, show/hide its direct children (UNC, BYU)
                
                while (nextRow && !nextRow.classList.contains('grandparent')) {
		    
		    if(nextRow.classList.contains('child') && !nextRow.classList.contains('hidden')){
                    	nextRow.classList.toggle('hidden');
		    }
		    else if(nextRow.classList.contains('parent')){
			nextRow.classList.toggle('hidden');
		    }	
		    nextRow = nextRow.nextElementSibling;
                }
            }
        }
    </script>
</body>
</html>
""")
# Close the file
file.close()