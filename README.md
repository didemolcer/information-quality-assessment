A Research Compedium of <h2>Quality Assessment of Web-Based Information on Type 2 Diabetes</h2> 
<hr>

This platform is a research compedium of our academic publication below.

<i>Didem Ölçer, and Tugba Taskaya Temizel (2020). Quality Assessment of Web-Based Information on Type 2 Diabetes, Online Information Review, Emerald Insight (submitted).</i>
<hr>

<p style="text-align: justify;">The study investigates the impact of <i>textual and content-based features</i> in predicting the quality of health-related texts. The experiments were conducted for websites about type-2 diabetes and mainly focuses on assessing the quality of written information about treatment choices.</p>
<ul>
<li>Which textual features reveal the quality of health websites? Are the linguistic styles of high-quality websites different from those of low-quality websites?
<ul>
<li>Are textual features derived from professional health literacy guidelines useful in assessing the quality of websites?</li>
<li>Is there any relationship between the frequencies of certain sentence types and the quality of websites? How is the number of auxiliary verbs related to the quality of websites?</li>
</ul>
</li>
<li>How are content-based features related to the quality and coverage of websites?</li>
<li>Does the use of both textual and content-based features perform better than the sole use of textual or content-based features in the classification of websites in terms of quality?</li>
</ul>
<hr>

<b><i>The platform provides the following materials:</i></b>
<hr>
<p></p>
<p><h3>documents/</b></h3>

<p>This subdirectory contains detailed information about our process of selection of websites and employed methodology (process.md).</p>
<p>It contains description of all textual features and information of how they are calculated (description of textual features.md).</p>
<p>In addition, it contains all selected terms from ADA and their weirdness scores (list of content-based features.md).</p>

<h3>code/</h3>

The code/ directory contains an RStudio project and two subdirectories, exploration/ which contains R Markdown exploratory analyses, and scripts/ which contains all the code for actually cleaning, combining, and generating the data. All paths in the scripts are relative to the code/ base (where the .Rproj file lives).

In the scripts/ subdirectory, functions live in the functions/ subdirectory and all have the naming convention xx_funs_yy.R. Action scripts which call the functions all have the naming convention xx_run_yy.R.

Each .R script has a summary at the top of what it does. The scripts are numbered in the order in which they would typically be run.

<h3>data/</h3>

<p style="text-align: justify;">The original text of websites cannot be given for copyright. Also, as these websites were collected between June 2016 and August 2016, their content may have changed when viewed up to date. Therefore the description of all features is given in <code>documents/</code> and in the <code>code/</code> how they are generated is given.</p>
 
Any data that is produced using code is contained in data/processed_data/.

Modeling results are saved in the data/results/ subdirectory



 
