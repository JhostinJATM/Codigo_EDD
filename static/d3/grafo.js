var nodes = new vis.DataSet([{id: 1,label:"Adelaide Smith"},
{id: 2,label:"Joel Johnson"},
{id: 3,label:"Lilith Brown"},
{id: 4,label:"Ennar Taylor"},
{id: 5,label:"Lilith Brown"},
]);
var edges = new vis.DataSet([{from:1,to:2, label:"4"},
{from:2,to:3, label:"5"},
]);
var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);