

    const patientData = [
      {
        id:'P101',
        name:'Aarav Sharma',
        disease:'Diabetes',
        doctor:'Dr. Mehta',
        department:'Endocrinology',
        days:'5',
        bill:'₹25,000'
      },
      {
        id:'P102',
        name:'Ananya Verma',
        disease:'Dengue',
        doctor:'Dr. Rao',
        department:'General Medicine',
        days:'7',
        bill:'₹18,000'
      },
      {
        id:'P103',
        name:'Rohan Patel',
        disease:'Heart Disease',
        doctor:'Dr. Kapoor',
        department:'Cardiology',
        days:'13',
        bill:'₹95,000'
      }
    ];

    const searchButton = document.querySelector('.search-box button');
    const searchInput = document.querySelector('.search-box input');
    const table = document.querySelector('table');

    searchButton.addEventListener('click', () => {

      const searchValue = searchInput.value.toLowerCase();

      const filteredPatients = patientData.filter(patient =>
        patient.name.toLowerCase().includes(searchValue) ||
        patient.disease.toLowerCase().includes(searchValue)
      );

      let tableHTML = `
        <tr>
          <th>Patient ID</th>
          <th>Name</th>
          <th>Disease</th>
          <th>Doctor</th>
          <th>Department</th>
          <th>Days Admitted</th>
          <th>Bill Amount</th>
        </tr>
      `;

      if(filteredPatients.length === 0){

        tableHTML += `
          <tr>
            <td colspan="7" style="text-align:center; padding:20px;">
              No patient record found.
            </td>
          </tr>
        `;
      }

      else{

        filteredPatients.forEach(patient => {

          tableHTML += `
            <tr>
              <td>${patient.id}</td>
              <td>${patient.name}</td>
              <td>${patient.disease}</td>
              <td>${patient.doctor}</td>
              <td>${patient.department}</td>
              <td>${patient.days}</td>
              <td>${patient.bill}</td>
            </tr>
          `;
        });
      }

      table.innerHTML = tableHTML;

    });

