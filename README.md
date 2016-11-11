# Ethereum Ontology
_This document is a collaborative effort to define the scope and goals of the ethereum ontology._

__List of people that have committed to contribute:__
* Johannes Pfeffer (ontology engineering)
* Shahan Khatchadourian (ontology engineering)
* Herman (vocabulary)
* Maurycy (vocabulary)
* Marian Oancea
* Casey Detrio cdetrio@gmail.com (foundation, ethereum internals)
* Stefano Bertolo <stefano@ethereum.org> (foundation, review, testing)
* Alex Beregszaszi (foundation contractor, EVM developer, ethereum internals)

Please suggest further ontology developers or domain experts in the #priv-team-alethio slack channel. The ontology team should not get much bigger than 10 as that becomes hard to manage.


## Preface
Ethereum is an ideal field of application for ontologies because a consensus about the semantics of the involved concepts is a prerequisite for reaching consensus about the state of the network. Any deviation from this consensus results in a fork. An ethereum ontology may serve as a semantic specification of its concepts that complements its technical specification.


## Motivation
Ontologies are formal and schematic descriptions of an area of knowledge. The concepts of the domain are collected into a curated vocabulary and then organized. It can be explicitly defined how concepts relate to each other and what rules exist for their existence and the relations between them. The conclusiveness of concepts and their relations is a function of the desired application of the ontology.

As an example in the ethereum domain there may be the concept of a block. All blocks must have a preceding and succeeding block. This is true with the exception of the very first block, which only has a successor and the newest block for which the successor has not yet been found. Also, a block may contain a list of transactions. Blocks also have an associated miner. In an ontology these domain concepts are formalized in an ontology language so that they can be referenced, queried and used for inference. Referencing an ontology can be useful in many scenarios. An ethereum block explorer could, for example, reference the block concept of the ontology to state that the term block used in its user interface is identical to the one defined in the ontology. An API, be it from an ethereum client or a wallet service, can reference ontological concepts to state compliance with a standard. Then the ontology can be used to verify that the API actually complies to it. Querying an ontology can be useful to retrieve definitions of technical terms, in order to create a glossary. If a piece of data is retrieved from an API that identifies it as a block the ontology can be queried to find out about it’s structure, ranges of values and relations to other concepts. An ontology can also be used to infer knowledge. If a block doesn’t have a predecessor it can be concluded that it must be the first block of a blockchain.

The ethereum ontology that shall be developed in this effort serves as a shared knowledge base for developers and analysts to improve communication amongst them. It will be used as a reference for database schemas and future ethereum related APIs. Since it is based on semantic web technologies (OWL, RDF) it can be used to semantically enhance existing ethereum related web applications.


## Development strategy
Development of an ontology is best done in a medium sized team comprised of ontology experts and stakeholders of the finished ontology. The most important roles in this process are ontology developers, domain experts and reviewers.

Based on experience and review of the body of literature (insert citations) the following methodology will be applied (to be discussed):

* Define Competency questions
* Make a list of key concepts
* Organize concepts
* Repeat steps 2 & 3
* Raise expressiveness by adding logic

The ontology will be developed in public. Each step (Competency questions, concepts and relations between concepts) will be subjected to peer review. All steps will have feedback loops and will be repeated as often as necessary to achieve a consensus.

It is a goal to achieve medium level of structure. That means that not all relations of concepts and restrictions must be formally defined. Some remain informally described in plain text. The level of expressiveness will be increased as the ontology matures.

Regarding scope and granularity, the ontology should cover at least all ethereum related concepts mentioned in the ethereum white and yellow papers and match the granularity of these.


## Governance
The ultimate owner of the ontology is the public domain. 
During development of the first public release read/write access may be restricted according to the development strategy.
This ethereum ontology strives to be recognized by the ethereum foundation as canonical. Therefore, contributors from the ethereum foundation are especially welcome to join the effort.


## Scope
The scope of the ontology is defined by the competency questions.
However it should be taken care that the scope stays narrow for the first iteration of the ontology.
Guidelines
* Stick to ethereum intrinsic concepts. That means the concept bitcoin will not be part of the ontology.
* Focus on concepts that are part of the state of the chain. For example the concepts block, transaction and nonce are relevant to the state of the chain while mining, double spend and decentralization are not.


## Initial specifications
### IRI structure
All entities in an OWL ontology have a unique identifier in form of an IRI. That means that a concept block might have a unique identifier of the form http://prefix.foo/block. 
The IRI prefix for all ethereum specific concepts shall be http://ontology.ethereum.org/2016/11/. Date and month resemble the release date. Until an agreement with the ethereum foundation has been reached, as an intermediate prefix http://consensys.net/ethereum-ontology/2016/11/ will be used.
The IRI prefix will have a slash at the end. Entities are speaking, i.e. not random, and should resemble a camelCase version of the rdfs:label property.

### Ontology language
The ontology will be expressed in RDF/RDFS.

### Tooling
The ontology will be developed directly on GitHub. Discussions will be done through issues. Documentation in the wiki.


## Matters to decide
* The ontology should be versioned and tagged to accommodate future changes in hard forks and potentially an ethereum 2.0. 


## Intended use of the ontology
* First tier
   1. Shared knowledge base for blockchain analytics and other uses
   2. Improve communication among developers
   3. Use as basis for database schemas (graph or relational)
   4. Potentially use as reference for any future ethereum related APIs/Interfaces
   5. Verification of instances of the ontology, i.e. blockchain databases
* Second tier
   1. Automated reasoning across datasets
   2. Enable semantic web block explorers and dApps
