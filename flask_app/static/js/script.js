
// function createForm(){
//     var elem = document.querySelector('#sam')
// }

function clickSamurai(elem){
    elem.style = "color: dodgerblue"
    ninText()
    
}

function samuraiImg(){
    var x = document.getElementById("main");
    x.src="{{url_for('static', filename='img/main_classes/main_sam.jpg')}}"
    // "{{ url_for('static', filename='img/main_classes/main_sam.jpg') }}"
}

function ninText(){
    var elem = document.getElementById("ninja")
    elem.style = "color: black"
}

function samText(){
    var elem = document.getElementById("sam")
    elem.style = "color: black"
}

function clickNinja(elem){
    elem.style = "color: dodgerblue"
    samText()
    
}


function show() {
    var elem = document.getElementById("myDIV");
    elem.style.display = "block"
    // if (elem.style.display === "none") {
    //   elem.style.display = "block";
    // // } else {
    // //   elem.style.display = "none";
    // }
}

function show1() {
    var elem = document.getElementById("myDIV1");
    elem.style.display = "block"
    // if (elem.style.display === "none") {
    //   elem.style.display = "block";
    // } else {
    //   elem.style.display = "none";
    // }
}

function show2() {
    var elem = document.getElementById("myDIV2");
    elem.style.display = "block"
    // if (elem.style.display === "none") {
    //   elem.style.display = "block";
    // } else {
    //   elem.style.display = "none";
    // }
}

function show_all(){
    show();
    show1();
    show2();
}