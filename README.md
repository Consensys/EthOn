# EthOn - An Ethereum Ontology
_An Ethereum ontology that is closely aligned with the [Ethereum yellow paper](https://github.com/ethereum/yellowpaper)._

__Contributors:__
* Johannes Pfeffer (ontology engineering)
* Shahan Khatchadourian (ontology engineering)
* Herman Junge (domain knowledge)
* Maurycy (domain knowledge)
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

## 4 approaches to understanding EthOn
### 1. Look at the concept illustrations
#### Account concept
![Account concept](https://github.com/ConsenSys/ethereum-ontology/blob/master/spec_resources/img/account_concept.png)
#### Block concept
![Block concept](https://github.com/ConsenSys/ethereum-ontology/blob/master/spec_resources/img/block_concept.png)
#### Message concept
![Message concept](https://github.com/ConsenSys/ethereum-ontology/blob/master/spec_resources/img/message_concept.png)
#### Illustration key
![Illustration key](https://github.com/ConsenSys/ethereum-ontology/blob/master/spec_resources/img/key.png)

### 2. Visualize the Ontology
Visualize the ontology using [WebVOWL](http://vowl.visualdataweb.org/webvowl/).
[It should be enough to click this link](http://vowl.visualdataweb.org/webvowl/#iri=https://raw.githubusercontent.com/ConsenSys/ethereum-ontology/master/ethon.rdf?token=ABeN2FXA5BqQMkSypsnxRyvsbDQwgZGKks5YUVL0wA%3D%3D). 
WebVWOL is also developed on GitHub: https://github.com/VisualDataWeb/WebVOWL

### 3. Look at the specification
You can look at the specification that is generated automatically. Just clone the repo and open _ethon_spec.html_ in a browser.

There is also a fancy specification generator http://hacks.michelepasin.org/ontospy/. See https://github.com/lambdamusic/OntospyWeb.

### 4. Open the ontology in Protégé
Download [Protégé](http://protege.stanford.edu/) and open the ontology file to browse around and view all assertions.