import React from "react";
import axios from 'axios';

const App = () => {
    const [dados, setDados] = React.useState([]);

    const buscarDados = async () => {
        const url = "https://rickandmortyapi.com/api/character";

        try {
            const resposta = await axios.get(url);
            console.log(resposta.data.results); 
            setDados(resposta.data.results); 
        } catch (error) {
            console.error("Erro ao buscar dados", error);
        }
    };

    return (
        <div>
            <input
                type="button"
                value="Buscar"
                onClick={buscarDados} // Corrigido aqui
            />
            <ul>
                {dados.map(personagem => (
                    <li key={personagem.id}>{personagem.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
