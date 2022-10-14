window.jsPDF = window.jspdf.jsPDF;
document.querySelector(".theme-btn").addEventListener("click", function () {
  document
    .querySelectorAll("body")
    .forEach((l) => l.classList.toggle("page-black"));
  document
    .querySelectorAll("textarea")
    .forEach((l) => l.classList.toggle("field-black"));
  document
    .querySelectorAll("input")
    .forEach((l) => l.classList.toggle("field-black"));
  document
    .querySelectorAll("h2")
    .forEach((l) => l.classList.toggle("page-black"));
});
tinymce.init({
  selector: "textarea#neuroplay-text",
  toolbar:
    "undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
});
const login = (code) => {
  $.ajax({
    url: "/login",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ code: code }),
    success: function (result) {
      if (result.success) {
        $(".btn-text").prop("disabled", false);
      } else {
        console.log("NE SUETA NE KRUTO");
      }
    },
  });
};

const saveScenario = (scenario) => {
  $.ajax({
    url: "/scenario",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ scenario: scenario }),
    success: function (result) {
      console.log("huy", result);
    },
  });
};

const restoreScenario = () => {
  $.ajax({
    url: "/scenario",
    type: "GET",
    dataType: "json",
    contentType: "application/json",
    success: function (result) {
      tinymce.activeEditor.setContent(result.scenario);
    },
  });
};

const runContinue = (replic) => {
  $.ajax({
    url: "/continue",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ replic: replic }),
    success: function (result) {
      $("#continue-text").val(result.replic);
    },
  });
};

const runResponse = (replic) => {
  $('#run-btn-response').text('Загрузка...')
  $.ajax({
    url: "/response",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ replic: replic }),
    success: function (result) {
      $("#response-text").val(result.replic);
      $('#run-btn-response').text('Запустить')
    },
    error: function(result) {
      console.log(result)
    }
  });
};

const getFile = html => {
  const domain = "neuroplay.itatmisis.ru";
  $.ajax({
    url: "/getfile",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ html: html }),
    success: function (result) {
      window.open(`http://${domain}/getfile`, '_blank')
    },
    // error: function(result) {
    //   console.log(result)
    // }
  });
}

$(function () {
  $("#code-btn").click(function (e) {
    const code = $("#code-input").val();
    login(code);
  });

  $("#save-btn").click(function (e) {
    tinymce.triggerSave();
    const scenario = tinymce.activeEditor.getContent();
    saveScenario(scenario);
  });
  $("#restore-btn").click(function (e) {
    tinymce.triggerSave();
    restoreScenario();
  });
  $("#download-btn").click(function (e) {
    tinymce.triggerSave();
    let html = tinymce.activeEditor.getContent();
    getFile(html);
  });

  $("#clear-btn-continue").click(function (e) {
    $("#continue-text-input").val("");
    $("#continue-text").val("");
  });
  $("#clear-btn-response").click(function (e) {
    $("#response-text-input").val("");
    $("#response-text").val("");
  });

  $("#run-btn-continue").click(function (e) {
    const replic = $("#continue-text-input").val();
    runContinue(replic);
  });
  $("#run-btn-response").click(function (e) {
    const replic = $("#response-text-input").val();
    runResponse(replic);
  });
});
