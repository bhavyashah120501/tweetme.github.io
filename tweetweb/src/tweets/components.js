import React,{useState,useEffect} from 'react'
import {TweetList} from './list'
import {ActionBtn} from './buttons'
import {Tweet} from './detail'
import {TweetCreate} from './create'
import {loaddetailtweets} from './lookup'
import {FeedList} from './feed'



export function FeedComponent(props){
	const [newTweets , setNewTweets] = useState([])
	function handleNewTweet(newTweet){
		let tempNewTweets = [...newTweets]
		tempNewTweets.unshift(newTweet) 
		setNewTweets(tempNewTweets)
	}
	return(
		<div className='row'>
			<TweetCreate didTweet={handleNewTweet} />
			<div className='col-12'>
			<FeedList newTweets={newTweets}/>
			</div>
		</div>
		 )
}



export function TweetComponent(props){ 
	const [newTweets , setNewTweets] = useState([])
	function handleNewTweet(newTweet){
		let tempNewTweets = [...newTweets]
		tempNewTweets.unshift(newTweet) 
		setNewTweets(tempNewTweets)
	}
	return(
		<div className='row'>
			{props.canTweet && <TweetCreate didTweet={handleNewTweet}/>}
			<div className='col-12'>
			<TweetList newTweets={newTweets} {...props} />
			</div>
		</div>
		 )
}



export function TweetDetailComponent(props){

	const {tweetid}=props

	const [didLookup,setDidLookup] = useState(false)
	const [tweet,setTweet] = useState(null)
	useEffect(()=>{
		if(didLookup===false){
		
			loaddetailtweets(tweetid,(res,status)=>{
				if(status === 200){
					setTweet(res)
				}
				else{
					alert('alert')
				}
			})
			setDidLookup(true)
		}
	},[didLookup,tweetid])

	return tweet === null ? null : <Tweet hideActions={true} styling={'col-10 p-3 col-md-8 bg-white text-dark border'}  tweet = {tweet}  />
}


