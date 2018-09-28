let deleteFlag = false;
function deleteAffairRequest(affairId){
    $.ajax({
        url:'/index/todo-updateOrDelete-'+affairId.toString()+'/',
        type:'delete',
        async:false,
        success:function(data){
            data = JSON.parse(data)
            deleteFlag = data['status']
            console.log(deleteFlag)
        },
        error:function () {
            alert('error');
            deleteFlag = false
        }
    });
    return deleteFlag
}