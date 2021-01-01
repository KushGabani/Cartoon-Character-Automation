const handleDownloadClick = (text) => {
    text = text.replaceAll("<br>", "")
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', "./generated_script.txt");
    element.style.display = 'none';

    document.body.appendChild(element);
    element.click();

    document.body.removeChild(element);
}

try {
    document.getElementById("input").addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            let input = document.getElementById("input").value;
            submitInput(input);
        }
    });

    document.getElementById("default1").addEventListener("click", function(event) {
        console.log("Default 1!");
        let input = `Marge: Well, leave it to good old Mary Bailey to finally step in and do something about that hideous genetic mutation. <br/>
                     Homer: Mary Bailey well if I was governor i'd sure find better things to do with my time. <br/>
                     Marge: Like what? homer like getting,`
        submitInput(input);
    })

    document.getElementById("default2").addEventListener("click", function(event) {
        console.log("Default 2!");
        let input = `Lenny_Leonard: It's too late to turn back, Moe. We've exchanged meaningful looks. <br/>
                    Moe_Szyslak: No, you can still turn back! The point of no return is the whispered huddle. <br/>
                    Moe_Szyslak: Oh God, oh God! <br/>      
                    Homer_Simpson: Ahhh, that is so much better than hospital beer. <br/>
                    Lenny_Leonard: Homer, where you been the last`
        submitInput(input);
    })

    document.getElementById("default3").addEventListener("click", function(event) {
        console.log("Default 3!");
        let input = `Carl_Carlson: Calm down, calm down! She doesn't know it's you. <br/>
                    Carl_Carlson: (SCREAMS) Hide! Hide! <br/> 
                    Moe_Szyslak: Uh, hello? Oh, sure, Liser, your Dad's right here.<br/>
                    Lisa_Simpson: (ON PHONE) Dad? Did you just call? <br/>
                    Homer_Simpson: Uh, yeah. Hey, listen, your mom thinks that maybe you and I should have dinner together, sometime`
        submitInput(input);
    })

    let submitInput = (input) => {
        console.log(input);
        document.getElementById("input").value = input;
        document.getElementById("submit").click();
    }
   
}
catch {

}