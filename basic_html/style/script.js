function tasks_onload(){
    alert('\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n 🖼 Please open this web page on desktop\n 📢 Please select cipher method before you add text...\n');
}

function validate_affine_a(val_a,n){
    if(val_a<=25 && val_a>=0){
        if(n==0){
            var f=0;
            const val=[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25];
            for (let i = 0; i < val.length; i++) {
                if(val[i]==val_a){
                    f=1;
                }
            }
            if(f==0){
                // document.getElementById("encrypted-text").textContent = "";
                // document.getElementById('encrypted-text').value='Invalid Value Input...!!!';
                delay(function(){
                    alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value..!!! 🤐🤐🤐\n✔ Please Check Rules for Value of 'a' in Affine Cipher...\n✨ The possible values that 'a' could be are 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25 ✨");
                }, 00 );
            }
        }
        else{
            var f=0;
            const val=[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25];
            for (let i = 0; i < val.length; i++) {
                if(val[i]==val_a){
                    f=1;
                }
            }
            if(f==0){
                // document.getElementById("encrypted-text").textContent = "";
                // document.getElementById('encrypted-text').value='Invalid Value Input...!!!';
                delay(function(){
                    alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value..!!! 🤐🤐🤐\n✔ Please Check Rules for Value of 'a' in Affine Cipher...\n✨ The possible values that 'a' could be are 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25 ✨");
                }, 700 );
            }
        }
    }
}

function click_it(i) {
    document.getElementById(i).click();
}

var delay = (function(){
    var timer = 0;
    return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
   };
})();

function valid_it(n,a,r1,r2){
    r1=parseInt(r1, 10)
    r2=parseInt(r2, 10)
    delay(function(){
        if(n>r2 || n<r1){
            alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Valid Range for '"+a+"' is ("+r1+"-"+r2+"). ✨\n✔ Enter Values Accordingly Please...!!!");
        }
    }, 700 );
}


function genrandom(length) {
    if(length<0){
            // alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Only Positive Values Allowed For Length of Key. ✨\n✔ Enter Values Accordingly Please...!!!");
            location.reload();
    }
    else{
        var chars = "abcdefghiklmnopqrstuvwxyz";
        var string_length = length;
        var tmp = '';
        var randomstring = '';
        for (var i=0; i<string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        tmp=chars.substring(rnum,rnum+1);
        randomstring += tmp;
        chars = chars.replace(tmp, '');
    }
    return randomstring;
    }
}

function alertmsg(d,r1,r2){
    let n = document.getElementById(d).value;
    if((n>r2 || n<r1) && (d=="columnar_key_l")){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Valid Range for 'Length of key for Columnar Transposition Cipher' is ("+r1+"-"+r2+"). ✨\n✔ Enter Values Accordingly Please...!!!");
    }
    else if((n>r2 || n<r1) && (d=="play_fair_key_l")){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Valid Range for 'Length of key for Play fair Cipher' is ("+r1+"-"+r2+"). ✨\n✔ Enter Values Accordingly Please...!!!");
    }
    else if((n>r2 || n<r1) && (d=="vigenere_key_l")){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Valid Range for 'Length of key for Vigenere Cipher' is ("+r1+"-"+r2+"). ✨\n✔ Enter Values Accordingly Please...!!!");
    }
    else{
        alertify.message('Random Key Generation Successful..!!! 😎✌🎉'); 
    }
}
function alertsucc(d){
    let text = document.getElementById(d).value;
    if(text.length!=0){
        alertify.message('Input Data Submitted Successfully...!!! 😎✌🎉'); 
    }
    else if(d=="columnar_key"){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for Columnar Cipher Can Not Be Null/Empty\n✔ Check The Rules For Columnar Cipher\n🤝 Please Enter Valid Key...!!!");
    }
    else if(d=="play_fair_key"){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for Play Fair Cipher Can Not Be Null/Empty\n✔ Check The Rules For Play Fair Cipher\n🤝 Please Enter Valid Key...!!!");
    }
    else if(d=="vigenere_key"){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for Vigenere Cipher Can Not Be Null/Empty\n✔ Check The Rules For Vigenere Cipher\n🤝 Please Enter Valid Key...!!!");
    }
}

