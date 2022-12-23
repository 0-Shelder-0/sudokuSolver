import React from 'react';
import Table from "../Table";

import * as SC from './styles';

const Index = (props) => {
    const { tableSize } = props;
    const sudokuArray = new Array(tableSize * tableSize).fill('');

    console.log(sudokuArray);

    return (
        <SC.SudokuWrapper tableSize={tableSize}>
            {sudokuArray.map((table) => (
                <Table tableSize={tableSize}>

                </Table>
            ))}
        </SC.SudokuWrapper>
    );
};

export default Index;