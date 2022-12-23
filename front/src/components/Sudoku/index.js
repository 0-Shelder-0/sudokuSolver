import React from 'react';
import Table from "../Table";

import * as SC from './styles';

const Index = (props) => {
    const {tableSize, onUpdateTableHandler, getCellValue, dataLoading} = props;
    const sudokuArray = new Array(tableSize * tableSize).fill('');

    console.log(sudokuArray);

    return (
        <SC.SudokuWrapper tableSize={tableSize}>
            <Table
                tableSize={tableSize}
                onUpdateTableHandler={onUpdateTableHandler}
                getCellValue={getCellValue}
                dataLoading={dataLoading}
            >
            </Table>
        </SC.SudokuWrapper>
    );
};

export default Index;