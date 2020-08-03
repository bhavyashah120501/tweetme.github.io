import React from 'react'
import {backendLookup} from '../lookup'

export const getlist=(callback)=>{
	const endpoint = '/users'
	backendLookup('GET',endpoint,callback)
}