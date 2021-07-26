"use strict";
let overallIteration = -4;
let divWidth;
let videoSpeed = 1;
let speedFactor = 1.0;
let blue = "#00a8f3";
let purple = "#b83dba";

let fillSyringe = async () => {
  if (overallIteration === 4) {
    document.getElementById("line3").style.stopColor = "green";
    const line = document.getElementById("half-grad3");
    const yFinalPosition = 0;
    let yPos = 100;
    const interval = window.setInterval(() => {
      if (yPos < yFinalPosition) {
        line.setAttribute("y1", "0.1%");
        return window.clearInterval(interval);
      }
      yPos -= 0.6;
      line.setAttribute("y1", `${yPos}%`);
    }, 1);
    overallIteration++;
    if (overallIteration === 2) {
      document.getElementById("solvent-beaker").style.cursor = "pointer";
      document.getElementById("sample-beaker").style.cursor = "default";
    } else if (overallIteration === 5) {
      document.getElementById("mortar").style.cursor = "default";
    }
  }
};

let emptySyringe = async () => {
  document.getElementById("line3").style.stopColor = "white";
  const line = document.getElementById("half-grad3");
  const yFinalPosition = 0;
  let yPos = 100;
  const interval = window.setInterval(() => {
    if (yPos < yFinalPosition) {
      line.setAttribute("y1", "0.1%");
      return window.clearInterval(interval);
    }
    yPos -= 0.6;
    line.setAttribute("y1", `${yPos}%`);
  }, 1);

  // Filling the IR plate slit
  let path = document.getElementById("plate");
  let final = 1;
  let cur = 0;
  while (true) {
    if (cur > final) {
      break;
    }
    cur += 0.01;
    path.setAttribute("offset", cur);
    await new Promise((resolve) => setTimeout(resolve, 2));
  }

  document.getElementById("mortar").style.cursor = "default";
  document.getElementById("irplate").style.cursor = "pointer";
};

async function moveJrCell(x) {
  let image = document.getElementById("irplate");
  image.setAttribute("opacity", "1");
  let a1 = anime.timeline({
    targets: "#irplate",
    duration: 800,
    easing: "linear",
  });
  if (x === 0 && overallIteration === 6) {
    screenWidth();

    if (divWidth < 769) {
      a1.add({
        duration: 1000,
        translateY: 280,
        translateX: -60,
        scale: 0.25,
      }).add({
        opacity: 0,
      });
    } else {
      a1.add({
        duration: 1000,
        translateX: 410,
        scale: 0.25,
      }).add({
        opacity: 0,
      });
    }

    document.getElementById("instruction").innerHTML =
      "Click on Observe button to observe what is happening inside the desiccator and choose video speed according to your own liking.";

    document.getElementById("observation").innerHTML =
      "Click on Observe button to observe what is happening inside the desiccator and choose video speed according to your own liking.";
  } else if (x === 1) {
    let a1 = anime.timeline({
      targets: "#irplate",
      duration: 800,
      easing: "linear",
    });
    a1.add({
      duration: 1000,
      translateX: 0,
      translateY: 0,
      scale: 1,
    });
  }
}

let fillPipette = async () => {
  const line = document.getElementById("half-grad2");
  const yFinalPosition = 0;
  let yPos = 100;
  const interval = window.setInterval(() => {
    if (yPos < yFinalPosition) {
      line.setAttribute("y1", "0.1%");
      return window.clearInterval(interval);
    }
    yPos -= 0.6;
    line.setAttribute("y1", `${yPos}%`);
  }, 1);
};

