const d3 = require('d3');
const { createCanvas } = require('canvas');
const fs = require('fs');

const userData = JSON.parse(process.env.USER_DATA);
const languages = JSON.parse(userData.languages);

// Create radar chart of user's tech expertise
function generateDevRadar() {
    const canvas = createCanvas(800, 800);
    const context = canvas.getContext('2d');
    
    // D3 radar chart configuration
    const config = {
        w: 600,
        h: 600,
        margin: { top: 100, right: 100, bottom: 100, left: 100 },
        maxValue: 100,
        levels: 5,
        roundStrokes: true,
        color: d3.scaleOrdinal().range(["#26AF32", "#762712", "#2A2FE9", "#F7D794", "#83D2E4"])
    };

    // Generate random stats for demo
    const stats = languages.map(lang => ({
        language: lang,
        value: Math.floor(Math.random() * 85) + 15
    }));

    // D3 radar chart drawing logic here...
    // (Simplified for brevity, would include actual D3.js radar chart generation)

    // Save the generated SVG
    if (!fs.existsSync('./stats')){
        fs.mkdirSync('./stats');
    }
    fs.writeFileSync('./stats/dev_radar.svg', canvas.toBuffer());
}

generateDevRadar();