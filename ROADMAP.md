# ROADMAP

The ultimate goal of this repository is to store the visualization and data filtering code needed to create and deploy a web application. The application will be built using FastAPI web framework, embedding panel (bokeh) which is the reason for the directory structure that it will have.

In the future, we aim to deploy Generation Interval as a standalone web application, but for the moment no public deployment of the app is online, and this repo only aims to store and document the code that selects data and creates the plots. The app will be able to be run in an HPC cluster through ssh tunnels. Datasets will, for the moment be stored in cluster.

Once online, this repo will contain the updated version of the code. Finally, in the event that the app is not mantained online, this repository will contain a copy of the code which will be accessible in case someone finds it useful.

Generation Interval is currently under development, the steps will be:

**1.  Implement data manipulation code.**
    
- We aim to separate data manipulation and visualization as much as we can, as possible upgrades and optimizations during deployment could imply migrating the data (csv) to SQL.

**2. Implement code for visualization.**

- Prioritize simplicity and responsiveness for the plots, which is also the reason for using FastAPI as web framework.

**3. Deployment**

- Deploying as public web application, it is important to select the service and how we want to publicly serve the application. Also relevant to see where to upload the data so we can access it seamlessly.

**