function getvalue(a)
{
    var val = a.substr(0,a.length-2)
    val = parseInt(val)
    console.log(val)
    return val

}
function getstring(a)
{
    var str = a.toString()
    str +='px'
    // console.log()
    return str
}
function movespatula()
{
    console.log("inside movespatula")
    // var samplevar  = document.querySelector('#sample')
    // var spatulavar  = document.querySelector('#spatula')
    // // var spatstyle = getComputedStyle(spatulavar);
    // var spatheight = getvalue(spatstyle.getPropertyValue('height'));
    // var samplestyle = getComputedStyle(samplevar);
    // var top1 = getvalue(samplestyle.getPropertyValue('top'));
    // var left1 = getvalue(samplestyle.getPropertyValue('left'));
    // var width = getvalue(samplestyle.getPropertyValue('width'));
    // console.log(top1)
    // console.log(left1)
    // console.log(width)
    // getvalue(width)
    var test = 0
    var a1 = anime.timeline({
        targets: document.getElementById('spatula3'),
        duration: 1200, 
        easing:'linear',
       
        
    })
    var a0 = anime.timeline({
        targets: document.getElementById('spatula1'),
        duration: 1200, 
        easing:'linear',
       
        
    }).add({
        // top:getstring(top1-spatheight+36),
        opacity:1,
        // left:getstring(left1+width/3),
        
        
    }).add({
        translateY:'2vh',
    }).add({
        
    }).add({
        translateY: '-4vw',
    }).add({
        opacity:0,
    })
    a1.add({
        delay:5000,
        opacity:1,
    }).add({
        rotateZ:'20',
    }).add({
        opacity:0,
        zIndex:0,
    })
}

function fetchwater()
{
    var a1 = anime.timeline({
        targets: document.getElementById('dropper1'),
        duration: 1200, 
        easing:'linear',
       })

       var a2 = anime.timeline({
        targets: document.getElementById('dropper2'),
        duration: 1200, 
        easing:'linear',
       })
       var a3 = anime.timeline({
        targets: document.getElementById('water1'),
        duration: 1200, 
        easing:'linear',
       })
       var a4 = anime.timeline({
        targets: document.getElementById('water2'),
        duration: 1200, 
        easing:'linear',
       })

       a1.add({
           opacity:1,
       })
       a3.add({
           delay:1500,
           opacity:1,
       }).add({
           opacity:0,
       })
       a1.add({
           delay:2000,
           opacity:0,
       })

       a2.add({
           delay:3000,
           opacity:1,
       })
       a4.add({
           delay:3000,
           opacity:1,
       })
       a2.add({
           delay:1800,
           opacity:0,
       })
       a4.add({
           delay:1000,
           opacity:0,
       })

}

function movemixer()
{
    flag=2
    if (flag==1)
    {
    var a1 = anime.timeline({
        targets: document.getElementById('mixer'),
        duration: 1200, 
        easing:'linear',
       }).add({
           rotateZ:'-30',
           translateX:'-20',
       }).add({
           translateX:'20',
           rotateZ:'30',
       }).add({
        rotateZ:'-30',
        translateX:'-20',
         }).add({
        translateX:'20',
        rotateZ:'30',
        })
    }
    else if (flag==2)
    {
        console.log("isndide flag2")
        var a1 = anime.timeline({
            targets: document.getElementById('spatula3'),
            duration: 1200, 
            easing:'linear',
        })
        var a2 = anime.timeline({
            targets: document.getElementById('spatula4'),
            duration: 1200, 
            easing:'linear',
        })
        var a3 = anime.timeline({
            targets: document.getElementById('ircontent'),
            duration: 1200, 
            easing:'linear',
        })
        a1.add({
            zIndex:2,
        }).add({
            opacity:1,
        }).add({
            translateY:'-35',
        }).add({
            opacity:0,
        }).add({
            zIndex:0,
        })

        a2.add({
            zIndex:3,
        }).add({
            delay:3000,
            opacity:1,
        }).add({
            rotate:'30',
        }).add({
            opacity:0,
            
        }).add({
            zIndex:0,
        })

        a3.add({
            delay:6000,
            opacity:1,
        })
    }
}

