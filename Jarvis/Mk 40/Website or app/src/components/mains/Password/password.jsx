import React, { useState } from "react";
import Btn from "../../Button/btn";

function Password({ onSubmit }) {
  const [inputValue, setInputValue] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();
    if (typeof onSubmit === 'function') {
      onSubmit(inputValue);
      setInputValue('');
    }
    console.log(inputValue)
  };

  return (
    <form onSubmit={handleSubmit} className="password">
      <div className="headingpassword">Enter the Password</div>
      <div className="inputtagpassword">
        {/* <input className="inptagpass"type="text" name="" id="" /> */}
        <input 
          type="text" 
          value={inputValue} 
          onChange={(e) => setInputValue(e.target.value)} 
          placeholder="" 
          className="inptagpass"
        />
      </div>
      <div className="btnforpassword">  
        <Btn type="submit" text="Join"/>
      </div>
    </form>
  );
}

export default Password;
