function expandToggle(parent_id){
                
    const row = document.getElementById('reply-'+parent_id)

    if (row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }           
}