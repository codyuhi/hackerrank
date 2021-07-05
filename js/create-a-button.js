/*
--- The HTML section of the page looks like below:

--- The CSS section of the page looks like below:


*/

let button = document.createElement('button');
button.id = 'btn';
button.innerHTML = 0;
button.onclick = () => {
    let val = parseInt(button.innerText);
    val++;
    button.innerHTML = val;
}
button.style.width = '96px';
button.style.height = '48px';
button.style.fontSize = '24px';
document.body.append(button);