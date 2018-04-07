var datos = "memberid="+memberid+"&firstinitials="+iname+"&lastinitials="+lname+"&birthdate="+dob+"&gender="+gender+"&diagnosis="+diagnosis+"&diagcode="+diagcode;

$.ajax
({
    type: 'POST',
    data: datos,
    url: 'URL/AddPatient.php',
    timeout: 2000,
    async: true,
    success: function(result){	
        		
                var status = result.status;
                var patientid = result.patientid;
                
                switch(status) {
                    case 0:
                        console.log("Unable to add patient."); 
                        break;
                    case 1:
                        console.log("Patient added.")
                        sessionStorage.setItem('patientid', patientid);
                        break;
                    case 2:
                        console.log("Patient already exists");
                        break;
                    default:
                        console.log("Unable to add patient.");
                    }
                },
        error: function()
            {
                    alert("error");
            }
}); 