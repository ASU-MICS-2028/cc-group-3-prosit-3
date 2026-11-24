import { createRoot } from 'react-dom/client';

function Dashboard() {
  return (
    <main>
      <h1>SmartCity Accra</h1>
      <p>Accra Metropolitan Assembly dashboard</p>
    </main>
  );
}

const root = document.getElementById('root');

if (!root) {
  throw new Error('Dashboard root element is missing');
}

createRoot(root).render(<Dashboard />);
