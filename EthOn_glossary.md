# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
## A
### Account
Accounts have an intrinsic balance and transaction count maintained as part of the Ethereum state. They also have some (possibly empty) EVM Code and a (possibly empty) Storage State associated with them. Though homogenous, it makes sense to distinguish between two practical types of Account: those with empty associated EVM Code (thus the Account balance is controlled, if at all, by some external entity) and those with non-empty associated EVM Code (thus the Account represents an Autonomous Object). Each Account has a single Address that identifies it.
### AccountConcept
Groups EthOn concepts related to Accounts.
### AccountDataProperty
Groups all Data Properties that are specific to an Account.
### AccountObjectProperty
Groups all EthOn Account Object Properties
### AccountState
State of an Ethereum Account. It is comprised on four pieces of information: nonce, balance, storage root and code hash. The data is stored in a Merkle Patricia tree as a mapping between addresses and Account states.
### AccountStorage
A Merkle Patricia tree that encodes the storage contents of an Account. It is not used to store an Account's code, but the execution state of the code. The Account's code is stored in the
### Agent

### AutonomousObject
This is a more abstract term for a Contract Account.
### accountBalance
A scalar value equal to the number of Wei owned by an Account at a given Account state.
### accountCode
The imutable EVM bytecode of the Contract Account.
### accountCodeHash
The immutable hash of the EVM code of an Account.
### accountNonce
A scalar value equal to the number of transactions sent from this Account or, in the case of Accounts with associated code, the number of Contract-creations made by this Account.
### address
A 160-bit identifier for Accounts.
## B
### Block
A Block is the basic element of a Blockchain. It functions as a journal, recording a series of transactions together with a reference to the previous Block. A Block is chained to its preceeding Block by a cryptographic hash as a means of reference. Blocks contain an identifier for the final state after all transactions contained in it are validated. There is an incentive mechanism that provides incentives to generate new Blocks ("mine Blocks") that comply to the rules of Ethereum by issuing a reward to an Account specified by the miner.
### BlockConcept
Groups EthOn concepts related to Blocks.
### BlockDataProperty
Groups all Data Properties that are specific to a Block. These properties are usually functional because a Block can only be associated with a single instance of them.
### BlockObjectProperty
Groups all EthOn Block Object Properties
### Blockchain
An Ethereum Blockchain is a distributed database that maintains a continuously-growing list of records called *Blocks* secured from tampering and revision. Each Block contains a timestamp and a link to a previous Block in a Merkle tree structure.
### blockCreationTime
This Block's inception date and time.
### blockDifficulty
A scalar value corresponding to the difficulty level of this Block. This can be calculated from the previous Block's difficulty level and the timestamp.
### blockExtraData
An arbitrary byte array containing data relevant to this Block. This must be 32 bytes or fewer.
### blockGasLimit
A scalar value equal to the current limit of gas expenditure per Block.
### blockGasUsed
A scalar value equal to the total gas used in transactions in this Block.
### blockHash
The Keccak 256-bit hash of the Block's header, in its entierty.
### blockHeader
Relates a Block to its Block header data. The Block header data contains 15 pieces of information: 1. the parent hash, 2. the Ommers hash, 3. a beneficiary address, 4. a state root hash, 5. a transactions root hash, 6. a receipts root hash, 7. a log bloom filter, 8. the difficulty value, 9. the Block number, 10. the gas limit of the Block, 11. the gas used by all transactions in the Block, 12. a scalar timestamp in unix time() format, 13. a byte array containing extra data, 14. a mix hash and 15. the Block nonce. The property is functional because a Block can have only exactly one Block header.
### blockLogsBloom
The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list.
### blockMixHash
A 256-bit hash which proves combined with the nonce that a sufficient amount of computation has been carried out on this Block.
### blockNonce
A 64 bit hash which proves combined with the mix-hash that a sufficient amount of computation has been carried out on this Block.
### blockReward
Also base reward, amount of Wei a miner gets for finding a Block.
## C
### CallContractMsg
A Call Contract Message is a Contract Message that calls a function in another Contract.
### CallTx

### ContractAccount
A notional object existent only within the hypothetical state of Ethereum. Has an intrinsic address and thus an associated Account; the Account will have non-empty associated EVM Code. Incorporated only as the Storage State of that Account.
### ContractMsg
A Contract Message is passed between a Contract Account and any other Account (External or Contract). It is the result of an execution chain originally triggered by an External Account.
### CreateContractMsg
A create Contract Message is a special type of Contract Message that results in creation of a new Contract.
### CreateTx

