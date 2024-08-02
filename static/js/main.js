console.log("Main.js Hard Loaded");
// getting all records using fetch
function getALlProfiles(url) {
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
                // custom data was set to improve update
                const profileHTMLElement = `<li id=${profile.id} data-profile-id=${profile.id} data-profile-name=${profile.name} data-profile-email:${profile.email}>${profile.id} | ${profile.name} | ${profile.email}</li>`;
                //const profileHTMLElement = $('#')
                profileList.innerHTML += profileHTMLElement;
            });
        });
    console.log("Refreshing...");
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// POST (adding profile)
// credentials and cookies are to be noticed
// same-origin: in case where frontend and backend are hosted on different servers: CORS must be included
// post requests require csrf value, we must use the cookie value to generate csrf and send it along with the request
// one option is to use django's {% csrf_token %} to generate it automatically, but this requires an actual form to be created
// the other option is to aquire the cookie and generate it
function addProfile(url, payload) {
    fetch(url, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"), // to handle CSRF verification
        },
        body: JSON.stringify({ payload: payload })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}


function updateProfile(url, payload) {
    fetch(url, {
        method: "PUT",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ payload: payload })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}

function deleteThis(url) {
    fetch(url, {
        method: "DELETE",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}