import React,{useState,useEffect} from 'react'
import {loaddetailprofile,loadFollowing} from './lookup'
import numeral from 'numeral'
import {DisplayCount} from './utils'


const UserProfile=({user,didToggle,Loading})=>{
	var action = user.is_following ? 'UnFollow' : 'Follow'
	if(Loading === false){
		action = '...Loading'
	}
	const handleClick=(event)=>{
		event.preventDefault()
		if(Loading === true){
			didToggle(action.toLowerCase())
		}
	}
	return (
	<div className='my-2'>
	<p>
        <span className=' pointer px-3 py-2 rounded-circle bg-dark text-white'>{user.username[0]}</span>{user.first_name}{" "}{user.last_name}{" "}@{user.username}
    </p>
    <p>
    	Followers <DisplayCount>{user.follower_count}</DisplayCount>
    </p>
    <p>
        Following <DisplayCount>{user.following_count}</DisplayCount>
    </p>
    <p>
    	{user.bio}
    </p>
    <p>
    	{user.location}
    </p>
    <button className='btn btn-primary' onClick={handleClick}>{action}</button>
	</div>
	)
}


export function ProfileBadge({username}){
	const [didLookup,setDidLookup] = useState(false)
	const [profile,setProfile] = useState(null)
	const [Loading,setLoading] = useState(true)
	useEffect(()=>{
		if(didLookup===false){
			console.log('in')
			loaddetailprofile(username,(res,status)=>{
				if(status === 200){
					setProfile(res)
				}
				else{
					alert('error finding your profile')
				}
			})
			setDidLookup(true)
		}
	},[didLookup,username])
	console.log('profile',profile)
	const didToggle=(action)=>{
		console.log('action',action)
		setLoading(false)
		loadFollowing(username,action,(res,status)=>{
			if(status===200){
				setLoading(true)
				setProfile(res)
			}
		})
	}
	return profile === null ? null : <UserProfile user = {profile} didToggle={didToggle} Loading={Loading} />
}