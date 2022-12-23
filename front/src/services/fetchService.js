export const getData = async (url) => {
    const response = await fetch(url, {
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': '*/*',
        }
    });
    return response.json();
};

export const postData = async (url, body) => {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': '*/*',
        },
        body: JSON.stringify(body),
    });
    return response.json();
};
