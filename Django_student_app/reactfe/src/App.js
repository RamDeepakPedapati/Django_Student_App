import React, { Component } from 'react';
import { BrowserRouter as Router, Route,  Switch } from "react-router-dom";

// import './App.css';

import CollegeList from './collegeComponents/collegelist.js';
import Header from './HeaderComponent.js';
import CollegeDetail from './collegeComponents/CollegeDetail.js';
import InputEx from './inputComponent/inputComponent.js'


class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      collegesList: null
    };
  }

componentDidMount() {

  fetch("http://localhost:8000/api/v1/college/")
    .then(response => response.json())
    .then(responseJson => {
      this.setState({ collegesList: responseJson });
    })
    .catch(e => {
      console.log(e);
      console.log("Error occured in second catch");
    });
}

componentWillUnmount () {
  this.state.responseJson = this.state.responseJson.destroy();
}


  render(){
      const { title } = this.props;
      return (
        <React.Fragment>
          <Header title="Mentor App" isLoggedIn={true}/>
          <Router>            
              <Switch >
              <Route exact path="/log">
                <InputEx/>
              </Route>
              <Route exact path="/">
                <CollegeList collegesList={this.state.collegesList}/>
              </Route>
              <Route
                exact
                path="/college/:id"
                component={
                  (props)=>
                  <CollegeDetail college={this.state.collegesList ? this.state.collegesList[props.match.params.id] : {}} {...props}/>
                }>
              </Route>
              </Switch>
          </Router>
        </React.Fragment>
      );
  }
}

export default App;