import fetch from 'utils/fetch';
import apiURL from '../config'

export function getOrderList() { res => {}
  return fetch({
    url: apiURL.orderlist,
    method: 'get'
  });
}
