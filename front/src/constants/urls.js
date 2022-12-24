const HOST = 'https://localhost:8080';

export const SOLUTION_POST_URL = `${HOST}/solutions/`;

export const STATUS_GET_URL = (solutionId) => `${HOST}/status/${solutionId}`;

export const SOLUTION_GET_URL = (solutionId) => `${HOST}/solutions/${solutionId}`;
