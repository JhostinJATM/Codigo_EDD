var nodes = new vis.DataSet([{id: 1,label:"1"},
{id: 2,label:"2"},
{id: 3,label:"3"},
{id: 4,label:"4"},
{id: 5,label:"5"},
]);
var edges = new vis.DataSet([{from:1,to:2, label:"20"},
{from:1,to:3, label:"21"},
{from:1,to:4, label:"22"},
{from:1,to:5, label:"23"},
{from:2,to:1, label:"20"},
{from:2,to:3, label:"nan"},
{from:3,to:1, label:"21"},
{from:3,to:2, label:"nan"},
{from:4,to:1, label:"22"},
{from:5,to:1, label:"23"},
]);
var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);