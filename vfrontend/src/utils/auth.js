import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token'
const TokenTime = 'Admin-Token-Time'

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

export function setAvatar(avatar) {
      return Cookies.set(TokenKey, avatar)
}

export function getAvatar() {
      return Cookies.get(TokenKey)
}