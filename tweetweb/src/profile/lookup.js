import {backendLookup} from '../lookup'
import React from 'react'

export function loaddetailprofile(username,callback){
  let endpoint = `/profile/${username}`
  backendLookup('GET',endpoint,callback)
}


export function loadFollowing(username,action,callback){
	const endpoint = `/profile/${username}/follow`
	console.log(action,'action')
	const data={
		'action': action
	}
	backendLookup('POST',endpoint,callback,data)
}