### clientVersion
Relates a Node to a string identifying the Ethereum client version it runs. It composed of the client name (e.g. Geth) and a version identifier (e.g. v1.5.4).
### conformsTo
Relates an Ethereum concept to the Ethereum Protocol Variant it conforms to.
### containsTx
Relates a Block to a Transaction included in it. All containsTx relations of a Block comprise the Block's transaction list. The order of the transactions is determined by their index value. The property is inverse functional because a Transaction can only be included in one Block.
### controlsAccount
This property connects an External Actor an Account that it controls. This means the External Actor has control over the private Key for the Account. The control is not necessarily legitimate.
### creates
Relates a create transaction to the Contract Account it creates.
### createsState
Relates a Transition to the State it creates.
### cumulativeGasUsed
The cumulative gas used in the block containing the Transaction Receipt as of immediately after the Transaction has happened.
## D
### DASE_RULE

## E
### EthOnAnnotationProperty
Superclass of all EthOn specific annotation properties.
### EthOnConcept
Groups al EthOn concepts.
### EthOnDataProperty
Groups all Data Properties specific to EthOn.
### EthOnObjectProperty
Groups all EthOn Object Properties
### ExternalAccount
An Account owned by an External Actor.
### ExternalActor
A person or other entity able to interface to an Ethereum node, but External to the world of Ethereum. It can interact with Ethereum through depositing signed Transactions and inspecting the Blockchain and associated state. Has one (or more) intrinsic Accounts. While it is assumed that the ultimate External actor will be human in nature, software tools will be used in its construction and dissemination.
## F
### FullNode
A Full Node is a participant in an Ethereum Network that keeps a record of the full Blockchain, the full state and engages in mining., Ethereum Full Node
### from
Relates a Message with the Account it originates from.
## G
### GenesisBlock
A Genesis Block is the unmined, deliberately created, very first Block in a Blockchain. It has no predecessors, i.e. no parent Block.
## H
### hasAccountStorage
Relates an Account to the Merkle Patricia tree that encodes its storage contents at a certain Account State. This property is Functional because an Account State can have only one Instance of Account Storage and Inverse Functional because an Account Storage can have only one associated Account State.
### hasBeneficiary
Relates a Block to the Account to which all fees collected from the successful mining of this Block are transferred.
### hasCurrentState
This property relates an EthOn concept to its most current state.
### hasFork
Relates a Protocol variant to a forked version of it. It is inverse functional because a forked Blockchain can have only one Blockchain it forked from. It is Transitive because if a Blockchain C that was forked from Blockchain B that in turn was forked from Blockchain A, Blockchain C was also forked from Blockchain A. It is assymetric because if Blockchain A is forked from Blockchain B, B cannot be also forked from A. It is irreflexive because a Blockchain cannot be a fork of itself.
### hasLogEntry
Relates a Transaction Receipt to a Log Entry created by the Transaction of the Receipt.
### hasLogTopic
Relates a Log Entry to a Log Topic.
### hasNextState
Relates a State to the following State. In EthOn the state transition system has no branches.
### hasParentBlock
Relates a Block to its parent in the chain. It always points to the Block with a number that is decreased by one, compared to the Block it originates from. The relation is asymmetric because if Block A is parent to Block B then Block B can not be parent to Block A. It is also irreflexive because a Block cannot be parent to itself.
### hasPostBlockState
Relates a Block to the global state of the system after all Transactions in the Block have been executed.
### hasPostTxState
Relates a Transaction Receipt to the global state of the system after the Receipt's Transaction has been executed.
### hasReceipt
Relates a transaction to its receipt.
### hasReceiptsTrie
Relates a Block to the Trie that contains the Block's receipt data.
### hasState
This property relates an EthOn concept to a state. It is inverse functional because a state can only belong to one single EthOn concept. Only some EthOn concepts have associated states. This is defined in the domain restriction.
### hasTransition
Relates a State to a Transition (i.e. a Message) that creates a new State.
### hasTxTrie
Relates a Block to the trie that contains the data of the transactions contained in the Block.
## I
## J
## K
### knowsOfOmmer
Relates a Block to a known Ommer.
## L
### LightNode
A light node is a participant in an Ethereum Network that does not completely do any of the following: store the complete Blockchain, store the complete world state, engage in mining.
### LogEntry
A Log Entry is a tuple of a logger's address (i.e. the Account with that address), a series of 32-bytes Log Topics and some number of bytes of data.
### LogTopic
A 32-bytes long topic of a LogEntry. The LogTopics of a LogEntry have an order given by a topicIndex value.
### loggedBy
Relates a Log Entry to its logger's Account.
## M
### MessageConcept
Groups EthOn concepts related to Messages.
### MessageDataProperty
Groups all EthOn Message Data Properties.
### MessageObjectProperty
Groups all EthOn State Object Properties.
### ModifiedMerklePatriciaTree
Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings, although for the scope of this paper we are restricting keys and values to strings (to remove this restriction, just use any serialization format for other data types). They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
### Msg
Data (as a set of bytes) and value (specified as Ether) that is passed between two Accounts, either through the deterministic operation of an autonomous object (Contract Account) or the cryptographically secure signature of an External Account.
### minesFor
Relates a mining Node to the Blockchain it mines for.
## N
### Network
An Ethereum network is the group of all Nodes that conform to a certain Protocol Variant.
### NetworkConcept
Groups all EthOn Network concepts.
### NetworkDataProperty
Groups all EthOn Network Data Properties.
### NetworkObjectProperty
Groups all EthOn Network Object Properties.
### Node
A participan in an Ethereum Network.
### number
A scalar value equal to the number of ancestor Blocks. The genesis Block has a number of zero.
## O
### Ommer
An Ommer.
## P
### ProtocollVariant
A variant of the Ethereum protocol. Changes in the protocol result in a hard or soft fork.
### partOf
This is a general relation to express part of relationships. The classic study of parts and wholes, mereology, has three axioms: 1. the part-of relation is Transitive - "parts of parts are parts of the whole" - If A is part of B and B is part of C, then A is part of C Reflexive - "Everything is part of itself" - A is part of A Antisymmetric - "Nothing is a part of its parts" - if A is part of B and A != B then B is not part of A.
### payload
An unlimited size byte array specifying the data payload of the Message.
## Q
## R
### ReceiptsTrie
A trie structure that stores transaction receipts. Each Block has a reference to the root hash of a receipts trie that stores the receipts of the transactions included in the Block.
### receiptsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the Block.
### root

