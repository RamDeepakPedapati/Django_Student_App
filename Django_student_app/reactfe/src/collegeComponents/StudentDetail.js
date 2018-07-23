import React from 'react';




const StudentDetail=({student=this.props.student})=>(
    <div>
        {student.id}
        <h3>{student.name}</h3>
        <p>DB Folder={student.db_folder}<br/>
        Mail={student.email}
        </p>
    </div>
)


export default StudentDetail;