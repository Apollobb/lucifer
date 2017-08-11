import fetch from 'utils/fetch';
import apiURL from '@/config'

export function login(data) {
  return fetch({
    url: apiURL.login,
    method: 'post',
    data
  });
}

export function logout() {
  return "logout"
}

export function getInfo(username) {
  console.log(username);
  return fetch({
    url: apiURL.users,
    method: 'get',
    params: {
      username
    }
  });
}

