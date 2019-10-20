import React from 'react';
import './App.css';

function App() {
    return (
        <div className="App">
            <form action="/api/spam" method="post">
	        <textarea name="email" rows="10"></textarea>
	        <input type="submit" />
            </form>
        </div>
    );
}

export default App;
