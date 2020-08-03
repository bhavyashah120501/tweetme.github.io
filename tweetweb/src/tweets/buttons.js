import React from 'react'
import {actionTweet} from './lookup'






export function ActionBtn({tweet , action,handleActions}){
  const likes = tweet.likes
  const type = action.type
  const handleClick = (event)=>{
    event.preventDefault()
    actionTweet(tweet.id,type,(res,status)=>{
          handleActions(res,status)
    })
  }
  const display = type === 'like' ? `${likes} ${action.display}` : action.display
  return <button className='btn btn-primary' onClick = {handleClick}>{display}</button> 
} 