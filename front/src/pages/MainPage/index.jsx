import React from 'react';
import Sudoku from "../../components/Sudoku";
import {BUTTON_TYPES, TABLE_SIZES} from "../../constants/table";
import Button from "../../components/Button";

import * as SC from './styles';
import {ButtonGroup} from "./styles";

const Index = () => {
    return (
        <SC.MainLayout>
            <Sudoku tableSize={TABLE_SIZES.LARGE}></Sudoku>
            <SC.ButtonGroup>
                <Button type={BUTTON_TYPES.SUBMIT}>Solve</Button>
                <Button>Reset</Button>
            </SC.ButtonGroup>
        </SC.MainLayout>
    );
};

export default Index;