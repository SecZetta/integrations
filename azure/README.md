# Tutorial: Azure Active Directory SSO integration with SecZetta Identity Suite 

In this tutorial, you'll learn how to integrate SecZetta Identity Suite with Azure Active Directory (Azure AD). 
When you integrate SecZetta Identity Suite with Azure AD, you can:

-	Control in Azure AD who has access to the SecZetta solutions.
-	Enable your users to be automatically signed-in to the SecZetta Identity Suite with their Azure AD accounts.
-	Manage your accounts in one central location - the Azure portal.

The SecZetta Identity Suite consists of various products. The SSO integrations discussed in this tutorial are focus on:

- SecZetta Life Cycle
- SecZetta Collaboration

In general the setup is similar but there are some minor differences.

## Prerequisites
To get started, you need the following items:

-	An Azure AD subscription and administrative access.
-	SecZetta Identity Suite administrative access to configure SSO.
-	All of your SecZetta Identity User will need an account in Azure Active Directory with exactly the same email address.

## Scenario description
In this tutorial, you configure and test Azure AD SSO in a test environment.

1.	SecZetta Identity Suite supports SP and IDP initiated SSO for both the Life Cycle and Collaboration products.
2.  SeZetta Identity Suite does not support SAML JIT (Just In Time) provisioning.

## Add SecZetta from the gallery
To configure the integration of SecZetta Identity Suite into Azure AD, you need to add SecZetta from the gallery to your list of managed SaaS apps.

    1.	Sign in to the Azure portal using either a work or school account, or a personal Microsoft account.

    2.	On the left navigation pane, select the Azure Active Directory service.

    3.	Navigate to Enterprise Applications and then select All Applications.

    4.	To add new application, select New application.

    5.	In the Add from the gallery section, type SecZetta in the search box.

    6.	Select SecZetta from results panel and then add the app. Wait a few seconds while the app is added to your tenant.

## Configure and test Azure AD SSO for SecZetta Identity Suite

