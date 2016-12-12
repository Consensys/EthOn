# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
## A
### Account
Accounts have an intrinsic balance and transaction count maintained as part of the Ethereum state. They also have some (possibly empty) EVM Code and a (possibly empty) Storage State associated with them. Though homogenous, it makes sense to distinguish between two practical types of account: those with empty associated EVM Code (thus the account balance is controlled, if at all, by some external entity) and those with non-empty associated EVM Code (thus the account represents an Autonomous Object). Each Account has a single Address that identifies it.
### AccountConcept
Groups EthOn concepts related to Accounts.
### AccountState
State of an Ethereum account. It is comprised on four pieces of information: nonce, balance, storage root and code hash. The data is stored in a Merkle Patricia tree as a mapping between addresses and account states.
### AccountStorage
A Merkle Patricia tree that encodes the storage contents of an account. It is not used to store an account's code, but the execution state of the code. The account's code is stored in the
### Agent

### AutonomousObject
This is a more abstract term for a Contract Account.
### accountBalance
A scalar value equal to the number of Wei owned by an account at a given account state.
### accountCode
The imutable EVM bytecode of the Contract Account.
### accountCodeHash
The immutable hash of the EVM code of an account.
### accountNonce
A scalar value equal to the number of transactions sent from this account or, in the case of accounts with associated code, the number of contract-creations made by this account.
### address
A 160-bit identifier for Accounts.
## B
### Block
A block is the basic element of a blockchain. It functions as a journal, recording a series of transactions together with a reference to the previous block. A block is chained to its preceeding block by a cryptographic hash as a means of reference. Blocks contain an identifier for the final state after all transactions contained in it are validated. There is an incentive mechanism that provides incentives to generate new blocks ("mine blocks") that comply to the rules of Ethereum by issuing a reward to an account specified by the miner.
### BlockConcept
Groups EthOn concepts related to Blocks.
### Blockchain
An Ethereum Blockchain is a distributed database that maintains a continuously-growing list of records called *blocks* secured from tampering and revision. Each block contains a timestamp and a link to a previous block in a Merkle tree structure.
### blockCreationTime
A scalar value equal to the reasonable output of Unix's time() at this block's inception.
### blockDifficulty
A scalar value corresponding to the difficulty level of this block. This can be calculated from the previous block's difficulty level and the timestamp.
### blockExtraData
An arbitrary byte array containing data relevant to this block. This must be 32 bytes or fewer.
### blockGasLimit
A scalar value equal to the current limit of gas expenditure per block.
### blockGasUsed
A scalar value equal to the total gas used in transactions in this block.
### blockHash
The Keccak 256-bit hash of the block's header, in its entierty.
### blockHeader
Relates a Block to its block header data. The block header data contains 15 pieces of information: 1. the parent hash, 2. the ommers hash, 3. a beneficary address, 4. a state root hash, 5. a transactions root hash, 6. a receipts root hash, 7. a log bloom filter, 8. the difficulty value, 9. the block number, 10. the gas limit of the block, 11. the gas used by all transactions in the block, 12. a timestamp in unix time() format, 13. a byte array containing extra data, 14. a mix hash and 15. the block nonce. The property is functional because a Block can have only exactly one block header.
### blockLogsBloom
The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list.
### blockMixHash
A 256-bit hash which proves combined with the nonce that a sufficient amount of computation has been carried out on this block.
### blockNonce
A 64 bit hash which proves combined with the mix-hash that a sufficient amount of computation has been carried out on this block.
### blockReward
Also base reward, amount of Wei a miner gets for finding a Block.
## C
### CallContractMsg
A call contract message is a contract message that calls a function in another contract.
### CallTx

### ContractAccount
A notional object existent only within the hypothetical state of Ethereum. Has an intrinsic address and thus an associated account; the account will have non-empty associated EVM Code. Incorporated only as the Storage State of that account.
### ContractMsg
A contract message is passed between a contract account and any other account (external or contract). It is the result of an execution chain originally triggered by an external account.
### CreateContractMsg
A create contract message is a special type of contract message that results in creation of a new contract.
### CreateTx

### conformsTo
Relates an Ethereum concept to the Ethereum Protocol Variant it conforms to.
### containsTx
Relates a Block to a Transaction included in it. All containsTx relations of a block comprise the block's transaction list. The order of the transactions is determined by their index value. The property is inverse functional because a Transaction can only be included in one block.
### controlsAccount
This property connects an External Actor an Account that it controls. This means the External Actor has control over the private Key for the Account. The control is not necessarily legitimate.
### creates
Relates a create transaction to the Contract Account it creates.
### createsState

## D
## E
### EthOnAccountDataProperty
Groups all data propertiers that are specific to an Account.
### EthOnAccountObjectProperty
Groups all EthOn Account object properties
### EthOnAnnotationProperty
Superclass of all EthOn specific annotation properties.
### EthOnBlockDataProperty
Groups all data properties that are specific to a Block. These properties are usually functional because a block can only be associated with a single instance of them.
### EthOnBlockObjectProperty
Groups all EthOn Block object properties
### EthOnConcept
Groups al EthOn concepts.
### EthOnDataProperty
Groups all data properties specific to EthOn.
### EthOnMessageDataProperty

### EthOnMessageObjectProperty
Groups all EthOn State object properties.
### EthOnNetworkObjectProperty

