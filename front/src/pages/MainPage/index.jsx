import React, {useState} from 'react';
import Sudoku from "../../components/Sudoku";
import {BUTTON_TYPES, TABLE_SIZES} from "../../constants/table";
import Button from "../../components/Button";

import { checkError, getNineSizeArray } from "../../helpers/tableHelper";
import {postData} from "../../services/fetchService";
import SOLUTION_POST_URL from '../../constants/urls';
import * as SC from './styles';

const Index = () => {
    const [sudokuTable, setSudokuTable] = useState(getNineSizeArray());
    const [sudokuId, setSudokuId] = useState(null);
    const [dataLoading, setDataLoading] = useState(false);

    const onUpdateTableHandler = (rowIndex, columnIndex, value) => {
        sudokuTable[rowIndex][columnIndex] = value;
        setSudokuTable(sudokuTable);
    };

    const onResetTableHandler = () => {
        setSudokuTable(getNineSizeArray());
    };

    const onSubmitHandler = () => {
        const isError = checkError(sudokuTable);
        if (!isError) {
            const body = { solution: sudokuTable };
            const solId = postData(SOLUTION_POST_URL, body);
            setSudokuId(solId);
        }
    };

    const getCellValue = (rowIndex, columnIndex) => {
        return sudokuTable[rowIndex][columnIndex];
    };

    return (
        <SC.MainLayout>
            <Sudoku
                sudokuTable={sudokuTable}
                tableSize={TABLE_SIZES.LARGE}
                onUpdateTableHandler={onUpdateTableHandler}
                getCellValue={getCellValue}
                dataLoading={dataLoading}
            >
            </Sudoku>
            <SC.ButtonGroup>
                <Button type={BUTTON_TYPES.SUBMIT} onClick={onSubmitHandler}>Solve</Button>
                <Button onClick={onResetTableHandler}>Reset</Button>
            </SC.ButtonGroup>
        </SC.MainLayout>
    );
};

export default Index;