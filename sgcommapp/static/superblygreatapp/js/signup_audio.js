function StopAllAudio(){
  $('#signup_username_audio').get(0).pause();
  $('#signup_username_audio').get(0).currentTime = 0;
  $('#signup_password_audio').get(0).pause();
  $('#signup_password_audio').get(0).currentTime = 0;
  $('#notice_audio').get(0).pause();
  $('#notice_audio').get(0).currentTime = 0;
  $('#narrator_audio').get(0).pause();
  $('#narrator_audio').get(0).currentTime = 0;
  $('#01').get(0).pause();
  $('#01').get(0).currentTime = 0;
  $('#02').get(0).pause();
  $('#02').get(0).currentTime = 0;
  $('#03').get(0).pause();
  $('#03').get(0).currentTime = 0;
  $('#04').get(0).pause();
  $('#04').get(0).currentTime = 0;
  $('#05').get(0).pause();
  $('#05').get(0).currentTime = 0;
  $('#06').get(0).pause();
  $('#06').get(0).currentTime = 0;
  $('#07').get(0).pause();
  $('#07').get(0).currentTime = 0;
  $('#08').get(0).pause();
  $('#08').get(0).currentTime = 0;
  $('#09').get(0).pause();
  $('#09').get(0).currentTime = 0;
  $('#10').get(0).pause();
  $('#10').get(0).currentTime = 0;
  $('#11').get(0).pause();
  $('#11').get(0).currentTime = 0;
  $('#12').get(0).pause();
  $('#12').get(0).currentTime = 0;
  $('#13').get(0).pause();
  $('#13').get(0).currentTime = 0;
  $('#14').get(0).pause();
  $('#14').get(0).currentTime = 0;
  $('#15').get(0).pause();
  $('#15').get(0).currentTime = 0;
  $('#16').get(0).pause();
  $('#16').get(0).currentTime = 0;
  $('#17').get(0).pause();
  $('#17').get(0).currentTime = 0;
  $('#18').get(0).pause();
  $('#18').get(0).currentTime = 0;
  $('#19').get(0).pause();
  $('#19').get(0).currentTime = 0;
  $('#20').get(0).pause();
  $('#20').get(0).currentTime = 0;
  $('#captcha_answer_audio').get(0).pause();
  $('#captcha_answer_audio').get(0).currentTime = 0;
  $('#signup_audio').get(0).pause();
  $('#signup_audio').get(0).currentTime = 0;
};

// Audio for the blind
// Sign-up
function SignupAudio(){
  $('#username-signup').focusin(function(){
    StopAllAudio();
    $('#signup_username_audio').get(0).play();
  });
  $('#password-signup').focusin(function(){
    StopAllAudio();
    $('#signup_password_audio').get(0).play();
  });
  $('#notice').focusin(function(){
    StopAllAudio();
    $('#notice_audio').get(0).play();
  });
  $('#narrator').focusin(function(){
    StopAllAudio();
    $('#narrator_audio').get(0).play();
  });

  $('#captcha_question').focusin(function(){
    if ($('#captcha_question').val() == "Is potato a fruit?") {
      StopAllAudio();
      $('#01').get(0).play();
    };
    if ($('#captcha_question').val() == "H2O is?") {
      StopAllAudio();
      $('#02').get(0).play();
    };
    if ($('#captcha_question').val() == "Who sang the song Bad Blood?") {
      StopAllAudio();
      $('#03').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the name of the evil robot in the movie Avengers?") {
      StopAllAudio();
      $('#04').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the abbreviation for central processing unit?") {
      StopAllAudio();
      $('#05').get(0).play();
    };
    if ($('#captcha_question').val() == "Who is the amazing web crawler?") {
      StopAllAudio();
      $('#06').get(0).play();
    };
    if ($('#captcha_question').val() == "Who invented Linux?") {
      StopAllAudio();
      $('#07').get(0).play();
    };
    if ($('#captcha_question').val() == "Who co-founded Apple Inc.?") {
      StopAllAudio();
      $('#08').get(0).play();
    };
    if ($('#captcha_question').val() == "Who founded Microsoft?") {
      StopAllAudio();
      $('#09').get(0).play();
    };
    if ($('#captcha_question').val() == "What band who sang the song: 'All You Need Is Love'") {
      StopAllAudio();
      $('#10').get(0).play();
    };
    if ($('#captcha_question').val() == "Who is the first comic book superhero?") {
      StopAllAudio();
      $('#11').get(0).play();
    };
    if ($('#captcha_question').val() == "Who is the father of Luke Skywalker?") {
      StopAllAudio();
      $('#12').get(0).play();
    };
    if ($('#captcha_question').val() == "What year was star wars first released?") {
      StopAllAudio();
      $('#13').get(0).play();
    };
    if ($('#captcha_question').val() == "Larry Page and Sergey Brin founded what company?") {
      StopAllAudio();
      $('#14').get(0).play();
    };
    if ($('#captcha_question').val() == "Amazon is founded by whom?") {
      StopAllAudio();
      $('#15').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the oldest living dinosaur") {
      StopAllAudio();
      $('#16').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the last book in the Christian bible?") {
      StopAllAudio();
      $('#17').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the fastest car in the world?") {
      StopAllAudio();
      $('#18').get(0).play();
    };
    if ($('#captcha_question').val() == "What is the cleanest renewable energy?") {
      StopAllAudio();
      $('#19').get(0).play();
    };
    if ($('#captcha_question').val() == "Who is the first man created?") {
      StopAllAudio();
      $('#20').get(0).play();
    };
  });

  $('#captcha_answer').focusin(function(){
    StopAllAudio();
    $('#captcha_answer_audio').get(0).play();
  });

  $('#signup-button').focusin(function(){
    StopAllAudio();
    $('#signup_audio').get(0).play();
  });
};
