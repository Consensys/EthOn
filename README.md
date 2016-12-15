# EthOn - An Ethereum Ontology
_An Ethereum ontology that is closely aligned with the [Ethereum yellow paper](https://github.com/ethereum/yellowpaper)._

An ontology is a formalization of concepts and relations within a domain.
EthOn is written in [RDF](https://de.wikipedia.org/wiki/Resource_Description_Framework) and [OWL](OWL).
__Contributors:__
* Johannes Pfeffer (ontology engineering)
* Shahan Khatchadourian (ontology engineering)
* Herman Junge (requirements, ethereum knowledge)
* Maurycy (requirements, ethereum knowledge)
* Marian Oancea (domain knowledge)
* Casey Detrio cdetrio@gmail.com (ethereum internals)
* Alex Beregszaszi (ethereum internals)
* Stefano Bertolo <stefano@ethereum.org> (review, testing)

## Status and scope
EthOn is currently under heavy development. It is not complete, nor ever will be, probably. The goal is to model Ethereum as a [State Transition System](https://en.wikipedia.org/wiki/Transition_system).

EthOn can be used
* as a glossary of Ethereum terms
* as a learning ressource for understanding Ethereum and the yellow paper
* as a means to improve communication (among developers, among technical and non-technical people, ...)
* for checking the consistency of modeled aspects of blockchain data via reasoning
* to semantically annotate content provided by Ethereum based tools and dApps (e.g. block explorers, analysis tools, markets, ...)
(incomplete list)

## Five approaches to understanding EthOn
### 1. Look at simplified EthOn model of Ethereum
![EthOn model](doc_resources/img/EthOn_model.png)

Find more illustrations here: [EthOn illustrations](EthOn_illustrations.md)

### 2. Visualize the Ontology
Visualize the ontology using [WebVOWL](http://vowl.visualdataweb.org/webvowl/).
[It should be enough to click this link](http://vowl.visualdataweb.org/webvowl/#iri=https://raw.githubusercontent.com/ConsenSys/ethereum-ontology/master/EthOn.rdf?token=ABeN2BS6JNYwG2ADzI7vBJihTu02xpgjks5YWBKpwA%3D%3D). 
WebVWOL is also developed on GitHub: https://github.com/VisualDataWeb/WebVOWL

### 3. Look at the specification
You can look at the specification that is generated automatically. Just clone the repo and open _EthOn_spec.html_ in a browser.

There is also a fancy specification generator http://hacks.michelepasin.org/ontospy/. See https://github.com/lambdamusic/OntospyWeb.

### 4. Open the ontology in Protégé
Download [Protégé](http://protege.stanford.edu/) and open the ontology file to browse around and view all assertions.

### 5. Look at some examples
Among other things, EthOn can be used to formally describe Ethereum artefacts. 
The following [Turtle](https://www.w3.org/TR/turtle/) snippet is a description of the Genesis Block of the current Ethereum main net.
#### Describing an Account
    @prefix ethon: http://consensys.net/ethereum-ontology/
    @prefix ethereum: http://consensys.net/ethereum-data/
    
    ethereum:Account0000000000000000000000000000000000000000
        a ethon:Account ;
        rdfs:label "Genesis Address" ;
        ethon:address "0000000000000000000000000000000000000000"^^xsd:hexBinary ;
        ethon:hasState ethereum:AccountState0 ;
        rdfs:seeAlso <https://etherscan.io/address/0x0000000000000000000000000000000000000000> .
    
    ethereum:AccountState0
        ethon:accountBalance 0 ;
        ethon:accountNonce 0 .
        

#### Describing a Block

    ethereum:Block0
        a ethon:Block ;
        rdfs:label "Genesis Block" ;
        rdfs:comment "This is the block with block number 0. It is the Genesis Block of the Ethereum blockchain. ;
        ethon:number 0 ;
        ethon:blockBeneficary ethereum:Account0000000000000000000000000000000000000000 ;
        ethon:blockReward 5000000000000000000 ;
        ethon:gasLimit 5000 ;
        ethon:blockNonce "0000000000000042"^^xsd:hexBinary ;
        [...]
        rdfs:seeAlso <https://etherscan.io/block/0> .

## Axioms and constraints
Axioms are sentences in [description logic](https://en.wikipedia.org/wiki/Description_logic) statements. 
At this early stage only a few axioms have been defined in EthOn. The expressiveness will increase as the structure of
EthOn matures. The axioms can be used with reasoners to infer information from data. You can best have a look at them if you open EthOn in Protégé (see above).

### Some example axioms

__Informal statement:__ _Blocks_ have exactly one property _blockHash_ of type _xsd:hexBinary_.  
__EthOn axiom__ in [Manchester Syntax](https://www.w3.org/TR/owl2-manchester-syntax/): `Class: Block SubClassOf: blockHash exactly 1 xsd:hexBinary SubClassOf Block`
  
To be exact the axiom states "A Block is a subclass of the theoretical class of 'all things that have exactly one _blockHash_ property with a value of type _xsd:hexBinary_'".
We have specified a necessary but not sufficient condition. We are saying there might be other things that have a _blockHash_ and are not _Blocks_. 

Also, something that doesn't have such a property may still be a _Block_. We don't know, maybe it's just one that is not as well described (see [open world assumption](https://en.wikipedia.org/wiki/Open-world_assumption)).

__Informal statement:__ _Blocks_ with a _number_ of 0 are _Genesis Blocks_.  
__EthOn axiom__: `Block and (number some {"0"^^xsd:int}) EquivalentTo GenesisBlock`

__Informal statement:__ When a _Tx Receipt_ has a _post Tx state_, the _Tx_ itself has a _createsState_ property relation.  
__EthOn axiom__: `hasReceipt o hasPostTxState SubPropertyOf: createsState`

## Why "EthOn"?
Ethon is in Greek, Latin and Inidan mythology the name of one of the horses [that pull the sun across the sky](https://books.google.de/books?id=mvLBAgAAQBAJ&pg=PA121&hl=en&q=ethon&f=false#v=snippet&q=ethon&f=false).