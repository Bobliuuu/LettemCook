import React from 'react';


interface RoadmapProps {
title: string;
}

const Roadmap: React.FC<RoadmapProps> = ({ title }) => {
    return (
        <div className="p-4 bg-gray-100">
            <h2 className="text-xl font-bold">{title}</h2>
            {/* Add your roadmap content here */}
        </div>
    );
};


export default Roadmap;