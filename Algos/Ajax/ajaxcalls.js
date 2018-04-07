var datos = "memberid="+memberid+"&firstinitials="+iname+"&lastinitials="+lname+"&birthdate="+dob+"&gender="+gender+"&diagnosis="+diagnosis+"&diagcode="+diagcode;

  $.ajax
    ({
        type: 'POST',
        data: datos,
        url: 'URL/AddPatient.php',
        timeout: 2000,
        async: true,
        success: function(result)
                 {			
                     
                    var status = result.status;
                    var patientid = result.patientid;
                    
                    if (status === 0){
                        console.log("Unable to add patient.");  
                    }
                     
                    if (status === 1){
                        console.log("Patient added.")
                        sessionStorage.setItem('patientid', patientid);
                    }
                     
                    if (status === 2){
                        console.log("Patient already exists");
                    }
                     
                 },
         error: function()
                {
                      alert("error");
                }
    }); 