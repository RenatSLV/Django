document.getElementById('btn1').addEventListener('click', () => {
     inp1 = document.getElementById('inp1').value
     if (inp1 === ""){
         alert('Поле должно быть заполнено!!!')
     } else{
         window.location.href = Main_page_url
     }
})
