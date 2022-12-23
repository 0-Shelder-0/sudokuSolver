import React, {useState} from 'react';

import * as SC from './styles';
import Input from "../Input";

const Index = (props) => {
    const {tableSize} = props;
    const newTableSize = tableSize;
    const sudokuArray = new Array(newTableSize).fill('');

    return (
        <SC.Wrapper>
            {sudokuArray.map((table) => (
                <SC.Row>
                    {sudokuArray.map((table) => (
                        <Input />
                    ))}
                </SC.Row>
            ))}
        </SC.Wrapper>
    );
};

export default Index;