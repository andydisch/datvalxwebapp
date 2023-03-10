import { NavLink } from "react-router-dom";
import "./Component.css";


const Navbar = () => {
  return (
    <>
      <div className="nav">
        <div className="nav-menu">
          <NavLink className="nav-link" to="/futureproject">
            Alerts
          </NavLink>
          <NavLink className="nav-link" to="http://localhost:8000/admin/">
            Config
          </NavLink>
        </div>
      </div>
    </>
  );
};

export default Navbar;