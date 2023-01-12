import { useState } from "react";

const Navbar = () => {
    const [name,setName]=useState('Autobots');
    const handleClick=()=>{
        setName('Afourathon')
    }
    return ( 
        <nav className="navbar">
            <h1>{name}</h1>
            <div className="links">
                <a className="sub-name" href="/">Home</a>
                <a className="sub-name" href="/team">Teams</a>
                <a className="sub-name" href="/create-team">New Team</a>
                <a className="sub-name" href="/create-team-members">New Team member</a>

                <button onClick={handleClick}>Click me</button>
            </div>
        </nav>
     );
}
 
export default Navbar;