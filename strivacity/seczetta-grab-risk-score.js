/** This function will be called from the Post identification hook in a blocking manner.
 *
 * @param {Object}   args                              Input arguments
 * @param {Object}   args.application                  Application related information
 * @param {string}   args.application.name             Name
 * @param {string}   args.application.client_id        OAuth client ID
 * @param {Object}   args.oidc_context                 Information about the originating OpenID Connect request
 * @param {string[]} args.oidc_context.acr_values      ACR values
 * @param {string[]} args.oidc_context.ui_locales      UI locales
 * @param {Object}   args.customer                     Customer related information
 * @param {string}   args.customer.ip_address          HTTP client IP coming from the X-Forwarded-For header
 * @param {string[]} args.customer.store               ID of store containing the customer
 * @param {string[]} args.customer.info                map holding stored information about the user
 * @param {string}   args.customer.info.id             ID of the customer
 * @param {Object[]} args.customer.groups              List of groups the customer is the members of
 * @param {Object[]} args.authenticators               List of enrolled authenticators
 * @param {string[]} args.requested_scopes             Scopes requested in the originating OIDC auth request
 * @param {Object}   args.session                      Session store
 * @param {Object}   args.continue_context             Continue context
 * @param {postIdentificationCallback} callback
 * @param {denyRequestCallback} error
 */


const config = {
  SECZETTA_API_KEY: 'c6bda210f92142188032f5a7b59ed0f6',
  SECZETTA_BASE_URL: 'https://idproofdemo.nonemployee.com/api',
  SECZETTA_ATTRIBUTE_ID: '7cffa07d-ad6d-4398-ba07-b3d1e5f9ee9f',
  SECZETTA_PROFILE_TYPE_ID: 'efa0e8e1-a193-4596-9081-ccf4ea9d0c07',
  SECZETTA_ALLOWABLE_RISK: 3,
  SECZETTA_MAXIMUM_ALLOWED_RISK: 7,
  SECZETTA_AUTHENTICATE_ON_ERROR: true,
  SECZETTA_RISK_KEY: 'overall_score'
}



