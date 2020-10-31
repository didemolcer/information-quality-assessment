<h2>Textual Features</h2>
<p>The textual features consist of the distinctive formal (particularly stylistic and structural) aspects of an utterance, text, or artwork in any medium (Oxford Dictionary, 2019).&nbsp; They were investigated under six categories, which four of six were adapted from (Dalip, Gon&ccedil;alves, Cristo, &amp; Calado, 2011; Dalip, Lima, Cristo, &amp; Calado, 2014) and two were introduced for the first time in this study: Text Structure, Text Style, Text Length, Text Sentence Type, Level of Readability and Lexical Variety. All categories are described as follows:</p>
<ul>
<li><strong><em>Text Structure</em></strong> features are to describe the structure of how well a text is organized. The HTML tags were counted to obtain the number of structural features:
<ul>
<li>Section count
<ul>
<li>Counting tags &lt;h1&gt; to &lt;h6&gt;</li>
</ul>
</li>
<li>Paragraph count
<ul>
<li>Counting tag &lt;p&gt;,</li>
</ul>
</li>
<li>Bullet count
<ul>
<li>Counting tag &lt;li&gt;</li>
</ul>
</li>
<li>Length of shortest section
<ul>
<li>Minimum length of total word count in sections</li>
</ul>
</li>
<li>Number of images
<ul>
<li>Counting tag &lt;img&gt;</li>
</ul>
</li>
<li>Average section length
<ul>
<li>Length of total word count in sections / Number of sections</li>
</ul>
</li>
<li>Average paragraph length
<ul>
<li>Length of total word count in paragraphs / Number of paragraphs</li>
</ul>
</li>
</ul>
</li>
<li><strong><em>Text Style</em></strong> features are used to capture the way authors write their articles through their word usage; they try to capture how the text is written, how author used the language and whether the text has some specific characteristics. Also, professional health literacy guidelines encourage the use of active voice instead of passive voice (Best Practice Guidance on Patient Information Leaflets, 2014; Toolkit for producing patient information, 2003; U.S. Department of Health and Human Services, 2015; MedlinePlus, 2018). Text style features aim to capture such specific usages.
<ul>
<li>Number of uses of verb to be
<ul>
<li>Counting &ldquo;am, is, are, was, were, being, been, and be&rdquo; in sentences</li>
</ul>
</li>
<li>Number of passive voice sentences
<ul>
<li>Counting &lsquo;nsubjpass&rsquo; parser from Stanford dependency parser for English syntax</li>
</ul>
</li>
<li>Number of nouns
<ul>
<li>Counting &ldquo;NN, NNP, NNPS, NNS&rdquo; POS tags from Stanford POS Tagger toolkit</li>
</ul>
</li>
<li>Number of auxiliary verbs
<ul>
<li>Counting &ldquo;MD&rdquo; POS tags from Stanford POS Tagger toolkit</li>
</ul>
</li>
<li>Number of verbs
<ul>
<li>Counting &ldquo;VB, VBD, VBG, VBN, VBP, VBZ&rdquo; POS tags from Stanford POS Tagger toolkit</li>
</ul>
</li>
<li>Number of adjectives
<ul>
<li>Counting &ldquo;JJ, JJR, JJS&rdquo; POS tags from Stanford POS Tagger toolkit</li>
</ul>
</li>
<li>Number of sentences starting with a pronoun
<ul>
<li>Counting if first tag of sentence&rsquo; is &ldquo;PRP, PRP$&rdquo; from POS tags from Stanford POS Tagger toolkit</li>
</ul>
</li>
<li>Short sentence rate
<ul>
<li>Calculate the percentage of sentences whose length is less than 15 words</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><strong><em>Text Length </em></strong>features used by (Rassbach, Pincock, &amp; Mingus, 2007; Blumenstock, 2008; Dalip, Lima, Cristo, &amp; Calado, 2014) such as word count, sentence count, and character count are related to the size of the text in different aspects. These features are useful in assessing whether the information is complete and comprehensive.
<ul>
<li>Character count
<ul>
<li>Total character length of each word</li>
</ul>
</li>
<li>Word count
<ul>
<li>Counting by using the method word_tokenize() from nltk to split a sentence into words</li>
</ul>
</li>
<li>Sentence count
<ul>
<li>Counting by using the method sent_tokenize() from nltk to split text into sentences</li>
</ul>
</li>
</ul>
</li>
<li><strong><em>The Level of Readability</em></strong> features are used as a way to verify if the text is well written, understandable, and free of unnecessary complexity. Flesch Kincaid Grade Level (FKGL) and Simple Measure of Gobbledygook (SMOG) indices are frequently used. In the calculation of SMOG, at least 30 sentences in a row near the beginning, in the middle and in the end are selected from text. The motivation behind this is health websites are expected to provide understandable health information regardless of age, background or reading level (Toolkit for producing patient information, 2003; Best Practice Guidance on Patient Information Leaflets, 2014; MedlinePlus Trusted Health Information for You, 2018).</li>
</ul>
<div align="center"><p><em>SMOG=1.0430&radic;(number of polysyllables*30/(number of sentences ))+3.1291</em></p></div>
<div align="center"><em>FKGL=0.39((total words)/(total sentences))+11.8 ((total syllables)/(total words))-15.59</em></p></div>
<p>Apart from adopted features, the following feature set was developed:</p>
<ul>
<li><strong><em>Text Sentence Type</em></strong> features are constructed to analyse the types of sentences. Unlike other studies, sentence types were used as a feature in this study. The motivation behind this is health websites generally use imperative and declarative sentences to guide patients. Five different types of sentences in English were considered: Imperative, Interrogative, Exclamatory, Existential and Declarative. Table 1 shows an example for each sentence type.</li>
</ul>
<div align="center"><p>Table 1: Examples of sentence types</p>
<table style="margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td width="142">
<p><strong>Sentence types</strong></p>
</td>
<td width="366">
<p><strong>Examples</strong></p>
</td>
</tr>
<tr>
<td width="142">
<p>Imperative sentences</p>
</td>
<td width="366">
<p>&ldquo;<em>Monitor</em> your blood glucose every three to four hours.&rdquo;</p>
</td>
</tr>
<tr>
<td width="142">
<p>Interrogative sentences</p>
</td>
<td width="366">
<p>&ldquo;How do insulin pumps work<em>?</em>&rdquo;</p>
</td>
</tr>
<tr>
<td width="142">
<p>Exclamatory sentences</p>
</td>
<td width="366">
<p>&ldquo;Initially take it slow you don't want to start off too hard, if you are not used to the exercise you will be sore the next day and this will not make exercising a fun experience<em>!</em>&rdquo;</p>
</td>
</tr>
<tr>
<td width="142">
<p>Existential sentences</p>
</td>
<td width="366">
<p>&ldquo;<em>There</em> are different types of insulin depending on how quickly they work, when they peak, and how long they last.&rdquo;</p>
</td>
</tr>
<tr>
<td width="142">
<p>Declarative sentences</p>
</td>
<td width="366">
<p>&ldquo;Inside the pancreas, beta cells make the hormone insulin.&rdquo;</p>
</td>
</tr>
</tbody>
</table></div>
<p>&nbsp;</p>
<ul style="list-style-type: circle;">
<li>If the first word of the sentence is a verb (&ldquo;VB, VBD, VBG, VBN, VBP, VBZ&rdquo; POS tags), then the sentence is labelled as imperative.</li>
<li>The sentence is marked as an interrogative sentence when it has a question mark (?).</li>
<li>If it has an exclamation mark (!), it is regarded as an exclamatory sentence.</li>
<li>An existential sentence is a sentence that asserts the existence or nonexistence of something; if a sentence starts with existential &ldquo;there&rdquo; (&ldquo;DT, EX&rdquo; POS tags), it is considered as an existential sentence.</li>
<li>The rest of the sentences apart from these in the text are labelled as declarative.</li>
</ul>
<ul>
<li><strong><em>Lexical variety</em></strong> is the normalized measure of the unique words used in a text with all words. The motivation behind this is if a website is comprehensive, the lexical variety is expected to be high.</li>
</ul>
<div align="center"><em>Lexical variety=(number of unique words)/(number of words)</em></p></div>


