let path = anime.path('#demo-svg path')
let spatulaflag = 0
let dropperflag = 0
let mixerflag1 = 1
let mixerflag2 = 0
let messagearr = [
    'Hello1',"hello2","hello3"
]
// var movspat = anime({
//     targets : document.getElementById('mysvg'),
//     translateX: path('x'),
//     translateY: path('y'),
//     easing: 'linear',
//     duration: 5000,
//     loop: true

// })
function movespatula()
{
    if (spatulaflag==0)
    {
    console.log("inside function")
    var a1 = anime.timeline({
    targets: document.getElementById('spatula'),
    // opacity:'0.5',
    duration: 1200, 
    easing: 'linear',
})
a1.add({
    translateY: '5vw',
    opacity:'1'
}).add({ 
    translateY: '-5vw',
    
}).add({
    // opacity:'0',
    translateX:'10vw',
    
    // opacity:'1',
}).add({
    translateY:'9.8vw',
    
}).add({
    rotateZ:'30',
    
    // rotatez:'20',
}).add({
    rotateZ:'30',
    opacity:'0',
    // rotatez:'20',
}).add({
    update: function(anim) {
        document.getElementById("message").innerHTML = messagearr[0];
    }
});
    }
    spatulaflag = spatulaflag + 1;
}

function movedropper()
{
    if (dropperflag==0)
    {

    // var a1 = anime.timeline({
    //     targets: document.getElementById('dropperwater'),
    //     // opacity:'0.5',
    //     duration: 1200, 
    //     easing: 'linear',
    // })
    
   
    // a1.add({
    //     opacity:0.5,
    //     easing: 'linear',
    // })
    
   
 
var a2 = anime.timeline({
    targets:  document.getElementById('dropper'),
    //duration: 1200, 
    easing: 'linear',
})
a2.add({
    opacity:'1',
}).add({ 
    translateY: '5vw',
    
})
var a3 = anime.timeline({
    targets: document.getElementById('dropperwater'),
    //duration: 1200, 
    easing: 'linear',
})
var a5 = anime.timeline({
    targets: document.getElementById('dropper3'),
    //duration: 1200, 
    easing: 'linear',
})
a3.add({
   // delay:3000,
   delay:2900,
    opacity:1,
})

a2.add({
    //delay:2700,
    delay:1500,
    opacity:0,
})


a3.add({
    delay:10,
    opacity:0,
})


var a4 = anime.timeline({
    targets: [document.getElementById('dropper2'),document.getElementById('dropperwater2')],
    //duration: 1200, 
    easing: 'linear',
})
a4.add({
    //delay:7000,
    delay: 2000,
    opacity:1,
    // translateY:'-10vw',
}).add({
    delay:1500,
    translateY:'-10vw',
}).add({
    translateX:'-10.6vw',
}).add({
    translateY:'5.5vw',
}).add({
    delay:1000,
    opacity:0,
})
a5.add({
    delay:8000,
    opacity:1,
}).add({
    delay:1000,
    opacity:0,
}).add({
    update: function(anim) {
        document.getElementById("message").innerHTML = messagearr[2];
    }
})

console.log("inside function")
     }
    dropperflag = dropperflag + 1;
}

function movemixer()
{
    console.log("inside movemixer")
    if (mixerflag1==1)
    {
    var a1 = anime.timeline({
        targets:"#mixer",
        duration: 1000, 
        easing: 'linear',
    }).add({
        translateX:'-3vw',
        rotateZ:'-28',
    }).add({
        translateX:'1vw',
        rotateZ:'28',
    }).add({
        translateX:'-3vw',
        rotateZ:'-28',
    }).add({
        translateX:'1vw',
        rotateZ:'28',
    }).add({
        update: function(anim) {
            document.getElementById("message").innerHTML = messagearr[1];
        }
    })
    mixerflag1=0
    mixerflag2=1
    }
    else if(mixerflag2==1)
    {
        var a1 = anime.timeline({
            targets: document.getElementById('spatula2'),
            // opacity:'0.5',
            duration: 1200, 
            easing: 'linear',
        })
        var a2 = anime.timeline({
            targets: document.getElementById('ircontent'),
            // opacity:'0.5',
            duration: 1200, 
            easing: 'linear',
        })
        a1.add({ 
            opacity:1,
            translateY: '-5vw',
            
        }).add({
            // opacity:'0',
            translateX:'11vw',
            
            // opacity:'1',
        }).add({
            translateY:'0.5vw',
            
        }).add({
            rotateZ:'30',
            
            // rotatez:'20',
        }).add({
            rotateZ:'30',
            opacity:'0',
            // rotatez:'20',
        }).add({
            update: function(anim) {
                document.getElementById("message").innerHTML = messagearr[0];
            }
        });
        a2.add({
            delay:4000,
            opacity:1,
        })
    }
}

function circles()
{
    console.log("inside construct circle")
    var a1 = anime.timeline({
        targets:"#createcircle",
        duration: 1000, 
        easing: 'linear',
    }).add({
        opacity:1,
    })
}

function moveirplates()
{
    var a1 = anime.timeline({
        targets: document.getElementById('irplate1'),
        // opacity:'0.5',
        duration: 1200, 
        easing: 'linear',
    })
    var a2 = anime.timeline({
        targets: document.getElementById('irplate2'),
        // opacity:'0.5',
        duration: 1200, 
        easing: 'linear',
    })
    a1.add({ 
        translateY: '-5vw',
        
    }).add({
        // opacity:'0',
        translateX:'20vw',
        
        // opacity:'1',
    }).add({
        translateY:'0.2vw',
        opacity:'0',
        
    }).add({
        translateX:'-0.2vw',
        opacity:'0',
        
    }).add({
        update: function(anim) {
            document.getElementById("message").innerHTML = messagearr[0];
        }
    });
    
}

function fitplate()
{
    console.log("inside fitplate")
    var a2 = anime.timeline({
        targets: document.getElementById('withoutborderplate'),
        // opacity:'0.5',
        duration: 1200, 
        easing: 'linear',
    })
    var a1 = anime.timeline({
        targets: [document.getElementById('irplate2'),document.getElementById('redcircle')],
        // opacity:'0.5',
        duration: 1200, 
        easing: 'linear',
    }).add({
        translateY:'9.25vw',

    })
    a2.add({
        delay:3000,
        translateX:'-20vw',
    })

}
