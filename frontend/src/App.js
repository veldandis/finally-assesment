import { Container } from 'react-bootstrap'
import { HashRouter as Router, Route } from 'react-router-dom'

import Header from './components/Headers'
import Footer from './components/Footers'

import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'
import LoginScreen from './screens/LoginScreen'

function App() {
  return (
    <Router>
      <Header />
      <main className='py-3'>
        <Container>

            <Route path='/' component={HomeScreen} exact />
            <Route path='/product/:id' component={ProductScreen} />
            <Route path='/login' component={LoginScreen} />
          
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
