function pad(n){return n<10 ? "0"+n : n}

let mon = {
    "Jan." : 1, "Feb." :  2, "Mar." :  3, "Apr." : 4,
    "May." : 5, "Jun." :  6, "Jul." :  7, "Aug." : 8,
    "Sep." : 9, "Oct." : 10, "Nov." : 11, "Dec." : 12
};
let title = document.querySelectorAll(".panel-faq-title");
for (let i = 0 ; i < title.length ; i++){
    let arr = title[i].innerText;
    arr = arr.trim();
    arr = arr.split(" ");

    let year = parseInt(arr[2].slice(0, -1));
    let month = pad(mon[arr[0]]);
    let day = pad(parseInt(arr[1].slice(0, -1)));
    let tt = arr[3].split(':');
    let ap = arr[4][0] == 'a' ? "오전" : "오후";
    let hour = pad(parseInt(tt[0]));
    let minute = pad(parseInt(tt[1]));
    let result = year + "년 " + month + "월 " + day + "일 " + ap + " "+ hour + "시 " + minute + "분";
    title[i].innerText = result;
}