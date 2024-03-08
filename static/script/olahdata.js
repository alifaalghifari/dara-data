$(document).ready(function () {

    let FILES;
    // READ CSV FILE 
    $('#fileInput').on('change', function() {
        const fileNameDisplay = $('#fileNameDisplay');
        const allowedExtensions = /(\.csv)$/i;

        if (allowedExtensions.exec(this.value)) {
            fileNameDisplay.text(this.files.length > 0 ? `File Yang Dipilih: ${this.files[0].name}` : '');
            FILES = this.files[0]
        } else {
            // Reset input and display an error message
            fileNameDisplay.text('Please select a valid CSV file.');
            this.value = '';
        }
    });

    // SEND DATA
    $('#dataCreate').click(function () {

        // Create FormData object
        var formData = new FormData();
        formData.append('csvFile', FILES);

        // Use jQuery Ajax to call the Flask API
        $.ajax({
            type: 'POST',
            url: '/modify/data_create',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                // Hide notes 
                $('#notes').addClass('hidden')
                console.log(response)
                
                // Add step
                let message = $("<p>").text(response.message);
                $('#result').append(message);
                
                // Display the result on the page
                $('#result').append(response.data);

                
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });

    // GET INFO OFF DATA
    $('#dataInfo').click(function () {

        var formData = new FormData();
        formData.append('csvFile', FILES);
        
        $.ajax({
            type: 'POST',
            url: '/modify/data_info',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                // Add step
                let message = $("<p>").text(response.message);
                $('#result').append(message);

                // DISPLAY RESULT ON THE PAGE
                let formattedHtml = response.data.replace(/\n/g, '<br>')
                $('#result').append(formattedHtml);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    })

    // GET HEAD N OFF DATA
    $('#dataHead').click(function () {

        var formData = new FormData();
        formData.append('csvFile', FILES);
        formData.append('n', 6)
        console.log(formData)
        $.ajax({
            type: 'POST',
            url: '/modify/data_head',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                // Add step
                let message = $("<p>").text(response.message);
                $('#result').append(message);

                // DISPLAY RESULT ON THE PAGE
                $('#result').append(response.data);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    })

    // GET TAIL N OFF DATA
    $('#dataTail').click(function () {

        var formData = new FormData();
        formData.append('csvFile', FILES);
        formData.append('n', 6)
        console.log(formData)
        $.ajax({
            type: 'POST',
            url: '/modify/data_tail',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                // Add step
                let message = $("<p>").text(response.message);
                $('#result').append(message);

                // DISPLAY RESULT ON THE PAGE
                $('#result').append(response.data);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    })
});