
# Heinz College SkillScraper #
Do you have only 24 units left of electives and want to make sure your choices are aligned with employer demands? Let the Heinz College SkillScraper help you build the skills you need to land your dream job! The Heinz College SkillScraper is a one-stop shop for:
- Researching current employment trends and salary stats (**Bureau of Labor Statistics**)
- Learning about hot skills in today's marketplace (**Payscale.com**)
- Aggregating job board listings (**Indeed.com**)
- Choosing the most relevant courses to these demands, based on course descriptions and keywords (**Heinz Course Catalog**)

## Group 7 Members
- Jonathan Dyer, jondyer@cmu.edu
- Devraj Kori, dkori@andrew.cmu.edu
- Muriel Pokol, mpokol@andrew.cmu.edu
- Brian Rhindress, brhindre@andrew.cmu.edu
- Matthew Samach, msamach@andrew.cmu.edu

## Installation Instructions

Community modules used in the Heinz SkillScraper include:
- SpaCy: https://spacy.io/usage/
- Pandas: https://anaconda.org/conda-forge/pandas
- Tkinter: https://docs.python.org/3/library/tkinter.html
- BeautifulSoup: https://pypi.org/project/beautifulsoup4/


Installation for the above modules is straightforward:   
1. Ensure you have the latest version of Python (3.7) installed on your machine, preferably via Anaconda.

2. Open your Anaconda prompt (or any command prompt if not using Anaconda) and activate whatever environment you plan to use.  

3. Run the following command (replacing `conda` with `pip` if not using Anaconda) and select `[y]` or press `enter` when prompted:   
`conda install pandas beautifulsoup4 spacy lxml`  

4. Now run the following command **as Administrator** (`sudo` on \*nix, run Anaconda prompt "as Administrator" on Windows):  
`python -m spacy download en`

That's it! You're all ready to run the SkillScraper application.  


## Run Instructions

After installing necessary modules, simply run the **SkillScraper.py** program to launch the GUI.  The integrated master controller within the GUI will call other necessary modules.  Select a job from the drop-down menu and wait for the information!

## Screenshots and Video
![Program Output](https://github.com/dkori/Course-Job-Match/blob/master/Final/img/output_screenshot.png)
<!-- ![](https://github.com/dkori/Course-Job-Match/blob/master/Final/img/output_screenshot.png) -->

Demo video: https://youtu.be/ve7diLk9Or0

## Sub-modules in this project:

- :iphone: **Interface.py**: The Main Controller. This script creates the Heinz SkillScraper GUI, allows for user input, and draws on data from each of the other modules.

- :chart: **bls_data_frame.py**: This script generates a data frame, list of BLS-tracked jobs, and a list of salary and employment figures for a selected job.

- :dollar: **payscale_scraper.py**: This scrapes payscale.com for an up-to-date list of payscale.com skill listings. Not used in production version.

- :briefcase: **match_indeed_to_skill.py**: Scrapes the top 5-pages from a selected indeed.com job search. Cross-compares and counts the number of job skill occurrences, based on payscale.com skill lists.

- :school: **heinz_scraper.py**: This script scrapes the current Heinz course catalog, parses course descriptions, and compares keywords against key skill-words identified in the indeed.com scrape.  It then returns a list of all courses matching the job-skill pair.

## License
Carnegie Mellon University  
Heinz College of Information Systems and Public Policy  
Heinz SkillScraper ©
