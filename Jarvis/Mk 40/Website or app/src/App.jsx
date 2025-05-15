import { useState } from 'react'
import Navbar from './components/Navbar/navbar.jsx'
import Password from'./components/mains/Password/password.jsx'
import Chat from './components/mains/Chat/chat.jsx'

import './App.css'

function App() {
  return (
    <>
      <Navbar/>
      <div className="main">
      {/* <Password /> */}
      <Chat />
      </div>
    </>
  )
}

export default App
