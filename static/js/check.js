
function checkEmailFormat(Email) {
    return /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(Email)
}

function checkDateFormat(Date){
    let mp=/\d{4}-\d{2}-\d{2}/;
    let matchArray = Date.match(mp);
    if (matchArray==null) return false;
    let iaMonthDays = [31,28,31,30,31,30,31,31,30,31,30,31];
    let iaDate = new Array(3);
    let year, month, day;
    iaDate = Date.split("-");
    year = parseFloat(iaDate[0])
    month = parseFloat(iaDate[1])
    day = parseFloat(iaDate[2])
    if (year < 2018 || year > 2100) return false;
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) iaMonthDays[1]=29;
    if (month < 1 || month > 12) return false;
    if (day < 1 || day > iaMonthDays[month - 1]) return false;
    return true;
}


function checkRepeatPassword(p1,p2) {
    return p1 == p2
}

// export {checkDateFormat, checkRepeatPassword, checkEmailFormat}

