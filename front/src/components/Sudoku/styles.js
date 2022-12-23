import styled, {css} from "styled-components";
import {TABLE_SIZES} from "../../constants/table";

export const SudokuWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;

  ${({tableSize}) =>
          tableSize === TABLE_SIZES.SMALL &&
          css`
            width: 240px;
          `
  }

  ${({tableSize}) =>
          tableSize === TABLE_SIZES.LARGE &&
          css`
            width: 490px;
          `
  }
`;