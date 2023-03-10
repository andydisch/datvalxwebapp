import { NavLink } from "react-router-dom";
import "./Component.css";


const Sitebar = () => {
  return (
    <>
      <div className="nav-site">
        <div className="nav-menu">
          <NavLink className="nav-link" to="/uwo">
            UWO
          </NavLink>
          <NavLink className="nav-link" to="/viererfeld">
            Viererfeld
          </NavLink>
          <NavLink className="nav-link" to="/futureproject">
            Future Project
          </NavLink>
        </div>
        <div
          className="nav-container col-md-9 ml-auto"
        >
          <a className="nav-containertext" href={"https://www.eawag.ch/en/department/sww/projects/urbanhydrologisches-feldlabor/"}>
            datValX
          </a>
          <div className="nav-origintext">by adisch</div>
        </div>
      </div>
    </>
  );
};

export default Sitebar;
