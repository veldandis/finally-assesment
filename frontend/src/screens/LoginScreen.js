import React, { useState,useEffect } from 'react'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'
import { login } from '../actions/userActions'

function LoginScreen() {
  
  const [email,setEmail] = useState('');
  const [password,setPassword] = useState('');
   
    return (
    <div>LoginScreen</div>
  )
}

export default LoginScreen