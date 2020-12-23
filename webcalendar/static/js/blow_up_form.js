function showModalWin() {
    var darkLayer = document.createElement('div');
    darkLayer.id = 'shadow';
    document.body.appendChild(darkLayer);

    var modalWin = document.getElementById('popupWin');
    modalWin.style.display = 'block';

    darkLayer.onclick = function () {
        darkLayer.parentNode.removeChild(darkLayer); 
        modalWin.style.display = 'none';
        return false;
    };
}

function check_time_start() {
    var case_nums = Number(document.getElementById("case_nums").textContent);
    cases_times = [];
    cases_labels = [];
    full_day = []
    full_day.length = 24
    for (var i = 0; i <= 24; i++) full_day[i] = "Free";
    for (var i = 1; i <= case_nums; i++)
    {
        cases_times[i] = document.getElementById(i+"_duration").textContent;
        cases_labels[i] = document.getElementById(i+"_name").textContent;
        
        start_time =  document.getElementById(i+"_start").textContent.toString().slice(-2);
        end_time =  Number(document.getElementById(i+"_end").textContent.toString().slice(-2));
        for (var j = start_time; j <= end_time; j++){
            full_day[j] = document.getElementById(i+"_name").textContent.toString().slice(7);
        }
    }

    
    var start_time_user =  Number(document.getElementById("start_time").value.toString().slice(0, -3));
    var end_time_user = Number(document.getElementById("end_time").value.toString().slice(0, -3));
    flag = false;

    if ((full_day[start_time_user] != "Free") || (full_day[start_time_user] == "Free" && full_day[start_time_user+1] != "Free")){
        flag = true;
    }
    if (full_day[start_time_user] != "Free" && full_day[start_time_user+1] == "Free"){
        flag = false;
    }
    if (end_time_user - end_time_user < 0 ){
        flag = true;
        document.getElementById("alert").textContent = "Time cannot go back";
    }
    for (var j = start_time_user+1; j < end_time_user; j++){
        if (full_day[j] != "Free"){
            flag = true;
            document.getElementById("alert").textContent = "Find another gap inside the gap";
        }
    }
    
    if (flag){
        document.getElementById("send_btn").disabled = true;
        document.getElementById("alert").style.display = "flex";
    }
    else{
        document.getElementById("send_btn").disabled = false;
        document.getElementById("alert").style.display = "none";
    }
    
}

function check_time_end() {
    var case_nums = Number(document.getElementById("case_nums").textContent);
    cases_times = [];
    cases_labels = [];
    full_day = []
    full_day.length = 24
    for (var i = 0; i <= 24; i++) full_day[i] = "Free";
    for (var i = 1; i <= case_nums; i++)
    {
        cases_times[i] = document.getElementById(i+"_duration").textContent;
        cases_labels[i] = document.getElementById(i+"_name").textContent;
        
        start_time =  document.getElementById(i+"_start").textContent.toString().slice(-2);
        end_time =  Number(document.getElementById(i+"_end").textContent.toString().slice(-2));
        for (var j = start_time; j <= end_time; j++){
            full_day[j] = document.getElementById(i+"_name").textContent.toString().slice(7);
        }
    }

    var start_time_user =  Number(document.getElementById("start_time").value.toString().slice(0, -3));
    var end_time_user = Number(document.getElementById("end_time").value.toString().slice(0, -3));
    flag = false;

    if (full_day[end_time_user] != "Free" && full_day[end_time_user+1] == "Free"){
        flag = true;
    }

    if (full_day[end_time_user] != "Free" && end_time_user-end_time_user != 1 ){
        flag = true;
    }

    if (end_time_user-end_time_user < 0 ){
        flag = true;
        document.getElementById("alert").textContent = "Time cannot go back";
    }

    for (var j = start_time_user+1; j < end_time_user; j++){
        if (full_day[j] != "Free"){
            flag = true;
            document.getElementById("alert").textContent = "Find another gap inside the gap";
        }
    }


    if (flag){
        document.getElementById("send_btn").disabled = true;
        document.getElementById("alert").style.display = "flex";
    }
    else{
        document.getElementById("send_btn").disabled = false;
        document.getElementById("alert").style.display = "none";
    }
    
}