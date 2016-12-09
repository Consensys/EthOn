# EthOn Glossary
This glossary is compiled of the _rdfs:comment_ annotations of the EthOn ontology.

{%- for letter, terms in glossary.iteritems() %}
## {{ letter }}
{%- for term, description in terms.iteritems() %}
### {{ term }}
{{ description}}
{%- endfor %}
{%- endfor %}