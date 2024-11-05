import { useState } from "react";


export default function ToDoList() {

    const [tasks, setTasks] = useState([]);    // Stockage selon l'état
    const [newTask, setNewTask] = useState("");

    const addTask = () => {
        if (newTask.trim() === "") return; // Pas d'ajout de tâches vides
        const newTaskObject = {
            text: newTask,     
            completed: false     
        };
        setTasks([...tasks, newTaskObject]); 
        setNewTask(""); // Réinitialise l'entrée de texte
    };

    const toggleTaskCompletion = (index) => {
        setTasks(tasks.map((task, i)=>
            i === index ? { ...task, completed: !task.completed } : task
        ));
    };

    return (
        <div>
            <h1>To-Do List</h1> 
            <div>
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                    placeholder="Ajouter une tâche..."
                />
                <button onClick={addTask}>Ajouter</button>
            </div>

            <ul>
                {tasks.map((task, index) => (
                    <li
                        key={index}
                        onClick={() => toggleTaskCompletion(index)}
                        style={{
                            textDecoration: task.completed ? "line-through" : "none",
                            cursor: "pointer"
                        }}
                    >
                        {task.text}
                    </li>
                ))}
            </ul>
        </div>
    );
}