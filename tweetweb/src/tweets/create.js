import React,{useState,useEffect} from 'react'
import {createTweet} from './lookup'



export function TweetCreate({ didTweet }){
	const textAreaRef = React.createRef()
	const handleBackEndUpdate =(res,status)=>{
		if(status===201){
			didTweet(res)
		}
		else{
			alert('an error occured')
		}
	}
	const handleSubmit=(event)=>{
		event.preventDefault()
		const newVal = textAreaRef.current.value
		createTweet(newVal,handleBackEndUpdate)
		textAreaRef.current.value=''
	}	
	return(

				<div className='col-12 mb-3'>
				<form onSubmit={handleSubmit}>
				  <textarea ref={textAreaRef} required  className='form-control'>
				  </textarea>
				  <button type='submit' className='btn btn-primary' value='Submit'> Tweet </button>
				</form>
				</div>

		 )
    
}
