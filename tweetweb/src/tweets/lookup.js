import {backendLookup} from '../lookup'


export function actionTweet(tweetId,action,callback){
	const data = {id:tweetId,action:action , content:'...'}
	backendLookup("POST",'/tweets/action',callback,data)
}

export function createTweet(newVal,callback){
  backendLookup('POST','/tweet/create',callback,{tweet:newVal})
}


export function loadtweets(username,callback,nextUrl){
  let endpoint = '/tweets'
  if(username!=null){
  	endpoint=`/tweets?username=${username}`
  }
  if(nextUrl !== null && nextUrl !== undefined){
    endpoint = nextUrl.replace("http://localhost:8000/api","")
  }
  backendLookup('GET',endpoint,callback)
}

export function loaddetailtweets(tweetId,callback){
  let endpoint = `/tweets/${tweetId}`
  backendLookup('GET',endpoint,callback)
}
export function loadfeeds(callback,nextUrl){
  let endpoint = '/tweets/feed'
  if(nextUrl !== null && nextUrl !== undefined){
    endpoint = nextUrl.replace("http://localhost:8000/api","")
  }
  backendLookup('GET',endpoint,callback)
}




export function loaddetailprofile(tweetId,callback){
  let endpoint = `/tweets/${tweetId}`
  backendLookup('GET',endpoint,callback)
}