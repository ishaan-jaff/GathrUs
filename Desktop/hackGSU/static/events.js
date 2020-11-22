document.addEventListener('DOMContentLoaded', () => {
    var elems = document.querySelectorAll(".myButton");
    for (var i=elems.length; i--;) {
        elems[i].addEventListener('click', function(){
            let eventName = $(this).parent().children("p")[0].innerHTML;
            let eventDescription = $(this).parent().children("p")[1].innerHTML;
            let eventLocation = $(this).parent().children("p")[2].innerHTML;
            let eventAttendees = $(this).parent().children("p")[3].innerHTML;
            let eventType = $(this).parent().children("p")[4].innerHTML;

            $(this).addClass('clicked');
            $.ajax({
                type: 'POST',
                data: JSON.stringify({'eventName': eventName, 'eventDescription': eventDescription,
                'eventAttendees': eventAttendees, 'eventType': eventType, 'eventLocation': eventLocation}),
                contentType: 'application/json;charset=UTF-8',
                url : "/events",
                success: function() {
                    // window.href = "/";
                    $(this).parent().css({'border-color': 'green'});
                },
                error: function(err){
                    console.log("Error: " + JSON.stringify(err));
                }
            })

        }, false);
    }
    
})