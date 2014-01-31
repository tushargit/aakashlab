/* Getting the current url*/
 var url = window.location.href;

/* cropping the unwanted address from the url */

var urls = url.split('/');

var str = "/";

for(i=3;i<urls.length-1;i++)
{
	str += urls[i] + "/";
}

var len = $('.navbar-nav li').length;


for(i=0;i<len;i++)
{
var href = $(".navbar-nav li:eq("+(i)+") a").attr('href'); 

	if(href == str)
	{
		$(".navbar-nav li:eq("+(i)+")").addClass("active");
	}
	else{
		$(".navbar-nav li:eq("+(i)+")").removeClass('active');
	}

}

/* Left side bar current active tab code
*/


$('.sidebar li').click(function(){

 if ($(".sidebar li").hasClass('active') == true) {
    $('.sidebar li').removeClass('active');
 }
 $(this).addClass('active');
});


