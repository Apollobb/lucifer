import fetch from 'utils/fetch';
import apiURL from '@/config'

//jobs
export function postJob(data) {
    return fetch({
        url: apiURL.jobs,
        method: 'post',
        data
    });
}
export function getJobList(query) {
    return fetch({
        url: apiURL.jobs,
        method: 'get',
        params: query
    });
}

export function putJob(id, data) {
    return fetch({
        url: apiURL.jobs + id + '/',
        method: 'put',
        data
    });
}

export function deleteJob(id) {
    return fetch({
        url: apiURL.jobs + id,
        method: 'delete',
    });
}


// jobgroups
export function postJobGroup(data) {
    return fetch({
        url: apiURL.jobgroups,
        method: 'post',
        data
    });
}

export function getJobGroupList(query) {
    return fetch({
        url: apiURL.jobgroups,
        method: 'get',
        params: query
    });
}

export function putJobGroup(id, data) {
    return fetch({
        url: apiURL.jobgroups + id + '/',
        method: 'put',
        data
    });
}

export function deleteJobGroup(id) {
    return fetch({
        url: apiURL.jobgroups + id,
        method: 'delete',
    });
}