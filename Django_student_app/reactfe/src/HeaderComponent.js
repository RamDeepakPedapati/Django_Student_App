import React,{Component} from 'react';
import "./styles.css"

class Header extends Component{
    state={
        isLoggedIn:this.props.isLoggedIn
    }
    toggleLoggedIn=() =>
    {
        this.setState(prev=>({isLoggedIn : !prev.isLoggedIn}))
    }
    render()
    {
    const {title} = this.props;
    const {isLoggedIn} = this.state;
    return (
    <div className="header">
    <h2>{title}</h2>
    <button className="menu" onClick={this.toggleLoggedIn}>
        {
            isLoggedIn ?
            <span>Logout</span>
            :<span>Login</span>
        }
    </button>
    </div>
    )
}
}



export default Header