import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DatValX from "./component/DatValX.js";
import Uwo from "./component/Uwo.js";
import Viererfeld from "./component/Viererfeld.js";
import FutureProject from "./component/FutureProject";
import Sitebar from "./component/Sitebar.js";
import "./App.css";

const App = () => {
  return (
    <Router>
      <Sitebar />
      <Routes>
        <Route path="/" element={<DatValX />} />
        <Route path="/uwo" element={<Uwo />} />
        <Route path="/viererfeld" element={<Viererfeld />} />
        <Route path="/futureproject" element={<FutureProject />} />
      </Routes>
    </Router>
  );
};

export default App;
