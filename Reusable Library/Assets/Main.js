/*  Main.js
    Saturday, 15 August, 2015
    Alexander Rhett Crammer
    Reusable Library  */

document.forms[0].addEventListener("submit", function (submissionEvent) {
  submissionEvent.preventDefault(); // Prevent the form from submitting until evaluation has completed
  var deviceForm = submissionEvent.target;
  var deviceFormFields = [
    document.getElementById("company").value,
    document.getElementById("model").value,
    document.getElementById("portable").value,
    document.getElementById("condition").value,
    document.getElementById("kind").value,
    document.getElementById("operating_system").value,
    document.getElementById("age").value
  ];
  console.log(deviceFormFields);
});