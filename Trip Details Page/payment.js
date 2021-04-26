const handleChangePassword = () => {
    const pwFields = document.getElementsByClassName("password-field");
    console.log(pwFields);

    for (let i = 0; i < pwFields.length; i++) {
        const field = pwFields[i];
        console.log(field.style.display);

        if (field.style.display === "none") {
            field.style.display = "inherit";
        } else {
            field.style.display = "none";
        }
    }
};

document
    .getElementById("files")
    .addEventListener("change", handleFileSelect, false);

function handleFileSelect(evt) {
    var files = evt.target.files;

    var f = files[0];

    var reader = new FileReader();

    reader.onload = (function (theFile) {
        return function (e) {
            document.getElementById("list").innerHTML = [
                '<img src="',
                e.target.result,
                '" title="',
                theFile.name,
                '" width="50" >',
            ].join("");
            document.getElementById("upload").innerHTML = "Change Image";
        };
    })(f);

    reader.readAsDataURL(f);
}
