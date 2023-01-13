import { useState, useEffect } from "react";
import axiosInstance from "../API";
import { Navigate } from "react-router-dom";

const ViewCompany = () => {

    const [companies, setCompanies] = useState([])
    
    useEffect(() => {
        refreshCompanies();
    }, []);

    const refreshCompanies = () => {
      axiosInstance.get("companies/")
        .then((res) => {
            setCompanies(res.data.results);
        })
        .catch(console.error);
    }


    const onDelete = (id) => {
        axiosInstance.delete(`companies/${id}/`).then((res) => refreshCompanies());
    };

    function selectCompany(id) {
        let item = companies.filter((company) => company.id === id)[0];
        return (
            <Navigate to="/addcompany" replace={true} item={item} />
        )
    }

    return (
        <div className="bg-light text-dark text-center" style={{backgroundColor:'#282c34', minHeight:'82vh'}}>
            <h2>Liste des entreprises</h2>
        <table className="container table col-md-8 mt-5">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Nom</th>
              <th scope="col">Catégorie</th>
              <th scope="col">Ville</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            {companies.map((company) => {
                  return (
                    <tr key={company.id}>
                      <th scope="row">{company.id}</th>
                      <td>{company.legal_name}</td>
                      <td>{company.category.name}</td>
                      <td>{company.city}</td>
                      <td>
                        <i
                          className="fa fa-pencil-square text-primary d-inline"
                          aria-hidden="true"
                          onClick={() => selectCompany(company.id)}
                        ></i>
                        <i
                          className="fa fa-trash-o text-danger d-inline mx-3"
                          aria-hidden="true"
                          onClick={() => onDelete(company.id)}
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

export default ViewCompany;