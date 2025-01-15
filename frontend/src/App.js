import React from 'react';

const App = () => {
    return (
        <div className="min-h-screen bg-white text-lightGrey">
            <nav className="flex justify-between p-4 bg-blue">
                <h1 className="text-2xl font-bold text-white">Pitch Book</h1>
                <ul className="flex space-x-6">
                    <li>Precedent Transaction</li>
                    <li>Public Comps</li>
                    <li>Benchmarking</li>
                    <li>US Indicators</li>
                    <li>Pitch Book</li>
                </ul>
            </nav>
            <main className="p-8">Welcome to the Pitch Book Application!</main>
        </div>
    );
};

export default App;
