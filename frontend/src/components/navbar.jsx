import React from 'react';

export default function Navbar(){
    return (
        <div className='navbar ' >
            <img className="logo" src="logo.png" alt="Logo"/>
            <div >
                <a className='link' href="#">Home</a>                
                <a className='link' href="#">Chatbot</a>              
                <a className='link' href="#">Community forum</a>
                <a className='link'  href="#">About</a>
                <a className='link' href="#">Contact</a>
            </div>
        </div>
    );
};