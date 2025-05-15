import React from 'react';
import navbarImage from '../../assets/Navbar.png';

function Navbar() {
  return (
    <div className="navbar">
      <img src={navbarImage} alt="Navbar" className="imgnav"/>
    </div>
  );
}

export default Navbar;
