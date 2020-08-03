import React,{useState,useEffect} from 'react'
import {loadtweets} from './lookup'
import {createTweet} from './lookup'

import {Tweet} from './detail.js'



export function TweetList({newTweets,username}){
  const [tweetsinit ,setTweetsinit] = useState([])
  const [Tweets,setTweets] = useState([])
  const [tweetDidSet,setTweetDidSet] = useState(false)
  const [nextUrl,setNextUrl] = useState(null)
  useEffect(()=>{
    const final = [...newTweets].concat(tweetsinit)
    if(final.length !== Tweets.length){
      
      
      setTweets(final)
      
      
    }
  },[newTweets,tweetsinit,Tweets])
  useEffect(()=>{
    if(tweetDidSet === false)
    {
      const Mycallback=(response,status)=>{
        if(status === 200){
          setNextUrl(response.next)
          setTweetsinit(response.results)
          setTweetDidSet(true)
        }
        else{
          alert('There was an error')
        }
      }
      loadtweets(username,Mycallback)
    }
  },[tweetsinit,tweetDidSet,setTweetDidSet])
  const handleTweetRetweet=(newt)=>{
    
    let final = [...tweetsinit]
    final.unshift(newt)
    setTweetsinit(final)
    let final2 = [...Tweets]
    final2.unshift(newt)
    setTweets(final2)
  }
  const handleLoadNext=(event)=>{
    event.preventDefault()
    const callback=(response,status)=>{
       if(status === 200){
          setNextUrl(response.next)
          newTweets = [...Tweets].concat(response.results)
          setTweetsinit(newTweets)
        }
        else{
          alert('There was an error')
        }
    }
    if(nextUrl!== null){
       loadtweets(username,callback,nextUrl)
    }
  }
  return (<div className='row'>
            {Tweets.map((tweet,index)=>{
              return <Tweet hideActions={false} isRetweet={false} handleTweetRetweet={handleTweetRetweet} styling={'col-12 mt-3 bg-white text-dark border'}  tweet = {tweet}  key={index} />
            })}
            <div className='col'>
            {nextUrl != null && <button onClick={handleLoadNext} className='btn btn-lg mt-2 btn-outline-primary'>Load Tweets</button>}
            </div>
          </div>)
}

