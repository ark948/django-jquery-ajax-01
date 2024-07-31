// getting all records using fetch
function getALlProfiles(url) {
    console.log("Requesting data...");
    fetch(url, {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    })
        .then(resposne => resposne.json())
        .then(data => {
            const profileList = document.getElementById("profilelist");
            profileList.innerHTML = "";

            (data.context).forEach(profile => {
                const profileHTMLElement = `
                    <li>
                        <p>Name: ${profile.name}</p>
                        <p>Email: ${profile.email}</p>
                    </li>`
                profileList.innerHTML += profileHTMLElement;
            });
        });
    console.log("Data received.");
}