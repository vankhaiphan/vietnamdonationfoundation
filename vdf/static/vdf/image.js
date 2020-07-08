//Image input file
$('.image-file-com input').change(function () {
    readURL(this);
});

$('.image-file-com .close').click(function () {
    $(this).closest('.image-file-com').removeClass('has-image').find('.embed-responsive-item').removeAttr('style').find('input').val(null);
});

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(input).closest('.embed-responsive-item').css('background', "url(" + e.target.result + ") #f3f3f3 no-repeat center center").closest('.image-file-com').addClass('has-image');
        };

        reader.readAsDataURL(input.files[0]);
    }
}

// Js cho thang hien thi nhieu it
$('#toggle-campaign-content').on('click', function () {
    var $content = $('#campaign-content'),
        $button = $(this);
    $content.toggleClass('full-view');
    if ($content.hasClass('full-view')) {
        $button.html($button.attr('data-expandText'));
    } else {
        $button.html($button.attr('data-collapseText'));
    }
});