function moveplates()
{
    var ir2prop  = document.querySelector('#irplate2')
    var ir3prop  = document.querySelector('#irplate3')
    var plate1prop  = document.querySelector('#plate1')
    var plate2prop  = document.querySelector('#plate2')
    var ir2style = getComputedStyle(ir2prop);
    var ir3style = getComputedStyle(ir3prop);
    var plate1style = getComputedStyle(ir2prop);
    var plate2style = getComputedStyle(ir3prop);
    var leftir2 = getvalue(ir2style.getPropertyValue('left'));
    var leftir3 = getvalue(ir3style.getPropertyValue('left'));

    var irheight = getvalue(ir3style.getPropertyValue('height'));

    var leftpl1 = getvalue(plate1style.getPropertyValue('left'));
    var leftpl2 = getvalue(plate2style.getPropertyValue('left'));

    var plheight = getvalue(plate1style.getPropertyValue('height'));
    var pltop = getvalue(plate1style.getPropertyValue('top'));
    var irtop = getvalue(ir2style.getPropertyValue('top'));

    console.log("above values")
    console.log("height=",plheight)
    console.log(leftir2,leftir3)
    console.log("diff=",leftir2-leftir3)
    var shift = getstring(leftir2-leftir3)
    console.log("top=",pltop)
    console.log("shift=",shift)
    console.log("topper1=",pltop)
    console.log("topper2=",irtop)
    var downshift = getstring(-pltop+irtop);
    console.log("downshift = ",downshift)
  
    var a2 = anime.timeline({
        targets: document.getElementById('irplate3'),
        duration: 1200, 
        easing:'linear',
    })
    var a5 = anime.timeline({
        targets: document.getElementById('irplate2'),
        duration: 1200, 
        easing:'linear',
    })
    var a3 = anime.timeline({
        targets: document.getElementById('plate2'),
        duration: 1200, 
        easing:'linear',
    })

    a2.add({
        translateY:'-2em',
    }).add({
        opacity:0,
        zIndex:0,
    })

    var a1 = anime.timeline({
        targets: document.getElementById('irplate4'),
        duration: 1200, 
        easing:'linear',
    }).add({
        delay:3000,
        opacity:1,
        translateY:'3em',
        
    }).add({
        opacity:0,
    })

    
    

}

function moveborderplates()
{
    console.log("inside moveborderplates")
    var a5 = anime.timeline({
        targets: document.getElementById('irplate2'),
        duration: 1200, 
        easing:'linear',
    })
    var a2 = anime.timeline({
        targets: [document.getElementById('irplate2'),document.getElementById('redcircle1')],
        duration: 1200, 
        easing:'linear',
    })
    var a4 = anime.timeline({
        targets: [document.getElementById('irplate5'),document.getElementById('redcircle2')],
        duration: 1200, 
        easing:'linear',
    })
    var a3 = anime.timeline({
        targets: document.getElementById('plate2'),
        duration: 1200, 
        easing:'linear',
    })
    a4.add({
        delay:2000,
        opacity:1,
    })
    a2.add({
        translateY:'3em',
    }).add({
        opacity:0,
        zIndex:0,
    })
    a3.add({
        delay:4000,
        zIndex:7,
        translateY:'-14em',
    })
}

function shiftmovable()
{
    var a1 = anime.timeline({
        targets: document.getElementById('movable'),
        duration: 1200, 
        easing:'linear',
    }).add({
        translateY:'4em',
    })
}

function shiftir()
{
    var a1 = anime.timeline({
        targets: document.getElementById('line1'),
        duration: 1200, 
        easing:'linear',
    })
    var a2 = anime.timeline({
        targets: document.getElementById('line2'),
        duration: 1200, 
        easing:'linear',
    })
    var a3 = anime.timeline({
        targets: document.getElementById('lineup1'),
        duration: 1200, 
        easing:'linear',
    })
    var a4 = anime.timeline({
        targets: document.getElementById('lineup2'),
        duration: 1200, 
        easing:'linear',
    })
    var a5 = anime.timeline({
        targets: document.getElementById('lineright1'),
        duration: 1200, 
        easing:'linear',
    })
    var a6 = anime.timeline({
        targets: document.getElementById('lineright2'),
        duration: 1200, 
        easing:'linear',
    })
    var a7 = anime.timeline({
        targets: document.getElementById('linedown1'),
        duration: 1200, 
        easing:'linear',
    })
    var a8 = anime.timeline({
        targets: document.getElementById('linedown2'),
        duration: 1200, 
        easing:'linear',
    })
    a1.add({
        opacity:1
    })
    a2.add({
        delay:320,
        opacity:1,
    })
    a3.add({
        delay:800,
        opacity:1,
    })
    a4.add({
        delay:960,
        opacity:1,
    })

    a5.add({
        delay:800,
        opacity:1,
    })
    a6.add({
        delay:1070,
        opacity:1,
    })

    a3.add({
        delay:100,
        opacity:0,
    })
    a4.add({
        opacity:0,
    })
    a5.add({
        delay:100,
        opacity:0,
    })
    a6.add({
        opacity:0,
    })

    a4.add({
        delay:300,
        opacity:1,
    })
    a3.add({
        delay:610,
        opacity:1,
    })

    a6.add({
        delay:300,
        opacity:1,
    })
    a5.add({
        delay:630,
        opacity:1,
    })

    a7.add({
        delay:5200,
        opacity:1,
    })

    a8.add({
        delay:5500,
        opacity:1,
    })




}