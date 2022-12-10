import React, { useState,useEffect } from 'react'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Rating from '../components/Rating'
import { listProductDetails } from '../actions/productActions'
import products from '../products'
import { listProducts } from '../actions/productActions'


function ProductScreen ({ match }) {
  const [qty, setQty] = useState(1)
  const dispatch = useDispatch()
  //const params = useParams();
  const productDetails = useSelector(state => state.productDetails);

  console.log("The received productDetails in the ProduCtScreen is:");
  console.log(productDetails);
  
  

  useEffect(() => {
      dispatch(listProductDetails(match.params.id))
  },[dispatch, match])

  const { loading, error, product } = productDetails
  console.log("The value of the received product in the ProductScreen js file is:");
  console.log(product);
  //const product = {}
  return (
    <div>
    
      <Link to='/' className='btn btn-light my-3'> Go Back </Link>
      <Row>
        <Col md={6}>
          <h1>Name: {product.name}</h1>
        </Col>

        <Col md={3}>

          <ListGroup variant="flush">

            <ListGroup.Item>
              <h3>Name: {product.name}</h3>
            </ListGroup.Item>

            <ListGroup.Item>
              <h3>Brand: {product.brand}</h3>
            </ListGroup.Item>
          
          </ListGroup>
        
        </Col>
      </Row>
    </div>);
};

export default ProductScreen