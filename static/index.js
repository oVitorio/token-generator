/**
 * The code snippet is an event listener that handles the behavior of a checkbox, input fields, and a button on a web page.
 * It updates the visibility of a "Custom Salt" field and label based on the state of a checkbox.
 * It also sends settings to the backend and updates the results on the page when a button is clicked.
 * Additionally, it detects changes in a slider and updates the character count text accordingly.
 *
 * Example Usage:
 * ```javascript
 * // HTML
 * <input type="checkbox" id="useGenericSalt">
 * <input type="text" id="customSalt">
 * <input type="range" id="customRange1">
 * <label for="customSalt">Custom Salt</label>
 * <button id="generateToken">Generate Token</button>
 * <p id="tokenResult"></p>
 * <p id="usedSaltResult"></p>
 * <p id="encryptedTokenResult"></p>
 * <p id="charCount"></p>
 *
 * // JavaScript
 * document.addEventListener('DOMContentLoaded', function () {
 *     // Code snippet
 * });
 * ```
 *
 * @summary Handles the behavior of a checkbox, input fields, and a button on a web page.
 * @function
 */
document.addEventListener('DOMContentLoaded', function () {
    var useGenericSaltCheckbox = document.getElementById('useGenericSalt');
    var customSaltInput = document.getElementById('customSalt');
    var characterCountInput = document.getElementById('customRange1');
    var customSaltLabel = document.querySelector('label[for="customSalt"]'); // Select the label for Custom Salt field

    // Function to update the visibility of the "Custom Salt" field and label
    function updateCustomSaltInput() {
        if (useGenericSaltCheckbox.checked) {
            customSaltInput.style.display = 'none';
            customSaltInput.value = ''; // Clear the field
            customSaltLabel.style.display = 'none'; // Hide the label
        } else {
            customSaltInput.style.display = 'block';
            customSaltLabel.style.display = 'block'; // Show the label
        }
    }

    // Call the function when the page loads and when the checkbox changes
    updateCustomSaltInput();
    useGenericSaltCheckbox.addEventListener('change', updateCustomSaltInput);

    document.getElementById('generateToken').addEventListener('click', function () {
        var characterCount = characterCountInput.value;
        var useGenericSalt = useGenericSaltCheckbox.checked;
        var customSalt = customSaltInput.value;

        // Send settings to the backend
        axios.post('/generate_token', {
            characterCount: characterCount,
            useGenericSalt: useGenericSalt,
            customSalt: customSalt
        })
            .then(function (response) {
                // Update the results on the page
                document.getElementById('tokenResult').textContent = response.data.token;
                document.getElementById('usedSaltResult').textContent = response.data.salt;
                // Simple example of encryption, replace with your real implementation
                document.getElementById('encryptedTokenResult').textContent = response.data.sha;
            })
            .catch(function (error) {
                console.error(error);
            });
    });

    const slider = document.getElementById("customRange1");
    const charCount = document.getElementById("charCount");

    // Add an event listener to detect changes in the slider
    slider.addEventListener("input", () => {
        // Update the character count text with the current slider value
        charCount.textContent = slider.value;
    });

});
