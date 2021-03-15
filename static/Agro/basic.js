//additional javascript for cart object
var x = document.getElementsByClassName("cart")[0];
if (x==undefined){
}
else{
    var x = document.getElementsByClassName("cart")[0].getAttribute("href");
    if (x=="/Food/cart//1"){    
        var elem=document.getElementsByClassName("cart");
        for(i=0;i<elem.length;i++){
            document.getElementsByClassName("cart")[i].style.display="none";
        }
        var y=document.getElementsByClassName("productId");
        for(i=0;i<y.length;i++){
            document.getElementsByClassName("productId")[i].style.display="none"; 
        }
    }
}
