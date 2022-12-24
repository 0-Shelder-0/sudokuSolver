export const checkCorrectDataEntry = (value) => {
    return isNaN(value);
};

export const checkWhitespace = (value) => {
    return value.trim().length < 1;
};

export const getNineSizeArray = () => (
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
);

export const getFourSizeArray = () => (
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
);

export const checkError = (array) => {
    let isError = false;
    array.forEach((row) => {
        row.forEach((cell) => {
            if (checkCorrectDataEntry(cell)) {
                isError = true;
            }
        })
    })
    return isError;
};

export const checkEmptyString = (value) => {
    return value.length === 0;
};

export const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}