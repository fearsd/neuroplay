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
    .querySelectorAll("h4")
    .forEach((l) => l.classList.toggle("page-black"));
    $(".huy").attr('style', 'background-color: #262626;');


});

count=0;
$(function () {
  $('.theme-btn').on('click' ,function(event) {
    count++;
    if(count%2==1){
      //alert($.cookie('save'));
      $(".huy").attr('style', 'background-color: #262626; color: #b3b3ba;');

      a=tinymce.activeEditor.getContent();
      tinymce.activeEditor.destroy();

      tinymce.init({
    selector: "textarea#neuroplay-text",
    content_css: 'dark',
    skin: 'tinymce-5-dark',
    plugins: 'advlist anchor autolink charmap code codesample directionality fullscreen help image insertdatetime link lists media nonbreaking pagebreak preview searchreplace table template toc visualblocks visualchars wordcount',
    toolbar:"undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | addcomment showcomments | spellcheckdialog a11ycheck | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | numlist bullist outdent indent | removeformat fullscreen",
      
    templates: [
      {title: 'Some title', description: 'Some description', content: 'Some content'},
       ],
   });

      tinymce.activeEditor.setContent(a);
  }
    else{
      $(".huy").removeAttr('style', 'background-color: #262626; color: #b3b3ba;');   


      a=tinymce.activeEditor.getContent();
      tinymce.activeEditor.destroy();

      tinymce.init({
    selector: "textarea#neuroplay-text",
    content_css: 'default',
    plugins: 'advlist anchor autolink charmap code codesample directionality fullscreen help image insertdatetime link lists media nonbreaking pagebreak preview searchreplace table template toc visualblocks visualchars wordcount',
    toolbar:"undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | addcomment showcomments | spellcheckdialog a11ycheck | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | numlist bullist outdent indent | removeformat fullscreen",
      
    templates: [
      {title: 'Some title', description: 'Some description', content: 'Some content'},
       ],
   });

      tinymce.activeEditor.setContent(a); 
  }
  });
});


//alert($.cookie("save2"));
//$.cookie('save',"huy");
/*
tinymce.init({
  selector: "textarea#neuroplay-text",
  content_css: 'default',
  toolbar:
    "undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
});
*/
tinymce.init({
    selector: "textarea#neuroplay-text",
    content_css: 'default',
    plugins: 'advlist anchor autolink charmap code codesample directionality fullscreen help image insertdatetime link lists media nonbreaking pagebreak preview searchreplace table template toc visualblocks visualchars wordcount',
    toolbar:"undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | addcomment showcomments | spellcheckdialog a11ycheck | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | numlist bullist outdent indent | removeformat fullscreen",
      
    templates: [
      {title: 'Some title', description: 'Some description', content: 'Some content'},
       ],
   });
/*
if($.cookie("save")!="undefined" || $.cookie("save")!=""){
tinymce.activeEditor.setContent($.cookie("save2"));
}
*/


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
        $(".btn").attr('style', 'cursor: pointer;'); 
        $(".code").addClass('is-valid');
      } else {
        console.log("NE SUETA NE KRUTO");
        $('#code-input').val('');
        alert('Вы ввели неверный пароль! Спробуйте сызнова');

      }
    },
  });
};

const saveScenario = (scenario) => {
  $(".btn-suc").addClass('saved');
  //$("#save-btn").html('Hi there!');
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
  setTimeout(function () {
$(".btn-suc").removeClass('saved');
}, 1000); 
  
  
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
  var data = new FormData(form);
  var output = "";
  for (const entry of data) {
    output = entry[0] + "=" + entry[1] + "\r";
  };
  if (output.toString().includes('continue')){
  //alert(output);

$('#run-btn-continue').text('Загрузка...')
$('<i class="icon-btn pause-icon"></i>').prependTo('#run-btn-continue');
  $.ajax({
    url: "/continue",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ replic: replic }),
    success: function (result) {
      $("#continue-text").val(result.replic);
      $('#run-btn-continue').text('Запустить');

      $('<i class="icon-btn run-icon"></i>').prependTo('#run-btn-continue');
    },
    error: function(result) {
      console.log(result)
    }
  });
}else{

$('#run-btn-continue').text('Загрузка...')
$('<i class="icon-btn pause-icon"></i>').prependTo('#run-btn-continue');
  $.ajax({
    url: "/response",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ replic: replic }),
    success: function (result) {
      $("#continue-text").val(result.replic);
      $('#run-btn-continue').text('Запустить');
      $('<i class="icon-btn run-icon"></i>').prependTo('#run-btn-continue');
    },
    error: function(result) {
      console.log(result)
    }
  });

}
};

const runResponse = (replic) => {
  var data = new FormData(form);
  var output = "";
  for (const entry of data) {
    output = entry[0] + "=" + entry[1] + "\r";
  };
  if (output.toString().includes('response')){
  alert(output);


  $('#run-btn-continue').text('Загрузка...')
  $.ajax({
    url: "/response",
    type: "POST",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({ replic: replic }),
    success: function (result) {
      $("#response-text").val(result.replic);
      $('#run-btn-continue').text('Запустить')
    },
    error: function(result) {
      console.log(result)
    }
  });
}
};


var form = document.querySelector("form");
form.addEventListener("submit", function(event) {
  alert('2');
  var data = new FormData(form);
  var output = "";
  for (const entry of data) {
    output = entry[0] + "=" + entry[1] + "\r";
  };
  alert(data);
  Console.log(output);
}, false);



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

    function binaryAgent(str) {
      var binString = '';
      str.split(' ').map(function(bin) {
          binString += String.fromCharCode(parseInt(bin, 2));
        });
      return binString;
    }

    function Export2Word(element){
      var preHtml = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
      var postHtml = "</body></html>";
      var html = preHtml+tinymce.activeEditor.getContent()+postHtml;

      var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html);

      var downloadLink = document.createElement("a");

    document.body.appendChild(downloadLink);
    downloadLink.href = url;
        downloadLink.download = 'текст пьесы.doc';
        
        downloadLink.click();
    
    document.body.removeChild(downloadLink);
      
}
Export2Word(tinymce.activeEditor.getContent());
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


/*

function setCookie(name, value, options) {
      options = options || {};
      var expires = options.expires;

      if (typeof expires == "number" && expires) {
          var d = new Date();
          d.setTime(d.getTime() + expires * 1000);
          expires = options.expires = d;
      }
      if (expires && expires.toUTCString) {
          options.expires = expires.toUTCString();
      }

      value = encodeURIComponent(value);

      var updatedCookie = name + "=" + value;

      for (var propName in options) {
          updatedCookie += "; " + propName;
          var propValue = options[propName];
          if (propValue !== true) {
              updatedCookie += "=" + propValue;
          }
       }

      document.cookie = updatedCookie;
}
var password = document.getElementById('password');
var button = document.getElementsByClass('btn-check')[0];

button.addEventListener('click', setCookie('nick_name', password.value));
*/
/*

let timerId = setTimeout(function tick() {

  tinymce.triggerSave();
  $.cookie('save',tinymce.activeEditor.getContent());
  alert($.cookie('save'));


  timerId = setTimeout(tick, 2000);
}, 2000);
*/


function success() {
   if(document.getElementById("continue-text-input").value==="") { 
            document.getElementById('run-btn-continue').disabled = true; 
        } else { 
            document.getElementById('run-btn-continue').disabled = false;
        }
    }