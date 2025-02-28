import React, { useState } from "react"

const Filho = ({ texto,cor}) =>{

        return (
            <div style={{ backgroundColor: cor, width:"400px" }}>
                <h1>{ texto}</h1>
            </div>
        )
}


export default Filho