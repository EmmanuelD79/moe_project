import { Container, Row, Col , Form, Button, FormSelect } from "react-bootstrap";
import { useRef, useState, useContext, useEffect} from "react";
import AuthContext from "../utils/context";
import axiosInstance from "../API";
import ErrorForms from "./ErrorForms";
import { useNavigate } from "react-router-dom";

const AddCompany = () => {

    const navigate = useNavigate()

    const { user } = useContext(AuthContext);

    const [error, setError] = useState(null)
    const [categories, setcategories] = useState([])
    const [category, setCategory] = useState()

    const legal_name = useRef("")
    const identification_type = useRef("")
    const identification_code = useRef("")
    const status = useRef("")
    const phone = useRef("")
    const mobile = useRef("")
    const address = useRef("")
    const zip_code = useRef(null)
    const city = useRef("")
    const country = useRef("")
    const website = useRef("")


    useEffect(() => {
        refreshCategories();
    }, []);

    const refreshCategories = () => {
    axiosInstance.get("companycategories/")
        .then((res) => {
            setcategories(res.data.results);
        })
        .catch(console.error);
    }

    const submitCompany = async (newCompany) => {
        let response = await axiosInstance.post("companies/", newCompany, {
        });
        return response
        };

    const onCategory = (e) => {
        setCategory(e.target.value)
    }

    const onSubmit = async () => {
    let newCompany = {
        legal_name: legal_name.current.value,
        identification_type: identification_type.current.value,
        identification_code: identification_code.current.value,
        category: category,
        status: status.current.value,
        phone: phone.current.value,
        mobile: mobile.current.value,
        address: address.current.value,
        zip_code: zip_code.current.value,
        city: city.current.value,
        country: country.current.value,
        website: website.current.value,
        owner_email: user?.email
    }
    try {
        let apiResponse = await submitCompany(newCompany);
        if (apiResponse===201){
            navigate('/company');
        }} catch (e) {
        if (e.response.status===400){
            setError(e.response.data)
        }};
    }
        return (
            <div>
                <Container className='py-4 bg-light text-dark w-50'>
                    <h3 className="text-center pt-3">Ajouter une société</h3>
                    <Form className="my-4 mx-4">
                        <Row>
                            <Form.Group as={Col} className="mb-3" controlId="formLegalName">
                                <Form.Label>Nom commercial</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Nom commercial"
                                    name='legal_name'
                                    ref={legal_name}
                                />
                                <ErrorForms error={error?.legal_name} />
                            </Form.Group>
                            <Form.Group sm={4} as={Col} className="mb-3" controlId="formIdType">
                                <Form.Label>Forme juridique</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Forme juridique"
                                    name='identification_type'
                                    ref={identification_type}
                                />
                                <ErrorForms error={error?.identification_type} />
                            </Form.Group>
                        </Row>
                        <Form.Group className="mb-3" controlId="formLegalName">
                            <Form.Label>Siret</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Siret"
                                name='identification_code'
                                ref={identification_code}
                            />
                            <ErrorForms error={error?.identification_code} />
                        </Form.Group>
                        <Row>
                            <Form.Group as={Col} className="mb-3" controlId="formCategory">
                                <Form.Label>Catégorie</Form.Label>
                                <Form.Control as={FormSelect} name='category' onChange={onCategory}>
                                    <option>---</option>
                                    {categories.map((category) => {
                                        return (
                                            <option key={category.id} value={category.id}>{category.name}</option>
                                        )})
                                    };

                                </Form.Control>
                                <ErrorForms error={error?.category} />
                            </Form.Group>
                            <Form.Group as={Col} className="mb-3" controlId="formStatus">
                                <Form.Label>Statut</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Statut"
                                    name='status'
                                    ref={status}
                                />
                                <ErrorForms error={error?.status} />
                            </Form.Group>
                        </Row>
                        <Row>
                            <Form.Group as={Col} className="mb-3" controlId="formBasicPhone">
                                <Form.Label>Téléphone</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Téléphone"
                                    name='phone'
                                    ref={phone}
                                />
                                <ErrorForms error={error?.phone} />
                            </Form.Group>
                            <Form.Group as={Col} className="mb-3" controlId="formBasicMobile">
                                <Form.Label>Mobile</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Mobile"
                                    name='mobile'
                                    ref={mobile}
                                />
                                <ErrorForms error={error?.mobile} />
                            </Form.Group>
                        </Row>
                        <Form.Group className="mb-3" controlId="formBasicAddress">
                            <Form.Label>Adresse</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Adresse"
                                name='address'
                                ref={address}
                            />
                            <ErrorForms error={error?.address} />
                        </Form.Group>
                        <Row>
                            <Form.Group as={Col} className="mb-3" controlId="formCompanyZipCode">
                                <Form.Label>Code Postal</Form.Label>
                                <Form.Control
                                    type="text"
                                    placeholder="Code Postal"
                                    name='zip_code'
                                    ref={zip_code}
                                />
                                <ErrorForms error={error?.zip_code} />
                            </Form.Group>
                            <Form.Group sm={6} as={Col} className="mb-3" controlId="formBasicCity">
                                <Form.Label>Ville</Form.Label>
                                <Form.Control
                                type="text"
                                placeholder="Ville"
                                name='city'
                                ref={city}
                                />
                                <ErrorForms error={error?.city} />
                            </Form.Group>
                            <Form.Group as={Col} className="mb-3" controlId="formBasicCountry">
                                <Form.Label>Pays</Form.Label>
                                <Form.Control
                                type="text"
                                placeholder="Pays"
                                name='country'
                                ref={country}
                                />
                                <ErrorForms error={error?.country} />
                            </Form.Group>
                        </Row>
                        <Form.Group as={Col} className="mb-3" controlId="formWebsite">
                            <Form.Label>Url</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="website"
                                name='website'
                                ref={website}
                            />
                            <ErrorForms error={error?.website} />
                        </Form.Group>
                        <Form.Group className="d-flex justify-content-end py-4">
                            <Button className="btn-lg" variant="light" type="button">
                                Annuler
                            </Button>
                            <Button className="ms-2 btn-lg" variant="warning" type="button" onClick={onSubmit}>
                                Ajouter
                            </Button>
                    </Form.Group>
                    </Form>
                </Container>
            </div>
        )
}

export default AddCompany;