import React,{Component} from 'react';
import "../styles.css"

class InputEx extends Component{
	state={name:'',pass:''};


saveName=(event)=>
{
	const {target: {value}} = event;
	this.setState({name:value});
}

savePass=(event)=>
{
	const {targe: {value}} =event;
	this.setState({
	pass:value
	})
}

submit=(e) => {
	const {name,pass}=this.state;
	fetch("http://locathost:8000/api/v1/token/",{
	mehtod:'post',
	header:{
	'Content-type': "application/x-www-fore-urlencoded; charset-UTF-8"
	},
	body: 'username=${name} & password =${pass}'
	}).then(res=>res.json()).then(response => {
		console.log('response',response);
	})

}
render()
{
    return(<div>
        <input onChange={this.saveName} name='name'/>
        <br/>
        <input onChange={this.savePass} name='pass'/>
        <br/>
        <button onClick={this.submit} >Submit </button>
    </div>)
}

}


export default InputEx