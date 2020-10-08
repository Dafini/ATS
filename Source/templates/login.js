function setup(){
    createCanvas(400,400);
    background(51);
    loadJason('/login', gotData)
    console.log('running');
}
function gotData(data){
    console.log(data);
}