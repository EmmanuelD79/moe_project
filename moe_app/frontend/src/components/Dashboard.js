// import { Navigate } from "react-router-dom";
import { useContext } from 'react';
import AuthContext from "../utils/context";

const Dashboard = () => {

  const { user } = useContext(AuthContext);

    return (
        <div className="App-header">
            <p>Welcome to your Dashboard {user?.email}</p>
        </div>
    );

};

export default Dashboard;