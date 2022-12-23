import './reset.css';
import { Route, Routes } from "react-router";
import MainPage from "./pages/MainPage";

function App() {
    return (
        <div>
            <Routes>
                <Route exact path="/" element={<MainPage />} />
            </Routes>
        </div>
    );
}

export default App;
