import React from 'react';
// import navbarImage from '../../assets/Navbar.png';
// Example usage in parent component:

{/* <Btn 
    text="Submit" 
    onSubmit={handleSubmit}
    /> */}
function Btn({ text }) {
  return (
    <div className="btndiv">
      <button 
        type="submit" 
        className="btn"
      >
        {text}
      </button>
    </div>
  );
}

export default Btn;
