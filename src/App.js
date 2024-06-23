import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [allValues, setAllValues] = useState([]);

  const handleAdd = async (e) => {
    e.preventDefault();  // 기본 폼 제출 동작 방지
    try {
      await axios.post('http://localhost:8000/add/', { value: inputValue });
      setInputValue('');
    } catch (error) {
      console.error("There was an error adding the data!", error);
    }
  };

  const handleGetAll = async () => {
    try {
      const response = await axios.get('http://localhost:8000/get_all/');
      setAllValues(response.data);
    } catch (error) {
      console.error("There was an error retrieving the data!", error);
    }
  };

  return (
    <div id='wrap'>
      <section id='secOne'>
        <form onSubmit={handleAdd}>
          <input
            type='text'
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}
            placeholder='텍스트 입력창'
          />
          <button type='submit'>add</button>
        </form>
      </section>

      <section id='secTwo'>
        <div>
          <button onClick={handleGetAll}>가져오기</button>
        </div>
        <div className='ulBox'>
          <ul>
            {allValues.map((item) => (
              <li key={item.id}>{item.value}</li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}

export default App;
