//This code is for contactus page
//----------------------------------------------
//clear all the fields

const music = new Audio("https://www.soundjay.com/buttons/sounds/button-19.mp3");
const textmusic = new Audio("https://www.soundjay.com/buttons/sounds/button-29.mp3");

function clearFields()
{
        document.getElementById('fname').value = "";
        document.getElementById('lastname').value = "";
        document.getElementById('mobile').value = "";
        document.getElementById('email').value = "";
        document.getElementById('message').value = "";
        document.getElementById('fname').focus();
}

document.getElementById("btnclear").addEventListener('click', function(){
        music.play();
        clearFields();
        });

document.getElementById("fname").addEventListener("click", function(){
    textmusic.play();
});
document.getElementById("lastname").addEventListener("click", function(){
    textmusic.play();
});
document.getElementById("email").addEventListener("click", function(){
    textmusic.play();
});
document.getElementById("mobile").addEventListener("click", function(){
    textmusic.play();
});
document.getElementById("message").addEventListener("click", function(){
    textmusic.play();
});
document.getElementById("lastname").addEventListener("focusin", function(){
    textmusic.play();
});

function validatePhoneNumber() {
    // Get and trim phone number input
    const phoneNumber = document.getElementById('mobile').value.trim();

    // Regex pattern for 10-digit phone number
    const pattern = /^\d{10}$/;

    // Validate phone number and update message
    const isValid = pattern.test(phoneNumber);
    if(!isValid){
        alert("Please enter a valid 10-digit phone number.")
//        document.getElementById("mobile").focus();
//        document.getElementById("mobile").value="";
    }

    // Return validation status
    return isValid;
}
document.getElementById("mobile").addEventListener("blur", function(){
    validatePhoneNumber();


});
function validateNumber(e)
{
     const pattern = /^[0-9]$/;
     return pattern.test(e.key);
}

function validateEmail(emailField){
        var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        if (reg.test(emailField.value) == false)
        {
            alert('Invalid Email, Please check and try again');
//            document.getElementById("email").value=""
            return false;
        }
        return true;
}