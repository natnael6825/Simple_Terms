 
function start(){

    var loadingScreen = document.getElementById("word");

    const word=loadingScreen.value;
    

    sessionStorage.setItem("a", word);






}





function load(){


    const storedParagraph = sessionStorage.getItem('a');


    var loadingScreen = document.getElementById("last");

   
       
            const text =storedParagraph;
             
            // Send the text to your Flask app running on 127.0.0.1
            fetch('http://127.0.0.1:5000', { // Assuming your Flask app is running on port 5000
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:  text 
            })
            .then(response => response.json())
            .then(data => {

                loadingScreen.textContent=data
                console.log( data);


            })
            .catch(error => {
                console.error('Error:', error);
            });
       
    



}