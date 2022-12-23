import styled from "styled-components";

export const Table = styled.table`
  width: 100px;
  height: 100px;

  border: 1px solid black;
  border-collapse: collapse;

  text-align: center;
  line-height: 50px;

  td {
    border: 1px dashed black;
  }
`;

export const Wrapper = styled.div`
  border: 1px solid black;
  
  input {
    width: 50px;
    height: 50px;
  }
`;

export const Row = styled.div`
  display: flex;
  
  border-collapse: collapse;
`;

export const Input = styled.input`
  text-align: center;
  line-height: 50px;
  
  margin: 0;
  padding: 0;
  border: 0.5px dashed lightgray;
  outline: none;
  border-collapse: collapse;
`;