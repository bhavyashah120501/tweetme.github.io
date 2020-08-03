import React from 'react'
import {useState,useEffect} from 'react'
import {getlist} from './lookup'
import './search.css'


const list=(val)=>{
	
	const handleLink=(event)=>{
		
		window.location.href = `/profile/${val}`
	}
	return <li className='pointer list' onClick={handleLink}> {val} </li>
}


const display=(match)=>{
	
	return (
		<div className='col-7 col-sm-12'>
			<ul className='list-group'>
			{
				match.length === 0 ? <p> No Match</p> : match.map((val,index)=> list(val) )
			}
			</ul> 
		</div>
		)
}

const searchBox=(users,search)=>{
	
	const match = users.filter((user)=>{
		if(user.toLowerCase().includes(search.toLowerCase())){
			return user
		}
	})
	return display(match)
}


export const SearchComponent=()=>{
	
	var searchRef = React.createRef()
	const [users,setUsers] = useState([])
	const [didSet,setdidSet] = useState(false)
	const [changed,setdidChange] = useState(false)
	const [search,setSearch] = useState()
	useEffect(()=>{
		if(!didSet){
			setdidSet(true)
			getlist((res,status)=>{
				setUsers(res.user)
			})
		}
	})
	const handleInput=(event)=>{
		event.preventDefault()
		
		setSearch(searchRef.current.value)
		setdidChange(true)
	}
	const handleBlur=(event)=>{
		setdidChange(false)
	}
	return (
		<div>
		<div className='row'>
		<input type='text' ref = {searchRef} onBlur={handleBlur} className='form-control col-7 col-sm-12' placeholder='Search' onChange={handleInput} />
		</div>
		<div className='row'>
		{changed && searchBox(users,search)}
		</div>
		</div>
		)
}


