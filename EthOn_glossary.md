# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
## A
### Account
Accounts have an intrinsic balance and transaction count maintained as part of the Ethereum state. They also have some (possibly empty) EVM Code and a (possibly empty) Storage State associated with them. Though homogenous, it makes sense to distinguish between two practical types of account: those with empty associated EVM Code (thus the account balance is controlled, if at all, by some external entity) and those with non-empty associated EVM Code (thus the account represents an Autonomous Object). Each Account has a single Address that identifies it.
### AccountConcept
Groups EthOn concepts related to Accounts.
### AccountState
State of an Ethereum account. It is comprised on four pieces of information: nonce, balance, storage root and code hash.
### AccountStorage
Merkle Patricia tree that encodes the storage contents of an Account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
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
### BlockHeader
The header of a Block.
### beneficary
The 160-bit address to which all fees collected from the successful mining of this block be transferred.
### blockHash
The Keccak 256-bit hash of the block's header, in its entierty.
### blockNonce
A 64 bit hash which proves combined with the mix-hash that a sufficient amount of computation has been carried out on this block.
### blockReward
Also base reward, amount of Wei a miner gets for finding a Block.
## C
### ContractAccount
A notional object existent only within the hypothetical state of Ethereum. Has an intrinsic address and thus an associated account; the account will have non-empty associated EVM Code. Incorporated only as the Storage State of that account.
### ContractAccountState
State of an Ethereum Contract Account. In addition to the fields of an Account State it also references an Account Storage.
### containsTransaction
Relates a Block to a Transaction included in it. The property is inverse functional because a Transaction can only be included in one block.
### controlsAccount
This property connects an External Actor an Account that it controls. This means the External Actor has control over the private Key for the Account. The control is not necessarily legitimate.
## D
### difficulty
A scalar value corresponding to the difficulty level of this block. This can be calculated from the previous block's difficulty level and the timestamp.
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
### EthOnObjectProperty
Groups all EthOn object properties
### EthereumState
The world state (mostly just "state"), is a mapping between addresses (160-bit identifiers) and account states (a data structure serials as RLP). The mapping is not stored on the blockchain itself but in a modified Merkle Patricia tree.
### ExternalAccount
An account owned by an External Actor.
### ExternalActor
A person or other entity able to interface to an Ethereum node, but external to the world of Ethereum. It can interact with Ethereum through depositing signed Transactions and inspecting the blockchain and associated state. Has one (or more) intrinsic Accounts. While it is assumed that the ultimate external actor will be human in nature, software tools will be used in its construction and dissemination.
### extraData
An arbitrary byte array containing data relevant to this block. This must be 32 bytes or fewer.
## F
## G
### gasLimit
A scalar value equal to the current limit of gas expenditure per block.
### gasUsed
A scalar value equal to the total gas used in transactions in this block.
## H
### hasAccountStorage
Relates an Account to the Merkle Patricia tree that encodes its storage contents at a certain Account State. This property is Functional because an Account State can have only one Instance of Account Storage and Inverse Functional because an Account Storage can have only one associated Account State.
### hasCurrentState
This property relates an EthOn concept to its most current state., has current State
### hasHeader
Relates a Block to its Block Header. The property is functional because a Block can have only exactly one Block Header and it is also inverse functionals because a Block header can only be associated with exactly one Block.
### hasState
This property relates an EthOn concept to a state. It is inverse functional because a state can only belong to one single EthOn concept. Only some EthOn concepts have associated states. This is defined in the domain restriction.
## I
## J
## K
### knowsOfOmmer
Relates a Block to a known Ommer.
## L
### logsBloom
The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list.
## M
### MerklePatriciaTree
Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings, although for the scope of this paper we are restricting keys and values to strings (to remove this restriction, just use any serialization format for other data types). They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
### MessageConcept

### mixHash
A 256-bit hash which proves combined with the nonce that a sufficient amount of computation has been carried out on this block.
## N
### number
A scalar value equal to the number of ancestor blocks. The genesis block has a number of zero.
## O
### Ommer
An Ommer.
### OmmerHeader
The header of an Ommer.
### ommersHash
The keccak 256-bit hash of the uncles list portion of this block.
## P
### parentHash
The Keccak 256-bit hash of the parent block's header, in its entierty.
## Q
## R
### receiptsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the block.
## S
### stateRoot
The Keccak 256-bit hash of the root node of the state trie, after all transactions are executed and finalisations applied.
### storageRoot
A 256-bit hash of the root node of a Merkle Patricia tree that encodes the storage contents of the account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
### suggestedStringRepresentation
This property relates an EthOn concept with a suggested string representation. It can be used to give the concept a name, e.g. in program code.
## T
### Transaction

### TransactionReceipt

### timestamp
A scalar value equal to the reasonable output of Unix's time() at this block's inception.
### transactionsRoot
The Keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the block.
## U
## V
## W
## X
## Y
## Z