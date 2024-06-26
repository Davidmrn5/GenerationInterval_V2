# ROADMAP

The ultimate goal of this repository is to store the visualization and data filtering codebase needed to create the plots and then deploy a web application, hence the structure of the repository. The application will be built using panel based mainly on bokeh plots.

In the future, we aim to deploy Generation Interval as a standalone web application, but for the moment no public deployment of the app is online, and this repo only aims to store and document the code that selects data and creates the plots. The app will be able to be run in an HPC cluster through ssh tunnels. Datasets will, for the moment be stored in cluster.

Once online, this repo will contain the updated version of the code. Finally, in the event that the app is not mantained online, this repository will contain a copy of the code which will be accessible in case someone finds it useful.

Generation Interval is currently under development, the steps will be:

**1.  Implement data manipulation code.**
    
- We aim to separate data manipulation and visualization as much as we can, as possible upgrades and optimizations during deployment could imply migrating the data (csv) to SQL.

**2. Implement code for visualization.**

- Prioritize simplicity and responsiveness for the plots, which is also the reason for using FastAPI as web framework.

**3. Deployment**

- Deploying as public web application, it is important to select the service and how we want to publicly serve the application. Also relevant to see where to upload the data so we can access it seamlessly.

**Other ideas** I want to keep a list of things that come to my mind and could be done in the future:

- Migrating csv files to RDBMS so we can use it with SQL (check SQLAlchemy to use it as a Pythonic approach).
- Once decided where the databases will be stored, we could dockerize the app. This way anyone could download it from this repo and use it out of the box.

