const HOST = 'https://localhost:80';

export const SOLUTION_POST_URL = `${HOST}/solutions/`;

export const STATUS_GET_URL = (solutionId) => `${HOST}/status/${solutionId}`;
