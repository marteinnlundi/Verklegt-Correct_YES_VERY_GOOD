$(document).ready(function() {
    $("#confirm-button").click(function(event) {
      event.preventDefault();
      var paymentMethod = $("input[name='payment-method']:checked").val();
      if (paymentMethod !== "pay-at-pickup") {
        if ($("#id_full_name").val() === "" ||
            $("#id_phone").val() === "" ||
            $("#id_email").val() === "" ||
            $("#id_address").val() === "") {
          alert("Please fill in all the required fields.");
          return;
        }
      }
      $("form").submit();
    });
  });
  