jQuery(document).ready(function($)
{
    var find_closest = function(pos,list) {
        var closest=99999;
        var index=0;
        var count=0;
        list.forEach(function(lpos) {
            if (Math.abs(lpos-pos)<closest) {
                closest=lpos-pos;
                index=count;
            }
            count++;
        });

        if (index==list.length-1) index--;
        return index;
    };

    var image_positions=[0];
    var current_pos=0;
    var last_x=0;
    var auto_scroll=true;

    $(".slider-items").children().each(function(t,v) {
        current_pos+=v.width;
        image_positions.push(-current_pos);
    });

    var up = function(event) {
        auto_scroll=false;
        last_x=event.clientX;
    };

    $('.slider-items').mousedown(up);
    $('.slider-items').mouseout(up);

    $('.slider-items').mouseup(function(event) {
        var cur = parseInt($(this).css("left"), 10);
        var pos = cur+(event.clientX-last_x);

        $('.slider-items').animate({
            left: ""+image_positions[find_closest(pos,image_positions)]+"px"
        });
    });

    $('.slider-items').bind('drag',function(event){
        var cur = parseInt($(this).css("left"), 10);
        var pos = cur+(event.clientX-last_x);
        $(this).css({
            left: pos
        });
        last_x = event.clientX;
    });

    var current_image=0;

    $.timer(function () {
        if (auto_scroll) {
            current_image++;
            if (current_image>image_positions.length-2) current_image=0;

            console.log(image_positions[current_image]);

            $('.slider-items').animate({
                left: ""+image_positions[current_image]+"px", top: "0px"
            });
        }
    },
    6000,
    true);

});