function pur() {
  if (overallIteration === 1) {
    changeMessage();
    console.log("spooooooom");
    let image = document.getElementById("spoon1");
    image.setAttribute("opacity", "1");
    image.style.transform = "translate(200%, -5%);";
    image.style.pointerEvents = "none";
    let a1 = anime.timeline({
      targets: "#spoon1",
      duration: 800,
      easing: "linear",
    });

    screenWidth();
    let endX = "300%";
    let endY = "120%";

    if (divWidth < 769) {
      endY = "240%";
      endX = "250%";
    }

    a1.add({
      duration: 0,
      translateX: "280%",
      translateY: "-125%",
    })
      .add({
        duration: 800,
        translateY: "-55%",
      })
      .add({
        translateY: "-125%",
        update: function (anim) {
          document.getElementById("spoon-mouth").style.fill = purple;
          document.getElementById("spoon-mouth").style.opacity = "1";
        },
      })
      .add({
        duration: 800,
        translateX: endX,
        translateY: endY,
      })
      .add({
        delay: "800",
        rotateZ: "45",
      })
      .add({
        update: function (anim) {
          document.getElementById("spoon-mouth").style.fill = purple;
          document.getElementById("spoon-mouth").style.opacity = "0";
          document.getElementById("bottom").style.fill = purple;
        },
        opacity: 0,
      });
    document
      .getElementById("solvent-beaker")
      .setAttribute("onclick", "movePipette()");
    overallIteration++;
    document.getElementById("sample-beaker").style.cursor = "default";
    document.getElementById("solvent-beaker").style.cursor = "pointer";

    if (restartAnimation) {
      a1.restart();
    }
  }
}

async function liftPiston() {
  let image = document.getElementById("syringe-piston");
  image.style.transform = "translate(100%, -5%);";
  image.style.pointerEvents = "none";
  let a1 = anime.timeline({
    targets: "#syringe-piston",
    duration: 800,
    easing: "linear",
  });
  a1.add({
    duration: 0,
    translateY: "8%",
  }).add({
    duration: 800,
    translateY: "-3%",
  });
}

async function movePipette() {
  if (overallIteration === 2) {
    changeMessage();
    let image = document.getElementById("pipette");
    image.setAttribute("opacity", "1");
    image.style.pointerEvents = "none";
    let a1 = anime.timeline({
      targets: "#pipette",
      duration: 800,
      easing: "linear",
    });
    let startX = "450%";
    let startY = "-150%";

    screenWidth();
    console.log("DivWidth for movePipette: ", divWidth);

    let endX = "-290%";
    let endY = "110%";

    if (divWidth < 769) {
      startY = "-120%";
      startX = "480%";
      endY = "230%";
      endX = "-450%";
    }

    a1.add({
      duration: 0,
      translateY: startY,
      translateX: startX,
    });
    fillPipette();

    await new Promise((r) => setTimeout(r, 1000));
    a1.add({
      duration: 500,
      translateX: endX,
    })
      .add({
        duration: 800,
        translateY: endY,
      })
      .add({
        update: function (anim) {
          document.getElementById("top").style.fill = blue;
        },
        opacity: 0,
      });
    document.getElementById("mortar").setAttribute("onclick", "shakeBeaker()");
    overallIteration++;
    document.getElementById("solvent-beaker").style.cursor = "default";
    document.getElementById("mortar").style.cursor = "pointer";

    if (restartAnimation) {
      a1.restart();
    }
  }
}

async function shakeBeaker() {
  if (overallIteration === 3) {
    changeMessage();
    let image = document.getElementById("mixer");
    image.style.opacity = 1;
    let sc = 1;
    screenWidth();
    if (divWidth < 769) {
      sc = 0.5;
    }
    let a1 = anime.timeline({
      targets: "#mixer",
      duration: 800,
      easing: "easeInOutSine",
      direction: "alternate",
      loop: 0,
    });

    let startY = "-100%";
    let startX = "-600%";

    if (divWidth < 769) {
      startX = "-300%";
      startY = "-70%";
    }

    a1.add({
      duration: 0,
      translateY: startY,
      translateX: startX,
      scale: sc,
    })
      .add({
        rotate: [20, 0, -20, 0],
      })
      .add({
        update: function (anim) {
          document.getElementById("top").style.fill = "green";
          document.getElementById("bottom").style.fill = "green";
        },
      })
      .add({
        opacity: 0,
      });
    document.getElementById("mortar").setAttribute("onclick", "moveSyringe()");
    overallIteration++;

    if (restartAnimation) {
      a1.restart();
    }
  }
}

