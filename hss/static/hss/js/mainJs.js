// This is the main JS file that handles the slide sequence, etc.
function showAlert() {
    alert("In showSlides function. Path = " + window.location.pathname);
}

function showImage() {
    $("#imageDiv").html("This is the image div");
    $("#imageDiv").append('<img src="static/hss/images/CoopsApp2.PNG">');
    // getSlide();
}

function showSlides() {
    // $("#imageDiv").html("This is the image div");
    // $("#imageDiv").append('<img src="static/hss/images/CoopsApp2.PNG">');
    getSlide();
}

// 12/15/2018
// ?? I can see this function getting executed, but the call never returns.
// Maybe an issue with this served JS calling back to same server for data?
// Not sure. For now, we go back to holiday_ss template and experiment there.
function getSlide() {
    $.ajax({
        url: 'http://127.0.0.1:8000/hello',
        type: 'GET', 
        data: null,
        dataType: 'json',
        success: function(data) {
            $("#captionDiv").html("<p>Success</p>");
            console.log("Success...");
            alert(data);
        },
        failure: function(data) { 
            $("#captionDiv").html("<p>Failure</p>");
            console.log("Failure...");
            alert('Got an error dude');
        }
    }); 
}