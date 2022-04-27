// Table with all the features
$(document).ready(function () {
    var table = $('#tabledata').DataTable();
});

document.getElementById('profile-edit-btn').addEventListener('click', function(e){
    e.preventDefault();
    document.getElementById('tab-account-link').click(); 
})

