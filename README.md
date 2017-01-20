# EthOn - An Ethereum Ontology
_An Ethereum ontology that is closely aligned with the [Ethereum yellow paper](https://github.com/ethereum/yellowpaper)._

An ontology is a formalization of concepts and relations within a domain.
EthOn is written in [RDF](https://de.wikipedia.org/wiki/Resource_Description_Framework) and [OWL](https://en.wikipedia.org/wiki/Web_Ontology_Language).

## Status and scope
EthOn is currently under heavy development. It is not complete, nor ever will be, probably. The goal is to model Ethereum 
as a [State Transition System](https://en.wikipedia.org/wiki/Transition_system).

EthOn is not canonical (i.e. "official"). However, it might be submitted as an EIP at some point in the future.

For information on [contributing](https://github.com/ConsenSys/EthOn/wiki/How-to-contribute-to-EthOn), [versioning](https://github.com/ConsenSys/EthOn/wiki/Versioning-system) and [usage](https://github.com/ConsenSys/EthOn/wiki/Usage), please have a look at the [wiki](https://github.com/ConsenSys/EthOn/wiki).

### Extensions
* [ERC-20](ERC20) - Adds modeling for ERC-20 tokens

### EthOn can be used
* as a [glossary of Ethereum terms](EthOn_glossary.md)
* as a learning ressource for understanding Ethereum and the yellow paper
* as a means to improve communication (among developers, among technical and non-technical people, ...)
* for checking the consistency of modeled aspects of blockchain data via reasoning
* to semantically annotate content provided by Ethereum based tools and dApps (e.g. block explorers, analysis tools, markets, ...)

### EthOn covers the following major Ethereum concepts:
* _Blockchain and State Transition concepts:_ Blocks, Accounts, Transactions, Contract Messages, Block-, Transaction-, Message- and World-State, 
State Transition
* _Network concepts:_ Blockchain, Node, Protocol Variant, Fork, Network

### The following aspects are not covered (yet):
* EVM states and EVM execution
* Relation to other blockchain implementations, e.g. Bitcoin

## Five approaches to understanding EthOn
### 1. Look at simplified EthOn model of Ethereum
![EthOn model](doc_resources/img/EthOn_overview.png)

Find more illustrations here: [EthOn illustrations](EthOn_illustrations.md)

### 2. Visualize the Ontology
Visualize the ontology using [WebVOWL](http://vowl.visualdataweb.org/webvowl/).
[It should be enough to click this link](http://vowl.visualdataweb.org/webvowl/#iri=https://raw.githubusercontent.com/ConsenSys/ethereum-ontology/master/EthOn.rdf). 
WebVWOL is also developed on GitHub: https://github.com/VisualDataWeb/WebVOWL

### 3. Read the specification
You can look at the automatically generated [EthOn specification](https://consensys.github.io/EthOn/EthOn_spec.html).

There is another more fancy specification generator available: http://hacks.michelepasin.org/ontospy/. The GitHub project page can be found here: https://github.com/lambdamusic/OntospyWeb.

### 4. Open the ontology in Protégé
Download [Protégé](http://protege.stanford.edu/) and open the ontology file to browse around and view all assertions.

### 5. Look at some examples
Among other things, EthOn can be used to formally describe Ethereum artefacts. 
The following [Turtle](https://www.w3.org/TR/turtle/) snippet is a description of the Genesis Block of the current Ethereum main net.
#### Describing an Account
    @prefix ethon: <http://ethon.consensys.net/>
    @prefix ethereum: <http://ethereumrdf.consensys.net/>
    
    ethereum:Account0000000000000000000000000000000000000000
        a ethon:Account ;
        rdfs:label "Genesis Address" ;
        ethon:address "0000000000000000000000000000000000000000"^^xsd:hexBinary ;
        ethon:hasState ethereum:AccountState0 ;
        [...]
        rdfs:seeAlso <https://etherscan.io/address/0x0000000000000000000000000000000000000000> .
    
    ethereum:AccountState0
        ethon:accountBalance 0 ;
        [...]
        ethon:accountNonce 0 .
        

#### Describing a Block

    ethereum:Block0
        a ethon:Block ;
        rdfs:label "Genesis Block" ;
        rdfs:comment "This is the block with block number 0. It is the Genesis Block of the Ethereum blockchain." ;
        ethon:number 0 ;
        ethon:blockBeneficary ethereum:Account0000000000000000000000000000000000000000 ;
        ethon:blockReward 5000000000000000000 ;
        ethon:gasLimit 5000 ;
        ethon:blockNonce "0000000000000042"^^xsd:hexBinary ;
        [...]
        rdfs:seeAlso <https://etherscan.io/block/0> .

## "EthOn"?
Ethon is in Greek, Latin and Indian mythology the name of one of the horses [that pull the sun across the sky](https://books.google.de/books?id=mvLBAgAAQBAJ&pg=PA121&hl=en&q=ethon&f=false#v=snippet&q=ethon&f=false).
