$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-blood .modal-content").html("");
        $("#modal-blood").modal("show");
      },
      success: function (data) {
        $("#modal-blood .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#blood-table tbody").html(data.html_blood_list);
          $("#modal-blood").modal("hide");
        }
        else {
          $("#modal-blood .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-blood").click(loadForm);
  $("#modal-blood").on("submit", ".js-blood-create-form", saveForm);

  // Update book
  $("#blood-table").on("click", ".js-update-blood", loadForm);
  $("#modal-blood").on("submit", ".js-blood-update-form", saveForm);

  // Delete book
  $("#blood-table").on("click", ".js-delete-blood", loadForm);
  $("#modal-blood").on("submit", ".js-blood-delete-form", saveForm);

});