## S
### State
The concept of a state in a generic state transition system.
### StateConcept
Groups EthOn concepts related to state.
### StateDataProperty

### StateObjectProperty
Groups all EthOn State Object Properties.
### StateTransition

### stateRoot
The Keccak 256-bit hash of the root node of the state trie, after all transactions are executed and finalisations applied.
### storageRoot
A 256-bit hash of the root node of a Merkle Patricia tree that encodes the storage contents of the Account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
### suggestedStringRepresentation
This property relates an EthOn concept with a suggested string representation. It can be used to give the term a name, e.g. in program code.
## T
### Tx

### TxReceipt
The transaction receipt is a tuple of four items comprising the post-transaction-state, the cumulative gas used in the block containing the transaction receipt as of immediately after the transaction has happened, the set of logs created through execution of the transaction and the bloom filter composed from information in those logs.
### TxTrie
A trie structure that stores transactions. The header of a Block contains a reference to the root of a Tx trie with all transactions contained in the Block.
### to
Relates a Message with the Account it is sent to.
### topicData
Relates a Log Topic to the 32 bytes of data it contains.
### topicIndex
Relates a Log Topic to its index in the Log Entry. The topic index defines the order of the Log Topics of a Log Entry.
### transactionsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the Block.
### txLogsBloom
Relates a Transaction Receipt to the Bloom filter of its Log Entries.
## U
## V
### ValueContractMsg
Value Contract Messages go from a Contract to an External Account.
### ValueTx

### value
A scalar value equal to the number of Wei to be transferred to the Message call's recipient. In the case of Contract creation it is the initial balance of the Contract Account, paid by the sending Account.
## W
### WorldState
The world state, is a mapping between addresses (160-bit identifiers) and Account states (a data structure serialised as Recursive Length Prefix). The mapping is not stored on the Blockchain itself but in a modified Merkle Patricia tree. An individual state is identified by the root hash of the trie.
## X
## Y
## Z