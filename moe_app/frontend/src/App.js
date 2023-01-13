import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Welcome from './components/Welcome';
import Viewcontacts from './components/ViewContacts';
import AddContact from './components/AddContact';
import Header from './components/Header';
import Footer from './components/Footer';
import ProtectedRoute from './components/ProtectedRoute';
import Register from './components/Register';
import Company from './components/Company';
import AddCompany from './components/AddCompany';

function App() {

  return (
    <>
      <Header />
      <BrowserRouter>
        <Routes>
            <Route index element={<Welcome />} />
            <Route path="login" element={
                <ProtectedRoute accessBy="non-authenticated">
                  <Login />
                </ProtectedRoute>}/>
            <Route path="register" element={
                <ProtectedRoute accessBy="non-authenticated">
                  <Register />
                </ProtectedRoute>}/>
            <Route path="dashboard" element={
                <ProtectedRoute accessBy="authenticated">
                  <Dashboard />
                </ProtectedRoute>} />
            <Route path="addcontact" element={
                <ProtectedRoute accessBy="authenticated">
                  <AddContact />
                </ProtectedRoute>} />
            <Route path="contact" element={
                <ProtectedRoute accessBy="authenticated">
                    <Viewcontacts />
                </ProtectedRoute>} />
            <Route path="company" element={
                <ProtectedRoute accessBy="authenticated">
                    <Company />
                </ProtectedRoute>} />
            <Route path="addcompany" element={
                <ProtectedRoute accessBy="authenticated">
                    <AddCompany />
                </ProtectedRoute>} />
            <Route path="addcontact" element={
                <ProtectedRoute accessBy="authenticated">
                    <AddContact />
                </ProtectedRoute>} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;
