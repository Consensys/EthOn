# EthOn Contracts extension Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn Contracts ontology extension.
Please also consider looking at the [specification of Contracts EthOn extension](http://ethon.consensys.net/Contracts/EthOn_Contracts_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.

{%- for letter, terms in glossary.iteritems() %}
## {{ letter }}
{%- for term, description in terms.iteritems() %}
### {{ term }}
{{ description}}
{%- endfor %}
{%- endfor %}