
$(document).ready(function() {
    console.log("ready!")
     $('.image-section').hide();
     $('#spinner').hide();
     $('#result').hide();

     function readURL(input) {
         if(input.files && input.files[0]) {
             var reader = new FileReader();
             reader.onload = function(e) {
                 $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                 $('#imagePreview').hide();
                 $('#imagePreview').fadeIn(650);
             }
             reader.readAsDataURL(input.files[0]);
         }
     }

     $('#image-upload').change(function() {
        document.getElementById("shiftUp").style.transition = "all 0.3s"
        document.getElementById("shiftUp").style.paddingTop = 0;
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
     });

     $('#btn-predict').click(function() {
         var form_data = new FormData($('#uploadForm')[0]);
         $(this).hide();
         $('#spinner').show();

         $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function(data) {
                $('#spinner').hide();
                $('#result').fadeIn(600);
                $('#result').text("Looks like it's <b>" + data + "</b> here.");
                console.log('Success!');
            }
         });
     });
});