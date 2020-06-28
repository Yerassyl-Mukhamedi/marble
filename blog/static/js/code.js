
// (function() {
//     try {
//         let url = location.href.match('#(.*)')[1];
//         localStorage.setItem("check", url);
//         document.getElementById(url).style.display = "block";
//     } catch (e) {
        
//     }
//     // if(location.href.match('specific')){
//     //     let check = localStorage.getItem("check");
//     //     console.log(check);
//     //     document.getElementById(check).style.display = "block";
//     // }
// })();


// $( document ).ready(function() {
//         try {
//             let url = location.href.match('#(.*)')[1];
//             localStorage.setItem("check", url);
//             document.getElementById(url).style.display = "block";
//         } catch (e) {
//             $('.post').css('display',)
//         }
// });

function zapros_choice(pk){
    setNone(document.getElementsByClassName('list'))
    document.getElementById('list'+pk).style.display = 'block';
}


function toner_choice(pk){
    if(pk == 4){
        setBlock(document.getElementsByClassName('toner'))
    }
    else{
        setNone(document.getElementsByClassName('toner'))
        document.getElementById('toner'+pk).style.display = 'block';
    }
}

function toner_date(){
    let month = document.getElementById('month').value;
    setNone(document.getElementsByClassName('item'));
    setBlock(document.getElementsByClassName('month'+month));
}


let family, company;

function family_choice(pk){
    family = pk;
    setNone(document.getElementsByClassName('item'));
    setBlock(document.getElementsByClassName(family));
}

function company_choice(pk){
    company = pk;
    document.getElementById('dropdownMenuButton').innerHTML = company;
}

function apply(){
    // alert(family + ' ' + company);
    setNone(document.getElementsByClassName('item'));
    setBlock(document.getElementsByClassName(family + ' ' + company));
}