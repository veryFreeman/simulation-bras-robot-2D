// transition entre pages

function display_or_hide(class_name) {
    document.querySelectorAll('.box').forEach(item => {
        if(!item.classList.contains(class_name)) item.style.display = 'none';
        else {
            item.classList.add('apear-zoom-out');
            item.style.display = 'flex';
        }
    })
}

document.querySelector('#pwd_forgeted').addEventListener('click', () => display_or_hide('recover_mdp'));
document.querySelectorAll('.back').forEach(item => {
   item.addEventListener('click', async() => {
    // on ferme la camera a chaque appuie sur retour
    // await eel.release_cam()();
    document.querySelectorAll('.box').forEach(item => {
        if(!item.classList.contains('login')) item.style.display = 'none';
        else {
            item.classList.add('apear-zoom-in')
            item.style.display = 'flex';
        }
    })
   })
})


// connexion via email et mdp
document.querySelector('#login_submit').addEventListener('click', async (e) => {
    e.preventDefault();
    if(document.querySelector('#mail').value === '' || document.querySelector('#pwd').value === '') {
        document.querySelector('#errorBox').classList.add('on_error');
        document.querySelector('#errorBox').innerText = 'Les champs ne peuvent etres vides';
        setTimeout(() => {
            document.querySelector('#errorBox').classList.remove('on_error');
            document.querySelector('#errorBox').innerText = ''}
            , 6000);
    } else {
        let user = document.querySelector('#mail').value;
        let pwd = document.querySelector('#pwd').value;

        await eel.login(user, pwd)(data => {
            console.log(data);
            if (data) location.replace('http://localhost:8000/_index_.html')
        })
    }
})