function alertotpsucc(d){
    let text = document.getElementById(d).value;
    let in1 = document.getElementById("input-text").value;
    let in2 = document.getElementById("encrypted-text2").value;
    if(text.length!=0){
        if(in1.length!=text.length && t==2){
            alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for OTP Cipher Should Be Same As Length Of Input Text\n✔ Check The Rules For OTP Cipher\n🤝 Please Enter Valid Key...!!!");
        }
        if(in2.length!=text.length && t==1){
            alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for OTP Cipher Should Be Same As Length Of Input Text\n✔ Check The Rules For OTP Cipher\n🤝 Please Enter Valid Key...!!!");
        }
        else{
            alertify.message('Input Data Submitted Successfully...!!! 😎✌🎉'); 
        }
    }
    else if(d=="otp_key"){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for OTP Cipher Can Not Be Null/Empty\n✔ Check The Rules For OTP Cipher\n🤝 Please Enter Valid Key...!!!");
    }
}

function check_negative(n){
    delay(function(){
    if(n<=1){
        alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Key for Rail Fence Cipher Can Not Be Null or Negative\n✔ Check The Rules For Rail Fence Cipher\n🤝 Please Enter Valid Key...!!!");
    }
    }, 700 );
}

function anyrand(length) {
    if(length<0){
        // alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Only Positive Values Allowed For Length of Key. ✨\n✔ Enter Values Accordingly Please...!!!");
        location.reload();
    }
    else{
        var result           = '';
        var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        var charactersLength = characters.length;
        for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * 
        charactersLength));
        }
        return result;
    }
}

function hasDuplicates(array) {
    return (new Set(array)).size !== array.length;
}

function check_dup(str1){
    const split_string = str1.split('');
    let x = hasDuplicates(split_string);
    if(x){
        delay(function(){
            alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n✖ Invalid Input Value...!!! 🤐🤐🤐\n🤝Try Again With Valid Set Of Inputs 🤗🤗🤗\n✨ Key Should Not Contain Duplicated Characters. ✨\n✔ Enter Values Accordingly Please...!!!");
        }, 700 );
    }
}

// function click_hidden(hidden_id){
//     document.getElementById(hidden_id).click();
// }


function js_alert(s){
    alert("\n                             😎😎😎 Cyberhood Guard 😎😎😎 \n\n"+s);
    location.reload();
}

var t=2;
function checkbox_toggle(){
    var remember = document.getElementById("toggle");
    if (remember.checked) {
        document.getElementById("display-block1").style.display = "none";
        document.getElementById("display-block2").style.display = "flex";
        t=1;
    } else {
        document.getElementById("display-block1").style.display = "flex";
        document.getElementById("display-block2").style.display = "none";
        t=2;
  }
}

function call_fun(){
    return t;
}

function otprand(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * 
 charactersLength));
   }
   return result;
}

function isCharacterALetter(char) {
    return (/[a-zA-Z]/).test(char)
}

function decide_otp(){
    var result           = '';
    var useit           = '';
    let l=0;
    let in1 = document.getElementById("input-text").value;
    let in2 = document.getElementById("encrypted-text2").value;
    if(t==2){
        l=in1.length;
        useit=in1;
    }
    else{
        l=in2.length;
        useit=in2;
    }
    for (var x = 0; x < useit.length; x++)
    {
        var c = useit.charAt(x);
        if(isCharacterALetter(c)){
            result=result+otprand(1);
        }
        else{
            result=result+c;
        }
    }
    return result;
}









// var delay = alertify.get('notifier','delay');
// alertify.set('notifier','delay', 10);
// alertify.success('Current delay : ' + alertify.get('notifier','delay') + ' seconds');
// alertify.set('notifier','delay', delay);