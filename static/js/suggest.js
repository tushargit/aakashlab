$('#suggest_ac_id').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/ac/suggest_id/', {suggest_ac_id: query}, function(data){
	$('#cats').html(data);
    });
});

$('#suggest_ac_name').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/ac/suggest_name/', {suggest_ac_name: query}, function(data){
	$('#cats').html(data);
    });
});

$('#suggest_ac_city').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/ac/suggest_city/', {suggest_ac_city: query}, function(data){
	$('#cats').html(data);
    });
});

$('#suggest_ac_state').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/ac/suggest_state/', {suggest_ac_state: query}, function(data){
	$('#cats').html(data);
    });
});

$('#suggest_project_name').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/ac/suggest_project/', {suggest_project_name: query}, function(data){
	$('#cats').html(data);
    });
});
