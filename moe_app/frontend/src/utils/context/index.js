import { createContext, useState } from "react";
import jwt_decode from "jwt-decode";
import axiosInstance from "../../API";
 
const AuthContext = createContext();
 
export const AuthContextProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    if (localStorage.getItem("tokens")) {
      let tokens = JSON.parse(localStorage.getItem("tokens"));
      return jwt_decode(tokens.access);
    }
    return null;
  });
 
  const login = async (payload) => {
    const apiResponse = await axiosInstance.post("login/", payload);
    localStorage.setItem("tokens",  JSON.stringify(apiResponse.data.token));
    setUser(jwt_decode(apiResponse.data.token.access));
    axiosInstance.defaults.headers['Authorization'] = `Bearer ${apiResponse.data.token.access}`;
  };

  const logout = async () => {
    // invoke the logout API call, for our NestJS API no logout API
 
    localStorage.removeItem("tokens");
    setUser(null);

  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );

};
 
export default AuthContext;