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
    if ( query.time_lte == 'NaN-aN-aN' || query.time_lte == '1970-01-01') {
        delete query.time_gte;
        delete query.time_lte;
    }
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


//upload
export function postUpload(data) {
    return fetch({
        url: apiURL.uploads,
        method: 'post',
        data
    });
}

export function getUploadList(query, id) {
    if ( query.time_lte == 'NaN-aN-aN' || query.time_lte == '1970-01-01') {
        delete query.time_gte;
        delete query.time_lte;
    }
    if (id) {
        var url = apiURL.uploads + id;
    } else {
        var url = apiURL.uploads;
    }
    return fetch({
        url: url,
        method: 'get',
        params: query
    });
}

export function putUpload(id, data) {
    return fetch({
        url: apiURL.uploads + id + '/',
        method: 'put',
        data
    });
}

export function deleteUpload(id) {
    return fetch({
        url: apiURL.uploads + id,
        method: 'delete',
    });
}