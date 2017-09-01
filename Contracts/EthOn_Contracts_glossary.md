# EthOn Contracts extension Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn Contracts ontology extension.
Please also consider looking at the [specification of Contracts EthOn extension](http://ethon.consensys.net/Contracts/EthOn_Contracts_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.
## A
## B
## C
### calls Function
[`ethon:callsFunction`](http://ethon.consensys.net/Contracts/callsFunction)   
Relates a Function Call to the Function that is called by it.
### cost
[`ethon:cost`](http://ethon.consensys.net/Contracts/cost)   
Specifies the amount of gas that has to be paid to execute an Opcode.
## D
### Dynamic Function
[`ethon:DynamicFunction`](http://ethon.consensys.net/Contracts/DynamicFunction)   
Dynamic Functions are Functions that potentially change the state of the blockchain when executed. Executing a dynamic function costs gas and is broadcast to the network. When a Dynamic Function is called, the resulting computation is carried out by every Full Node in the Network.
## E
### EthOn Contracts Data Property
[`ethon:EthOnContractsDataProperty`](http://ethon.consensys.net/Contracts/EthOnContractsDataProperty)   
Groups all EthOn Contracts extension Data Properties.
### EthOn Contracts Object Property
[`ethon:EthOnContractsObjectProperty`](http://ethon.consensys.net/Contracts/EthOnContractsObjectProperty)   
Groups all EthOn Contracts extension Object Properties
### Event
[`ethon:Event`](http://ethon.consensys.net/Contracts/Event)   
Events are structures implemented in smart contracts in order to create a LogEntry. Once created they cannot be accessed from the contract but can be used from the outside, e.g. by a web application that reacts to Events in a smart contract.
## F
### Function
[`ethon:Function`](http://ethon.consensys.net/Contracts/Function)   
Functions are structures in smart contracts that implement functionality, just as functions or methods do in general programming. Functions can be called by Accounts (External Accounts or Contract Accounts) to execute the code stored in it. Functions can have Inputs (parameters) and Outputs (return values).
### Function Call
[`ethon:FunctionCall`](http://ethon.consensys.net/Contracts/FunctionCall)   
Functions Calls are calls to Functions that are recorded in the blockchain. They are a subset of all Messages in a blockchain. Examples for Function Calls are Transactions (which is a sub-type of a Message) that call a Dynamic Function in a smart contract and Contract Calls that call Dynamic or Static Functions in smart contracts. Function Calls originate from either an External Account or a Contract Account and are always directed towards Contract Accounts.
### function Selector
[`ethon:functionSelector`](http://ethon.consensys.net/Contracts/functionSelector)   
A function can be identified by its function Selector. It is generated from an abbreviated version of the signature. For example the Function bar(uint32 x, bool y) returns (bool r) has the abbreviated signature bar(uint32,bool). The first 4 bytes of the Keccac 256 hash of this forms the functionSelector of the Function, in the example that would be 0xcdcd77c0.
## G
## H
### has Input
[`ethon:hasInput`](http://ethon.consensys.net/Contracts/hasInput)   
Relates an Event or a Function to an Input of that Event or Function. An Event or Function may have 0 or more Inputs but an Input can only belong to a single Event or Function.
### has Input Value
[`ethon:hasInputValue`](http://ethon.consensys.net/Contracts/hasInputValue)   
Relates a FunctionCall or a LogEntry to an Input Value that is represented by it. For example a Function Call add(5,6) would be related to two Input Values, one for each Input to the Function.
### has Output
[`ethon:hasOutput`](http://ethon.consensys.net/Contracts/hasOutput)   
Relates a Function to an Output of that Function. A Function may have 0 or more Outputs but an Output can only belong to a single Function.
### has Output Value
[`ethon:hasOutputValue`](http://ethon.consensys.net/Contracts/hasOutputValue)   
Relates a FunctionCall to an Output Value that is represented by it. For example a Function Call add(5,6) that returns the sum of two integers would be related to one Output Value, that contains the result of the addition.
### hex Value
[`ethon:hexValue`](http://ethon.consensys.net/Contracts/hexValue)   
Specifies the hexadecimal code that represents an Opcode. This is the actual value used for the Opcode in byte code.
## I
### Input
[`ethon:Input`](http://ethon.consensys.net/Contracts/Input)   
An Input represents a single input parameter of a Function or an Event. It's properties include a data type of the Input Value a name and a position in the signature of its Function or Event. 

If it represents an Input of an Event it can have the boolean property isIndexed. If true, the values of this Input should be stored in a modified merkle patricia tree structure and be created as LogTopics to be easily queryable. Otherwise the value is stored in the data of a LogEntry.
### Input Value
[`ethon:InputValue`](http://ethon.consensys.net/Contracts/InputValue)   
Represents an Input Value of a Function Call or or a Log Entry. For example, if a smart contract has the function decryptXY(string x, bytes32 y) and the function is called in a Message, the two input values are each represented by an instance of this class. The value itself is a direct data property of this class, while the data type, the position and name are data properties of the the Input of this Input Value.
### implements Event
[`ethon:implementsEvent`](http://ethon.consensys.net/Contracts/implementsEvent)   
Relates a Contract Account to Events it implements.
### implements Function
[`ethon:implementsFunction`](http://ethon.consensys.net/Contracts/implementsFunction)   
Relates a Contract Account to Functions it implements.
### is anonymous
[`ethon:isAnonymous`](http://ethon.consensys.net/Contracts/isAnonymous)   
Specifies if an Event is anonymous. Anonymous Events will not store the Event signature as the LogTopic of a LogEntry.
### is constant
[`ethon:isConstant`](http://ethon.consensys.net/Contracts/isConstant)   
Functions with the property isConstant set to true promise to not modify the state of the blockchain. For instance, in solidity this can be achieved by a function modifier that declares the function to be constant (solidity doesn't enforce this, yet).
### is indexed
[`ethon:isIndexed`](http://ethon.consensys.net/Contracts/isIndexed)   
True if the Input of an Event should be stored as a LogTopic of a LogEntry. Up to three parameters can receive this property which will cause the respective arguments to be treated as LogTopics instead of data. All non-indexed arguments will be stored in the data part of the LogEntry that represents the Event.
### is payable
[`ethon:isPayable`](http://ethon.consensys.net/Contracts/isPayable)   
True if a Function can receive Ether together with a FunctionCall.
## J
## K
## L
## M
## N
### name
[`ethon:name`](http://ethon.consensys.net/Contracts/name)   
A property that defines the name of Functions, Events, Inputs, Outputs and Opcodes as specified in code or specification. There can be only one name for each Individual of these types.
## O
### Opcode
[`ethon:Opcode`](http://ethon.consensys.net/Contracts/Opcode)   
An Opcode an instruction in the instruction set of the Ethereum virtual machine. The set of existing Opcodes are defined as Individuals (instances) of this class.
### Output
[`ethon:Output`](http://ethon.consensys.net/Contracts/Output)   
An Output represents a single return value of a Function in a smart contract. It's properties include a data type of the Output Value, a name and a position in the signature of its Function.
### Output Value
[`ethon:OutputValue`](http://ethon.consensys.net/Contracts/OutputValue)   
Represents an Output Value of a Function Call. For example, if a smart contract has the function decryptXY(string x, bytes32 y) returns(string) and the function is called in a Contract Message, the returned string is represented as an instance of this class. The return value itself is a direct data property of this class, while the data type, the position and name are data properties of the the Output of this Output Value.
### of Input
[`ethon:ofInput`](http://ethon.consensys.net/Contracts/ofInput)   

### of Output
[`ethon:ofOutput`](http://ethon.consensys.net/Contracts/ofOutput)   
Relates an Output Value to the Output it is a value of.
## P
### position
[`ethon:position`](http://ethon.consensys.net/Contracts/position)   
Specifies the position of the Input or Output parameter in an Event's or Function's signature.
## Q
## R
### represents Event
[`ethon:representsEvent`](http://ethon.consensys.net/Contracts/representsEvent)   
Relates a LogEntry to the Event it represents.
## S
### Static Function
[`ethon:StaticFunction`](http://ethon.consensys.net/Contracts/StaticFunction)   
Static Functions are Functions don't change the state of the blockchain. They can be executed on the local copy of the blockchain and it's not necessary to broadcast the call to the network. Calling a Static Function doesn't cost any gas. They are only executed by the node calling it.
### signature
[`ethon:signature`](http://ethon.consensys.net/Contracts/signature)   
The signature of the function in the canonical form which is used to create the functionSelector. Example: "bar(uint32,bool)"
### stack items added
[`ethon:stackItemsAdded`](http://ethon.consensys.net/Contracts/stackItemsAdded)   
Specifies the number of items added to the stack by executing an Opcode.
### stack items removed
[`ethon:stackItemsRemoved`](http://ethon.consensys.net/Contracts/stackItemsRemoved)   
Specifies the number of items removed from the stack when executing an Opcode.
## T
### topic
[`ethon:topic`](http://ethon.consensys.net/Contracts/topic)   
An Event can be identified by its topic. It is generated from an abbreviated version of its signature. For example the Event Foo(uint32 x, bool y) has the abbreviated signature Foo(uint32,bool). The Keccac 256 hash of this forms the event topic.
### type
[`ethon:type`](http://ethon.consensys.net/Contracts/type)   
Specifies the canonical type of the Input or Output, e.g. uint32.
## U
### uses Opcode
[`ethon:usesOpcode`](http://ethon.consensys.net/Contracts/usesOpcode)   
Relates a Contract Account to an Opcode used in the code of that Account.
## V
### value
[`ethon:value`](http://ethon.consensys.net/Contracts/value)   
The actual value of an InputValue or OutputValue. It is of the type defined in the Input or Output of the InputValue or OutputValue.
## W
## X
## Y
## Z