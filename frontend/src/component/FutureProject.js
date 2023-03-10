import { Component } from "react";
import "./Component.css";
import axios from "axios";
import Navbar from "./FutureProjectNavbar.js";

class FutureProject extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeList: [],
      acknowledgedList: [],
      clearedList: [],
      sortActive: false,
      searchInput: "",
    };
  }

  componentDidMount() {
    this.refreshList();
  }


  customFilterFunction = (searchinput) => {
    return function(element) {
        return element.source.includes(searchinput) || element.alarming_fact.includes(searchinput) || element.variable.includes(searchinput);
    }
  }

  refreshList = () => {
    if (this.state.sortActive) {
      axios
        .get("/api/alarms", { params: { status: "active", oldest_first: true } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ activeList: res}));
      axios
        .get("/api/alarms", { params: { status: "acknowledged", oldest_first: true } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ acknowledgedList: res }));
      axios
        .get("/api/alarms", { params: { status: "cleared", oldest_first: true } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ clearedList: res }));
    } else {
      axios
        .get("/api/alarms", { params: { status: "active" } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ activeList: res}));
      axios
        .get("/api/alarms", { params: { status: "acknowledged" } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ acknowledgedList: res }));
      axios
        .get("/api/alarms", { params: { status: "cleared" } })
        .then((res) => { return res.data.filter(this.customFilterFunction(this.state.searchInput) ); } )
        .then((res) => this.setState({ clearedList: res }));
    }
  };
  
  handleClick = () => {
    this.state.sortActive = !this.state.sortActive
    this.refreshList();
  }

  handleChange = (e) => {
    this.state.searchInput = e.target.value.toLowerCase();
    this.refreshList();
  }

  render() {
    return (
      <>
      <Navbar site="uwo"/>
      <div className="col-md-6 col-sm-10 mx-auto p-0">
        <div className="input-bar">
          <input className="input-searchbar" placeholder=" Filter ... " onChange={(e) => this.handleChange(e)} />
          <label className="input-checkbox">
            Oldest on top: <input className="input-checkbox-box" type="checkbox" checked={ this.state.sortActive } onChange={() => this.handleClick()} />                  
          </label>
        </div>
        <div className="card">
          <div className="tab-alarm-title">Active</div>
          <ul className="list-group list-group-flush border-top-0">
            {}
          </ul>
          <div className="tab-alarm-title">Acknowledged</div>
          <ul className="list-group list-group-flush border-top-0">
            {}
          </ul>
          <div className="tab-alarm-title">Cleared</div>
          <ul className="list-group list-group-flush border-top-0">
            {}
          </ul>
        </div>
      </div>
      </>
    );
  }
}

export default FutureProject;