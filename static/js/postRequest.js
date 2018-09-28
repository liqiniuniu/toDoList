let postFlag ;

function addAffairRequest(user_id){
    $.ajax({
        url:'/index/todo/',
        type:'post',
        async:false,
        data:{
            'user':user_id,
            'affair':$('#affairInput').val(),
            'priority':$('#priorityInput').val(),
            'finished':'0',
            'time':$('#dateInput').val(),
        },
        dataType:'json',
        success:function(data){
            postFlag = data.id;
            console.log(postFlag);
        },
        error:function () {
            alert('error');
            postFlag = -1
        }
    });
    return postFlag
}

function finishAffairRequest(affairId){
    $.ajax({
        url:'/index/todo/',
        type:'post',
        async:false,
        data:{
            'type':'finish',
            'id':affairId.toString(),
            'finished':'1',
        },
        dataType:'json',
        success:function(data){
            postFlag = data.status;
            console.log(postFlag);
        },
        error:function () {
            alert('error');
            postFlag = false
        }
    });
    return postFlag
}

function updateAffairRequest(affairId, affair, time, priority) {
    if (!checkDateFormat(time)){
        alert("date error")
        return false
    }
    priority = (priority=='普通'?1:(priority=='紧急'?2:(priority=='重要'?3:0)))
    if(!priority){
        alert("priority error")
        return false
    }
    $.ajax({
        url:'/index/todo/',
        type:'post',
        async:false,
        data:{
            'type':'update',
            'id':affairId.toString(),
            'priority':priority,
            'affair':affair,
            'time':time,
        },
        dataType:'json',
        success:function(data){
            postFlag = data.status;
            console.log(postFlag);
        },
        error:function () {
            alert('error');
            postFlag = false
        }
    });
    return postFlag
}