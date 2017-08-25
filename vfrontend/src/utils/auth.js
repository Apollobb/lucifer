import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token';
const TokenTime = 'Admin-Token-Time';
const Userinfo = 'userinfo';

export function setToken(token) {
      return Cookies.set(TokenKey, token)
}

export function getToken() {
      return Cookies.get(TokenKey)
}

export function removeToken() {
      return Cookies.remove(TokenKey)
}

export function setTokenTime(token) {
      return Cookies.set(TokenTime, token)
}

export function getTokenTime() {
      return Cookies.get(TokenTime)
}

export function removeTokenTime() {
      return Cookies.remove(TokenTime)
}

export function setUserinfo(userinfo) {
      return Cookies.set(Userinfo, userinfo)
}

export function getUserinfo() {
      return Cookies.get(Userinfo)
}

export function removeUserinfo() {
      return Cookies.remove(Userinfo)
}