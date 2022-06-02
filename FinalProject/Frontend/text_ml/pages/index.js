import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import { useState } from 'react'
const axios = require('axios');

export default function Home() {
  const [txtdata,setTxtdata] = useState("hi")
  // const [arr,setArr] = useState([])
  const [result,setResult] = useState("")
  const submitValue=()=>{

    axios.post('http://192.168.43.57:3100/all', {
      data: txtdata,
    })
    .then(function (response) {
      console.log(response.data);
      setResult(response.data)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  let output=""
  let lst = [1,2,3]

  return (
    <>
    
    <div className="container pt-2 mt-2">
    <h1 className='title is-size-1 '>Question Level Predictor </h1>
    <br></br>
    <h1>A Model Based On Bloom's Taxonomy </h1>
      {/* <h1>Data is {txtdata}</h1> */}

      <hr/>
    <input type="text" className='textarea is-success' placeholder="Enter Data" onChange={e => setTxtdata(e.target.value)} />
    <button className='button is-primary' onClick={submitValue}>Submit</button>
    <br></br>
    <br></br>
    <h2 className='heading is-size-2'>Predicted Level</h2>
    <hr></hr>
    <h2 className='is-size-3'>{result}</h2>


    </div>
    </>
  )
}
