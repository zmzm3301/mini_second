let p_run_time = document.querySelector('.runtime_info')
let accor_runtime = document.querySelector('#accor_runtime')

let second = parseInt(parseInt(p_run_time.innerText) / 1000);

let minute = parseInt(second / 60);
second = second % 60;

let hour   = parseInt(minute / 60);
minute = minute % 60;

let result = '';
if (hour > 0){
   result += hour + '시간 ';
}
if (minute > 0){
   result += minute + '분 ';
}
if (second > 0){
   result += second + '초';
}
if (!second && !minute && !hour){
  result = 'NULL';
}
p_run_time.innerText = result;
if(accor_runtime != null){
accor_runtime.innerText = '구동시간 : ' + result;
}
