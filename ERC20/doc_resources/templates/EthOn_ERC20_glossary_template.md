# EthOn ERC-20 Token extension Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ERC-20 ontology extension.
Please also consider looking at the [specification of ERC-20 EthOn extension](http://ethon.consensys.net/ERC20/EthOn_ERC20_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.

{%- for letter, terms in glossary.iteritems() %}
## {{ letter }}
{%- for term, description in terms.iteritems() %}
### {{ term }}
{{ description}}
{%- endfor %}
{%- endfor %}