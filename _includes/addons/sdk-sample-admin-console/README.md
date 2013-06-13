SDK Sample Admin Console Component
==================================

This project defines a common source directory layout, [Eclipse](http://www.eclipse.org/) project configuration and [Ant](http://ant.apache.org/) build script that is used by all the Share Extras add-ons, in addition to some sample files from a basic 'Hello World' admin console component.

The sample project is intended to help you build your own Admin Console components, using standard tools such as Eclipse and Ant.

Creating Your Own Projects
--------------------------

To use the sample project, download the `sample-admin-console-src.zip` file from the [Downloads](http://code.google.com/p/share-extras/downloads/list) area, and use this to start a new project using Eclipse's Import wizard (click _File_ > _New_ and then select _General_ > _Existing Projects into Workspace_).

Once you have created your project, it should be named _Sample Admin Console_ in Eclipse. You should rename this to something of your choosing and update the corresponding JAR file name specified in `build.properties`.

You should also update the information in `README.txt` and `MAINTAINERS.txt` to give some basic information about your project.

###Project Web Scripts

All admin console projects will define one `admin-console` family web-tier [http://wiki.alfresco.com/wiki/Web_Scripts web script] for each component, but may also use additional web-tier scripts, or repository scripts for loading data.

The `admin-console` family web script is mandatory and the example component is implemented using the web script provided below `config/alfresco/site-webscripts`. You can modify this script as you require, but you should also rename the web script file names, update the `org/mycompany' package and change the web script URL (specified in the `.desc.xml` file) to something unique for your project.

The project supports any number of additional repository-tier and web-tier web scripts. The scripts must be added in the following directories below `config`.

For web-tier web scripts, place your scripts under

  * `alfresco/site-webscripts` for your custom web scripts
  * `alfresco/web-extension/site-webscripts` for any existing web-tier scripts that you want to override.

For repository-tier web scripts, place scripts under

  * `alfresco/templates/webscripts` for your custom web scripts
  * `alfresco/extension/templates/webscripts` for any existing repository scripts that you want to override.

Below these locations you should place scripts in a folder hierarchy as per standard web script packaging techniques, e.g. `org/mycompany/projectname` or `org/mycompany/components/dashlets`.

Note that Java web scripts are not supported by the sample project.

###Project Resource Files

The project defines a single client-side JavaScript file and a single CSS stylesheet to implement the basic example, which you can rename and modify as per your requirements. These files can be found within the `source/web` directory in the project.

The files are linked into the user interface via mark-up in the `.head.ftl` web-tier web script, therefore you must also update the file names and paths referenced there, if you change these.

You can add additional client-side resources such as JavaScript, CSS and image files within the `source/web` directory. To link to other client-side assets, you can use the resources servlet in the Share webapp at `http://server/share/res/path/to/asset`. Within your Freemarker templates, you can construct links using code such as

    <img src="${url.context}/res/mycompany/components/dashlets/refresh.png" alt="Image description here" />

The resources servlet will look for assets under the path following `/res`, first within the Share web application (from 3.4c / 3.4 Enterprise) and then in the `META-INF` folders of any JAR files on the web application's class path. The build targets defined in `build.xml` will ensure that resources are packaged up so as to be accessible via this method.

###SpringSurf Configuration

For more advanced customisations, you can place additional global-scoped configuration in the file `alfresco/web-extension/share-config-custom.xml` within `config`.

###Spring Configuration

The project defines a single Spring bean in the file `config/org/springframework/extensions/surf/mycompany_hello-world-console-context.xml`, which is responsible for loading the name and description labels for the component's left-hand-side navigation link.

For more advanced customisations, you can place additional Spring configuration in the directory `alfresco/web-extension` within `config`.

In order to be imported, your configuration must reside in one or more XML files with the suffix `-context.xml` and each file must have a globally unique name.

Building Your Project
---------------------

The Ant build script `build.xml` can be used to help you distribute your customisations for testing or deployment. You can run the script from a command line or using Eclipse's _External Tools Configurations_ dialogue (_Run_ > _External Tools_ > _External Tools Configurations_).

  * Use the `build-jar` target to build a JAR file in the `dist` directory, suitable for deploying as a shared library on any Share 3.3+ installation.
  * Use the `hotcopy-tomcat-jar` target to copy the JAR file containing the customisations into a local Tomcat installation on your system. You will need to specify the location of your Tomcat installation by defining the variable `tomcat.home` when you call the script.
  * Use the `hotcopy-tomcat-zip` target to copy all the individual configuration and resource files into a local Tomcat installation on your system for testing. Unlike `hotcopy-tomcat-jar`, this method allows you to reload changes to your files without having to restart the Tomcat server, and so is better suited for development. You will need to specify the location of your Tomcat installation by defining the variable `tomcat.home` when you call the script.
  * Use the `reload-webscripts-repo` and `reload-webscripts-share` targets to reload the repository and web-tier web scripts respectively. This will not reload resources deployed in JAR files but is suitable for local testing in combination with the `hotcopy-tomcat-zip` target.

For more information on these targets and the other targets available in `build.xml`, see the inline comments within the [build script](build.xml).

###Command line examples

If you have Ant installed and have configured your system `PATH` correctly as per the [Ant manual](http://ant.apache.org/manual/), you can run the targets from a command line as per the following examples.

    ant build-jar

This will build a JAR file using the default file name specified in `build.properties`, containing the custom files.

    ant -Djar.name=my-custom.jar build-jar

This will build a JAR file named `my-custom.jar`

    ant -Dtomcat.home=C:\Alfresco\tomcat hotcopy-tomcat-zip

This will copy all your custom files into the Tomcat instance installed at `C:\Alfresco\tomcat`. Configuration files will be placed into `shared/classes`, while resources will be copied below `webapps/share`.

    ant -Dtomcat.repo.home=C:\Alfresco\tomcat -Dtomcat.share.home=C:\Alfresco\tomcat-share hotcopy-tomcat-zip

This will copy all your custom repository files into the Tomcat instance installed at `C:\Alfresco\tomcat` and your custom Share files into the Tomcat instance installed at `C:\Alfresco\tomcat-share`.