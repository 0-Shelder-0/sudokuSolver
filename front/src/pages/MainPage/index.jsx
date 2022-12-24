import React, {useState} from 'react';
import Sudoku from "../../components/Sudoku";
import {BUTTON_TYPES, TABLE_SIZES} from "../../constants/table";
import Button from "../../components/Button";

import {checkError, getNineSizeArray, sleep} from "../../helpers/tableHelper";
import {getData, postData} from "../../services/fetchService";
import * as SC from './styles';
import {SOLUTION_GET_URL, SOLUTION_POST_URL, STATUS_GET_URL} from "../../constants/urls";

const Index = () => {
    const [sudokuTable, setSudokuTable] = useState(getNineSizeArray());
    let sudokuId = 0;
    const [dataLoading, setDataLoading] = useState(false);
    let status = 0;

    const onUpdateTableHandler = (rowIndex, columnIndex, value) => {
        sudokuTable[rowIndex][columnIndex] = value;
        setSudokuTable(sudokuTable);
    };

    const onResetTableHandler = () => {
        setSudokuTable(getNineSizeArray());
        window.location.reload();
    };

    const onSubmitHandler = async () => {
        const isError = checkError(sudokuTable);
        if (!isError) {
            const body = {solution: sudokuTable};
            const response = await postData(SOLUTION_POST_URL, body);
            console.log(response, 'response');
            sudokuId = response.solution_id

            while (status !== 4 && status !== 5) {
                const statusResponse = await getData(STATUS_GET_URL(sudokuId));
                status = statusResponse.status;
                if (status === 4 || status === 5) break;
                await sleep(1000);
            }

            const solutionResponse = await getData(SOLUTION_GET_URL(sudokuId));
            setSudokuTable(solutionResponse.solution);
            setDataLoading(true);
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