# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
## A
### Account
`ethon:Account`   
Accounts have an intrinsic balance and transaction count maintained as part of the Ethereum state. They also have some (possibly empty) EVM Code and a (possibly empty) Storage State associated with them. Though homogenous, it makes sense to distinguish between two practical types of Account: those with empty associated EVM Code (thus the Account balance is controlled, if at all, by some external entity) and those with non-empty associated EVM Code (thus the Account represents an Autonomous Object). Each Account has a single Address that identifies it.
### Account State
`ethon:AccountState`   
State of an Ethereum Account. It is comprised on four pieces of information: nonce, balance, storage root and code hash. The data is stored in a Merkle Patricia tree as a mapping between addresses and Account states. The Account State is part of the World State, as it resembles the state of exactly one Account.
### Account balance
`ethon:accountBalance`   
A scalar value equal to the number of Wei owned by an Account at a given Account state.
### Account code
`ethon:accountCode`   
The imutable EVM bytecode of the Contract Account.
### Account code hash
`ethon:accountCodeHash`   
The immutable hash of the EVM code of an Account.
### Account nonce
`ethon:accountNonce`   
A scalar value equal to the number of transactions sent from this Account or, in the case of Accounts with associated code, the number of Contract-creations made by this Account.
### Address
`ethon:address`   
A 160-bit identifier for Accounts.
### Autonomous Object
`ethon:AutonomousObject`   
This is a more abstract term for a Contract Account.
## B
### Block
`ethon:Block`   
A Block is the basic element of a Blockchain. It functions as a journal, recording a series of transactions together with a reference to the previous Block. A Block is chained to its preceeding Block by a cryptographic hash as a means of reference. Blocks contain an identifier for the final state after all transactions contained in it are validated. There is an incentive mechanism that provides incentives to generate new Blocks ("mine Blocks") that comply to the rules of Ethereum by issuing a reward to an Account specified by the miner.
### Block Timestamp
`ethon:blockCreationTime`   
This Block's inception date and time.
### Block difficulty
`ethon:blockDifficulty`   
A scalar value corresponding to the difficulty level of this Block. This can be calculated from the previous Block's difficulty level and the timestamp.
### Block extra data
`ethon:blockExtraData`   
An arbitrary byte array containing data relevant to this Block. This must be 32 bytes or fewer.
### Block hash
`ethon:blockHash`   
The Keccak 256-bit hash of the Block's header, in its entierty.
### Block header
`ethon:blockHeader`   
Relates a Block to its Block header data. The Block header data contains 15 pieces of information: 1. the parent hash, 2. the Ommers hash, 3. a beneficiary address, 4. a state root hash, 5. a transactions root hash, 6. a receipts root hash, 7. a log bloom filter, 8. the difficulty value, 9. the Block number, 10. the gas limit of the Block, 11. the gas used by all transactions in the Block, 12. a scalar timestamp in unix time() format, 13. a byte array containing extra data, 14. a mix hash and 15. the Block nonce. The property is functional because a Block can have only exactly one Block header.
### Block nonce
`ethon:blockNonce`   
A 64 bit hash which proves combined with the mix-hash that a sufficient amount of computation has been carried out on this Block.
### Block number
`ethon:number`   
A scalar value equal to the number of ancestor Blocks. The genesis Block has a number of zero.
### Block reward
`ethon:blockReward`   
Also base reward, amount of Wei a miner gets for finding a Block.
## C
### Call Contract Message
`ethon:CallContractMsg`   
A Call Contract Message is a Contract Message that calls a function in another Contract.
### Call Transaction
`ethon:CallTx`   
A type of Transaction that is directed towards a Contract Account and calls a method in the Contract's code.
### Contract Account
`ethon:ContractAccount`   
A notional object existent only within the hypothetical state of Ethereum. Has an intrinsic address and thus an associated Account; the Account will have non-empty associated EVM Code. Incorporated only as the Storage State of that Account.
### Contract Message
`ethon:ContractMsg`   
A Contract Message is passed between a Contract Account and any other Account (External or Contract). It is the result of an execution chain originally triggered by an External Account.
### Create Contract Message
`ethon:CreateContractMsg`   
A create Contract Message is a special type of Contract Message that results in creation of a new Contract.
### Create Transaction
`ethon:CreateTx`   
A type of Transaction that results in creation of a new Contract Account.
### call data
`ethon:data`   
An unlimited size byte array specifying the input data of the call.
### conforms to
`ethon:conformsTo`   
Relates an Ethereum concept to the Ethereum Protocol Variant it conforms to.
### contains Transaction
`ethon:containsTx`   
Relates a Block to a Transaction included in it. All containsTx relations of a Block comprise the Block's transaction list. The order of the transactions is determined by their index value. The property is inverse functional because a Transaction can only be included in one Block.
### controls Account
`ethon:controlsAccount`   
This property connects an External Actor an Account that it controls. This means the External Actor has control over the private Key for the Account. The control is not necessarily legitimate.
### creates
`ethon:creates`   
Relates a create transaction to the Contract Account it creates.
### creates State
`ethon:createsState`   
Relates a Transition to the State it creates.
### creates post Block execution State
`ethon:createsPostBlockState`   
Relates a Block to the global state of the system after all Transactions in the Block have been executed.
### creates post Transaction execution State
`ethon:createsPostTxState`   
Relates a Transaction Receipt to the global state of the system after the Receipt's Transaction has been executed.
### cumulative gas used
`ethon:cumulativeGasUsed`   
The cumulative gas used in the block containing the Transaction Receipt as of immediately after the Transaction has happened.
## D
## E
### EthOn Account Data Property
`ethon:AccountDataProperty`   
Groups all Data Properties that are specific to an Account.
### EthOn Account Object Property
`ethon:AccountObjectProperty`   
Groups all EthOn Account Object Properties
### EthOn Account concept
`ethon:AccountConcept`   
Groups EthOn concepts related to Accounts.
### EthOn Block Data Property
`ethon:BlockDataProperty`   
Groups all Data Properties that are specific to a Block. These properties are usually functional because a Block can only be associated with a single instance of them.
### EthOn Block Object Property
`ethon:BlockObjectProperty`   
Groups all EthOn Block Object Properties
### EthOn Block concept
`ethon:BlockConcept`   
Groups EthOn concepts related to Blocks.
### EthOn Concept
`ethon:EthOnConcept`   
Groups al EthOn concepts.
### EthOn Data Property
`ethon:EthOnDataProperty`   
Groups all Data Properties specific to EthOn.
### EthOn Message concept
`ethon:MessageConcept`   
Groups EthOn concepts related to Messages.
### EthOn Network Concept.
`ethon:NetworkConcept`   
Groups all EthOn Network concepts.
### EthOn Network Data Property
`ethon:NetworkDataProperty`   
Groups all EthOn Network Data Properties.
### EthOn Network Object Property
`ethon:NetworkObjectProperty`   
Groups all EthOn Network Object Properties.
### EthOn Object Property
`ethon:EthOnObjectProperty`   
Groups all EthOn Object Properties
### EthOn State Concept
`ethon:StateConcept`   
Groups EthOn concepts related to state.
### EthOn State Object Property
`ethon:StateObjectProperty`   
Groups all EthOn State Object Properties.
### Ethereum Blockchain
`ethon:Blockchain`   
An Ethereum Blockchain is a distributed database that maintains a continuously-growing list of records called *Blocks* secured from tampering and revision. Each Block contains a timestamp and a link to a previous Block in a Merkle tree structure.
### Ethereum Full Node
`ethon:FullNode`   
A Full Node is a participant in an Ethereum Network that keeps a record of the full Blockchain, the full state and engages in mining.
### Ethereum Light Node
`ethon:LightNode`   
A light node is a participant in an Ethereum Network that does not completely do any of the following: store the complete Blockchain, store the complete world state, engage in mining.
### Ethereum Network
`ethon:Network`   
An Ethereum network is the group of all Nodes that conform to a certain Protocol Variant.
### Ethereum Protocol Variant
`ethon:ProtocollVariant`   
A variant of the Ethereum protocol. Changes in the protocol result in a hard or soft fork.
### External Actor
`ethon:ExternalActor`   
A person or other entity able to interface to an Ethereum node, but External to the world of Ethereum. It can interact with Ethereum through depositing signed Transactions and inspecting the Blockchain and associated state. Has one (or more) intrinsic Accounts. While it is assumed that the ultimate External actor will be human in nature, software tools will be used in its construction and dissemination.
### Externally controlled Account
`ethon:ExternalAccount`   
An Account owned by an External Actor.
## F
### from
`ethon:from`   
Relates a Message with the Account it originates from.
## G
### Gas limit
`ethon:blockGasLimit`   
A scalar value equal to the current limit of gas expenditure per Block.
### Gas used
`ethon:blockGasUsed`   
A scalar value equal to the total gas used in transactions in this Block.
### Genesis Block
`ethon:GenesisBlock`   
A Genesis Block is the unmined, deliberately created, very first Block in a Blockchain. It has no predecessors, i.e. no parent Block.
## H
### has Account Storage
`ethon:hasAccountStorage`   
Relates an Account to the Merkle Patricia tree that encodes its storage contents at a certain Account State. This property is Functional because an Account State can have only one Instance of Account Storage and Inverse Functional because an Account Storage can have only one associated Account State.
### has Fork
`ethon:hasFork`   
Relates a Protocol variant to a forked version of it. It is inverse functional because a forked Blockchain can have only one Blockchain it forked from. It is Transitive because if a Blockchain C that was forked from Blockchain B that in turn was forked from Blockchain A, Blockchain C was also forked from Blockchain A. It is assymetric because if Blockchain A is forked from Blockchain B, B cannot be also forked from A. It is irreflexive because a Blockchain cannot be a fork of itself.
### has Log Entry
`ethon:hasLogEntry`   
Relates a Transaction Receipt to a Log Entry created by the Transaction of the Receipt.
### has Log Topic
`ethon:hasLogTopic`   
Relates a Log Entry to a Log Topic.
### has Transition
`ethon:hasTransition`   
Relates a State to a Transition (i.e. a Message) that creates a new State.
### has beneficiary
`ethon:hasBeneficiary`   
Relates a Block to the Account to which all fees collected from the successful mining of this Block are transferred.
### has current State
`ethon:hasCurrentState`   
This property relates an EthOn concept to its most current state.
### has parent Block
`ethon:hasParentBlock`   
Relates a Block to its parent in the chain. It always points to the Block with a number that is decreased by one, compared to the Block it originates from. The relation is asymmetric because if Block A is parent to Block B then Block B can not be parent to Block A. It is also irreflexive because a Block cannot be parent to itself.
### has receipts tree
`ethon:hasReceiptsTrie`   
Relates a Block to the Trie that contains the Block's receipt data.
### has state
`ethon:hasState`   
This property relates an EthOn concept to a state. It is inverse functional because a state can only belong to one single EthOn concept. Only some EthOn concepts have associated states. This is defined in the domain restriction.
### has transaction receipt
`ethon:hasReceipt`   
Relates a transaction to its receipt.
### has transactions trie
`ethon:hasTxTrie`   
Relates a Block to the trie that contains the data of the transactions contained in the Block.
## I
### init code
`ethon:init`   
An unlimited size byte array specifying the EVM-code for the account initialisation procedure.
## J
## K
### knows of Ommer
`ethon:knowsOfOmmer`   
Relates a Block to a known Ommer.
## L
### Log Entry
`ethon:LogEntry`   
A Log Entry is a tuple of a logger's address (i.e. the Account with that address), a series of 32-bytes Log Topics and some number of bytes of data.
### Log Topic
`ethon:LogTopic`   
A 32-bytes long topic of a LogEntry. The LogTopics of a LogEntry have an order given by a topicIndex value.
### Log Topic data
`ethon:topicData`   
Relates a Log Topic to the 32 bytes of data it contains.
### Logs bloom filter
`ethon:blockLogsBloom`   
The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list.
### logged by
`ethon:loggedBy`   
Relates a Log Entry to its logger's Account.
## M
### Merkle Patricia Tree
`ethon:ModifiedMerklePatriciaTree`   
Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings, although for the scope of this paper we are restricting keys and values to strings (to remove this restriction, just use any serialization format for other data types). They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
### Message
`ethon:Msg`   
Data (as a set of bytes) and value (specified as Ether) that is passed between two Accounts, either through the deterministic operation of an autonomous object (Contract Account) or the cryptographically secure signature of an External Account.
### Message payload
`ethon:payload`   
An unlimited size byte array specifying the data payload of the Message.
### Mix hash
`ethon:blockMixHash`   
A 256-bit hash which proves combined with the nonce that a sufficient amount of computation has been carried out on this Block.
### mines for
`ethon:minesFor`   
Relates a mining Node to the Blockchain it mines for. Mining is the process of dedicating effort (working) to bolster one series of Transactions (a Block) over any other potential competitor Block. It is achieved thanks to a cryptographically secure proof.
## N
### Node
`ethon:Node`   
A participan in an Ethereum Network.
### next Post Block State
`ethon:nextBlockState`   
Relates a Post Block State to the following Post Block State.
### next Post Message State
`ethon:nextMsgState`   
Relates a Post Message State to the following Post Message State.
### next Post Transaction State
`ethon:nextTxState`   
Relates a Post Transaction State to the following Post Transaction State.
### next State
`ethon:nextState`   
Relates a State to the following State. In EthOn the state transition system has no branches.
## O
### Ommer
`ethon:Ommer`   
An Ommer (or Uncle) is the direct child of the k'th generation ancestor of a Block B, where 2<=k<=7 but not a direct ancestor of B. They are blockchain blocks found by a miner, when a different miner has already found another block for the corresponding place in the blockchain. They are also known as “stale blocks”. The parent of an Uncle is an ancestor of the inserting block, located at the tip of the blockchain.
## P
### part of
`ethon:partOf`   
This is a general relation to express part of relationships. The classic study of parts and wholes, mereology, has three axioms: 1. the part-of relation is Transitive - "parts of parts are parts of the whole" - If A is part of B and B is part of C, then A is part of C Reflexive - "Everything is part of itself" - A is part of A Antisymmetric - "Nothing is a part of its parts" - if A is part of B and A != B then B is not part of A.
## Q
## R
### Receipts Trie
`ethon:ReceiptsTrie`   
A trie structure that stores transaction receipts. Each Block has a reference to the root hash of a receipts trie that stores the receipts of the transactions included in the Block.
### Receipts root
`ethon:receiptsRoot`   
The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the Block.
### runs client
`ethon:clientVersion`   
Relates a Node to a string identifying the Ethereum client version it runs. It composed of the client name (e.g. Geth) and a version identifier (e.g. v1.5.4).
## S
### State
`ethon:State`   
The concept of a state in a generic state transition system.
### State Transition
`ethon:StateTransition`   
The concept of a transition in a state transition system.
### State root
`ethon:stateRoot`   
The Keccak 256-bit hash of the root node of the state trie, after all transactions are executed and finalisations applied.
### Storage
`ethon:AccountStorage`   
A Merkle Patricia tree that encodes the storage contents of an Account. It is not used to store an Account's code, but the execution state of the code. The Account's code is stored in the
### Storage root
`ethon:storageRoot`   
A 256-bit hash of the root node of a Merkle Patricia tree that encodes the storage contents of the Account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
## T
### Transaction
`ethon:Tx`   
Transactions represent a valid arc between two states. A transaction is a single cryptographically-signed instruction constructed by an actor externally to the scope of Ethereum. While is assumed that the ultimate external actor will be human in nature, software tools will be used in its construction and dissemination.
### Transaction Logs Bloom filter
`ethon:txLogsBloom`   
Relates a Transaction Receipt to the Bloom filter of its Log Entries.
### Transaction gas limit
`ethon:txGasLimit`   
A scalar value equal to the maximum amount of gas that should be used in executing this transaction. This is paid up-front, before any computation is done and may not be increased later.
### Transaction gas price
`ethon:txGasPrice`   
A scalar value equal to the number of Wei to be paid per unit of gas for all computation costs incurred as a result of the execution of this Transaction.
### Transaction nonce
`ethon:txNonce`   
A scalar value equal to the number of transactions sent by the sender.
### Transaction r-value
`ethon:txR`   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The txR value is a Byte array of length 32.
### Transaction s-value
`ethon:txS`   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The value txS is a byte array of length 32.
### Transaction v-value
`ethon:txV`   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The value txV is aecovery id, a 1 byte value specifying the sign and finiteness of the curve point. This value is in the range of [27,30], however we declare the upper to possibilities, representing infinite values, invalid.
### TransactionReceipt
`ethon:TxReceipt`   
The transaction receipt is a tuple of four items comprising the post-transaction-state, the cumulative gas used in the block containing the transaction receipt as of immediately after the transaction has happened, the set of logs created through execution of the transaction and the bloom filter composed from information in those logs.
### Transactions Trie
`ethon:TxTrie`   
A trie structure that stores transactions. The header of a Block contains a reference to the root of a Tx trie with all transactions contained in the Block.
### Transactions root
`ethon:transactionsRoot`   
The Keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the Block.
### to
`ethon:to`   
Relates a Message with the Account it is sent to.
### topic index
`ethon:topicIndex`   
Relates a Log Topic to its index in the Log Entry. The topic index defines the order of the Log Topics of a Log Entry.
### triggers Contract Message
`ethon:triggersMsg`   
Relates a Message that was direct to a Contract Account to the Contract Messages that result from the call to the Contract Account. The chain of triggersMsg relations represents a call graph.
## U
### Uncle
`ethon:Uncle`   

## V
### Value Contract Message
`ethon:ValueContractMsg`   
Value Contract Messages go from a Contract to an External Account.
### Value Transaction
`ethon:ValueTx`   
A type of Transaction that transfers only value.
### value in Wei
`ethon:value`   
A scalar value equal to the number of Wei to be transferred to the Message call's recipient. In the case of Contract creation it is the initial balance of the Contract Account, paid by the sending Account.
## W
### World State
`ethon:WorldState`   
The world state, is a mapping between addresses (160-bit identifiers) of all Accounts and their States (a data structure serialised as Recursive Length Prefix). The mapping is not stored on the Blockchain itself but in a modified Merkle Patricia tree. An individual state is identified by the root hash of the trie.
## X
## Y
## Z