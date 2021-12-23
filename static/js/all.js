// icon show for password
function hidepass(){
    var mypass =document.getElementById("myinput")
    var hideepass =document.getElementById("hide1")
    var showpass =document.getElementById("hide2")
    if(mypass.type === "password"){
        mypass.type = "text";
        hideepass.style.display = "block";
        showpass.style.display = "none";
    }
    else{
        mypass.type = "password";
        hideepass.style.display = "none";
        showpass.style.display = "block";
    }
};

function hidepass1(){
  var mypass2 =document.getElementById("myinput2")
  var mypass1 =document.getElementById("myinput1")
  var hideepass1 =document.getElementById("hide3")
  var showpass1 =document.getElementById("hide4")
  if(mypass2.type === "password" && mypass1.type === "password"){
      mypass2.type = "text";
      mypass1.type = "text";
      hideepass1.style.display = "block";
      showpass1.style.display = "none";
  }
  else{
      mypass2.type = "password";
      mypass1.type = "password";
      hideepass1.style.display = "none";
      showpass1.style.display = "block";
  }
};
// for product detail imgs
$(document).ready(function(){
    $(".changeimg").click(function(){
         $(".changeimgresult").html($(this).html());
    });
});

    // side bar
    $(".lab1").click(function(){
      $(".hidemenu1").fadeToggle();
      });   

    $(".lab2").click(function(){
      $(".hidemenu2").fadeToggle();
      });  

    $(".lab3").click(function(){
      $(".hidemenu3").fadeToggle();
      });  
// order management
    $(".showorder1").click(function(){
      $(".hidordermanage1").fadeToggle();
      });
    $(".showorder2").click(function(){
      $(".hidordermanage2").fadeToggle();
      });
    $(".showorder3").click(function(){
      $(".hidordermanage3").fadeToggle();
      });