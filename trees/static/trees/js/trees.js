
// On document ready hides all tiles for sorting and filtering
// On click hides and shows appropriate tiles for sorting and filtering

$( document ).ready(function(){
    $(".feature-tile").hide();
    $(".sorting-tile-wide").hide();
    $(".sorting-tile-mobile").hide();

    $("#filter-tile").click(function(){
        $(".feature-tile").show();
        $(".sorting-tile-wide").hide();
        $(".sorting-tile-mobile").hide();
        $(this).removeClass("text-white").addClass("text-success");
        $("#sorting-tile-wide").removeClass("text-success").addClass("text-white"); 
        $("#sorting-tile-mobile").removeClass("text-success").addClass("text-white");   
    })

    $("#sorting-tile-wide").click(function(){
        $(".sorting-tile-wide").show();
        $(".feature-tile").hide();
        $(this).removeClass("text-white").addClass("text-success");
        $("#filter-tile").removeClass("text-success").addClass("text-white");  
    })
    $("#sorting-tile-mobile").click(function(){
        $(".sorting-tile-mobile").show();
        $(".feature-tile").hide();
        $(this).removeClass("text-white").addClass("text-success"); 
        $("#filter-tile").removeClass("text-success").addClass("text-white"); 
    })

})
