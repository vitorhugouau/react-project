import React from "react"


const App = () =>{
        
    const [ valor, setValor] = React.useState(10) 

    var numero = 4
    numero = numero * 8

    const Clique = () => {
        numero = numero + 10
        setValor( valor + 1 )
    }
     
        return(
            <div>
                <h1>Hello World</h1>
                <h1>vitorhugouau</h1>
                <h3>{numero}</h3>
            <input type='button'
                onClick={ () => {Clique()} }
                value='clique aqui'
                />
                <h3>{valor}</h3>
                
            </div>
        )
}

export default App