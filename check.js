const axios = require('axios'); // Use axios for HTTP requests
const math = require('mathjs'); // Use mathjs for mathematical operations

let opstr = 0.1;
let coeff = 400;
let kfact = 25;
let diff = 1;
let dstr = 0.4;
let rankings = {};
let year = 2001;
let month = 8;

(async () => {
    for (let m = 0; m < 6; m++) {
        for (let d = 0; d < 31; d++) {
            let date;

            if (Math.floor((month + m) / 10) < 1) {
                date = String(year) + "0" + String(month + m) + "01" + String(d);
            } else {
                if ((month + m) > 12) {
                    date = String(year + 1) + "0" + String(month + m - 12) + "01" + String(d);
                } else {
                    date = String(year) + String(month + m) + "01" + String(d);
                }
            }

            try {
                const apiResult = await axios.get(`https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=${date}`);
                const events = apiResult.data.events;

                console.log(date);

                if (events.length) {
                    for (let i = 0; i < events.length; i++) {
                        if (events[i]) {
                            let competition = events[i].competitions[0];
                            let Team1 = competition.competitors[0].team.abbreviation;
                            let Team1Win = competition.competitors[0].winner;
                            let Team1Score = competition.competitors[0].score;
                            let Team2 = competition.competitors[1].team.abbreviation;
                            let Team2Score = competition.competitors[1].score;

                            if (!(Team1 in rankings)) rankings[Team1] = 1000;
                            if (!(Team2 in rankings)) rankings[Team2] = 1000;

                            let eloChange;
                            if (Team1Win) {
                                eloChange = kfact * (1 - (1 / (1 + Math.pow(10, ((rankings[Team1] - rankings[Team2]) / coeff)))));
                                eloChange *= Math.log((parseInt(Team1Score) - parseInt(Team2Score)) + 1);
                                eloChange = Math.round(eloChange * 100) / 100; // Round to 2 decimal places
                                rankings[Team1] += eloChange;
                                rankings[Team2] -= eloChange;

                                if (Team1 === "WASH") {
                                    console.log(`${Team1} + ${eloChange}`);
                                    console.log(`${Team2} - ${eloChange}`);
                                    console.log();
                                }
                            } else {
                                eloChange = kfact * (1 - (1 / (1 + Math.pow(10, ((rankings[Team1] - rankings[Team2]) / coeff)))));
                                eloChange *= (dstr * Math.log((parseInt(Team2Score) + 1 - parseInt(Team1Score)) + 1) + diff);
                                eloChange = Math.round(eloChange * 100) / 100; // Round to 2 decimal places
                                rankings[Team1] -= eloChange;
                                rankings[Team2] += eloChange;
                            }
                        }
                    }
                } else {
                    console.log(`${date} no events`);
                }
            } catch (error) {
                console.error(`Error fetching data for ${date}:`, error);
            }
        }
    }

    let rankings2 = {};
    while (Object.keys(rankings).length) {
        const Tempmax = Object.entries(rankings).reduce((max, curr) => (curr[1] > max[1] ? curr : max));
        console.log(`${Tempmax[0]} ${Math.round(Tempmax[1] * 100) / 100}`);
        delete rankings[Tempmax[0]];
    }
})();