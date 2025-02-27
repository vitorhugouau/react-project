import React from 'react';
import ReactDOM from 'react-dom/client';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <div>Vitor</div>
  <Texto /> 
  </React.StrictMode>
);

function Texto(){
  var [ valor, setValor] = React.useState()
  function mudarValor (e){
    setValor(e.target.value * 5)
  } 
  return (
    <div>
      <input type="text"
        onChange={ (e) => mudarValor(e)}
        />
        <spam> {valor} </spam>

        <hr/>
    </div>

  )
}
