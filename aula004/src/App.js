import React, { useState } from "react"
import Filho from './component/Filho'

const App = () => {
    const [valor, setValor] = useState("");
    const [cor, setCor] = useState("");

    return (
        <div style={{ backgroundColor: {valor} }}>
            <input
                type="text"
                onChange={(e) => setValor(e.target.value)}
                value={valor} 
            />
            <input
                type="text"
                onChange={(e) => setCor(e.target.value)}
                value={cor} 
            />
            <Filho texto={valor} cor={cor} />
            
        </div>
    );
};

export default App;
