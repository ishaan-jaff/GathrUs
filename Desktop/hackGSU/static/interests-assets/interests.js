document.addEventListener('DOMContentLoaded', () => {
    var colors = ['#00C7E6', '#3CD68F', '#3CD38F']
    var interests = []

    $(".interests").on("click",function(){
        if ($(this).hasClass('clicked')){
            let arrIndex = interests.indexOf($(this).children('h2')[1].innerHTML)
            interests.splice(arrIndex, 1);
            $(this).removeClass('clicked');
            $(this).css({"background-color": "",
            "color": ""});
        }else{
            $(this).addClass('clicked');
            let index = Math.floor(Math.random() * 3)
            $(this).css({"background-color": colors[index],
            "color": "white"});
            interests.push($(this).children('h2')[1].innerHTML)
            console.log(interests)
        } 
    });

    document.getElementById("nextClick").onclick = () => {
        $.ajax({
            type: 'POST',
            data: JSON.stringify({'interestList': interests}),
            contentType: 'application/json;charset=UTF-8',
            url : "/interests",
            success: function() {
                // window.href = "/";
                console.log("success")
                window.location.href = "/events";
            },
            error: function(err){
                console.log("Error: " + JSON.stringify(err));
            }
        })
    }
})