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

    const selectElement = document.getElementById("convertToFormat");

    imageFormats.forEach(format => {
        const option = document.createElement("option");
        option.value = format.value;
        option.textContent = format.label;
        selectElement.appendChild(option);
    });
}
document.addEventListener("DOMContentLoaded", populateImageFormatSelection);

document.getElementById('convertImages').addEventListener('submit', function(event) {
    event.preventDefault();

    // Show the loading spinner
    document.getElementById('loading_spinner').style.display = 'inline-block';

    const fileInput = document.getElementById('imageFile');
    const toFormat = document.getElementById('convertToFormat').value;

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('toFormat', toFormat);

    fetch('/convert', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide the loading spinner
        document.getElementById('loading_spinner').style.display = 'none';
        
        // Display the result on the page
        if (data) {
            document.getElementById('result_response').textContent = data.formatConvert_response;
            document.getElementById('result_container').style.display = 'block'; // Show the result container
        } else {
            alert('Image Conversion failed.');
        }
    })
    .catch(error => {
        // Hide the loading spinner
        document.getElementById('loading_spinner').style.display = 'none';

        console.error('Error:', error);
        alert('An error occurred during Image Conversion.');
    });
});
