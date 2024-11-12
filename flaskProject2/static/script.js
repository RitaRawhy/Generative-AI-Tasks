function createTrainingInputs() {
    var numExamples = document.getElementById("num_examples").value;
    var trainingInputsDiv = document.getElementById("training_inputs");
    trainingInputsDiv.innerHTML = "";

    for (var i = 1; i <= numExamples; i++) {
        var inputContainer = document.createElement("div");
        inputContainer.classList.add("input-container");

        var inputLabel = document.createElement("label");
        inputLabel.setAttribute("for", "train_input_" + i);
        inputLabel.textContent = "Question"+ i + ": " + "\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Answer " + i + ": ";

        var inputTextbox = document.createElement("input");
        inputTextbox.setAttribute("type", "text");
        inputTextbox.setAttribute("id", "train_input_" + i);
        inputTextbox.setAttribute("name", "train_input_" + i);
        inputTextbox.setAttribute("required", true);

        var outputTextbox = document.createElement("input");
        outputTextbox.setAttribute("type", "text");
        outputTextbox.setAttribute("id", "train_output_" + i);
        outputTextbox.setAttribute("name", "train_output_" + i);
        outputTextbox.setAttribute("required", true);

        inputContainer.appendChild(inputLabel);
        inputContainer.appendChild(inputTextbox);
        inputContainer.appendChild(outputTextbox);
        trainingInputsDiv.appendChild(inputContainer);
        trainingInputsDiv.appendChild(document.createElement("br"));
    }
}