import { Outlet } from 'react-router-dom';
import MyNavbar from './components/MyNavbar';

 export default function App() {
  return (
    <>
      <MyNavbar />
      <Outlet />
    </>
  );
}
