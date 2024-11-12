function createTrainingInputs() {
    var numExamples = document.getElementById("num_examples").value;
    var trainingInputsDiv = document.getElementById("training_inputs");
    trainingInputsDiv.innerHTML = "";

    for (var i = 1; i <= numExamples; i++) {
        var exampleDiv = document.createElement("div");
        exampleDiv.classList.add("example");

        var inputLabel = document.createElement("label");
        inputLabel.setAttribute("for", "train_input_" + i);
        inputLabel.textContent = "Enter Question " + i + ":";

        var inputTextbox = document.createElement("input");
        inputTextbox.setAttribute("type", "text");
        inputTextbox.setAttribute("id", "train_input_" + i);
        inputTextbox.setAttribute("name", "train_input_" + i);
        inputTextbox.setAttribute("required", true);

        var outputLabel = document.createElement("label");
        outputLabel.setAttribute("for", "train_output_" + i);
        outputLabel.textContent = "Enter Answer:";

        var outputTextbox = document.createElement("input");
        outputTextbox.setAttribute("type", "text");
        outputTextbox.setAttribute("id", "train_output_" + i);
        outputTextbox.setAttribute("name", "train_output_" + i);
        outputTextbox.setAttribute("required", true);

        exampleDiv.appendChild(inputLabel);
        exampleDiv.appendChild(inputTextbox);
        exampleDiv.appendChild(outputLabel);
        exampleDiv.appendChild(outputTextbox);

        trainingInputsDiv.appendChild(exampleDiv);
    }

    var button2 = document.getElementById('CreateTest');
    button2.style.display = 'block';
}