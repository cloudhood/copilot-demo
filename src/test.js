function calculateDaysBetweenDates(start, end) {
    var startDate = new Date(start);
    var endDate = new Date(end);
    var millisecondsPerDay = 1000 * 60 * 60 * 24;
    return Math.floor((endDate - startDate) / millisecondsPerDay);
}

// Convert a date to a string of the form "YYYY-MM-DD"
function dateToString(date) {
    return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
}
