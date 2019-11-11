import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function Form(props) {
    const getSpamminess = () => {
        let message = document.getElementById("email").value;
        axios.post('/api/spam', {
            email: message
        },
        {
            headers: {'Content-Type': 'application/json'}
	}).then((response) => {
            console.log(response.data.spam);
            props.setspam(response.data.spam);
        }, (error) => {
            console.log(error);
        });
    };
    
    return (
        <div className="form">
	    <textarea id="email"></textarea><br/>
	    <button onClick={getSpamminess}>Evaluate</button>
	</div>
    );
}

function Results(props) {
    if (props.spam == null) {
        return <p>No values here</p>;
    }
    
    if (props.spam == 'spam') {
        return <p>It is spam</p>;
    } else if ( props.spam == 'nonspam') {
        return <p>It is not spam</p>
    }
}

function App() {
    const [isSpam, setSpam] = useState(null);
    
    return (
        <div className="App">
            <Form setspam={setSpam} />

            <div className="results">
                <Results spam={isSpam}/>
            </div>
        </div>
    );
}

export default App;
