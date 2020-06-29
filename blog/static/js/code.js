
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


let family = 'Ноутбук', company;

function family_choice(pk){
    family = pk;
    setNone(document.getElementsByClassName('item'));
    removeClass(document.getElementsByClassName('item'), 'oncount');
    setBlock(document.getElementsByClassName(family + ' ' + company));
    addClass(document.getElementsByClassName(family + ' ' + company), 'oncount');

    setTimeout(function() {
        let parent = document.getElementById('list');
        let count = parent.childElementCount;
        let total = 0;
        for(var i=0; i<count; i++){
            if((parent.children[i]).classList.contains('oncount')){
                total++;
            }
        }
        console.log(total);
    }, 1);
}

function company_choice(pk){
    company = pk;
    document.getElementById('dropdownMenuButton1').innerHTML = company;
}

function addClass(elements, klas){
    for(var i=0;i<elements.length;i++){
        elements[i].classList.add(klas);
    }
}
function removeClass(elements, klas){
    for(var i=0;i<elements.length;i++){
        elements[i].classList.remove(klas);
    }
}

function apply(){
    // alert(family + ' ' + company);
    setNone(document.getElementsByClassName('item'));
    if(company == "all"){
        company = '';
        // setBlock(document.getElementsByClassName(family + ' ' + company));
        // removeClass(document.getElementsByClassName('item'), 'oncount');
        setBlock(document.getElementsByClassName(family));
        
    }
    else{
        setBlock(document.getElementsByClassName(family + ' ' + company));
        removeClass(document.getElementsByClassName('item'), 'oncount');
        addClass(document.getElementsByClassName(family + ' ' + company), 'oncount')
    }

    setTimeout(function() {
        let parent = document.getElementById('list');
        let count = parent.childElementCount;
        let total = 0;
        for(var i=0; i<count; i++){
            if((parent.children[i]).classList.contains('oncount')){
                total++;
            }
        }
        console.log(total);
    }, 1);
}

