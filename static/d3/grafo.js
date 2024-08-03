var nodes = new vis.DataSet([{id: 1,label:"1"},
{id: 2,label:"2"},
{id: 3,label:"3"},
{id: 4,label:"4"},
{id: 5,label:"5"},
{id: 6,label:"6"},
]);
var edges = new vis.DataSet([]);
var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);