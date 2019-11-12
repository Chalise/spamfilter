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
        return null;
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
            <Form setspam={setSpam} />
            <Results spam={isSpam}/>
        </div>
    );
}

export default App;