async function moveSyringe() {
  if (overallIteration === 4) {
    let image = document.getElementById("syringe");
    image.style.opacity = 1;
    image.style.pointerEvents = "none";
    let a1 = anime.timeline({
      targets: "#syringe",
      duration: 800,
      easing: "linear",
    });

    let startX = "-1500%";
    let startY = "-240%";
    let endX = "-1000%";
    let endY = "-180%";

    screenWidth();
    console.log("DivWidth for moveSyringe: ", divWidth);

    // if (divWidth > 1759) {
    //   startX = "-1500%";
    //   startY = "-240%";
    //   endX = "-1000%";
    //   endY = "-180%";
    // }

    if (divWidth < 769) {
      startX = "-260%";
      startY = "-920%";
      endX = "520%";
      endY = "-890%";
    }

    a1.add({
      duration: 0,
      translateY: startY,
      translateX: startX,
      rotateZ: 0,
    });
    liftPiston();
    fillSyringe();
    await new Promise((r) => setTimeout(r, 1000));
    a1.add({
      duration: 100,
      rotateZ: 90,
    }).add({
      duration: 1000,
      translateY: endY,
      translateX: endX,
    });
    await new Promise((r) => setTimeout(r, 1300));
    emptySyringe();
    await new Promise((r) => setTimeout(r, 1300));
    document.getElementById("syringe").style.opacity = 0;
    changeMessage();
    overallIteration++;

    if (restartAnimation) {
      a1.restart();
    }

    restartAnimation = false;
  }
}

let setupMessages = [
  "Click on the Sample Beaker option in the Apparatus Menu to introduce it into the workspace.",
  "Click on the Solvent Beaker option in the Apparatus Menu to introduce it into the workspace.",
  "Click on the Mortar option in the Apparatus Menu to introduce it into the workspace.",
  "Click on the IR Plate option in the Apparatus Menu to introduce it into the workspace.",
  "Click on the Dessicator option in the Apparatus Menu to introduce it into the workspace.",
];

let setup = 0;

function setupMessage() {
  document.getElementById("instruction").innerHTML = setupMessages[setup];
  document.getElementById("observation").innerHTML = setupMessages[setup];
  setup++;
}

setupMessage();
async function visibility(x) {
  if (x === 1 && overallIteration === -4) {
    document.getElementById("sample-beaker").style.visibility = "visible";
    overallIteration++;
    setupMessage();
  } else if (x === 2 && overallIteration === -3) {
    document.getElementById("solvent-beaker").style.visibility = "visible";
    overallIteration++;
    setupMessage();
  } else if (x === 3 && overallIteration === -2) {
    document.getElementById("mortar").style.visibility = "visible";
    overallIteration++;
    setupMessage();
  } else if (x === 4 && overallIteration === -1) {
    document.getElementById("irplate").style.visibility = "visible";
    overallIteration++;
    setupMessage();
  } else if (x === 5 && overallIteration === 0) {
    document.getElementById("desiccator-row").style.visibility = "visible";
    overallIteration++;
    changeMessage();
  }
}

let instructionMessages = [
  "Click on the Sample Beaker to transfer small amount (around 1mg) of the Sample substance into the empty Mortar",
  "Click on the Solvent Beaker to transfer 5 ml of the Solvent (Nizol) to the Mortar.",
  "Click on the  Mortar to grind the mixture and make a paste.",
  "Click on the Mortar to draw 1 ml of the solution prepared to load on to the IR Plate.",
  "Click on the IR Plate to put it into the Desiccator.",
];
let iter1 = -1;
function changeMessage() {
  iter1++;
  document.getElementById("instruction").innerHTML = instructionMessages[iter1];
  document.getElementById("observation").innerHTML = instructionMessages[iter1];
}

