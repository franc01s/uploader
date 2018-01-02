Dropzone.options.myAwesomeDropzone = { // The camelized version of the ID of the form element

    // The configuration we've talked about above
    url: '/upload',
    clickable: ".fileinput-button",
    autoProcessQueue: false,
    uploadMultiple: true,
    parallelUploads: 100,
    maxFiles: 5,
    paramName: "file",
    acceptFiles: 'image/*',

    // The setting up of the dropzone
    init: function () {
        var myDropzone = this;

        // First change the button to actually tell Dropzone to process the queue.
        this.element.querySelector("button[type=submit]").addEventListener("click", function (e) {
            // Make sure that the form isn't actually being sent.
            e.preventDefault();
            e.stopPropagation();
            myDropzone.processQueue();
        });
        this.element.querySelector("#actions .cancel").onclick = function () {
            document.querySelector("#total-progress").style.opacity = "0";
            document.querySelector(".start").removeAttribute("disabled");
            document.querySelector(".fileinput-button").removeAttribute("disabled");
            myDropzone.removeAllFiles(true);
        }

        // Listen to the sendingmultiple event. In this case, it's the sendingmultiple event instead
        // of the sending event because uploadMultiple is set to true.
        this.on("sendingmultiple", function () {
            this.element.querySelector("#total-progress").style.opacity = "1";
            this.element.querySelector(".start").setAttribute("disabled", "disabled");
            this.element.querySelector(".fileinput-button").setAttribute("disabled", "disabled");


            // Gets triggered when the form is actually being sent.
            // Hide the success button or the complete form.
        });
        this.on("successmultiple", function (files, response) {
            // Gets triggered when the files have successfully been sent.
            // Redirect user or notify of success.
            myDropzone.removeAllFiles(true);
            this.element.querySelector("#total-progress").style.opacity = "0";
            this.element.querySelector(".start").removeAttribute("disabled");
            this.element.querySelector(".fileinput-button").removeAttribute("disabled");
        });
        this.on("errormultiple", function (files, response) {
            // Gets triggered when there was an error sending the files.
            // Maybe show form again, and notify user of error
        });

        // Update the total progress bar
        this.on("totaluploadprogress", function (progress) {
            this.element.querySelector("#total-progress .progress-bar").style.width = progress + "%";

        });

    }
}

