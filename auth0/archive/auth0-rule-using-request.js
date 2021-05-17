/* global configuration */
/**
 * @title Fraud Prevention
 * @overview Send the user's IP address, user agent, email address and username in MD5 to MaxMind's MinFraud API.
 *
 * This rule will send the user's IP address, user agent, email address (in MD5) and username (in MD5) to MaxMind's MinFraud API. This API will return information about this current transaction like the location, a risk score, ...
 *
 * > Note: You will need to sign up here to get a license key https://www.maxmind.com/
 *
 */

// eslint-disable-next-line no-unused-vars
async function userRiskScore(user, context, cb) {
    // For Logging Events
    const log = global.getLogger ? global.getLogger('Get Risk Score', cb): {
          callback: cb,
          error: console.error,
          info: console.log,
          debug: console.log
        };
    const { callback } = log;
  
    // Skip if not user facing app type
    /*if (context.clientMetadata.userApp !== 'true') {
      log.info(`Skipping risk check as not enabled for app ${context.clientName}`);
      return callback(null, user, context);
    }*/
  
    const MINFRAUD_API = `https://${configuration.MINFRAUD_ACCOUNT_ID}:${configuration.MINFRAUD_LICENSE_KEY}@minfraud.maxmind.com/minfraud/v2.0/score`;
  
    // Set to false to trigger high risk
    // Will set IP to Russian IP and change user agent.
    const fakeData = false;
  
    const ipAddress = fakeData ? '87.242.77.197' : context.request.ip;
    const userAgent = fakeData ? 'naughty-fraud-agent' : context.request.userAgent;
  
    try {
      const request = require('request-promise');
     
      const result = await request.get('https://taylordemo.mynonemployee.com/api/risk_scores?object_id=633b5e71-090c-4a47-a1a3-d0b8338df872', {
        headers: {
             'Content-Type':'application/json',
          'Authorization':'Token token=a1989931dbe14d02a1e0d323a8ca599d',
          'Accept':'application/json'
        },
        json: true,
        timeout: 3000
      });
  
      const userInfo = `${user.email || user.username} (${user.user_id})`;
      log.info(`Fraud response for user ${userInfo}: ${JSON.stringify(result, null, 2)}`);
  
      user.risk = {
        score: result.risk_scores[0].overall_score
      };
  
      // Append to tokens
      context.idToken['https://travel0.net/risk'] = user.risk;
      context.accessToken['https://travel0.net/risk'] = user.risk;
    } catch (err) {
      // If the service is down, the request failed, or the result is OK just continue.
      log.error(`Error while attempting fraud check: ${err.message}`);
    }
    return callback(null, user, context);
  }