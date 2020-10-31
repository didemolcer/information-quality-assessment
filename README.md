A Research Compedium of <b>Quality Assessment of Web-Based Information on Type 2 Diabetes</b> 

This platform is a research compedium of our academic publication below.

<i>Didem Ölçer, and Tugba Taskaya Temizel (2020). Quality Assessment of Web-Based Information on Type 2 Diabetes, Online Information Review, Emerald Insight (submitted).</i>

<p>The study investigates the impact of textual and content-based features in predicting the quality of health-related texts. The experiments were conducted for websites about type-2 diabetes and mainly focuses on assessing the quality of written information about treatment choices.</p>
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
<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg>
<b><i>The platform provides the following materials:</i></b>
<p></p>
<p><b>documents/</b>>/p>

<p>This subdirectory contains detailed information about our process of selection of websites and employed methodology (process.md).</p>
<p>It contains description of all textual features and information of how they are calculated (description of textual features.md).</p>
<p>In addition, it contains all selected terms from ADA and their weirdness scores (list of content-based features.md).</p>

<b>code/</b>

The code/ directory contains an RStudio project and two subdirectories, exploration/ which contains R Markdown exploratory analyses, and scripts/ which contains all the code for actually cleaning, combining, and generating the data. All paths in the scripts are relative to the code/ base (where the .Rproj file lives).

In the scripts/ subdirectory, functions live in the functions/ subdirectory and all have the naming convention xx_funs_yy.R. Action scripts which call the functions all have the naming convention xx_run_yy.R.

Each .R script has a summary at the top of what it does. The scripts are numbered in the order in which they would typically be run.

<b>data/</b>

The original text of websites cannot be given for copyright. Therefore the description of all features is given in <code>documents/</code> and in the <code>code/</code> how they are generated is given.
 
Any data that is produced using code is contained in data/processed_data/.

Modeling results are saved in the data/results/ subdirectory



 