### EthOnObjectProperty
Groups all EthOn object properties
### EthOnStateDataProperty

### EthOnStateObjectProperty

### ExternalAccount
An account owned by an External Actor.
### ExternalActor
A person or other entity able to interface to an Ethereum node, but external to the world of Ethereum. It can interact with Ethereum through depositing signed Transactions and inspecting the blockchain and associated state. Has one (or more) intrinsic Accounts. While it is assumed that the ultimate external actor will be human in nature, software tools will be used in its construction and dissemination.
## F
### FullNode
Ethereum Full Node, A Full Node is a participant in an Ethereum Network that keeps a record of the full blockchain, the full state and engages in mining.
### from
Relates a Message with the Account it originates from.
## G
## H
### hasAccountStorage
Relates an Account to the Merkle Patricia tree that encodes its storage contents at a certain Account State. This property is Functional because an Account State can have only one Instance of Account Storage and Inverse Functional because an Account Storage can have only one associated Account State.
### hasBeneficiary
Relates a block to the Account to which all fees collected from the successful mining of this block are transferred.
### hasCurrentState
This property relates an EthOn concept to its most current state.
### hasFork
Relates a Protocol variant to a forked version of it. It is inverse functional because a forked Blockchain can have only one Blockchain it forked from. It is Transitive because if a Blockchain C that was forked from Blockchain B that in turn was forked from Blockchain A, Blockchain C was also forked from Blockchain A. It is assymetric becauce if Blockchain A is forked from Blockchain B, B cannot be also forked from A. It is irreflexive because a Blockchain cannot be a fork of itself.
### hasParentBlock
Relates a block to its parent in the chain. It always points to the block with a number that is decreased by one, compared to the block it originates from. The relation is asymmetric because if block A is parent to block B then block B can not be parent to block A. It is also irreflixive because a block cannot be parent to itself.
### hasPostExecutionState
Relates a Block to the global state of the system after all Transactions in the Block have been executed.
### hasReceipt
Relates a transaction to its receipt.
### hasReceiptsTrie
Relates a block to the Trie that contains the block's receipt data.
### hasState
This property relates an EthOn concept to a state. It is inverse functional because a state can only belong to one single EthOn concept. Only some EthOn concepts have associated states. This is defined in the domain restriction.
### hasTxTrie
Relates a block to the trie that contains the data of the transactions contained in the block.
## I
## J
## K
### knowsOfOmmer
Relates a Block to a known Ommer.
## L
### LightNode
A light node is a participant in an Ethereum Network that does not completely do any of the following: store the complete Blockchain, store the complete world state, engage in mining.
## M
### MessageConcept
Groups EthOn concepts related to messages.
### ModifiedMerklePatriciaTree
Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings, although for the scope of this paper we are restricting keys and values to strings (to remove this restriction, just use any serialization format for other data types). They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
### Msg
Data (as a set of bytes) and value (specified as Ether) that is passed between two accounts, either through the deterministic operation of an autonomous object (contract account) or the cryptographically secure signature of an external account.
### minesFor
Relates a mining Node to the Blockchain it mines for.
## N
### Network
An Ethereum network is the group of all Nodes that conform to a certain Protocol Variant.
### NetworkConcept
Groups all EthOn Network concepts.
### Node
A participan in an Ethereum Network.
### number
A scalar value equal to the number of ancestor blocks. The genesis block has a number of zero.
## O
### Ommer
An Ommer.
## P
### ProtocollVariant
A variant of the Ethereum protocol. Changes in the protocol result in a hard or soft fork.
### partOf
This is a general relation to express part of relationships. The classic study of parts and wholes, mereology, has three axioms: 1. the part-of relation is Transitive - "parts of parts are parts of the whole" - If A is part of B and B is part of C, then A is part of C Reflexive - "Everything is part of itself" - A is part of A Antisymmetric - "Nothing is a part of its parts" - if A is part of B and A != B then B is not part of A.
## Q
## R
### ReceiptsTrie
A trie structure that stores transaction receipts. Each block has a reference to the root hash of a receipts trie that stores the receipts of the transactions included in the block.
### receiptsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the block.
### root

## S
### State
The concept of a state in a generic state transition system.
### StateConcept
Groups EthOn concepts related to state.
### StateTransition

### stateRoot
The Keccak 256-bit hash of the root node of the state trie, after all transactions are executed and finalisations applied.
### storageRoot
A 256-bit hash of the root node of a Merkle Patricia tree that encodes the storage contents of the account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
### suggestedStringRepresentation
This property relates an EthOn concept with a suggested string representation. It can be used to give the concept a name, e.g. in program code.
## T
### Tx

### TxReceipt

### TxTrie
A trie structure that stores transactions. The header of a block contains a reference to the root of a tx trie with all transactions contained in the block.
### to
Relates a Message with the Account it is sent to.
### transactionsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the block.
## U
## V
### ValueContractMsg
Value contract messages go from a contract to an external account.
### ValueTx

### value

## W
### WorldState
The world state, is a mapping between addresses (160-bit identifiers) and account states (a data structure serialised as Recursive Lenth Prefix). The mapping is not stored on the blockchain itself but in a modified Merkle Patricia tree. An individual state is identified by the root hash of the trie.
## X
## Y
## Z