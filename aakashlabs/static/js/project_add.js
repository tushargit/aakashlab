// Update ElementIndex 
function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
								       replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}


// this is add form
function addForm(btn, prefix, classname) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    // You can only submit a maximum of 20  
    if (formCount < 20) {
	// Clone a form (without event handlers) from the first form
	var row = $("."+classname+":first").clone(false).get(0);
	// Insert it after the last form
	$(row).removeAttr('id').hide().insertAfter("."+classname+":last").slideDown(300);
	
	// Remove the bits we don't want in the new row/form
	// e.g. error messages
	$(".errorlist", row).remove();
	$(row).children().removeClass('error');
	
	// Relabel/rename all the relevant bits
	$(row).children().children().each(function() {
            updateElementIndex(this, prefix, formCount);
            if ( $(this).attr('type') == 'text' )
		$(this).val('');
	});

	// Update the total form count
	$('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1); 

    } // End if
    else {
	alert("Sorry, you can only enter a maximum of 20 items.");
    }
    return false;
}

// Delete a form
function deleteForm(btn, prefix, delclassname) {
    var forms = $('.'+delclassname); // Get all the forms
    if (forms.length > 1) {
	// Delete the item/form
        $(btn).parents('.'+delclassname).remove();
	
	// Update the total number of forms (1 less than before)
	$('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);

	var i = 0;
	// Go through the forms and set their indices, names and IDs
	for (formCount = forms.length; i < formCount; i++) {
            $(forms.get(i)).children().children().each(function() {
		updateElementIndex(this, prefix, i);
            });
	}
    }
    // End if
    else {
        alert("You have to enter at least one data!");
    }
    return false;
}
