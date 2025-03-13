import React, { useState } from "react";
import dataJSON from './data.json';

const App = () => {

    const [valor, setValor] = useState('John Doe');

    const tabelaFiltrada = dataJSON.filter(item => 
        item.name.toLocaleLowerCase().includes(valor.toLocaleLowerCase())
    );

    return (
        <div style={{alignItems: "center", display: "flex", justifyContent: "center", 
            flexDirection: "column", gap: "15px" , marginTop: "15px"}}>
                
            <input 
                type="text" 
                value={valor} 
                onChange={(e) => setValor(e.target.value)} 
                placeholder="Digite o nome"
            />
            <table border="1">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {tabelaFiltrada.map((item, index) => (
                        <tr key={index}>
                            <td>{item.name}</td>
                            <td>{item.age}</td>
                            <td>{item.email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default App;
