// Event listener for task submission
document.getElementById("submitTask").addEventListener("click", function(event) {
    // Prevent default keybinds from happening and get new task from input field
    event.preventDefault();
    const newTask = document.getElementById("newTask").value;

    // Grab container for tasks
    const tasks_container = document.getElementById("tasks");

    // Create label with task name to be appended under container
    const label = document.createElement("label");
    label.id = newTask;
    label.classList = "labelForCheck";
    
    // Create input element for checkbox to be appended under label
    const input = document.createElement("input");
    input.type = "checkbox";
    input.classList = "checkWithLabel";
    input.id = newTask;

    // Create span to hold text after input box inside of label
    const span = document.createElement('span');
    span.textContent = newTask;
    
    // Append input under label and label under tasks_container
    label.appendChild(input);
    label.appendChild(span);
    tasks_container.appendChild(label);

    // Reset input text field and form as a whole
    document.forms["addTask"].reset()
})

// Event listener to delete tasks after completed
document.querySelectorAll('.checkWithLabel').addEventListener("click", function(event) {
    // Prevent default keybinds and get the 
})