document.getElementById("sample-beaker").style.cursor = "pointer";

let iter2 = -1;
let observationMessages = [
  "Now observe the zoomed in animation of the Desiccator. The ray goes from the IR Source to the Beam Splitter, from where it further proceeds to the Fixed and Movable Mirrors. The reflected rays are merged at the Beam Splitter and proceed towards the Detector for detection.",
  "The points on the graph are used to depict the Intensity of the ray detected.",
];

function observeMessage() {
  if (restartAnimation) {
    return;
  }
  iter2++;
  console.log("Exists");
  document.getElementById("instruction").innerHTML = observationMessages[iter2];
  document.getElementById("observation").innerHTML = observationMessages[iter2];
}

function screenWidth() {
  divWidth = document.getElementById("workspace").clientWidth;
}

let originalSimulationHeight =
  document.getElementById("simulation").clientHeight;

document.getElementById("simulation").style.minHeight =
  originalSimulationHeight + "px";

let restartAnimation = false;

async function restart() {
  moveJrCell(1);
  document.getElementById("simulation").style.height = originalSimulationHeight;

  document.getElementById("animation-video").style.display = "none";
  document.getElementById("plotted-graph-window").style.display = "none";

  document.getElementById("head-instructions").innerHTML = "Instructions";
  document.getElementById("head-observations").innerHTML = "Instructions";
  document.getElementById("instruction").innerHTML = "";
  document.getElementById("observation").innerHTML = "";
  overallIteration = -4;
  iter2 = -1;
  iter1 = -1;
  setup = 0;
  setupMessage();
  document.getElementById("syringe").style.opacity = 0;
  document.getElementById("apparatus-bottles").style.display = "block";
  document.getElementById("apparatus-desiccator").style.display = "block";
  document.getElementById("sample-beaker").style.visibility = "hidden";
  document.getElementById("solvent-beaker").style.visibility = "hidden";
  document.getElementById("mortar").style.visibility = "hidden";
  document.getElementById("desiccator-row").style.visibility = "hidden";
  document.getElementById("irplate").style.visibility = "hidden";
  document.getElementById("slidecontainer").style.display = "none";
  restartAnimation = true;

  document.getElementById("solvent-beaker").style.cursor = "default";
  document.getElementById("sample-beaker").style.cursor = "pointer";
  document.getElementById("mortar").style.cursor = "default";

  // Resetting the Mortar
  document.getElementById("top").style.fill = "none";
  document.getElementById("bottom").style.fill = "none";

  //Resetting the IR Plate
  let path = document.getElementById("plate");
  path.setAttribute("offset", "0%");
  document.getElementById("irplate").style.cursor = "default";
  document.getElementById("irplate").setAttribute("opacity", "1");
}

async function observe() {
  if (overallIteration === 6) {
    document.getElementById("slidecontainer").style.display = "block";
    document.getElementById("apparatus-bottles").style.display = "none";
    document.getElementById("apparatus-desiccator").style.display = "none";
    document.getElementById("animation-video").style.display = "block";
    document.getElementById("animation-bottom-right").play();
    document.getElementById("head-instructions").innerHTML = "Observations";
    document.getElementById("head-observations").innerHTML = "Observations";
    document.getElementById("observation").innerHTML = "";
    document.getElementById("instruction").innerHTML = "";

    observeMessage();

    await new Promise((r) => setTimeout(r, 8000 * speedFactor));

    if (!restartAnimation) {
      overallIteration++;

      document.getElementById("instruction").innerHTML =
        "Click on Observe option in the Control Menu again to see the graph.";
      document.getElementById("observation").innerHTML =
        "Click on Observe option in the Control Menu again to see the graph.";
    }
  } else if (overallIteration === 7) {
    observeMessage();

    document.getElementById("slidecontainer").style.display = "none";

    document.getElementById("animation-video").style.display = "none";
    document.getElementById("plotted-graph-window").style.display = "block";
    createGraph();

    overallIteration++;
    setTimeout(function () {
      document.getElementById("instruction").innerHTML =
        "Click on Restart option in the Control Menu to restart the experiment from scratch.";
      document.getElementById("observation").innerHTML =
        "Click on Restart option in the Control Menu to restart the experiment from scratch.";
    }, 10000);
  }
}

