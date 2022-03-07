$(document).ready(function(){
    $(document).on('click', '.ajax-form-like', function(event){
        event.preventDefault();
        var $formData = $(this).serialize()
        var $thisURL = $(this).attr('data-url') || window.location.href // or set your own url
        //console.log($formData)
        var that = this;
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: function(response){
                $(that).find('span').text(response.likes);
            },
            error: handleFormError,
        })
    })
    $(document).on('click', '.ajax-form-dislike', function(event){
        event.preventDefault();
        var $formData = $(this).serialize()
        var $thisURL = $(this).attr('data-url') || window.location.href // or set your own url
        //console.log($formData)
        var that = this;
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: function(response, textStatus, jqXHR){
                $(that).find('span').text(response.dislikes);
                console.log(textStatus,jqXHR)
            },
            error: handleFormError,
        })
    })

function handleFormSuccess(data, textStatus, jqXHR){
    console.log(data)
    //console.log(text)
    //$('.like-count').text(data.likes);
    //$('.dislike-count').text(data.dislikes);
    //console.log(textStatus)
    //console.log(jqXHR)
    //$myForm[0].reset(); // reset form data
}

function handleFormError(jqXHR, textStatus, errorThrown){
    console.log(jqXHR)
    console.log(textStatus)
    console.log(errorThrown)
}
})