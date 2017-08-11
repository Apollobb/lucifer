import fetch from 'utils/fetch';
import apiURL from '@/config'

//jobs
export function postDuty(data) {
    return fetch({
        url: apiURL.dutys,
        method: 'post',
        data
    });
}
export function getDutyList(query) {
    return fetch({
        url: apiURL.dutys,
        method: 'get',
        params: query
    });
}

export function putDuty(id, data) {
    return fetch({
        url: apiURL.dutys + id + '/',
        method: 'put',
        data
    });
}

export function deleteDuty(id) {
    return fetch({
        url: apiURL.dutys + id,
        method: 'delete',
    });
}