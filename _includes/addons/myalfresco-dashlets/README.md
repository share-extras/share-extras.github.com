MyAlfresco Dashlets
===============

Interact with the [MyAlfresco](https://my.alfresco.com/) service from your on-premise install. It currently provides a _MyAlfresco Sites_ dashlet, an extension to Share's search results page to search your Cloud content and an _API Explorer_ admin console component that allows you to run live queries against the Alfresco Cloud public API.

Pre-requisites
--------------

* Alfresco 4.2.d or later
* [Share-OAuth](https://github.com/share-extras/share-oauth) v2.3.0 or later

Building and Installing
-----------------------

Use Maven to build the JAR file, which you can then install into the Tomcat instance where you have the Share webapp deployed

    mvn clean package && \
      cp myalfresco-dashlets/target/myalfresco-dashlets-1.0-SNAPSHOT.jar <TOMCAT_HOME>/webapps/share/WEB-INF/lib

If you prefer to install an AMP file, you can find this in the `myalfresco-dashlets-amp` subdirectory.

There is no need to install any repository-side component, but as mentioned in _Pre-requisites_ above, you must have already installed Share OAuth as detailed in that project.

Configuring
-----------

If you are not running your Share instance on `localhost:8081`, then before using the add-on you must register a new application of your own on the Alfresco [developer portal](https://developer.alfresco.com/) and specify the _Callback URL_ as `http://host:port/share/page/extras/oauth/auth2-return/myalfresco-api`.

Then, [add some configuration](http://docs.alfresco.com/4.2/topic/com.alfresco.enterprise.doc/tasks/share-customizing-custom-config-file.html) to your `share-config-custom.xml` to override the endpoint used by the dashlets, e.g.

```
    <config evaluator="string-compare" condition="Remote">
        <remote>
            <endpoint>
                <id>myalfresco-api</id>
                <name>Custom MyAlfresco Public API</name>
                <connector-id>myalfresco</connector-id>
                <endpoint-url>https://api.alfresco.com</endpoint-url>
                <client-id>myclientid</client-id>
                <client-secret>myclientsecret</client-secret>
                <access-token-url>https://api.alfresco.com/auth/oauth/versions/2/token</access-token-url>
            </endpoint>
        </remote>
    </config>
```

Your config should contain the correct details for the app you registered.

 * You will need to insert the correct values that identify your newly-created application in the `client-id` and `client-secret` parameters, which you can find in the developer portal
 * The `name` field can be anything of your choosing, whatever makes sense to you, but do not change the `id` value
 
### Configuring the Search page extension
 
 You must deploy the _My Alfresco Search_ module in the Module Deployment Console in order to enable this functionality. Once added, Cloud search results will be displayed for any user who has recently used the dashlet or the API Explorer console.
