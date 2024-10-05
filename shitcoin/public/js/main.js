import colorPossiblities from "./colors.js";


const pushingButton = document.querySelector(".pushing-button");
const layer1 = document.querySelector(".layer1");
const layer2 = document.querySelector(".layer2");
const scn = document.querySelector(".scn");
const mainContainer = document.querySelector(".mainContainer");
const shitcoinTEXT = document.querySelector(".shitcoinTEXT");
const clickingAudio = document.querySelector(".clicking-audio");
const resetButton = document.querySelector(".reset-button");
const exitButton = document.querySelector(".exit-button");
const upgradeButton = document.querySelector(".upgrade-button");




let totalShitcoin = localStorage.getItem('totalShitcoin') || 0;
let clickingPoint = localStorage.getItem('clickingPoint') || 1;


let previousColorsetNumber = ['', ''];

const transformXpossiblities = [-6, -5, -4, -3, 3, 4, 5, 6];
const transformYpossiblities = [-5, -6, -7];



const updateCoin = (task) => {
    if (task === '+') {
        totalShitcoin = Number(totalShitcoin) + Number(clickingPoint)
        localStorage.setItem('totalShitcoin', totalShitcoin)
    } else if (task === '-') {
        totalShitcoin--
        localStorage.setItem('totalShitcoin', totalShitcoin)
    } else if (task === '=') {
        shitcoinTEXT.innerHTML = localStorage.getItem('totalShitcoin')
    }

    shitcoinTEXT.innerHTML = totalShitcoin;
}


const setClickerRandomColorset = () => {
    let randomColorsetNumber = Math.floor(Math.random() * colorPossiblities.length);;

    while (previousColorsetNumber[0] === colorPossiblities[randomColorsetNumber][0] && previousColorsetNumber[1] === colorPossiblities[randomColorsetNumber][1]) {
        randomColorsetNumber = Math.floor(Math.random() * colorPossiblities.length);;
    }

    previousColorsetNumber[0] = colorPossiblities[randomColorsetNumber][0];
    previousColorsetNumber[1] = colorPossiblities[randomColorsetNumber][1];
    
    layer1.style.backgroundColor = colorPossiblities[randomColorsetNumber][0];
    layer2.style.backgroundColor = colorPossiblities[randomColorsetNumber][1];
}



const updateClickingPoint = (cp) => {
    clickingPoint = cp;
    localStorage.setItem('clickingPoint', clickingPoint)
}


setClickerRandomColorset();
updateCoin('=');


pushingButton.addEventListener('click', () => {
    updateCoin("+");

    // clickingAudio.play()

    layer1.style.top = '1rem';
    setTimeout(() => {
        layer1.style.top = '0rem';
    }, 150);

    setClickerRandomColorset()

    const _pointDIV = document.createElement('div')
    const _pointP = document.createElement('p')

    _pointP.className = 'point-p';
    _pointP.innerHTML = `+${clickingPoint}`;

    const _X = transformXpossiblities[Math.floor(Math.random() * transformXpossiblities.length)];
    const _Y = transformYpossiblities[Math.floor(Math.random() * transformYpossiblities.length)];
    _pointDIV.className = 'point-div';
    _pointDIV.style.transform = `translate(${_X}rem, ${_Y}rem)`;
    
    setTimeout(() => {
        _pointDIV.style.transform = `translate(${_X}rem, ${_Y - 3}rem)`;
        _pointDIV.style.opacity = `0`;
    }, 10);

    _pointDIV.appendChild(_pointP)
    mainContainer.appendChild(_pointDIV)

    setTimeout(() => {
        mainContainer.removeChild(_pointDIV);
    }, 500);
})



resetButton.addEventListener('click', () => {
    localStorage.removeItem('totalShitcoin');
    localStorage.removeItem('clickingPoint');
    location.reload();
})


exitButton.addEventListener('click', () => {
    location.href = 'https://google.com';
})


upgradeButton.addEventListener('click', () => {
    if (totalShitcoin >= 100000) {
        updateClickingPoint(Number(clickingPoint) + 1)
    } else {
        alert("Do not have enough coin to upgrade your clicking point !\nPrize: 100,000 coin")
    }
})