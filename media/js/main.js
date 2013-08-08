jQuery(document).ready(function($)
{
    $("#bbsrc").hover(function () {
        $(this).attr("src", "../media/images/bbsrc-l.png");
    }, function () {
        $(this).attr("src", "../media/images/bbsrc.png");
    });

    $("#exeter").hover(function () {
        $(this).attr("src", "../media/images/exeter-l.png");
    }, function () {
        $(this).attr("src", "../media/images/exeter.png");
    });

    $("#sensory").hover(function () {
        $(this).attr("src", "../media/images/sensory-ecology-l.png");
    }, function () {
        $(this).attr("src", "../media/images/sensory-ecology.png");
    });

    $("#cu").hover(function () {
        $(this).attr("src", "../media/images/cu-l.png");
    }, function () {
        $(this).attr("src", "../media/images/cu.png");
    });

});
