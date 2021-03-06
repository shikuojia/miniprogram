;
var user_reset={
    init:function(){
        this.eventBind();

    },
    eventBind:function(){
        $('#save').click(function(){
            var btn_target = $(this);
            if(btn_target.hasClass('disabled')){
                common_ops.alert('正在处理，请不要重复提交！')
                return;
            }

            var old_password = $('#old_password').val();
            var new_password = $('#new_password').val();
           
            if(!old_password || old_password.length<6){
                common_ops.alert('请输入原始密码');
                return;
            }
            if(new_password.length<6){
                common_ops.alert('请输入不少于6位的密码！建议包含大写字母和数字组合');
                return;
            }

            btn_target.addClass('disabled');

            var data={
                old_password :old_password,
                new_password :new_password
            }
            

            $.ajax({
                url:common_ops.buildUrl('/user/reset-pwd'),
                type:'POST',
                data:data,
                dataType:'json',
                success:function(res){
                    btn_target.removeClass('disabled');
                    var callback = null;
                    if(res.code==200){
                        callback= function(){
                            window.location.href=window.location.href;
                        }
                    }
                    common_ops.alert(res.msg,callback);
                }
            })


        });

    }
};

$(document).ready(function(){
    user_reset.init()
});