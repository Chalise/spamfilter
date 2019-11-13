import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

const TRESHOLD = 0.8;

function Form(props) {
    const getSpamminess = () => {
        let message = document.getElementById("email").value;
        axios.post('/api/spam', {
            email: message
        },
        {
            headers: {'Content-Type': 'application/json'}
	}).then((response) => {
            console.log(response.data);
            let label  = response.data.spam;
            let probability = response.data.probability;
            if (label == 'spam' && probability < TRESHOLD) {
                props.setspam('nonspam')
            } else {
                props.setspam(label);
            }
        }, (error) => {
            console.log(error);
        });
    };

    const resetState = () => {
        props.setspam(null);
    }
    
    return (
        <div className="form">
	    <textarea id="email" placeholder="Paste email here..." onChange={resetState}></textarea><br/>
	    <button onClick={getSpamminess}>Evaluate</button>
	</div>
    );
}

function Results(props) {
    if (props.spam == null) {
        return (
            <div className="results none"></div>
        );
    }
    
    if (props.spam == 'spam') {
        return (
	    <div className="results warning">
		<p>It is spam!</p>
	    </div>
	);
    } else if ( props.spam == 'nonspam') {
        return (
	    <div className="results note">
		<p>It is ham.</p>
	    </div>
	);
    }
}

function App() {
    const [isSpam, setSpam] = useState(null);
    
    return (
        <div className="App">
            <h1>Machine-Learning Spam Filter</h1>
            <Form setspam={setSpam} />
            <Results spam={isSpam}/>
        </div>
    );
}

export default App;
