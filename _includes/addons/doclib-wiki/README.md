Document Library Wiki Implementation for Share
==============================================

This project provides an alternative implementation of the Alfresco Share
wiki re-using the Document Library components.

The code was developed by Will Abson and Nathan McMinn at the Alfresco 
Developer Conference 2012 Hackathon.

To build and deploy the project into a local Tomcat instance for testing, use
the Ant build script supplied.

    ant hotcopy-tomcat-jar -Dtomcat.home=/opt/Alfresco/tomcat

Where `tomcat.home` is the location of your local Tomcat instance where the
Share webapp `share.war` is deployed.

Repository changes
------------------

Add the Markdown mimetype to the built-in respository mimetypes in 
`alfresco/mimetype/mimetype-map.xml`.

         <!-- Markdown  -->
         <mimetype mimetype="text/x-markdown" display="Markdown">
            <extension default="true">md</extension>
         </mimetype>

To enable inline editing for Markdown content it is necessary to override the Spring bean `evaluator.doclib.action.inlineEditMimetype`.

    <bean id="evaluator.doclib.action.inlineEditMimetype" parent="evaluator.doclib.action.isMimetype">
      <property name="mimetypes">
         <list>
            <value>text/plain</value>
            <value>text/html</value>
            <value>text/xml</value>
            <value>text/x-markdown</value>
         </list>
      </property>
    </bean>
