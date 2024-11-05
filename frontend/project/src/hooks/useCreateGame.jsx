
export default function useCreateGame(){
    const createGame = () => {
        fetch(`http://localhost:8000/api/create_question/`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question_text: "name",
                choices: ["str"]
            }),
        
        })
        .then((response) => {
            return response.json();
        })
        .then((response) =>{
            console.log(response)
        })
        .catch((reason) => {
            console.error(reason);
        });
    };

    return { createGame };
}