let sample = document.getElementById("sample-beaker");
sample.addEventListener("click", function () {
  pur();
});

let jrcell = document.getElementById("irplate");
jrcell.addEventListener("click", function () {
  moveJrCell(0);
});

let slider = document.getElementById("slider");
let vid = document.getElementById("animation-bottom-right");
slider.oninput = function () {
  videoSpeed = slider.value;
  vid.playbackRate = videoSpeed;
  speedFactor = 1 / videoSpeed;
};

function createGraph() {
  let trace1 = {
    x: [
      3495.0, 3490.0, 3485.0, 3480.0, 3475.0, 3470.0, 3465.0, 3460.0, 3455.0,
      3450.0, 3445.0, 3440.0, 3435.0, 3430.0, 3425.0, 3420.0, 3415.0, 3410.0,
      3405.0, 3400.0, 3395.0, 3390.0, 3385.0, 3380.0, 3375.0, 3370.0, 3365.0,
      3360.0, 3355.0, 3350.0, 3345.0, 3340.0, 3335.0, 3330.0, 3325.0, 3320.0,
      3315.0, 3310.0, 3305.0, 3300.0, 3295.0, 3290.0, 3285.0, 3280.0, 3275.0,
      3270.0, 3265.0, 3260.0, 3255.0, 3250.0, 3245.0, 3240.0, 3235.0, 3230.0,
      3225.0, 3220.0, 3215.0, 3210.0, 3205.0, 3200.0, 3195.0, 3190.0, 3185.0,
      3180.0, 3175.0, 3170.0, 3165.0, 3160.0, 3155.0, 3150.0, 3145.0, 3140.0,
      3135.0, 3130.0, 3125.0, 3120.0, 3115.0, 3110.0, 3105.0, 3100.0, 3095.0,
      3090.0, 3085.0, 3080.0, 3075.0, 3070.0, 3065.0, 3060.0, 3055.0, 3050.0,
      3045.0, 3040.0, 3035.0, 3030.0, 3025.0, 3020.0, 3015.0, 3010.0, 3005.0,
      3000.0, 2995.0, 2990.0, 2985.0, 2980.0, 2975.0, 2970.0, 2965.0, 2960.0,
      2955.0, 2950.0, 2945.0, 2940.0, 2935.0, 2930.0, 2925.0, 2920.0, 2915.0,
      2910.0, 2905.0, 2900.0, 2895.0, 2890.0, 2885.0, 2880.0, 2875.0, 2870.0,
      2865.0, 2860.0, 2855.0, 2850.0, 2845.0, 2840.0, 2835.0, 2830.0, 2825.0,
      2820.0, 2815.0, 2810.0, 2805.0, 2800.0, 2795.0, 2790.0, 2785.0, 2780.0,
      2775.0, 2770.0, 2765.0, 2760.0, 2755.0, 2750.0, 2745.0, 2740.0, 2735.0,
      2730.0, 2725.0, 2720.0, 2715.0, 2710.0, 2705.0, 2700.0, 2695.0, 2690.0,
      2685.0, 2680.0, 2675.0, 2670.0, 2665.0, 2660.0, 2655.0, 2650.0, 2645.0,
      2640.0, 2635.0, 2630.0, 2625.0, 2620.0, 2615.0, 2610.0, 2605.0, 2600.0,
      2595.0, 2590.0, 2585.0, 2580.0, 2575.0, 2570.0, 2565.0, 2560.0, 2555.0,
      2550.0, 2545.0, 2540.0, 2535.0, 2530.0, 2525.0, 2520.0, 2515.0, 2510.0,
      2505.0, 2500.0, 2495.0, 2490.0, 2485.0, 2480.0, 2475.0, 2470.0, 2465.0,
      2460.0, 2455.0, 2450.0, 2445.0, 2440.0, 2435.0, 2430.0, 2425.0, 2420.0,
      2415.0, 2410.0, 2405.0, 2400.0, 2395.0, 2390.0, 2385.0, 2380.0, 2375.0,
      2370.0, 2365.0, 2360.0, 2355.0, 2350.0, 2345.0, 2340.0, 2335.0, 2330.0,
      2325.0, 2320.0, 2315.0, 2310.0, 2305.0, 2300.0, 2295.0, 2290.0, 2285.0,
      2280.0, 2275.0, 2270.0, 2265.0, 2260.0, 2255.0, 2250.0, 2245.0, 2240.0,
      2235.0, 2230.0, 2225.0, 2220.0, 2215.0, 2210.0, 2205.0, 2200.0, 2195.0,
      2190.0, 2185.0, 2180.0, 2175.0, 2170.0, 2165.0, 2160.0, 2155.0, 2150.0,
      2145.0, 2140.0, 2135.0, 2130.0, 2125.0, 2120.0, 2115.0, 2110.0, 2105.0,
      2100.0, 2095.0, 2090.0, 2085.0, 2080.0, 2075.0, 2070.0, 2065.0, 2060.0,
      2055.0, 2050.0, 2045.0, 2040.0, 2035.0, 2030.0, 2025.0, 2020.0, 2015.0,
      2010.0, 2005.0, 2000.0, 1995.0, 1990.0, 1985.0, 1980.0, 1975.0, 1970.0,
      1965.0, 1960.0, 1955.0, 1950.0, 1945.0, 1940.0, 1935.0, 1930.0, 1925.0,
      1920.0, 1915.0, 1910.0, 1905.0, 1900.0, 1895.0, 1890.0, 1885.0, 1880.0,
      1875.0, 1870.0, 1865.0, 1860.0, 1855.0, 1850.0, 1845.0, 1840.0, 1835.0,
      1830.0, 1825.0, 1820.0, 1815.0, 1810.0, 1805.0, 1800.0, 1795.0, 1790.0,
      1785.0, 1780.0, 1775.0, 1770.0, 1765.0, 1760.0, 1755.0, 1750.0, 1745.0,
      1740.0, 1735.0, 1730.0, 1725.0, 1720.0, 1715.0, 1710.0, 1705.0, 1700.0,
      1695.0, 1690.0, 1685.0, 1680.0, 1675.0, 1670.0, 1665.0, 1660.0, 1655.0,
      1650.0, 1645.0, 1640.0, 1635.0, 1630.0, 1625.0, 1620.0, 1615.0, 1610.0,
      1605.0, 1600.0, 1595.0, 1590.0, 1585.0, 1580.0, 1575.0, 1570.0, 1565.0,
      1560.0, 1555.0, 1550.0, 1545.0, 1540.0, 1535.0, 1530.0, 1525.0, 1520.0,
      1515.0, 1510.0, 1505.0, 1500.0, 1495.0, 1490.0, 1485.0, 1480.0, 1475.0,
      1470.0, 1465.0, 1460.0, 1455.0, 1450.0, 1445.0, 1440.0, 1435.0, 1430.0,
      1425.0, 1420.0, 1415.0, 1410.0, 1405.0, 1400.0, 1395.0, 1390.0, 1385.0,
      1380.0, 1375.0, 1370.0, 1365.0, 1360.0, 1355.0, 1350.0, 1345.0, 1340.0,
      1335.0, 1330.0, 1325.0, 1320.0, 1315.0, 1310.0, 1305.0, 1300.0, 1295.0,
      1290.0, 1285.0, 1280.0, 1275.0, 1270.0, 1265.0, 1260.0, 1255.0, 1250.0,
      1245.0, 1240.0, 1235.0, 1230.0, 1225.0, 1220.0, 1215.0, 1210.0, 1205.0,
      1200.0,
    ],
    y: [
      0.9302, 0.9315, 0.9328, 0.9334, 0.9331, 0.9325, 0.9318, 0.9312, 0.9309,
      0.9309, 0.9321, 0.934, 0.9361, 0.9378, 0.9394, 0.9406, 0.9418, 0.9425,
      0.9432, 0.943, 0.9424, 0.9411, 0.939, 0.9361, 0.9327, 0.929, 0.9252,
      0.9192, 0.9113, 0.9039, 0.8973, 0.8907, 0.8853, 0.8806, 0.8759, 0.8713,
      0.8667, 0.8624, 0.8581, 0.8538, 0.8494, 0.8451, 0.8403, 0.8355, 0.8307,
      0.8259, 0.8205, 0.8146, 0.8087, 0.8017, 0.7945, 0.7871, 0.7798, 0.7725,
      0.7651, 0.7576, 0.7503, 0.7428, 0.7355, 0.7278, 0.7204, 0.7128, 0.7054,
      0.6978, 0.6901, 0.6825, 0.6749, 0.6671, 0.6595, 0.6518, 0.6441, 0.6362,
      0.6285, 0.6206, 0.6129, 0.6049, 0.597, 0.5891, 0.5812, 0.5732, 0.5652,
      0.5572, 0.5491, 0.541, 0.5329, 0.5248, 0.5167, 0.5085, 0.501, 0.4957,
      0.4905, 0.4862, 0.4819, 0.4776, 0.4737, 0.4706, 0.466, 0.4623, 0.4604,
      0.4591, 0.4585, 0.458, 0.4576, 0.4575, 0.4574, 0.4567, 0.4554, 0.4541,
      0.4533, 0.4528, 0.4531, 0.4545, 0.4576, 0.4617, 0.4649, 0.4665, 0.4669,
      0.4673, 0.4675, 0.4676, 0.4677, 0.4674, 0.4662, 0.4647, 0.463, 0.4615,
      0.4601, 0.4587, 0.4574, 0.4566, 0.4562, 0.456, 0.4568, 0.4575, 0.4582,
      0.459, 0.4595, 0.4601, 0.4616, 0.466, 0.472, 0.4787, 0.4862, 0.4953,
      0.5049, 0.5166, 0.5252, 0.5324, 0.5386, 0.5441, 0.5494, 0.5547, 0.5601,
      0.5659, 0.568, 0.5688, 0.5692, 0.5691, 0.5662, 0.5614, 0.5548, 0.5467,
      0.5339, 0.5246, 0.5202, 0.518, 0.5166, 0.5154, 0.5148, 0.5141, 0.5137,
      0.5138, 0.5142, 0.52, 0.5285, 0.5347, 0.5397, 0.5431, 0.5453, 0.5464,
      0.5469, 0.5465, 0.5429, 0.538, 0.5335, 0.5299, 0.5285, 0.5283, 0.5302,
      0.5312, 0.5317, 0.5322, 0.5321, 0.5319, 0.5333, 0.5365, 0.5453, 0.554,
      0.5625, 0.5705, 0.5784, 0.5849, 0.591, 0.5972, 0.6034, 0.6112, 0.6192,
      0.6273, 0.6349, 0.6425, 0.65, 0.6575, 0.6649, 0.6722, 0.6797, 0.6872,
      0.6934, 0.6987, 0.7031, 0.7069, 0.7108, 0.714, 0.7171, 0.72, 0.7228,
      0.7249, 0.7261, 0.7275, 0.7286, 0.7295, 0.7304, 0.7314, 0.7325, 0.7336,
      0.7357, 0.7431, 0.7517, 0.7591, 0.7656, 0.7719, 0.7778, 0.7836, 0.7897,
      0.7964, 0.8024, 0.8064, 0.8105, 0.8144, 0.8181, 0.8218, 0.8245, 0.8271,
      0.8293, 0.8313, 0.8332, 0.8352, 0.8365, 0.8375, 0.8388, 0.8399, 0.841,
      0.842, 0.8436, 0.846, 0.8485, 0.8514, 0.8546, 0.8589, 0.8631, 0.8657,
      0.8654, 0.8646, 0.8635, 0.863, 0.8635, 0.8665, 0.8687, 0.869, 0.8688,
      0.8659, 0.8607, 0.8581, 0.8568, 0.856, 0.8555, 0.8553, 0.8551, 0.8549,
      0.8545, 0.8541, 0.8537, 0.8535, 0.8533, 0.8531, 0.8531, 0.8536, 0.8563,
      0.8628, 0.8648, 0.8633, 0.8591, 0.8582, 0.8631, 0.8662, 0.8662, 0.8585,
      0.8493, 0.8441, 0.8434, 0.8474, 0.8509, 0.851, 0.8504, 0.8504, 0.8506,
      0.8508, 0.8509, 0.851, 0.851, 0.851, 0.8495, 0.8401, 0.8332, 0.8283,
      0.8257, 0.8243, 0.823, 0.8141, 0.7945, 0.7795, 0.7742, 0.7726, 0.7703,
      0.7645, 0.761, 0.761, 0.7599, 0.7483, 0.7154, 0.6851, 0.6628, 0.6444,
      0.623, 0.5521, 0.4493, 0.3459, 0.2421, 0.1849, 0.1283, 0.1188, 0.2162,
      0.3246, 0.4336, 0.531, 0.533, 0.5046, 0.426, 0.3473, 0.2678, 0.1879,
      0.1077, 0.0646, 0.0638, 0.075, 0.1203, 0.2332, 0.35, 0.4678, 0.5087,
      0.5405, 0.5823, 0.6243, 0.6665, 0.6989, 0.7128, 0.718, 0.6042, 0.4123,
      0.2216, 0.2766, 0.4662, 0.6515, 0.6954, 0.6895, 0.6601, 0.6691, 0.7208,
      0.7318, 0.7632, 0.7942, 0.81, 0.8124, 0.8254, 0.8328, 0.8349, 0.8328,
      0.828, 0.8239, 0.8274, 0.8338, 0.8278, 0.7262, 0.5509, 0.585, 0.6711,
      0.6882, 0.4887, 0.2768, 0.2334, 0.354, 0.5522, 0.5656, 0.5486, 0.5334,
      0.5284, 0.4286, 0.3927, 0.4276, 0.5092, 0.5681, 0.6275, 0.6786, 0.6772,
      0.5844, 0.4909, 0.3966, 0.3959, 0.5014, 0.6662, 0.7164, 0.7315, 0.7228,
      0.6826, 0.6198, 0.5428, 0.4524, 0.3239, 0.212, 0.1016, 0.0871, 0.1199,
      0.1584, 0.1939, 0.2392, 0.3194, 0.4022, 0.4304, 0.5367, 0.5207, 0.5019,
      0.6134, 0.6253, 0.6208, 0.5674, 0.4262, 0.2453, 0.1592, 0.2105, 0.2533,
      0.2791,
    ],
    mode: "lines",
    line: {
      color: "rgb(100, 0, 0)",
      width: 3,
    },
  };

  let data = [trace1];

  var layout = {
    title: "Intensity",
    xaxis: {
      showgrid: true,
      zeroline: true,
    },
    yaxis: {
      showline: true,
    },
  };

  Plotly.newPlot("chart-container", data, layout);
}
