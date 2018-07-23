import React,{Component} from 'react';
import "../styles.css"

import { BrowserRouter as Router, Route, Link } from "react-router-dom";




class StudentList extends Component {
    render() {    
        return(
            <React.Fragment>
            <div>
                <h2>Students List</h2>
                  {
                    <table>    
                     <tr><th>Name</th><th>Email</th><th>Db Folder</th></tr>
                     {
                            
                            this.props.studentsList && this.props.studentsList.map(student => (
                                <tr> 
                                    {
                                        console.log(student.id)
                                    }      
                                
                                <td><Link key={student.id} to={`/college/${student.college}/students/${student.id}/`}>{student.name}</Link></td>
                                
                                <td>{student.email}</td>
                                <td>{student.db_folder}</td>
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
  
export default StudentList