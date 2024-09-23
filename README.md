# INACH data curator
The codes in this repository are used to curate the data from the diferent files that the 'Instituto Antartico Chile' (INACH) handle and the data from [ANID](https://github.com/ANID-GITHUB).

The used data asociated to the INACH is related to the antartic science projects (PROCIEN), the antartic expeditions (ECA) and the papers asociated to antartic topics from Web Of Science (WOS). The main goal is unified scattered information that the institute had.


## Important details
Here are some details about how some data was obtained. All the codes create a basis .xlsx file that later is curated by hand to fix error and introduce more data. Also, all the personal data is treated using a private file and it will not me shared in this repository.

### Antartic science projects
In order to determinate de research area of each project, we use the conversion table (indicated in the analysis) for the ANID and OCDE objective, and the INACH one, we use the ones reported in the [ILAIA](https://www.inach.cl/category/publicaciones/revista-ilaia/).

Its important to remark that the INACH clasification change in the 2018 version (to the last one, 2024), where some of the old ones had a rename and a new one (social science) is added.

### ANID data
The only tasks with the ANID data was merge all the files and later select the projects related with the antarctic, the problem with that is some of them contain the word antarctic but is not a project related with it, so a manual filter is done to exclude these.