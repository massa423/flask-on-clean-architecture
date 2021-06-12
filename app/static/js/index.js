const form = document.getElementById('myform');

form.addEventListener('submit', function (event) {
  if (!confirm('Are you OK?')) {
    event.preventDefault();
  }
});


$(function(){
  // initial state is disable
  $("#submit").prop("disabled", true);
    // click to checkbox
    $("input[type='checkbox']").on('change', function () {
        // number of checkbox to be checked
        if ($(".form-check-input:checked").length === 2) {
          // button enabled
          $("#submit").prop("disabled", false);
        } else {
          // button disabled
          $("#submit").prop("disabled", true);
        }
    });
});