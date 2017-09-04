import axios from 'axios'
import { Message } from 'element-ui'
import store from '../store'
import {getToken} from "./auth"

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// 创建axios实例
const service = axios.create({
  baseURL: '', // api的base_url
  timeout: 5000                  // 请求超时时间
});

// request拦截器
service.interceptors.request.use(config => {
  // Do something before request is sent
  if (store.getters.token) {
      const token = getToken();
      config.headers.Authorization = 'token ' + token; // 让每个请求携带token--['X-Token']为自定义key 请根据实际情况自行修改
      config.headers['X-CSRFToken'] = token; //加上这个，解决build后 post出现403错误
  }
  return config;
}, error => {
  // Do something with request error
  console.log(error); // for debug
  Promise.reject(error);
});

// respone拦截器
service.interceptors.response.use(
  response => response,

  error => {
    console.log('err' + error);// for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    });
    return Promise.reject(error);
  }
);

export default service;
