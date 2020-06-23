
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
    if(pk == '1'){
        setBlock(document.getElementsByClassName('zapros_list'))
        setNone(document.getElementsByClassName('finished'))
    }
    else{
        setBlock(document.getElementsByClassName('finished'))
        setNone(document.getElementsByClassName('zapros_list'))
    }
}
