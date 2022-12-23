import styled, {css} from "styled-components";

export const Input = styled.input`
  text-align: center;
  line-height: 50px;
  
  margin: 0;
  padding: 0;
  border: 0.5px dashed lightgray;
  border-right-color: ${({ columnIndex }) => columnIndex === 2 || columnIndex === 5 ? 'black' : 'lightgray'};
  border-bottom-color: ${({ rowIndex }) => rowIndex === 2 || rowIndex === 5 ? 'black' : 'lightgray'};
  outline: none;
  
  ${({ isError }) => isError && css`
    border: 0.5px dashed red;
  `}
`;
