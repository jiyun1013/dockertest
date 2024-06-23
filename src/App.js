import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [latestValue, setLatestValue] = useState('');

  const handleAdd = async () => {
    try {
      await axios.post('http://localhost:8000/add/', { value: inputValue });
      setInputValue('');
    } catch (error) {
      console.error("There was an error adding the data!", error);
    }
  };

  const handleGet = async () => {
    try {
      const response = await axios.get('http://localhost:8000/get/');
      setLatestValue(response.data.value);
    } catch (error) {
      console.error("There was an error retrieving the data!", error);
    }
  };
  return (
    <div id='wrap'>
      <section id='secOne'>
        <form>
          <input 
          type='text' 
          value={inputValue} 
        onChange={e => setInputValue(e.target.value)}
          placeholder='텍스트 입력창'/>
          <button onClick={handleAdd}>add</button>
        </form>
      </section>

      <section id='secTwo'>
        <div>
        <button onClick={handleGet}>가져오기</button>
        </div>
        <label>{latestValue}</label>
      </section>
    </div>
  );
}

export default App;
