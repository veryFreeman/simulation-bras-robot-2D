let init = ' mpld3.draw_figure("graph", {"width": 262.5, "height": 251.29999999999998, "axes": [{"bbox": [0.125, 0.10999999999999999, 0.775, 0.77], "xlim": [7.0, 0.0], "ylim": [0.0, 9.0], "xdomain": [7.0, 0.0], "ydomain": [0.0, 9.0], "xscale": "linear", "yscale": "linear", "axes": [{"position": "bottom", "nticks": 10, "tickvalues": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "tickformat_formatter": "", "tickformat": null, "scale": "linear", "fontsize": 10.0, "grid": {"gridOn": true, "color": "#B0B0B0", "dasharray": "none", "alpha": 1.0}, "visible": true}, {"position": "right", "nticks": 10, "tickvalues": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "tickformat_formatter": "", "tickformat": null, "scale": "linear", "fontsize": 10.0, "grid": {"gridOn": true, "color": "#B0B0B0", "dasharray": "none", "alpha": 1.0}, "visible": true}], "axesbg": "#FFFFFF", "axesbgalpha": null, "zoomable": true, "id": "el5224139657372437904", "lines": [], "paths": [], "markers": [], "texts": [{"text": "Axe Y0", "position": [0.5, -0.05347374030223215], "coordinates": "axes", "h_anchor": "middle", "v_baseline": "hanging", "rotation": -0.0, "fontsize": 10.0, "color": "#000000", "alpha": 1, "zorder": 3, "id": "el5224139657372439968"}, {"text": "Axe X0", "position": [-0.009557945041816007, 0.5], "coordinates": "axes", "h_anchor": "middle", "v_baseline": "auto", "rotation": -90.0, "fontsize": 10.0, "color": "#000000", "alpha": 1, "zorder": 3, "id": "el5224139657372450336"}], "collections": [], "images": [], "sharex": [], "sharey": []}], "data": {}, "id": "el5224139658073113936", "plugins": [{"type": "reset"}, {"type": "zoom", "button": true, "enabled": false}, {"type": "boxzoom", "button": true, "enabled": false}]})';
window.addEventListener('DOMContentLoaded', () => {
    console.clear();
    eval(init);
})


document.querySelector('#dessiner').addEventListener('click', async() => {
    document.querySelector('#graph').innerHTML = ''
    await eel.dessiner(
        parseFloat(document.getElementsByClassName('lien')[0].value),
        parseFloat(document.getElementsByClassName('lien')[1].value),
        parseFloat(document.getElementsByClassName('lien')[2].value),
        parseFloat(document.getElementsByClassName('teta')[0].value),
        parseFloat(document.getElementsByClassName('teta')[1].value),
        parseFloat( document.querySelector('#x_b').value),
        parseInt( document.querySelector('#y_b').value),
        parseFloat(document.getElementsByClassName('temps')[0].value),
        parseFloat(document.getElementsByClassName('pas')[0].value)
    )(data => {
        eval(data);
    })
})
document.querySelector('#demo').addEventListener('click', () => {
    document.getElementsByClassName('lien')[0].value = 3
        document.getElementsByClassName('lien')[1].value = 3
        document.getElementsByClassName('lien')[2].value = 3
        document.getElementsByClassName('teta')[0].value = 55
        document.getElementsByClassName('teta')[1].value = 75
        document.querySelector('#x_b').value = 0
        document.querySelector('#y_b').value = 1
        document.getElementsByClassName('pas')[0].value = 10
        document.getElementsByClassName('temps')[0].value = 5
})
document.querySelector('#simuler').addEventListener('click', async()=> {
    
    await eel.simuler(
        parseFloat(document.getElementsByClassName('lien')[0].value),
        parseFloat(document.getElementsByClassName('lien')[1].value),
        parseFloat(document.getElementsByClassName('lien')[2].value),
        parseFloat(document.getElementsByClassName('teta')[0].value),
        parseFloat(document.getElementsByClassName('teta')[1].value),
        parseFloat(document.querySelector('#x_b').value),
        parseFloat(document.querySelector('#y_b').value),
        parseFloat(document.getElementsByClassName('temps')[0].value),
        parseFloat(document.getElementsByClassName('pas')[0].value)
    )(data => {
        let i = 0;
        let j = 0;
        inter = setInterval(() => {
            document.querySelector('#graph').innerHTML = ''
            eval(data[0][i])
            i += 1;
            if(i == data[0].length) {
                clearInterval(inter);
                document.querySelector('#graph').innerHTML = ''
                eval(data[0][data[0].length - 1])
            }
        }, 1000)
        console.clear();
        console.log('-----POSIITON INSTANTANEES------')
        console.log('les Xp :')
        console.log(data[1])
        console.log('les Yp : ')
        console.log(data[2])
    
        let debug = `-----POSITIONS INSTANTANEES------\n
            les Xp : ${data[1]}
            les Yp : ${data[2]}
        `
        document.querySelector('.debugg').innerText = debug;
    })
})
document.querySelector('#new').addEventListener('click',() => {
    let inputTab = document.querySelectorAll('input');
    inputTab.forEach(element => element.value = '');
    document.querySelector('#graph').innerHTML = '';
    eval(init);
})