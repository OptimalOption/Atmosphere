function openPopup() {
    $('.popup_bg').fadeIn(600);
    $('html').addClass('no-scroll', 'no-dots');
}

function closePopup() {
    $('.popup_bg').fadeOut(600);
    $('html').removeClass('no-scroll');
}

function isValidSubject() {
    var subject = $('#subject');
    if (!subject.val().trim()) {
        subject.addClass('errorBorder');
        return false;
    } else {
        subject.removeClass('errorBorder');
        return true;
    }
}

function isValidMessage() {
    var message = $('#message');
    if (!message.val().trim()) {
        message.addClass('errorBorder');
        return false;
    } else {
        message.removeClass('errorBorder');
        return true;
    }
}

function isValidEmail() {
    var email = $('#email');
    var emailRegex = /^\w+([-+.'][^\s]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    if (!emailRegex.test(email.val())) {
        email.addClass('errorBorder');
        return false;
    } else {
        email.removeClass('errorBorder');
        return true;
    }
}

function isValid() {

    if (isValidSubject() && isValidEmail() && isValidMessage()) return true;
    else return false;
}

function submitOrder() {
    if (isValid()) {
        $('#form').submit();
        closePopup();
    }
}
