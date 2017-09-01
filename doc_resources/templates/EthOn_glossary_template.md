# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
Please also consider looking at the [specification of EthOn](http://ethon.consensys.net/EthOn_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.

{%- for letter, terms in glossary.iteritems() %}
## {{ letter }}
{%- for term, description in terms.iteritems() %}
### {{ term }}
{{ description}}
{%- endfor %}
{%- endfor %}