
import { useState } from "react";
import axios from "axios";


function App() {


  const [mission, setMission] = useState("");
  const [goal, setGoal] = useState("");
  const [constraints, setConstraints] = useState("");

  const [result, setResult] = useState("");

  const [loading, setLoading] = useState(false);



  async function analyzeMission() {

    try {

      setLoading(true);


      const response = await axios.post(
        "http://localhost:8000/mission/analyze",
        {
          mission: mission,
          goal: goal,
          constraints: constraints
        }
      );


      setResult(
        response.data.analysis
      );


    } catch (error) {

      setResult(
        "Error connecting to SpaceMission AI backend."
      );

    }


    setLoading(false);

  }




  return (

    <div
      style={{
        padding: "40px",
        fontFamily: "Arial",
        maxWidth: "900px",
        margin: "auto"
      }}
    >


      <h1>
        🚀 SpaceMission AI
      </h1>


      <h3>
        AI-powered space mission planning assistant
      </h3>



      <hr />



      <h2>
        Mission Information
      </h2>



      <label>
        Mission Target
      </label>

      <br />

      <input

        style={{
          width: "80%",
          padding: "10px"
        }}

        placeholder="Example: Europa Exploration Mission"

        value={mission}

        onChange={
          (e) => setMission(e.target.value)
        }

      />



      <br /><br />



      <label>
        Mission Objective
      </label>

      <br />


      <textarea

        rows="4"

        style={{
          width: "80%",
          padding: "10px"
        }}

        placeholder="Example: Search for possible water resources"

        value={goal}

        onChange={
          (e) => setGoal(e.target.value)
        }

      />



      <br /><br />



      <label>
        Mission Constraints
      </label>

      <br />


      <textarea

        rows="4"

        style={{
          width: "80%",
          padding: "10px"
        }}

        placeholder="Example: Radiation, limited energy, communication delay"

        value={constraints}

        onChange={
          (e) => setConstraints(e.target.value)
        }

      />



      <br /><br />



      <button

        onClick={analyzeMission}

        style={{
          padding: "12px 25px",
          cursor: "pointer"
        }}

      >

        {loading
          ? "Analyzing..."
          : "Analyze Mission"}

      </button>




      <hr />



      <h2>
        AI Analysis Result
      </h2>



      <pre

        style={{
          whiteSpace: "pre-wrap",
          background: "#f5f5f5",
          padding: "20px",
          borderRadius: "10px"
        }}

      >

        {result}

      </pre>



    </div>

  );


}


export default App;
