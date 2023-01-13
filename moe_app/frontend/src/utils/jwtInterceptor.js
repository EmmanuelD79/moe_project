import axios from "axios";
import baseURL from '../API'
 
const jwtInterceptor = axios.create({});
const refreshUrl = baseURL + 'token/refresh/'
 
jwtInterceptor.interceptors.request.use((config) => {
  let tokensData = JSON.parse(localStorage.getItem("tokens"));
  config.headers.common["Authorization"] = `bearer ${tokensData.access}`;
  return config;
});


jwtInterceptor.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      if (error.response.status === 401) {
        const authData = JSON.parse(localStorage.getItem("tokens"));
        const payload = {
          access: authData.access,
          refresh: authData.refresh,
        };
   
        let apiResponse = await axios.post(
          refreshUrl,
          payload
        );
        localStorage.setItem("tokens", JSON.stringify(apiResponse.data.token));
        error.config.headers[
          "Authorization"
        ] = `bearer ${apiResponse.data.token.access}`;
        return axios(error.config);
      } else {
        return Promise.reject(error);
      }
    }
  );

export default jwtInterceptor;