$(document).ready(function(){
    $(document).on('submit', '.ajax-form-reply', function(event){
    event.preventDefault();
    console.log("TESTING")
    var $formData = $(this).serialize()
    var $thisURL = $(this).attr('data-url') || window.location.href // or set your own url
    var that = this;
    $(this)[0].reset();
    $.ajax({
        method: "POST",
        url: $thisURL,
        data: $formData,
        success: handleFormSuccess,
        error: handleFormError,
    })
})

function handleFormSuccess(data, textStatus, jqXHR){
console.log(data.comment_id)
console.log('#reply-'+data.comment_id)
$('#reply-'+data.comment_id +" .replies").append('<li>'+data.reply_text+'</li>');
}

function handleFormError(jqXHR, textStatus, errorThrown){
console.log(jqXHR)
console.log(textStatus)
console.log(errorThrown)
}
})