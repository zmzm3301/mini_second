const bat_fig = document.querySelector('.bat-fig').innerText
    const bat_prog_bar = document.querySelector('.bat-prog')
    const bat_prog = document.querySelector('.bat_prog_col')

    bat_prog_bar.style.width = `${bat_fig}%`


    const color_box = document.querySelector('.color_box_input')
        if(bat_fig <= 20){
            bat_prog.style.backgroundColor = "#DF0101";
        }else if(bat_fig <= 40){
            bat_prog.style.backgroundColor = "#FF4000";
        }else if(bat_fig <= 60){
            bat_prog.style.backgroundColor = "#DF7401";
        }else if(bat_fig <= 80){
            bat_prog.style.backgroundColor = "#D7DF01";
        }else if(bat_fig <= 100){
            bat_prog.style.backgroundColor = "#04B404";
        }