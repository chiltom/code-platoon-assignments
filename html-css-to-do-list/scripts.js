// Event listener for task submission
document.getElementById("submitTask").addEventListener("click", function(event) {
    event.preventDefault();
    const newTask = document.getElementById("newTask").value;

    const tasks_container = document.getElementById("tasks");
    const new_div = document.createElement("div");
    new_div.classList = "task";
    tasks_container.appendChild(new_div);

    const input = document.createElement("input");
    input.type = "checkbox";
    input.classList = "checkWithLabel";
    input.id = newTask;
    new_div.appendChild(input);

    const label = document.createElement("label");
    label.for = newTask;
    label.classList = "labelForCheck";
    label.textContent = newTask;
    new_div.appendChild(label);
})


