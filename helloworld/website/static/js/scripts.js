$( document ).ready(function() {
    $("#id_name").focus()
});

$("#id_name").focusout( () => {
    let value = $("#id_name").val()
    $("#id_slug").val(sanitizeTitle(value));
})

function sanitizeTitle(title) {
    let slug = "";
    // Change to lower case
    let titleLower = title.toLowerCase();
    // Letter "e"
    slug = titleLower.replace(/e|é|è|ẽ|ẻ|ẹ|ê|ế|ề|ễ|ể|ệ/gi, 'e');
    // Letter "a"
    slug = slug.replace(/a|á|à|ã|ả|ạ|ă|ắ|ằ|ẵ|ẳ|ặ|â|ấ|ầ|ẫ|ẩ|ậ/gi, 'a');
    // Letter "o"
    slug = slug.replace(/o|ó|ò|õ|ỏ|ọ|ô|ố|ồ|ỗ|ổ|ộ|ơ|ớ|ờ|ỡ|ở|ợ/gi, 'o');
    // Letter "u"
    slug = slug.replace(/u|ú|ù|ũ|ủ|ụ|ư|ứ|ừ|ữ|ử|ự/gi, 'u');
    // Letter "ç"
    slug = slug.replace(/ç/gi, 'c');
    // Letter "í"
    slug = slug.replace(/í/gi, 'i');
    // Letter "d"
    slug = slug.replace(/đ/gi, 'd');
    // Trim the last whitespace
    slug = slug.replace(/\s*$/g, '');
    // Change whitespace to "-"
    slug = slug.replace(/\s+/g, '-');

    return slug;
}
