function objects(arr){
    let i=1;
    console.log("EMPLOYEES");
    for (var employee of arr.employees) {
        let slen = employee.first_name.length + employee.last_name.length;
        console.log(i+" - "+employee.first_name+" "+employee.last_name+" - "+slen); 
        ++i;
    }
    console.log("MANAGERS");
    i = 1;
    for (var manager of arr.managers) {
        let slen = manager.first_name.length + manager.last_name.length;
        console.log(i+" - "+manager.first_name+" "+manager.last_name+" - "+slen);
        ++i;
    }
}


let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
 };


 objects(users);