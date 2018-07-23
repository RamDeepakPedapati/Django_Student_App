import React,  { Component }from 'react';
import StudentDetail from './StudentDetail.js'
import { BrowserRouter as Router, Route,  Switch } from "react-router-dom";
import StudentList from './StudentList.js'

class CollegeDetail extends Component {
    constructor(props){
      super(props);
      this.state = {
        studentsList: null
      };
    }  
    
componentDidMount() {
    var url="http://localhost:8000/api/v1/college/"+this.props.match.params.id+"/students/"
    console.log(url)    
    fetch("http://localhost:8000/api/v1/college/"+this.props.match.params.id+"/students/")

      .then(response => response.json())
      .then(responseJson => {
        this.setState({ studentsList: responseJson });
        console.log(this.state.studentsList)
      }).catch(e => {
        console.log(e);
        console.log("Error occured in second catch");
      });
  }
render(){
        const { title } = this.props;
        
        return (
          <React.Fragment>
            <Router>            
                <Switch >
                <Route exact path="/college/:id/">
                    <StudentList studentsList={this.state.studentsList}/>
                </Route>
                <Route
                  exact
                  path="/college/:id/students/:id1/"  
                  component={
                    (props)=>
                    <StudentDetail student = { this.state.studentsList ? this.state.studentsList.filter(elem => elem.id === 61) : {}} {...props}/>
                  }>
                </Route>
                </Switch>
            </Router>
          </React.Fragment>
        );
    }
}










// const CollegeDetail=({college=this.props.college})=>(
//     <div>
//         <h3>{college.name}</h3>
//         <p> Location -{college.location}<br/>
//         Contact={college.contact}
//         </p>
//     </div>
// )


export default CollegeDetail;