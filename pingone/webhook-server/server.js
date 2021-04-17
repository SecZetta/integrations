const express = require("express");
const bodyParser = require("body-parser");
const axios = require('axios');

// Initialize express and define a port
const app = express()
const PORT = 3000

const url = "https://idproofdemo.nonemployee.com/api"
const apiKey = "c6bda210f92142188032f5a7b59ed0f6"


axios.defaults.headers.post['Content-Type'] = 'application/json' // for POST requests
axios.defaults.headers.post['Authorization'] = 'Token token='+apiKey, // for POST requests
axios.defaults.headers.post['Accept'] = 'application/json' // for POST requests


// Tell express to use body-parser's JSON parsing
app.use(bodyParser.json())

// Start express on the defined port
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`))

app.use(bodyParser.json())

app.post("/hook", (req, res) => {
	console.log(req.body)

	if( req.body.length <= 0) {
			console.log("No Body found")
			return
	}

	hook = req.body[0];
	action = hook.action["type"];
	//client = hook.actors.client
	user = hook.actors.user
	resources = hook.resources;
	resource = resources[0];
	console.log("=========== ACTION ===========");
	console.log(action)
	console.log("=========== Client ===========");
	//console.log(client)
	console.log("=========== USER ===========");
	console.log(user)
	console.log("=========== RESOURCES ===========");
	console.log(resources)

	userId = resource.id;
	username = resource.name;
	apiRef = user.href;
	//clientId = client.id;
	environment = user.environment.id;

	data = {
		"profile": {
			"profile_type_id": "0a6bd686-1a21-4601-9b3d-15fe8c59aba3",
			"status": "Active",
			"attributes": {
				"display_name": username,
				"revalidation_date_ne_attribute": "06/10/2020",
				"application_ne_attribute": "PingOne",
				"ping_one_id_ne_attribute": userId,
				"pingone_api_ref_ne_attribute": apiRef,
				"pingone_env_id_ne_attribute": environment,
				"pingone_client_id_ne_attribute": "adminUI",
				"bot_owner_ne_attribute": "02e82a1f-587d-4999-8d46-1ce20ce246b9"
			}
		}
	}

	console.log(data)

	if( action == "USER.CREATED") {
		createProfile(data);
	}


  res.status(200).end() // Responding is important
})


async function createProfile(data) {
    try {
        response = await axios.post(url + "/profile", data);
        console.log(response.status);
				console.log(response.statusText);
    } catch (error) {
        console.log(`Error while calling Profile API: ${error.message}`);
    }
}

//createProfile({ test: "test"})