Configure and test Azure AD SSO with SecZetta using a test user called B.Simon For SSO to work, you need to establish a relationship between an Azure AD user and the related user in SecZetta Life Cycle or Collaboration.
To configure and test Azure AD SSO with SecZetta, perform the following steps:

    1.	[Configure Azure AD SSO](#Configure-Azure-AD-SSO) - to enable your users to use this feature.

        a.	Create an Azure AD test user - to test Azure AD single sign-on with B.Simon.

        b.	Assign the Azure AD test user - to enable B.Simon to use Azure AD single sign-on.

    2.	Configure SecZetta SSO - to configure the single sign-on settings on application side.
    
        a.  Create SecZetta test user - to have a counterpart of P.Simon in SecZetta that is linked to the Azure AD representation of user.

3.	Test SSO - to verify whether the configuration works.

### Configure Azure AD SSO

Follow these steps to enable Azure AD SSO in the Azure portal.

    1.	In the Azure portal, on the SecZetta application integration page, find the Manage section and select single sign-on.

    2.	On the Select a single sign-on method page, select SAML.

    3.	On the Set up single sign-on with SAML page, click the pencil icon for Basic SAML Configuration to edit the settings.

        ![SSO SAML Setup1](img/ssosetup1.png)

    4.	On the Basic SAML Configuration section, if you wish to configure the application in IDP and SP initiated mode, perform the following step:

        In the Reply URL text box, type a URL using the following pattern:

        - SecZetta Life Cycle use: https://<customer>.nonemployee.com/saml/consume

        - SecZetta Collaboration use:  https://<customer>.mynonemployeeportal.com /saml/consume?portal_url=portalname 

        `Note:` The portal name is the name configured for the respective collaboration portal in the SecZetta Collaboration administrative interface.

    5.	The SecZetta application expects the SAML assertions in a specific format, which requires you to add custom attribute mappings to your SAML token attributes configuration to match the SecZetta configuration for the expected attributes. 
        The following screenshot shows the list of configured attributes aligned with the configuration in SecZetta:

        ![SSO SAML Setup2](img/ssosetup2.png)

    6.  On the Setup single sign-on with SAML page, in the Federation Metadata XML section and select Download to download the XML metadata file and save it on your computer.

        ![SSO SAML Setup3](img/ssosetup3.png)
    
    7.	In the Setup SecZetta section, we use the XML metadata file to configure SSO for SecZetta.

#### Create an Azure AD test user
In this section, you'll create a test user in the Azure portal called B.Simon.

    1.	From the left pane in the Azure portal, select Azure Active Directory, select Users, and then select All users.

    2.	Select New user at the top of the screen.

    3.	In the User properties, follow these steps:

        a.	In the Name field, enter B.Simon.
        b.	In the User name field, enter the username@companydomain.extension. For example, B.Simon@contoso.com.
        c.	Select the Show password check box, and then write down the value that's displayed in the Password box.
        d.	Click Create.

#### Assign the Azure AD test user
In this section, you'll enable B.Simon to use Azure single sign-on by granting access to the SecZetta LifeCycle or Collaboration application.

    1.	In the Azure portal, select Enterprise Applications, and then select All applications.

    2.	In the applications list, select SecZetta.

    3.	In the app's overview page, find the Manage section and select Users and groups.

    4.	Select Add user, then select Users and groups in the Add Assignment dialog.

    5.	In the Users and groups dialog, select B.Simon from the Users list, then click the Select button at the bottom of the screen.

    6.	In the Add Assignment dialog, click the Assign button.

### Configure SecZetta SSO

The SSO configuration for the SecZetta products has small differences from a configuration perspective and the differences are indicated in this section.

To configure SSO for SecZetta we need the XML metadata file we downloaded earlier to make the SSO configuration simpler.

To configure SSO we recommended using two different browsers, so that in case of an SSO error, you have a chance to correct the error or disable SSO without locking yourself out.

### SSO Configuration for SecZetta Life Cycle

Login into your SecZetta Identity Suite environment as an administrator take the following steps:

    1.  Select the System section

        ![SSO SAML Setup4](img/ssosetup4.png)

    2.	Select authentication

    3.	Select the SSO section to configure SSO:
    
        a.	Toggle the SSO switch to ON
    
        b.	Enter an SSO Name
    
        c.	Enter the SP Entity ID

            The value corresponds to the Azure AD SSO Identifier configuration definition for the SecZetta Life Cycle application.

        d.	Enter the Name Attribute

            The value corresponds to the Azure AD name Claim configuration in the Azure AD SSO definition for the SecZetta Life Cycle application.

        e.	Enter the Email Attribute

            The value corresponds to the Azure AD email Claim configuration in the Azure AD SSO definition for the SecZetta Life Cycle application.

        f.	Enter the Groups Attribute

            The value corresponds to the Azure AD email Claim configuration in the Azure AD SSO definition for the SecZetta Life Cycle application.

            See below an example configuration of the various attributes

            ![SSO SAML Setup5](img/ssosetup5.png) 

            ![SSO SAML Setup6](img/ssosetup6.png)

        g.  Next we import the XML metadata we downloaded previously using the Import File option, so the IDP settings are automatically configured, as shown below:

            ![SSO SAML Setup7](img/ssosetup7.png)

        h.	Next select the SAVE button to save the SSO configuration.

### Create a SecZetta Life Cycle User

To create a user for SecZetta Life Cycle you can use the SecZetta Create User API.
You can use tools like POSTMAN to call the Create User API. 
For more details on using the Create User API, open the link to your SecZetta API documentation located at: https://<your domain>.mynonemployee.com/api/v1/neprofile.html#creating-a-user.

### Test SSO for SecZetta Life Cycle
In this section, you test your Azure AD single sign-on configuration with following options:

    1.	Service Provider (SP) Initiated SSO.

        Once SSO is enabled for SecZetta Life Cycle, a new button on the login screen appears with the name you assigned in the SSO configuration, as shown below:

        ![SSO SAML Setup8](img/ssosetup8.png)

        Select the new button to test the SSO configuration and see if you can successfully login with SP initiated SSO with a user that is assigned the application in Azure AD.

    2.	Identity Provider (IDP) Initiated SSO.

        As Azure AD is the Identity Provider here, you can either test the SSO configuration from the application SSO configuration screen, selecting the Test button, as shown below.

        ![SSO SAML Setup9](img/ssosetup9.png)

        Ensure that the logged in user to the Azure Portal has indeed access to the SecZetta Life Cycle application in Azure AD. 
        Alternatively the user can login to https://myapplications.microsoft.com and select the SecZetta Life Cycle application to initiate the IDP SSO login.

### SSO Configuration for SecZetta Collaboration

Login into your SecZetta environment as an administrator take the following steps:

    1.	Select the Collaboration section and from this section select portals:

        ![SSO SAML Setup10](img/ssosetup10.png)

    2.	Select the portal from the list you want to configure SSO for or add a new portal. 

    3.	Select the SSO section to configure SSO:
        
        a.	Toggle the SSO switch to ON
        
        b.	Enter an SSO Name
        
        c.	Enter the SP Entity ID 
            
            The value corresponds to the Azure AD SSO Identifier configuration definition for the SecZetta Collaboration application.

        d.	Enter the Name Attribute

            The value corresponds to the Azure AD name Claim configuration in the Azure AD SSO definition for the SecZetta Collaboration application.
        
        e.	Enter the Email Attribute

            The value corresponds to the Azure AD email Claim configuration in the Azure AD SSO definition for the SecZetta Collaboration application.

        f.	Enter the Groups Attribute
            
            The value corresponds to the Azure AD email Claim configuration in the Azure AD SSO definition for the SecZetta Collaboration application.

            See below an example configuration of the various attributes.

            ![SSO SAML Setup11](img/ssosetup11.png) 

        9.  Next we import the XML metadata we downloaded previously using the Import File option, so the IDP settings are automatically configured, as shown below:

            ![SSO SAML Setup12](img/ssosetup12.png) 

        h.	Next select the SAVE button to save the SSO configuration.

### Create a SecZetta Collaboration User

To create a user for SecZetta Collaboration you can use the following methods:

    1.	Use the Collaboration Account action in a Portal Registration workflow to create the new portal user.

    2.	Use the SecZetta Create User API.

        You can use tools like POSTMAN to call the Create User API. 
        For more details on using the Create User API, open the link to your SecZetta API documentation located at: https://<your domain>.mynonemployee.com/api/v1/neprofile.html#creating-a-user.

### Test SSO for SecZetta Collaboration

In this section, you test your Azure AD single sign-on configuration with following options:

    1.	Service Provider (SP) Initiated SSO.

        Once SSO is enabled for SecZetta Collaboration, a new button on the login screen appears with the name you assigned in the SSO configuration, as shown below:

        ![SSO SAML Setup13](img/ssosetup13.png)

        Select the new button to test the SSO configuration and see if you can successfully login with SP initiated SSO with a user that is assigned the application in Azure AD.

    2.	Identity Provider (IDP) Initiated SSO.

        As Azure AD is the Identity Provider here, you can either test the SSO configuration from the application SSO configuration screen, selecting the Test button, as shown below.

        ![SSO SAML Setup14](img/ssosetup14.png)

        Ensure that the logged in user to the Azure Portal has indeed access to the SecZetta Collaboration application in Azure AD. 
        Alternatively the user can login to https://myapplications.microsoft.com and select the SecZetta Collaboration application to initiate the IDP SSO login.

