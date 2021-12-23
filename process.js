let clients = [];
let immmatriculations = [];

d3.csv("Clients_0.csv", function(data) {
    for (var i = 0; i < data.length; i++) {
        clients.push([data[i].sexe, data[i].immatriculation]);
    }
});

d3.csv("Clients_8.csv", function(data) {
    for (var i = 0; i < data.length; i++) {
        clients.push([data[i].sexe, data[i].immatriculation]);
    }
});

d3.csv("Immatriculations.csv", function(data) {
    for (var i = 0; i < data.length; i++) {
        clients.forEach(infos_client => {
            if (infos_client[1] == data[i].immatriculation) {
                immmatriculations.push([data[i].immatriculation, data[i].marque, data[i].nom]);
            }
        })
    }
});

console.log(clients);
console.log(immmatriculations);
