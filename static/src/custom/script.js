// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrfToken = getCookie('csrftoken');

$(document).ready(()=>{
    $('#mail-tec').submit((e)=>{
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "message/",
            data: {
                sender: $('#full_name').val(),
                email: $('#email').val(),
                subject: $('#subject').val(),
                body: $('#message').val(),

                csrfmiddlewaretoken: csrfToken,
                messageTec: '1'
            },
        })
        .done((resp)=>{
            $('form').trigger('reset')

            const msgInitial = $('#msg-initial');
            msgInitial.css('display', 'none')

            const prompt = $('#msg-prmpt');
            prompt.css('display', 'flex')

            const closePrompt = $('#x-prompt');
            closePrompt.on('click', ()=>{
                const prompt = $('#msg-prmpt');
                prompt.css('display', 'none')

                const msgInitial = $('#msg-initial');
                msgInitial.css('display', 'block')
            })

        })

        .fail((data)=>{
            alert(data.error)
        })
    })
})


// Initializing Configuration
 
$(document).ready(()=>{
    $('.sidenav').sidenav();
    $('.slider').slider();
});