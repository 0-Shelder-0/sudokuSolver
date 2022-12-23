import React, {useState} from 'react';

import * as SC from './styles';
import Input from "../Input";

const Index = (props) => {
    const { tableSize, onUpdateTableHandler, getCellValue, dataLoading } = props;
    const newTableSize = tableSize;
    const sudokuArray = new Array(newTableSize).fill('');

    return (
        <SC.Wrapper>
            {sudokuArray.map((table, rowIndex) => (
                <SC.Row>
                    {sudokuArray.map((table, index) => (
                        <Input
                            rowIndex={rowIndex}
                            columnIndex={index}
                            onUpdateTableHandler={onUpdateTableHandler}
                            getCellValue={getCellValue}
                            dataLoading={dataLoading}
                        />
                    ))}
                </SC.Row>
            ))}
        </SC.Wrapper>
    );
};

export default Index;