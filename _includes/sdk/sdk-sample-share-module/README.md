Sample Extensibility Modules for Alfresco Share
===============================================

Author: Will Abson

This project is intended to demonstrate the new extensibility features of 
Alfresco Share 4.0 and to make it easy to define your own modules.

Share Modules are a new feature in Alfresco 4.0 and allow pages to be customised at the region, component or even the mark-up level.

The project builds on the [SDK Sample Dashlet](https://github.com/share-extras/sdk-sample-dashlet) and uses the same project structure, Ant build script and Eclipse project configuration, but is suitable for developing more complex customizations such as the examples in [Dave Draper's tutorials](http://blogs.alfresco.com/wp/ddraper/).

The project re-uses the tutorial code from Dave's blog to show examples of the following

  * Adding new regions in a page
  * Hiding existing regions or components
  * Overriding or adding new message bundle strings within components
  * Extending components' JavaScript controllers
  * Extending component Freemarker templates

The examples demonstrate the two main methods of extending existing components using Share modules, based on *sub-components* or *customizations* (of existing components/templates).

All the examples used in this project are taken directly from Dave Draper's
tutorials, with some small modifications to the folder structures.

You will need to be familiar with the concept of a Share Module and the differences between templates, pages, regions, components and sub-components in order to create your own projects. Reading the [blog examples](http://blogs.alfresco.com/wp/ddraper/) thoroughly will help you understand the background.

Creating Your Own Projects
--------------------------

To use the sample project, download the `sample-share-modules-src-<version>.zip` file from the [Downloads](http://code.google.com/p/share-extras/downloads/list) area, and use this to start a new project using Eclipse's Import wizard (click _File_ > _New_ and then select _General_ > _Existing Projects into Workspace_).

Once you have created your project, it should be named _Sample Share Module_ in Eclipse. You should rename this to something of your choosing and update the corresponding JAR file name and source ZIP name specified in `build.properties`.

You should also update the information in `README.txt` and `MAINTAINERS.txt` to give some basic information about your project.

### Module configuration

The example modules taken from the blog examples are declared in two XML files within the project configuration directory `config/alfresco/site-data/extensions`

  * `org_mycompany_sample-customization-modules.xml` declares the customization-based examples
  * `org_mycompany_sample-subcomponent-modules.xml` declares the sub-component-based examples

You can use either approach to define your own module(s) by copying the relevant file and making your modifications there. You are recommended to experiment with the two different approaches if possible, as there are pros and cons to each. Generally sub-components are simpler, but customizations provide more options and flexibility.

### Implementation files

You can add your own web scripts, components, pages, templates and template instances in the structures provided inside the `config/alfresco` folder.

  * `site-data/components` for component bindings
  * `site-data/pages` for pages
  * `site-data/template-instances` for page template instances
  * `site-webscripts` for web-tier web scripts
  * `templates` for page template

For more information on the exact locations required for web scripts, Spring/SpringSurf configuration, see the [SDK Sample Dashlet](https://github.com/share-extras/sdk-sample-dashlet).

Client-side resources such as CSS and JavaScript can also be included in the `source/web` folder, just as in the [SDK Sample Dashlet](https://github.com/share-extras/sdk-sample-dashlet).

Building Your Project
---------------------

See [Building Your Project](https://github.com/share-extras/sdk-sample-dashlet#building-your-project) in the [SDK Sample Dashlet](https://github.com/share-extras/sdk-sample-dashlet) docs.