import React, { useState } from 'react';

import {checkCorrectDataEntry, checkEmptyString, checkWhitespace} from "../../helpers/tableHelper";

import * as SC from "./styles";

const Index = (props) => {
    const { rowIndex, columnIndex, onUpdateTableHandler, getCellValue, dataLoading } = props;

    const [inputValue, setInputValue] = useState('');
    const [inputError, setInputError] = useState(false);


    const onChangeHandler = (e) => {
        const isDataCorrectly = !checkCorrectDataEntry(e.target.value);
        const isWhitespace = checkWhitespace(e.target.value);
        if (!isDataCorrectly && !isWhitespace) {
            setInputError(true);
            onUpdateTableHandler(rowIndex, columnIndex, e.target.value.trim())
            setInputValue(e.target.value.trim());
        } else if (!isWhitespace) {
            setInputError(false);
            onUpdateTableHandler(rowIndex, columnIndex, Number(e.target.value.trim()))
            setInputValue(e.target.value.trim());
        } else if (checkEmptyString(e.target.value)) {
            setInputError(false);
            onUpdateTableHandler(rowIndex, columnIndex, 0)
            setInputValue(e.target.value);
        }
    };

    return (
        <SC.Input
            maxLength={1}
            value={dataLoading ? getCellValue(rowIndex, columnIndex) : inputValue}
            onChange={onChangeHandler}
            isError={inputError}
        />
    );
};

export default Index;