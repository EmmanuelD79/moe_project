import { useState, useEffect } from "react";
import { Form } from "react-bootstrap";
import axiosInstance from "../API";
import { Navigate } from "react-router-dom";


const Viewcontacts = () => {

    const [contacts, setContacts] = useState([])
    
    useEffect(() => {
        refreshContacts();
    }, []);

    const refreshContacts = () => {
      axiosInstance.get("contacts/")
        .then((res) => {
            setContacts(res.data.results);
        })
        .catch(console.error);
    }

    const onDelete = (id) => {
        axiosInstance.delete(`contacts/${id}/`).then((res) => refreshContacts());
    };

    function selectContact(id) {
        let item = contacts.filter((contact) => contact.id === id)[0];
        return (
            <Navigate to="/addContact" replace={true} item={item} />
        )
        
    }

    return (
        <div className="bg-light text-dark text-center" style={{backgroundColor:'#282c34', minHeight:'82vh'}}>
            <h2>Liste des contacts</h2>
        <table className="container table col-md-8 mt-5">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Prénom</th>
              <th scope="col">Nom</th>
              <th scope="col">Société</th>
              <th scope="col">Privé</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            {contacts.map((contact) => {
                  return (
                    <tr key={contact.id}>
                      <th scope="row">{contact.id}</th>
                      <td>{contact.first_name}</td>
                      <td>{contact.last_name}</td>
                      <td>{contact.company}</td>
                      <td><Form.Check 
                          type="checkbox" 
                          readOnly
                          checked={contact.is_private}/>
                      </td>
                      <td>
                        <i
                          className="fa fa-pencil-square text-primary d-inline"
                          aria-hidden="true"
                          onClick={() => selectContact(contact.id)}
                        ></i>
                        <i
                          className="fa fa-trash-o text-danger d-inline mx-3"
                          aria-hidden="true"
                          onClick={() => onDelete(contact.id)}
                        ></i>
                      </td>
                    </tr>
                  );
                })}
          </tbody>
        </table>
      </div>
    )
}

export default Viewcontacts