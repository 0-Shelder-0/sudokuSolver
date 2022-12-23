import React from 'react';

import {BUTTON_TYPES} from "../../constants/table";

import * as SC from './styles';

const Index = (props) => {
    const { children, type = BUTTON_TYPES.BUTTON } = props;

    return (
        <SC.Button type={type}>
            {children}
        </SC.Button>
    );
};

export default Index;