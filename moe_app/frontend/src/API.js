import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/';

const tokens = JSON.parse(localStorage.getItem("tokens"));

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: tokens ? `Bearer ${tokens.access}` : null ,
		'Content-Type': 'application/json',
	}, 
});

export default axiosInstance;