module.exports = async function ({ application, oidc_context, customer, authenticators, requested_scopes, session, continue_context }, callback, error) {
// implement your logic here
  //success callback(new AllowAuthentication(session));
  //error error(new ErrorDenyRequest("description", "hint"));
  //show error?: callback(new ShowErrorMessage("Error shown in customer's browser", session));
  
  if (!config.SECZETTA_API_KEY || !config.SECZETTA_BASE_URL || ! config.SECZETTA_ATTRIBUTE_ID || !config.SECZETTA_PROFILE_TYPE_ID || !config.SECZETTA_ALLOWABLE_RISK || !config.SECZETTA_MAXIMUM_ALLOWED_RISK) {
      console.log("Missing required configuration. Skipping.");
      return error(new ErrorDenyRequest("Missing Required Configuration. Failing.", ""));
  }

  const URL = require("url").URL;
  const axios = require("axios");
  
  let profileResponse;
  let riskScoreResponse;

  let attributeId = config.SECZETTA_ATTRIBUTE_ID;
  let profileTypeId = config.SECZETTA_PROFILE_TYPE_ID;
  console.log("Got Attribute and Profile Ids: " + attributeId + " :: " + profileTypeId)

  let uid = "Felicia.Carroll@acme.com" //customer.info.username;
  const profileRequestUrl = new URL('/api/advanced_search/run', config.SECZETTA_BASE_URL);

  let advancedSearchBody = {
      advanced_search: {
      label: "All Contractors",
      condition_rules_attributes: [
          {
          "type": "ProfileTypeRule",
          "comparison_operator": "==",
          "value": profileTypeId
          },
          {
          "type": "ProfileAttributeRule",
          "condition_object_id": attributeId,
          "object_type": "NeAttribute",
          "comparison_operator": "==",
          "value": uid
          }
      ]
      }
  };
  

  try {
          profileResponse = await axios.post(profileRequestUrl.href,advancedSearchBody,{
          headers: {
          'Content-Type':'application/json',
          'Authorization': 'Token token='+config.SECZETTA_API_KEY,
          'Accept': 'application/json'
          },
      });

      console.log(profileResponse.data)
      //if the user isnt found via the advanced search. A 
          if( profileResponse.data.profiles.length === 0 ) {
              console.log("Profile not found. Empty Array sent back!");
              if( config.SECZETTA_AUTHENTICATE_ON_ERROR && config.SECZETTA_AUTHENTICATE_ON_ERROR ) {
                  callback(new AllowAuthentication(session));
              }
              return error(new ErrorDenyRequest("Error retrieving Risk Score. Failing.", ""));
          }
      
  } catch (profileError) {
      // Swallow risk scope API call, default is set to highest risk below.
      console.log(`Error while calling Profile API: ${profileError.message}`);
      if( config.SECZETTA_AUTHENTICATE_ON_ERROR && config.SECZETTA_AUTHENTICATE_ON_ERROR == true ) {
          callback(new AllowAuthentication(session));
      }
      return error(new ErrorDenyRequest("Error retrieving Risk Score. Failing.", ""));
  }
  
  //Should now have the profile in profileResponse. Lets grab it.
  let objectId = profileResponse.data.profiles[0].id;
  console.log(objectId);

  const riskScoreRequestUrl = new URL('/api/risk_scores?object_id=' + objectId, config.SECZETTA_BASE_URL);

  try {
      riskScoreResponse = await axios.get(riskScoreRequestUrl.href,{
      headers: {
          'Content-Type':'application/json',
          'Authorization': 'Token token='+config.SECZETTA_API_KEY,
          'Accept': 'application/json'
      },
      });
  } catch (riskError) {
      // Swallow risk scope API call, default is set to highest risk below.
      console.log(`Error while calling Risk Score API: ${riskError.message}`);
      if( config.SECZETTA_AUTHENTICATE_ON_ERROR && config.SECZETTA_AUTHENTICATE_ON_ERROR == true ) {
          callback(new AllowAuthentication(session));
      }
      return error(new ErrorDenyRequest("Error retrieving Risk Score. Failing.", ""));
  }

  //Should now finally have the risk score. Lets add it to the user
  var riskScoreObj = riskScoreResponse.data.risk_scores[0];
  const overallScore = riskScoreObj.overall_score;

  // Default risk value is set to highest if API fails or no score returned.
  //var riskScore = typeof apiResponse.riskScore === "number" ? riskScore : 100;

  const allowableRisk = parseInt(config.SECZETTA_ALLOWABLE_RISK, 10);
  const maximumRisk = parseInt(config.SECZETTA_MAXIMUM_ALLOWED_RISK, 10);
  
  //if risk score is below the maxium risk score but above allowable risk: Require MFA
  /*if ((allowableRisk && overallScore > allowableRisk && overallScore < maximumRisk) || (allowableRisk === 0)) {
      console.log(
      `Risk score ${overallScore} is greater than maximum of ${allowableRisk}. Prompting for MFA`
      );
      context.multifactor = {
      provider: 'any',
      allowRememberBrowser: false
      };
      return callback(null, user, context);
  
  }*/

  //if risk score is above the maxium risk score: Fail authN
  if (maximumRisk && overallScore >= maximumRisk) {
      console.log(
      `Risk score ${overallScore} is greater than maximum of ${maximumRisk}`
      );
      //error(new ErrorDenyRequest("A "+overallScore+" Risk score is too high. Maximum acceptable risk is " + maximumRisk, ""));
      return callback(new ShowErrorMessage("A "+overallScore+" Risk score is too high. Maximum acceptable risk is " + maximumRisk, session));
 }

  console.log("Success! Letting user authenticate.")
  callback(new AllowAuthentication(session));
      

};

/** AdditionalAuthenticator */
class AllowAuthentication {
authentication = null;
session = {}

/**
 * @constructor
 * @param {Object} session
 */
constructor(session) {
  this.authentication = 'ALLOW';
  this.session = session;
}
}