import React,{useState,useEffect} from 'react'
import {ActionBtn} from './buttons.js'

export function Tweet({styling,tweet,handleTweetRetweet,hideActions,isRetweet,reTweeter}){ 
  const [actionTweet,setactionTweet] = useState(tweet)
 
  var path = window.location.pathname
  var idReg = /(?<tweetid>\d+)/
  var match = path.match(idReg)
  const tweetid = match ? match.groups.tweetid : -1

  const isDetail = tweet!==null && `${tweetid}` === `${tweet.id}`
  const handleActions=(res,status)=>{
    if(status===200)
    {
      setactionTweet(res)
    }
    else if(status===201 && handleTweetRetweet){
      
      handleTweetRetweet(res)
    }
  }
  const handleLink=(event)=>{
    event.preventDefault()
    window.location.href = `/${tweet.id}`
  }
  var style = styling
  if(isRetweet===true){
    style = `${styling} mx-2  border-rounded small`
  }

  const UserLink=(event)=>{
    event.preventDefault()
    window.location.href=`/profile/${tweet.user.username}`
  }
  
  return   <div className = {style}>
           {isRetweet===true && <p className='text-muted mb-2 '>Retweet via <span onClick={UserLink}>@{reTweeter.username}</span></p>}
           <div className='d-flex my-4'>
            <div className='col-1'>
            
            <span className=' pointer px-3 py-2 rounded-circle bg-dark text-white' onClick={UserLink}>{tweet.user.username[0]}</span>
            </div>
           <div className='col-10 offset-1'>
           <p>
           {tweet.user.first_name}{" "}{tweet.user.last_name}{" "}<span className='pointer' onClick={UserLink} >@{tweet.user.username}</span>
           </p>
           <p>
           {tweet.tweet}
           </p> 
           <div>
            {tweet.parent && <Tweet reTweeter={tweet.user} tweet={tweet.parent} styling={styling} hideAction={true} isRetweet={true} />}
           </div>
           <div className = 'btn btn-group px-0'>
           {hideActions === false && 
           <React.Fragment>
           {<ActionBtn tweet = {actionTweet} handleActions={handleActions} action = { { type : 'like' , display: 'Like'} } />}
           {<ActionBtn tweet = {actionTweet} handleActions={handleActions} action = { { type : 'unlike' , display:'UnLike'} } />}
           {<ActionBtn tweet = {actionTweet} handleActions={handleActions} action = { { type : 'retweet' ,display : 'Retweet'} } />}
           </React.Fragment>}
           {isDetail === false ? <button onClick={handleLink} className='btn btn-outline-primary' > View </button> : null }
           </div>
           </div>
           </div>
           </div>
}


