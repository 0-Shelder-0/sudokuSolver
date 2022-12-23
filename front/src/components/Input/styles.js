import styled from "styled-components";

export const Input = styled.input`
  text-align: center;
  line-height: 50px;
  
  margin: 0;
  padding: 0;
  border: ${({ isError }) => isError ? '0.5px dashed red' : '0.5px dashed lightgray'};
  outline: none;
  border-collapse: collapse;
`;
