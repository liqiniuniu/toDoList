let dataGet ;

function FormatDate(ms) {
    let date = new Date(ms);
    let seperator = "-";
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    return year + seperator + month + seperator + strDate;
}

function oneWeekRequest(){
    let date = new Date();
    let today = FormatDate(date.getTime());
    let aWeekLater = FormatDate(date.getTime()+7*86400000);
    $.ajax({
        url:'/index/todo-'+today+'&'+aWeekLater+'/',
        type:'get',
        async:false,
        success:function(data){
            dataGet = data
        },
        error:function () {
            alert('error')
        }
    })
    return dataGet
}

function allRequest(){
    $.ajax({
        url:'/index/todo/',
        type:'get',
        async:false,
        success:function(data){
            dataGet = data
        },
        error:function () {
            alert('error')
        }
    })
    return dataGet;
}
function todayRequest(){
    let date = new Date();
    let today = FormatDate(date.getTime());
    $.ajax({
        url:'/index/todo-'+today+'/',
        type:'get',
        async:false,
        success:function(data){
            dataGet = data
        },
        error:function () {
            alert('error')
        }
    })
    return dataGet
}

function requestAsPriority(priority){
    let date = new Date();
    let today = FormatDate(date.getTime());
    $.ajax({
        url:'/index/todo-'+priority+'/',
        type:'get',
        async:false,
        success:function(data){
            dataGet = data
        },
        error:function () {
            alert('error')
        }
    })
    return dataGet
}

