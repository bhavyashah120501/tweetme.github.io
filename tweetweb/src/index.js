import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetComponent,TweetDetailComponent,FeedComponent} from './tweets'
import * as serviceWorker from './serviceWorker';
import {ProfileBadge} from './profile'
import {SearchComponent} from './search'


const appEl = document.getElementById('root')
if(appEl){
	ReactDOM.render(
	  <React.StrictMode>
	    <App />
	  </React.StrictMode>,
	  appEl
	);
}
const e = React.createElement
const tweetEl = document.getElementById('tweetme')
if(tweetEl){
	console.log(tweetEl.dataset)
	ReactDOM.render(
	    e(TweetComponent,tweetEl.dataset),tweetEl
	);
}


const tweetfd = document.getElementById('tweetmeFeed')
if(tweetfd){
	ReactDOM.render(
	  <React.StrictMode>
	    <FeedComponent  />
	  </React.StrictMode>,tweetfd
	);
}


const sea = document.getElementById('search')
if(sea){
	ReactDOM.render(
	  <React.StrictMode>
	    <SearchComponent />
	  </React.StrictMode>,sea
	);
}



const tweetDetail= document.querySelectorAll('.tweet-detail')

tweetDetail.forEach((container)=>{
	ReactDOM.render(
	   e(TweetDetailComponent,container.dataset),container
	);
})

const ProfileDetail= document.querySelectorAll('.profile-detail')

ProfileDetail.forEach((container)=>{
	ReactDOM.render(
	   e(ProfileBadge,container.dataset),container
	);
})



// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
