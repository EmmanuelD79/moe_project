import { FaFacebook } from 'react-icons/fa';
import { FaTwitter } from 'react-icons/fa';
import { FaGoogle } from 'react-icons/fa';
import { FaInstagram } from 'react-icons/fa';
import { FaLinkedin } from 'react-icons/fa';
import { FaGithub } from 'react-icons/fa';
// import { FaHome } from 'react-icons/fa';
// import { FaEnvelope } from 'react-icons/fa';
// import { FaPhone } from 'react-icons/fa';
// import { FaPrint } from 'react-icons/fa';



function Footer() {

    return (
        <footer className="text-center text-lg-start bg-light text-muted">
            <section className="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">

                <div className="me-5 d-none d-lg-block">
                    © 2023 Copyright:
                    <a className="text-reset fw-bold" href="https://lelab-dev.freeboxos.fr/">LELAB-DEV</a>
                </div>

                <div>
                <a href="/" className="me-4 text-reset">
                    <FaFacebook />
                </a>
                <a href="/" className="me-4 text-reset">
                   <FaTwitter />
                </a>
                <a href="/" className="me-4 text-reset">
                    <FaGoogle />
                </a>
                <a href="/" className="me-4 text-reset">
                    <FaInstagram />
                </a>
                <a href="/" className="me-4 text-reset">
                    <FaLinkedin />
                </a>
                <a href="/" className="me-4 text-reset">
                    <FaGithub />
                </a>
                </div>

            </section>

            {/* <section className="">
                <div className="container text-center text-md-start mt-5">

                <div className="row mt-3">

                    <div className="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">

                    <h6 className="text-uppercase fw-bold mb-4">
                        <i className="fas fa-gem me-3"></i>Company name
                    </h6>
                    <p>
                        Here you can use rows and columns to organize your footer content. Lorem ipsum
                        dolor sit amet, consectetur adipisicing elit.
                    </p>
                    </div>



                    <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">

                    <h6 className="text-uppercase fw-bold mb-4">
                        Products
                    </h6>
                    <p>
                        <a href="/" className="text-reset">Angular</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">React</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">Vue</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">Laravel</a>
                    </p>
                    </div>



                    <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">

                    <h6 className="text-uppercase fw-bold mb-4">
                        Useful links
                    </h6>
                    <p>
                        <a href="/" className="text-reset">Pricing</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">Settings</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">Orders</a>
                    </p>
                    <p>
                        <a href="/" className="text-reset">Help</a>
                    </p>
                    </div>



                    <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">

                    <h6 className="text-uppercase fw-bold mb-4">Contact</h6>
                    <p><FaHome className='me-3'/> New York, NY 10012, US</p>
                    <p>
                        <FaEnvelope className='me-3'/>
                        info@example.com
                    </p>
                    <p><FaPhone className='me-3' />+ 01 234 567 88</p>
                    <p><FaPrint  className='me-3'/> + 01 234 567 89</p>
                    </div>

                </div>

                </div>
            </section> */}

            {/* <div className="text-center p-4" style={{backgroundColor: 'rgba(0, 0, 0, 0.05)'}}>
                © 2021 Copyright:
                <a className="text-reset fw-bold" href="https://lelab-dev.freeboxos.fr/">LELAB-DEV</a>
            </div> */}
        </footer>
    );

}

export default Footer;