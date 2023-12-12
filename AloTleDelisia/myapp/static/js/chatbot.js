import { MDCTextField } from "https://cdn.skypack.dev/@material/textfield";
import { TextClassifier, FilesetResolver } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-text@0.10.0";
const textField = new MDCTextField(document.querySelector(".mdc-text-field"));
// Get the required elements
const input = document.getElementById("input");
const output = document.getElementById("output");
const submit = document.getElementById("submit");
const demosSection = document.getElementById("demos");
let textClassifier;
// Create the TextClassifier object upon page load
const createTextClassifier = async () => {
    const text = await FilesetResolver.forTextTasks("https://cdn.jsdelivr.net/npm/@mediapipe/tasks-text@0.10.0/wasm");
    textClassifier = await TextClassifier.createFromOptions(text, {
        baseOptions: {
            modelAssetPath: `https://storage.googleapis.com/mediapipe-models/text_classifier/bert_classifier/float32/1/bert_classifier.tflite`
        },
        maxResults: 5
    });
    // Show demo section now model is ready to use.
    demosSection.classList.remove("invisible");
};
createTextClassifier();

// Add a button click listener that classifies text on click
submit.addEventListener("click", async () => {
    if (input.value === "") {
        alert("Please write some text, or click 'Populate text' to add text");
        return;
    }
    output.innerText = "Detectando...";
    await sleep(5);
    const result = textClassifier.classify(input.value);
    displayClassificationResult(result);
});
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
// Iterate through the sentiment categories in the TextClassifierResult object, then display them in #output
function displayClassificationResult(result) {
    if (result.classifications[0].categories.length > 0) {
        output.innerText = "";
    }
    else {
        output.innerText = "Result is empty";
    }
    const categories = [];
    // Single-head model.
    for (const category of result.classifications[0].categories) {
        const categoryDiv = document.createElement("div");
        categoryDiv.innerText = `${category.categoryName}: ${category.score.toFixed(2)}`;
        // highlight the likely category
        if (category.score.toFixed(2) > 0.5) {
            categoryDiv.style.color = "#12b5cb";
        }
        output.appendChild(categoryDiv);
    }
}