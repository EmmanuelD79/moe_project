import { useRef, useState} from "react";
import { Button, Form, Container, Col, Row } from "react-bootstrap";
import { useContext } from 'react';
import AuthContext from "../utils/context";
import axiosInstance from "../API";
import ErrorForms from "./ErrorForms";
import { useNavigate } from "react-router-dom";


const AddContact = () => {

  const navigate = useNavigate()

  const { user } = useContext(AuthContext);
  const [error, setError] = useState(null)

  const email = useRef("")
  const birthday = useRef("")
  const is_private = useRef(false)
  const first_name = useRef("")
  const last_name = useRef("")
  const title = useRef("")
  const company = useRef("")
  const sub_type = useRef("")
  const phone = useRef("")
  const mobile = useRef("")
  const address = useRef("")
  const zip_code = useRef("")
  const city = useRef("")
  const country = useRef("")
  const url = useRef("")
  const photo_original = useRef(null)

  const submitContact = async (newContact) => {
    let response = await axiosInstance.post("contacts/", newContact, {
      headers: {
        "Content-Type": "multipart/form-data",
      }
    });
    return response
  };

   
  const onSubmit = async () => {
    let newContact = {
      email: email.current.value,
      birthday: birthday.current.value,
      is_private: is_private.current.checked,
      first_name: first_name.current.value,
      last_name: last_name.current.value,
      title: title.current.value,
      company: company.current.value,
      sub_type: sub_type.current.value,
      phone: phone.current.value,
      mobile: mobile.current.value,
      address: address.current.value,
      zip_code: zip_code.current.value,
      city: city.current.value,
      country: country.current.value,
      url: url.current.value,
      photo_original: photo_original.current.files[0],
      owner_email: user?.email
    }
    try {
      let apiResponse = await submitContact(newContact);
      if (apiResponse===201){
        navigate('/contact');
      }
      } catch (e) {
        if (e.response.status===400){
          setError(e.response.data)
        }
      };
    };

  return (
      <Container className='py-4 bg-light text-dark w-50'>
            <h3 className="text-center pt-3">Ajouter un Contact</h3>
            <Form onSubmit={onSubmit} className="my-4 mx-4">
              <Row>
                  <Col sm={6}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Email</Form.Label>
                        <Form.Control
                          type="email"
                          placeholder="Email"
                          name='email'
                          ref={email}
                        />
                        <ErrorForms error={error?.email} />
                    </Form.Group>
                  </Col>
                  <Col sm={4}>
                    <Form.Group className="mb-3" controlId="formBasicBirthday">
                      <Form.Label>Anniversaire</Form.Label>
                      <Form.Control
                        type="date"
                        name='birthday'
                        ref={birthday}
                      />
                      <ErrorForms error={error?.birthday} />
                    </Form.Group>
                  </Col>
                  <Col sm={2}>
                    <Form.Group as={Row} className="mb-3" controlId="formBasicIsPrivate">
                        <Form.Label>Privé</Form.Label>
                          <Form.Check 
                            type="checkbox" 
                            name='is_private'
                            ref={is_private}
                          />
                          <ErrorForms error={error?.is_private} />
                    </Form.Group>
                  </Col>
              </Row>
              <Row>
                <Form.Group as={Col} className="mb-3" controlId="formBasicFirstName">
                  <Form.Label>Prénom</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Prénom"
                    name='first_name'
                    ref={first_name}
                  />
                  <ErrorForms error={error?.first_name} />
                </Form.Group>
                <Form.Group  as={Col} className="mb-3" controlId="formBasicLastName">
                  <Form.Label>Nom</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Nom"
                    name='last_name'
                    ref={last_name}
                  />
                  <ErrorForms error={error?.last_name} />
                </Form.Group>
              </Row>
              <Form.Group className="mb-3" controlId="formBasicTitle">
                <Form.Label>Titre</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Titre"
                  name='title'
                  ref={title}
                />
                <ErrorForms error={error?.title} />
              </Form.Group>
              <Row>
                <Form.Group sm={8} as={Col} className="mb-3" controlId="formBasicCompany">
                  <Form.Label>Société</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Société"
                    name='company'
                    ref={company}
                  />
                  <ErrorForms error={error?.company} />
                </Form.Group>
                  <Form.Group as={Col} className="mb-3" controlId="formBasicType">
                  <Form.Label>Catégorie</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Catégorie"
                    name="sub_type"
                    ref={sub_type}
                  />
                  <ErrorForms error={error?.sub_type} />
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
                <Form.Group as={Col} className="mb-3" controlId="formBasicZipCode">
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
              <Form.Group className="mb-3" controlId="formBasicUrl">
                <Form.Label>URL</Form.Label>
                <Form.Control
                  type="text"
                  name='url'
                  ref={url}
                />
                <ErrorForms error={error?.url} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="formBasicPhoto">
                <Form.Label>Photo</Form.Label>
                <Form.Control
                  type="file"
                  name='photo_original'
                  ref={photo_original}
                />
                <ErrorForms error={error?.photo_original} />
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
    );
};

export default AddContact;
