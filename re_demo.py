'''
past the stanford-corenlp-full-2016-10-31 in the current directory
export CLASSPATH=./stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar:./stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar
python3 -m pynlp (for running the server in the other terminal) 
'''

from pynlp import StanfordCoreNLP
import re

data = "Unlike some jobs in the U.S., there’s no clear educational path to becoming a venture capitalist. Doctors (Dr.) have medical school. Lawyers have law school. Plumbers, electricians, welders, barbers, bartenders, and plenty of other trades have schools of their own. Some VCs were educated in the “school of hard knocks” by founding and building successful startups; however, many went to business schools. Others came to entrepreneurial finance after careers as academics and researchers. The educational backgrounds of VC investment professionals are in some ways surprisingly diverse, even if the population of investors generally isn’t. Still, there are some definite trends to suss out at all levels of the educational continuum, and that’s what we’re going to do today. Using Crunchbase data for approximately 4,500 US and Canadian investment partners—individuals associated with a particular investment firm who have made at least one investment on behalf of those firms—we extracted information about their educational backgrounds and alumni affiliations. In the following analysis, we’ll take a broad look at these two areas, looking first at alumni affiliations."

annotators = 'tokenize, ssplit'
nlp = StanfordCoreNLP(annotators=annotators)

parse_output = nlp(data)

for i in range(0, 5):
    print(parse_output[i])        
