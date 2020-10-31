A Research Compedium of <b>Quality Assessment of Web-Based Information on Type 2 Diabetes</b> 

This platform is a research compedium of our academic publication below.

<i>Didem Ölçer, and Tugba Taskaya Temizel (2020). Quality Assessment of Web-Based Information on Type 2 Diabetes, Online Information Review, Emerald Insight (submitted).</i>

The platform provides the following materials:

<b>documents/</b>

<p>This subdirectory contains detailed information about our process of selection of websites and employed methodology (process.md).</p>
<p>It contains description of all textual features and information of how they are calculated (description of textual features.md).</p>
<p>In addition, it contains all selected terms from ADA and their weirdness scores (list of content-based features.md).</p>

<b>code/</b>

The code/ directory contains an RStudio project and two subdirectories, exploration/ which contains R Markdown exploratory analyses, and scripts/ which contains all the code for actually cleaning, combining, and generating the data. All paths in the scripts are relative to the code/ base (where the .Rproj file lives).

In the scripts/ subdirectory, functions live in the functions/ subdirectory and all have the naming convention xx_funs_yy.R. Action scripts which call the functions all have the naming convention xx_run_yy.R.

Each .R script has a summary at the top of what it does. The scripts are numbered in the order in which they would typically be run.

<b>data/</b>

The original data is stored in the data/raw_data/ subdirectory.

Any data that is produced using code is contained in data/processed_data/.

Modeling results are saved in the data/results/ subdirectory


<b>Comparison of high- and low-quality websites.pdf:</b> It contains manual inspection of websites.

 
