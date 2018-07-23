import React,{Component} from 'react';
import "../styles.css"
// import '../App.css';

import { BrowserRouter as Router, Route, Link } from "react-router-dom";



class CollegeList extends Component {
    render() {    
        return(
            <React.Fragment>
            <div>
                <h2>College List</h2>
                  {
                    <table>
                     <tr><th>Name</th><th>Acronym</th><th>Location</th></tr>
                     {
                            this.props.collegesList && this.props.collegesList.map(college => (
                                <tr>       
                                <td><Link key={college.id} to={`/college/${college.id}/`}>{college.name}</Link></td>
                                <td>{college.acronym}</td>
                                <td>{college.location}</td>
                                </tr>
                                )
                            )
                     }
                    </table>
                  }
          </div>
          </React.Fragment>
  
  
        );
    };
    
};
  
export default CollegeList
