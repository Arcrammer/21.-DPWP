/*  Main.js
    Saturday, 15 August, 2015
    Alexander Rhett Crammer
    Reusable Library  */

document.forms[0].addEventListener("submit", function (submissionEvent) {
  submissionEvent.preventDefault(); // Prevent the form from submitting until evaluation has completed
  var deviceForm = submissionEvent.target;
  var deviceFormFields = [
    document.getElementById("company"),
    document.getElementById("model"),
    document.getElementById("portable"),
    document.getElementById("condition"),
    document.getElementById("kind"),
    document.getElementById("operating_system"),
    document.getElementById("age")
  ];
  var missingFormData = false;
  deviceFormFields.forEach(function (formField, index) {
    // Each form field
    if (formField.value == "") {
      // The field has no value
      deviceFormFields[index].style.borderColor = "red";
      missingFormData = true;
    }
  });
  if (!missingFormData) {
    // The user has completely filled the form
    deviceForm.submit();
  }
});