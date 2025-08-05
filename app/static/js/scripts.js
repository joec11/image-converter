window.addEventListener('load', function() {
    document.getElementById("file-input").value = "";
    document.getElementById("convert-to-format").value = "";
});

function populateImageFormatSelection() {
    const imageFormats = [
        { value: "bmp", label: "BMP (.bmp)" },
        { value: "gif", label: "GIF (.gif)" },
        { value: "heif", label: "HEIF (.heif)" },
        { value: "heic", label: "HEIF (.heic)" },
        { value: "ico", label: "ICO (.ico)" },
        { value: "jpg", label: "JPEG (.jpg)" },
        { value: "jpeg", label: "JPEG (.jpeg)" },
        { value: "png", label: "PNG (.png)" },
        { value: "raw", label: "RAW (.raw)" },
        { value: "cr2", label: "RAW (.cr2)" },
        { value: "nef", label: "RAW (.nef)" },
        { value: "svg", label: "SVG (.svg)" },
        { value: "tiff", label: "TIFF (.tiff)" },
        { value: "tif", label: "TIFF (.tif)" },
        { value: "webp", label: "WebP (.webp)" }
    ];

    const selectElement = document.getElementById("convert-to-format");

    imageFormats.forEach(format => {
        const option = document.createElement("option");
        option.value = format.value;
        option.textContent = format.label;
        selectElement.appendChild(option);
    });
}
document.addEventListener("DOMContentLoaded", populateImageFormatSelection);

document.getElementById('file-input').addEventListener('change', function(event) {
    const file = event.target.files[0]; // Get the selected file

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            imagePreview = document.getElementById('image-preview');

            // Set the data URL as the source for the image preview
            imagePreview.src = e.target.result;
        };

        reader.readAsDataURL(file); // Read the file as a data URL
    }
});

document.getElementById('convert-images').addEventListener('submit', function(event) {
    event.preventDefault();

    // Create the loading spinner
    document.getElementById('submit-container').appendChild(Object.assign(document.createElement("div"), { id: "loading-spinner" }));

    const fileInput = document.getElementById('file-input');
    const toFormat = document.getElementById('convert-to-format').value;

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('toFormat', toFormat);

    fetch('/convert', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Remove the loading spinner
        document.getElementById('loading-spinner').remove();

        // Display the result on the page
        if (data) {
            document.getElementById('result-response').textContent = data.formatConvert_response;
            document.getElementById('result-container').style.display = 'block'; // Show the result container
        } else {
            alert('Image Conversion failed.');
        }
    })
    .catch(error => {
        // Remove the loading spinner
        document.getElementById('loading-spinner').remove();

        console.error('Error:', error);
        alert('An error occurred during Image Conversion.');
    });
});
