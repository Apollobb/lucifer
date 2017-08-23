import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token';
const TokenTime = 'Admin-Token-Time';
const Avatar = 'avatar';
const Name = 'name';
const Roles = 'roles';
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

export function setAvatar(avatar) {
      return Cookies.set(Avatar, avatar)
}

export function getAvatar() {
      return Cookies.get(Avatar)
}

export function removeAvatar() {
      return Cookies.remove(Avatar)
}

export function setName(name) {
      return Cookies.set(Name, name)
}

export function getName() {
      return Cookies.get(Name)
}

export function removeName() {
      return Cookies.remove(Name)
}

export function setRoles(roles) {
      return Cookies.set(Roles, roles)
}

export function getRoles() {
      return Cookies.get(Roles)
}

export function removeRoles() {
      return Cookies.remove(Roles)
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