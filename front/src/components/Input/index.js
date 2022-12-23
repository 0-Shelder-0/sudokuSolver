import React, { useState } from 'react';

import { checkCorrectDataEntry } from "../../helpers/tableHelper";

import * as SC from "./styles";

const Index = () => {
    const [inputValue, setInputValue] = useState('');
    const [inputError, setInputError] = useState(false);

    const onChangeHandler = (e) => {
        const isDataCorrectly = !checkCorrectDataEntry(e.target.value);
        if (!isDataCorrectly) {
            setInputError(true);
        } else {
            setInputError(false);
        }
        setInputValue(e.target.value.trim());
    };

    return (
        <SC.Input
            maxLength={1}
            value={inputValue}
            onChange={onChangeHandler}
            isError={inputError}
        />
    );
};

export default Index;