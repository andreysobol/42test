$(function(){

    dat = function(){
        $('#id_birth').datepicker({ dateFormat: 'yy-mm-dd' });
    };
    dat()

    $('input[type="submit"]').css('display','none');
    mod = function(){
        $('input').change(function(){
            $('.mess').html('');
            $('input[type="submit"]').css('display','block');
        });
    }
    mod();

    $('input[type="submit"]').click(function(){
        $('form').ajaxSubmit(
            {
                url:'/edit/',
                type: 'post',
                success: function(response){
                    $('input').removeAttr('readonly');
                    $('textarea').removeAttr('readonly');
                    if(response=="Okay"){
                        $('.mess').html('Bio update. <a href="/">View.</a>');
                        $('.error').css('display','none');
                    }
                    else{
                        $('.mod').html(response);
                        $('.mess').html('');
                        mod();
                        dat();
                    }
                },
                beforeSubmit: function(){
                    $('input[type="submit"]').css('display','none');
                    $('input').attr('readonly','readonly');
                    $('textarea').attr('readonly','readonly');
                    $('.mess').html('<img src="/static/ajax-loader.gif" style="width:32px;"/>');
                }
            }
        );
        return false;
    });
});
