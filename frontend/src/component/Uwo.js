import { Component } from "react";
import "./Component.css";
import axios from "axios";
import Navbar from "./UwoNavbar.js";
import low_battery from './../battery-low-icon.svg';
import no_data from './../data-check-icon.svg';
import psr_qos from './../psr-qos-icon.svg';
import default_icon from './../default-icon.svg';
import rain_sum_icon from './../rain-sum-icon.svg';


function displayIcon(itemType){
  if (itemType==="last_data") {
    return (
      <img className="center-img" src={no_data} alt="last-data" />);
  } else if (itemType === "battery_level") {
    return (
      <img className="center-img" src={low_battery} alt="low-battery" />);
  } else if (itemType === "prs_qos") {
    return (
      <img className="center-img" src={psr_qos} alt="psr-qos" />);
  } else if (itemType === "rain_sum") {
    return (
      <img className="center-img" src={rain_sum_icon} alt="rain-sum" />);
  } else {
    return (
      <img className="center-img" src={default_icon} alt="default-icon" />);
  }
};

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString("de-CH", {
    weekday: "long",
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
  });
};

class Table extends Component {
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

  activateAlarm = (item) => {
    item["acknowledged_time"] = null;
    item["status"] = "active";
    item["time_of_occurrence"] = new Date(item["time_of_occurrence"]);
    item["created_time"] = new Date(item["created_time"]);
    axios
      .put(`/api/alarms/${item.id}/`, item)
      .then((res) => this.refreshList());
  };

  clearAlarm = (item) => {
    var localTime = new Date();
    item["cleared_time"] = localTime;
    item["status"] = "cleared";
    item["time_of_occurrence"] = new Date(item["time_of_occurrence"]);
    item["created_time"] = new Date(item["created_time"]);
    axios
      .put(`/api/alarms/${item.id}/`, item)
      .then((res) => this.refreshList());
  };

  acknowledgeAlarm = (item) => {
    var localTime = new Date();
    item["acknowledged_time"] = localTime;
    item["status"] = "acknowledged";
    item["time_of_occurrence"] = new Date(item["time_of_occurrence"]);
    item["created_time"] = new Date(item["created_time"]);
    console.log(JSON.stringify(item));
    axios
      .put(`/api/alarms/${item.id}/`, item)
      .then((res) => this.refreshList());
  };

  
  handleClick = () => {
    this.state.sortActive = !this.state.sortActive
    this.refreshList();
  }

  handleChange = (e) => {
    this.state.searchInput = e.target.value.toLowerCase();
    this.refreshList();
  }


  renderActiveItems = () => {
    return this.state.activeList.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-right"
      >
        <div className="tab-alarm-text">
        {formatDate(item.time_of_occurrence)}
          <br />
          {item.source}
          <br />
          {item.alarming_fact === null? item.variable + ": " + item.type: item.variable + ": " + item.alarming_fact }
        </div>
        <div className="tab-icon">
        { displayIcon(item.type) }
        </div>
        <div className="tab-buttons">
        <button
            className="tab-btn btn btn-secondary"
            onClick={() => this.acknowledgeAlarm(item)}
          >
            Acknowledge
          </button>
          <button
            className="btn btn-dark"
            onClick={() => this.clearAlarm(item)}
          >
            Clear
          </button>
        </div>
      </li>
    ));
  };

  renderAcknowledgedItems = () => {
    return this.state.acknowledgedList.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span className="tab-alarm-text">
          {formatDate(item.time_of_occurrence)}
          <br />
          {item.source}
          <br />
          {item.variable + ": " + item.type}
        </span>
        <span>
          <button
            className="btn btn-secondary"
            onClick={() => this.activateAlarm(item)}
          >
            Activate
          </button>
          <button
            className="btn btn-dark"
            onClick={() => this.clearAlarm(item)}
          >
            Clear
          </button>
        </span>
      </li>
    ));
  };

  renderClearedItems = () => {
    return this.state.clearedList.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span className="tab-alarm-text">
          {formatDate(item.time_of_occurrence)}
          <br />
          {item.source}
          <br />
          {item.variable + ": " + item.type}
        </span>
      </li>
    ));
  };

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
            {this.renderActiveItems()}
          </ul>
          <div className="tab-alarm-title">Acknowledged</div>
          <ul className="list-group list-group-flush border-top-0">
            {this.renderAcknowledgedItems()}
          </ul>
          <div className="tab-alarm-title">Cleared</div>
          <ul className="list-group list-group-flush border-top-0">
            {this.renderClearedItems()}
          </ul>
        </div>
      </div>
      </>
    );
  }
}

export default Table;
