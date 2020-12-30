try {
    document.getElementById("input").addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            let input = document.getElementById("input").value;
            console.log(input);
        }
    });

    document.getElementById("default1").addEventListener("click", function(event) {
        console.log("Default 1!");
        let input = `Moe_Szyslak: (INTO PHONE) Moe's Tavern. Where the elite meet to drink.
                    Bart_Simpson: Eh, yeah, hello, is Mike there? Last name, Rotch.
                    Moe_Szyslak: (INTO PHONE) Hold on, I'll check. (TO BARFLIES) Mike Rotch. Mike Rotch. Hey, has anybody seen Mike Rotch, lately?
                    Moe_Szyslak: (INTO PHONE) Listen you little puke. One of`
    })

    document.getElementById("default2").addEventListener("click", function(event) {
        console.log("Default 2!");
        let input = `Lenny_Leonard: It's too late to turn back, Moe. We've exchanged meaningful looks.
                    Moe_Szyslak: No, you can still turn back! The point of no return is the whispered huddle.
                    Moe_Szyslak: Oh God, oh God!            
                    Homer_Simpson: Ahhh, that is so much better than hospital beer.
                    Lenny_Leonard: Homer, where you been the last`
    })

    document.getElementById("default3").addEventListener("click", function(event) {
        console.log("Default 3!");
        let input = `Carl_Carlson: Calm down, calm down! She doesn't know it's you.
                    Carl_Carlson: (SCREAMS) Hide! Hide!
                    Moe_Szyslak: Uh, hello? Oh, sure, Liser, your Dad's right here.
                    Lisa_Simpson: (ON PHONE) Dad? Did you just call?
                    Homer_Simpson: Uh, yeah. Hey, listen, your mom thinks that maybe you and I should have dinner together, sometime`
    })
}
catch {

}