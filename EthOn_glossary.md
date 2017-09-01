# EthOn Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ontology.
Please also consider looking at the [specification of EthOn](http://ethon.consensys.net/EthOn_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.
## A
### Account
[`ethon:Account`](http://ethon.consensys.net/Account)   
*Account* is the superclass of all account types in Ethereum. All accounts are identified by an address (which, however, is derived differently for external and contract accounts) and an account state that contains the contract's balance and total message count, which is called its nonce. Contract accounts also have an associated storage state and EVM code. The address of an external account is derived from the public key of a public and private keypair, while a contract account address is a concatenation of the creator account's address and its nonce. Both contract accounts and external accounts can also be of type *protocol account* if they are specified in the Ethereum blockchain, i.e. the accounts pre-funded by the Ethereum crowdsale.
### Account State
[`ethon:AccountState`](http://ethon.consensys.net/AccountState)   
State of an Ethereum account. It is comprised on four pieces of information: nonce, balance, storage root and code hash. The data is stored in a Merkle Patricia tree as a mapping between addresses and account states. The account state is part of the world state, as it resembles the state of exactly one account.
### Account balance
[`ethon:accountBalance`](http://ethon.consensys.net/accountBalance)   
A scalar value equal to the number of Wei owned by an account at a given account state.
### Account balance prefunded
[`ethon:accountBalancePrefunded`](http://ethon.consensys.net/accountBalancePrefunded)   
The amount of Wei an account was prefunded with in a protocol variant. In the case that an account receives multiple prefunds in multiple protocol variants, the amounts are summed. In contrast to the regular account balance it is a property of the account itself and not of its state.
### Account code
[`ethon:accountCode`](http://ethon.consensys.net/accountCode)   
The immutable EVM bytecode of the contract account.
### Account code hash
[`ethon:accountCodeHash`](http://ethon.consensys.net/accountCodeHash)   
The immutable Keccak-256 hash of the EVM code of an account.
### Account nonce
[`ethon:accountNonce`](http://ethon.consensys.net/accountNonce)   
A scalar value equal to the number of transactions sent from this account or, in the case of accounts with associated code, the number of contract-creations made by this account.
### Account public key
[`ethon:accountPublicKey`](http://ethon.consensys.net/accountPublicKey)   
The public key of an external account.
### Address
[`ethon:address`](http://ethon.consensys.net/address)   
A 160-bit identifier for accounts.
## B
### Block
[`ethon:Block`](http://ethon.consensys.net/Block)   
A block is the basic element of a 'blockchain'. It functions as an entry in a distributed ledger, recording a series of transactions together with a reference to the previous block. A block is chained to its preceeding block by a cryptographic hash of its contents as a means of reference. Blocks contain an identifier for the final state after all transactions contained in it are validated. There is a consensus mechanism that provides incentives for nodes adding new blocks to the chain ("miners" in the Proof of Work protocol used by the main Ethereum network) that comply with the rules of Ethereum by issuing newly generated tokens ('Ether') to an account specified by the block's author.
### Block beneficiary reward
[`ethon:blockBeneficiaryReward`](http://ethon.consensys.net/blockBeneficiaryReward)   
The reward the beneficiary receives for mining a block. It is comprised of the base reward (5ETH), rewards for including uncles (1/32 of block reward per uncle) and the fees of the Tx in the block.
### Block creation time
[`ethon:blockCreationTime`](http://ethon.consensys.net/blockCreationTime)   
This block's inception date and time.
### Block difficulty
[`ethon:blockDifficulty`](http://ethon.consensys.net/blockDifficulty)   
A scalar value corresponding to the difficulty level of this block. This can be calculated from the previous block's difficulty level and the timestamp.
### Block extra data
[`ethon:blockExtraData`](http://ethon.consensys.net/blockExtraData)   
An arbitrary byte array containing data relevant to this block. This must be 32 bytes or fewer.
### Block gas limit
[`ethon:blockGasLimit`](http://ethon.consensys.net/blockGasLimit)   
A scalar value equal to the current limit of gas expenditure per block.  Its purpose is to keep block propagation and processing time low, thereby allowing for a sufficiently decentralized network. Miners have the option to increase or decrease it every block by a certain factor.
### Block gas used
[`ethon:blockGasUsed`](http://ethon.consensys.net/blockGasUsed)   
A scalar value equal to the total gas used by all transactions in this block.
### Block hash
[`ethon:blockHash`](http://ethon.consensys.net/blockHash)   
The Keccak 256-bit hash of the block's header, in its entierty.
### Block header
[`ethon:blockHeader`](http://ethon.consensys.net/blockHeader)   
Relates a block to its block header data. The block header data contains 15 pieces of information: 1. the parent hash, 2. the Uncle hash, 3. a beneficiary address, 4. a state root hash, 5. a transactions root hash, 6. a receipts root hash, 7. a log bloom filter, 8. the difficulty value, 9. the block number, 10. the gas limit of the block, 11. the gas used by all transactions in the block, 12. a scalar timestamp in unix time() format, 13. a byte array containing extra data, 14. a mix hash and 15. the block nonce. The property is functional because a block can have only exactly one block header.
### Block logs bloom filter
[`ethon:blockLogsBloom`](http://ethon.consensys.net/blockLogsBloom)   
The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list.
### Block mix hash
[`ethon:blockMixHash`](http://ethon.consensys.net/blockMixHash)   
A 256-bit hash which proves combined with the nonce that a sufficient amount of computation has been carried out on this block.
### Block nonce
[`ethon:blockNonce`](http://ethon.consensys.net/blockNonce)   
A 64 bit hash which proves combined with the mix-hash that a sufficient amount of computation has been carried out on this block.
### Block number
[`ethon:number`](http://ethon.consensys.net/number)   
A scalar value equal to the number of ancestor blocks. The genesis block has a number of zero.
### Block size
[`ethon:blockSize`](http://ethon.consensys.net/blockSize)   
The size of the block header in RLP format in bytes.
## C
### Call Contract Message
[`ethon:CallContractMsg`](http://ethon.consensys.net/CallContractMsg)   
A call contract message is a contract message that calls a function in another contract.
### Call Transaction
[`ethon:CallTx`](http://ethon.consensys.net/CallTx)   
A type of transaction that is directed towards a contract account and calls a method in the contract's code.
### Contract Account
[`ethon:ContractAccount`](http://ethon.consensys.net/ContractAccount)   
One of the two main types of accounts on Ethereum, a contract account is an account whose behaviour is controlled by a smart contract. Contract accounts are identified by their address which is derived from the creator account's address and nonce. A contract account has a non-empty associated EVM code. It's state data consists of the bytecode, the contract's balance and the storage state of the contract's code (for example the value of variables). A contract account can only act when it is triggered by a message. It may not create and sign transactions, but it can receive transactions from external accounts as well as send and receive contract messages, which may involve a transfer of Ether. Contract accounts can also contain events which create log entries when triggered.
### Contract Message
[`ethon:ContractMsg`](http://ethon.consensys.net/ContractMsg)   
A contract message is passed between a contract account and any other account (external or contract). It is the result of an execution chain originally triggered by an external eccount.
### Create Contract Message
[`ethon:CreateContractMsg`](http://ethon.consensys.net/CreateContractMsg)   
A create contract message is a subtype of a contract message that results in creation of a new contract account.
### Create Transaction
[`ethon:CreateTx`](http://ethon.consensys.net/CreateTx)   
A type of transaction that results in creation of a new contract account.
### call data
[`ethon:msgData`](http://ethon.consensys.net/msgData)   
An unlimited size byte array specifying the input data of the call.
### conforms to
[`ethon:conformsTo`](http://ethon.consensys.net/conformsTo)   
Relates an Ethereum concept to the Ethereum protocol variant it conforms to.
### contains Transaction
[`ethon:containsTx`](http://ethon.consensys.net/containsTx)   
Relates a block to a transaction included in it. All containsTx relations of a block comprise the block's transaction list. The order of the transactions is determined by their index value. The property is inverse functional because a transaction can only be included in one block.
### contract balance in Wei
[`ethon:msgRefundBalance`](http://ethon.consensys.net/msgRefundBalance)   
A scalar value equal to the number of Wei that will be refunded as the result of a selfdestruct contract message.
### controls Account
[`ethon:controlsAccount`](http://ethon.consensys.net/controlsAccount)   
This property connects an External Actor an Account that it controls. This means the External Actor has control over the private Key for the Account. The control is not necessarily legitimate.
### creates
[`ethon:creates`](http://ethon.consensys.net/creates)   
Relates a create transaction to the contract account it creates.
### creates State
[`ethon:createsState`](http://ethon.consensys.net/createsState)   
Relates a transition to the state it creates.
### creates post Block execution State
[`ethon:createsPostBlockState`](http://ethon.consensys.net/createsPostBlockState)   
Relates a block to the global state of the system after all transactions in the block have been executed.
### creates post Message execution State
[`ethon:createsPostMsgState`](http://ethon.consensys.net/createsPostMsgState)   
Relates a message to the global state of the system after all the message has been executed.
### creates post Transaction execution State
[`ethon:createsPostTxState`](http://ethon.consensys.net/createsPostTxState)   
Relates a transaction to the global state of the system after the transaction has been executed.
### cumulative gas used
[`ethon:cumulativeGasUsed`](http://ethon.consensys.net/cumulativeGasUsed)   
The cumulative gas used in the block containing the transaction as of immediately after the transaction has happened.
## D
## E
### EthOn Message Data Property
[`ethon:MessageDataProperty`](http://ethon.consensys.net/MessageDataProperty)   
Groups all EthOn message data properties.
### Ethereum Blockchain
[`ethon:Blockchain`](http://ethon.consensys.net/Blockchain)   
An Ethereum blockchain is a distributed database that maintains a continuously-growing list of records called *blocks* secured from tampering and revision. Each block contains a timestamp and a link to a previous block in a Merkle tree structure.
### Ethereum Full Node
[`ethon:FullNode`](http://ethon.consensys.net/FullNode)   
A full node is a participant in an Ethereum network that keeps a record of the full blockchain, the full state and may engage in mining.
### Ethereum Light Node
[`ethon:LightNode`](http://ethon.consensys.net/LightNode)   
A light node is a participant in an Ethereum network that does not completely do any of the following: store the complete blockchain, store the complete world state, engage in mining.
### Ethereum Network
[`ethon:Network`](http://ethon.consensys.net/Network)   
An Ethereum network is the group of all nodes that conform to a certain protocol variant.
### Ethereum Protocol Variant
[`ethon:ProtocolVariant`](http://ethon.consensys.net/ProtocolVariant)   
A variant of the Ethereum protocol. Changes in the protocol result in a hard or soft fork.
### External Actor
[`ethon:ExternalActor`](http://ethon.consensys.net/ExternalActor)   
A person or other entity able to interface to an Ethereum node, but external to the world of Ethereum. It can interact with Ethereum through depositing signed transactions and inspecting the blockchain and associated state. Has one (or more) intrinsic accounts. While it is assumed that the ultimate external actor will be human in nature, software tools will be used in its construction and dissemination.
### Externally Controlled Account
[`ethon:ExternalAccount`](http://ethon.consensys.net/ExternalAccount)   
One of the two main types of accounts on Ethereum, an external account is an account controlled by an external actor (as opposed to a contract account). The unique identifier of an external account is its address. It consists of the rightmost 160 bits of the keccak 256 hash of its public key (example: 0x1a1138875dAB9E0AC8b0fd4a37EEAC5eb26B870B). There is only one way external accounts can actively change the state of the blockchain. They can be used to send a valid transaction to the Ethereum blockchain. The transaction can be directed towards other external accounts or towards contract accounts. Since the private key is needed for sending, a valid transaction can only be created by the person or entity controlling the private key of the external account. Besides being target of transactions, external accounts can also be the target of contract messages, block beneficiary rewards, uncle beneficiary rewards or payouts of contract accounts that have self-destructed.
## F
### from
[`ethon:from`](http://ethon.consensys.net/from)   
Relates a message to the account it originates from.
## G
### Genesis Block
[`ethon:GenesisBlock`](http://ethon.consensys.net/GenesisBlock)   
A genesis block is the unmined, deliberately created, very first block in a blockchain. It has no predecessors, i.e. no parent block.
## H
### has Account Storage
[`ethon:hasAccountStorage`](http://ethon.consensys.net/hasAccountStorage)   
Relates an account to the Merkle Patricia tree that encodes its storage contents at a certain account state. This property is Functional because an account state can have only one instance of account storage and inverse functional because an account storage can have only one associated account state.
### has Fork
[`ethon:hasFork`](http://ethon.consensys.net/hasFork)   
Relates a blockchain to a forked version of it. It is inverse functional because a forked blockchain can have only one blockchain it forked from. It is transitive because if a blockchain C that was forked from blockchain B that in turn was forked from blockchain A, blockchain C was also forked from blockchain A. It is asymetric because if blockchain A is forked from blockchain B, B cannot be also forked from A. It is irreflexive because a blockchain cannot be a fork of itself.
### has Log Entry
[`ethon:hasLogEntry`](http://ethon.consensys.net/hasLogEntry)   
Relates a transaction to a log entry it creates.
### has Log Topic
[`ethon:hasLogTopic`](http://ethon.consensys.net/hasLogTopic)   
Relates a log entry to a log topic.
### has Originator Transaction
[`ethon:hasOriginatorTx`](http://ethon.consensys.net/hasOriginatorTx)   
Relates a contract message to the transaction it originated from.
### has Transition
[`ethon:hasTransition`](http://ethon.consensys.net/hasTransition)   
Relates a state to a transition (i.e. a message) that creates a new state.
### has beneficiary
[`ethon:hasBeneficiary`](http://ethon.consensys.net/hasBeneficiary)   
Relates a block to the account to which all fees collected from the successful mining of this block are transferred.
### has current State
[`ethon:hasCurrentState`](http://ethon.consensys.net/hasCurrentState)   
This property relates an EthOn concept to its most current state.
### has parent Block
[`ethon:hasParentBlock`](http://ethon.consensys.net/hasParentBlock)   
Relates a block to its parent in the chain. It always points to the block with a number that is decreased by one, compared to the block it originates from. The relation is asymmetric because if block A is parent to block B then block B can not be parent to block A. It is also irreflexive because a block cannot be parent to itself.
### has receipts trie
[`ethon:hasReceiptsTrie`](http://ethon.consensys.net/hasReceiptsTrie)   
Relates a block to the trie that contains the block's receipt data.
### has state
[`ethon:hasState`](http://ethon.consensys.net/hasState)   
This property relates an EthOn concept to a state. It is inverse functional because a state can only belong to one single EthOn concept.
### has transaction receipt
[`ethon:hasReceipt`](http://ethon.consensys.net/hasReceipt)   
Relates a transaction to its receipt.
### has transactions trie
[`ethon:hasTxTrie`](http://ethon.consensys.net/hasTxTrie)   
Relates a block to the trie that contains the data of the transactions contained in the block.
## I
## J
## K
### knows of Uncle
[`ethon:knowsOfUncle`](http://ethon.consensys.net/knowsOfUncle)   
Relates a block to a known uncle.
## L
### Log Entry
[`ethon:LogEntry`](http://ethon.consensys.net/LogEntry)   
A log ntry is the result of an event in a smart contract, emitted during creation or execution of a contract account's code. It is related to the TxReceipt it was created in, the contract account that had the event, a series of 32-bytes log topics and a number of bytes of data.
### Log Topic
[`ethon:LogTopic`](http://ethon.consensys.net/LogTopic)   
A 32-bytes long topic of a log entry. The log topics of a log entry have an order given by a topic index value.
### Log Topic data
[`ethon:logTopicData`](http://ethon.consensys.net/logTopicData)   
Relates a log topic to the 32 bytes of data it contains.
### Log Topic index
[`ethon:logTopicIndex`](http://ethon.consensys.net/logTopicIndex)   
Relates a log topic to its index in the log entry. The log topic index defines the order of the log topics of in log entry.
### Log data
[`ethon:logData`](http://ethon.consensys.net/logData)   
Relates a log entry to its data.
### Log index
[`ethon:logIndex`](http://ethon.consensys.net/logIndex)   
Relates a log entry to its index in the transaction reciept of a transaction. The log index defines the order of the log entries of a transaction.
### logged by
[`ethon:loggedBy`](http://ethon.consensys.net/loggedBy)   
Relates a log entry to its logger's account.
## M
### Merkle Patricia Tree
[`ethon:ModifiedMerklePatriciaTree`](http://ethon.consensys.net/ModifiedMerklePatriciaTree)   
Merkle Patricia trees provide a cryptographically authenticated data structure that can be used to store all (key, value) bindings, although for the scope of this paper we are restricting keys and values to strings (to remove this restriction, just use any serialization format for other data types). They are fully deterministic, meaning that a Patricia tree with the same (key,value) bindings is guaranteed to be exactly the same down to the last byte and therefore have the same root hash, provide the holy grail of O(log(n)) efficiency for inserts, lookups and deletes, and are much easier to understand and code than more complex comparison-based alternatives like red-black trees.
### Message
[`ethon:Msg`](http://ethon.consensys.net/Msg)   
Data (as a set of bytes) and value (specified as Ether) that is passed between two accounts, either through the deterministic operation of an autonomous object (contract account) or the cryptographically secure signature of an external account.
### Message call depth
[`ethon:msgCallDepth`](http://ethon.consensys.net/msgCallDepth)   
A scalar value equal to the depth of the contract message. A contract message is represented as a call in the Ethereum EVM. This value represents the number of CALL or CREATE opcodes being executed at the time of the message execution.
### Message error
[`ethon:msgError`](http://ethon.consensys.net/msgError)   
A boolean value indicating whether the message validation resulted in an error. A "true" value indicates an error.
### Message error string
[`ethon:msgErrorString`](http://ethon.consensys.net/msgErrorString)   
A string informally describing an error that occured during the validation of a message. Only exists if msgError is true.
### Message gas limit
[`ethon:msgGasLimit`](http://ethon.consensys.net/msgGasLimit)   
A scalar value equal to the maximum amount of gas that should be used in executing this transaction. This is paid up-front, before any computation is done and may not be increased later. If used with contract messages it represents the fraction of the original transaction gas limit still available for execution of the contract message. After all resulting computations are done, excess gas is returned to the sender of the original transaction.
### Message init code
[`ethon:msgInit`](http://ethon.consensys.net/msgInit)   
An unlimited size byte array specifying the EVM-code for the contract account initialisation procedure.
### Message output
[`ethon:msgOutput`](http://ethon.consensys.net/msgOutput)   
The reulting output data from a call contract message.
### Message payload
[`ethon:msgPayload`](http://ethon.consensys.net/msgPayload)   
An unlimited size byte array specifying the data payload of the message.
### Msg gas used
[`ethon:msgGasUsed`](http://ethon.consensys.net/msgGasUsed)   
The amount of gas that was used for processing a single message, regardless of which type of message it may be.
### mines for
[`ethon:minesFor`](http://ethon.consensys.net/minesFor)   
Relates a mining node to the blockchain it mines for. Mining is the process of dedicating effort (working) to bolster one series of transactions (a block) over any other potential competitor block. It is achieved thanks to a cryptographically secure proof.
## N
### Node
[`ethon:Node`](http://ethon.consensys.net/Node)   
A participant in an Ethereum network, specifically an instance of one of the client implementations, which may be either a full node or a light node.
### next Post Block State
[`ethon:nextBlockState`](http://ethon.consensys.net/nextBlockState)   
Relates a post block state to the following post block state.
### next Post Message State
[`ethon:nextMsgState`](http://ethon.consensys.net/nextMsgState)   
Relates a post message state to the following post message state.
### next Post Transaction State
[`ethon:nextTxState`](http://ethon.consensys.net/nextTxState)   
Relates a post transaction state to the following post transaction state.
### next State
[`ethon:nextState`](http://ethon.consensys.net/nextState)   
Relates a state to the following state. In EthOn the state transition system has no branches.
## O
## P
### Protocol Account
[`ethon:ProtocolAccount`](http://ethon.consensys.net/ProtocolAccount)   
A protocol account is a type of account in Ethereum. Protocol accounts are specified in the Ethereum protocol, and have so far only been used to store the initial balance for users who participated in the Ethereum crowdsale. Protocol accounts could be added with any protocol change and may be either external accounts or contract accounts.
### ProtocolState
[`ethon:ProtocolState`](http://ethon.consensys.net/ProtocolState)   
This is a special state that can be created after specification of the protocol or any protocol change. It allows for setting balances of accounts, e.g. for prefunded accounts, creating predefined contract accounts with storage or setting any other state property as part of the protocol specification.
### part of
[`ethon:partOf`](http://ethon.consensys.net/partOf)   
This is a general relation to express part of relationships. The classic study of parts and wholes, mereology, has three axioms: 1. the part-of relation is Transitive - "parts of parts are parts of the whole" - If A is part of B and B is part of C, then A is part of C Reflexive - "Everything is part of itself" - A is part of A Antisymmetric - "Nothing is a part of its parts" - if A is part of B and A != B then B is not part of A.
## Q
## R
### Receipts Trie
[`ethon:ReceiptsTrie`](http://ethon.consensys.net/ReceiptsTrie)   
A trie structure that stores transaction receipts. Each block has a reference to the root hash of a receipts trie that stores the receipts of the transactions included in the block.
### Receipts root
[`ethon:receiptsRoot`](http://ethon.consensys.net/receiptsRoot)   
The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the block.
### refunds
[`ethon:refunds`](http://ethon.consensys.net/refunds)   
Relates a selfdestruct contract message to the contract account it sends its refund balance to.
### runs client
[`ethon:clientVersion`](http://ethon.consensys.net/clientVersion)   
Relates a node to a string identifying the Ethereum client version it runs. It composed of the client name (e.g. Geth) and a version identifier (e.g. v1.5.4).
## S
### Selfdestruct Contract Message
[`ethon:SelfdestructContractMsg`](http://ethon.consensys.net/SelfdestructContractMsg)   
A selfdestruct contract message is a contract message that deletes the originating contract and refunds its balance to the receiver of the message.
### State
[`ethon:State`](http://ethon.consensys.net/State)   
The concept of a state in a generic state transition system.
### State Transition
[`ethon:StateTransition`](http://ethon.consensys.net/StateTransition)   
The concept of a transition in a state transition system.
### State root
[`ethon:stateRoot`](http://ethon.consensys.net/stateRoot)   
The Keccak 256-bit hash of the root node of the state trie that represents this state.
### Storage
[`ethon:AccountStorage`](http://ethon.consensys.net/AccountStorage)   
The account storage is part of the account state and it contains contains the values of all variables defined in the contract's code at a certain point in time. Usually Ethereum clients implement this structure as a Merkle Patricia Tree. Whenever any of the contract's variables are changed a new state is created.
### Storage root
[`ethon:storageRoot`](http://ethon.consensys.net/storageRoot)   
A 256-bit hash of the root node of a Merkle Patricia tree that encodes the storage contents of the account (a mapping between 265-bit integer values), encoded into the trie as a mapping from the Keccak 256-bit hash of the 256-bit integer keys to the RLP-encoded 256-bit integer values.
### spawns Block
[`ethon:spawnsBlock`](http://ethon.consensys.net/spawnsBlock)   
Relates an Ethereum node to a valid block it has transmitted to the network. This does not specify the proofing algorithm (e.g. proof of work or proof of authority).
### start Block number
[`ethon:startBlockNumber`](http://ethon.consensys.net/startBlockNumber)   
The block number of the first block in a new blockchain after a hard fork.
## T
### Transaction
[`ethon:Tx`](http://ethon.consensys.net/Tx)   
Transactions are messages between two accounts that may transfer Ether and may contain a payload. Transactions always originate from an external account that is controlled by an external actor by means of a private key.  The execution of a transaction creates a 'transaction receipt'.
### Transaction Logs Bloom filter
[`ethon:txLogsBloom`](http://ethon.consensys.net/txLogsBloom)   
Relates a transaction to the Bloom filter of its log entries.
### Transaction Receipt
[`ethon:TxReceipt`](http://ethon.consensys.net/TxReceipt)   
The transaction receipt is a tuple of four items comprising the post-transaction-state, the cumulative gas used in the block containing the transaction receipt as of immediately after the transaction has happened, the set of logs created through execution of the transaction and the bloom filter composed from information in those logs.
### Transaction gas price
[`ethon:txGasPrice`](http://ethon.consensys.net/txGasPrice)   
A scalar value equal to the number of Wei to be paid per unit of gas for all computation costs incurred as a result of the execution of this transaction.
### Transaction index
[`ethon:txIndex`](http://ethon.consensys.net/txIndex)   
The position of a transaction in a block.
### Transaction nonce
[`ethon:txNonce`](http://ethon.consensys.net/txNonce)   
A scalar value equal to the number of transactions sent by the sender.
### Transaction r-value
[`ethon:txR`](http://ethon.consensys.net/txR)   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The txR value is a Byte array of length 32.
### Transaction s-value
[`ethon:txS`](http://ethon.consensys.net/txS)   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The value txS is a byte array of length 32.
### Transaction v-value
[`ethon:txV`](http://ethon.consensys.net/txV)   
The values txV, txR and txS correspond to the signature of the transaction and are used to determine the sender of the transaction. The value txV specifies the sign and finiteness of the curve point. Since EIP-155 it is used to realize a replay attack protection. It is calculated in the following way: txV = CHAIN_ID * 2 + 36
### Transactions Trie
[`ethon:TxTrie`](http://ethon.consensys.net/TxTrie)   
A trie structure that stores transactions. The header of a block contains a reference to the root of a Tx trie with all transactions contained in the block.
### Transactions root
[`ethon:transactionsRoot`](http://ethon.consensys.net/transactionsRoot)   
The Keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the block.
### Tx gas used
[`ethon:txGasUsed`](http://ethon.consensys.net/txGasUsed)   
The total amount of gas that was used for processing this Tx and all contract messages resulting from it. It is the sum of all msgGasUsed by this Tx and resulting contract messages.
### Tx hash
[`ethon:txHash`](http://ethon.consensys.net/txHash)   
The Keccak 256-bit hash of the transaction
### to
[`ethon:to`](http://ethon.consensys.net/to)   
Relates a message with the account it is sent to.
### triggers Contract Message
[`ethon:triggersMsg`](http://ethon.consensys.net/triggersMsg)   
Relates a message that was direct to a contract account to the contract messages that result from the call to the contract account. The chain of triggersMsg relations represents a call graph.
## U
### Uncle
[`ethon:Uncle`](http://ethon.consensys.net/Uncle)   
An uncle is the direct child of the k'th generation ancestor of a block B, where 2<=k<=7 but not a direct ancestor of B. Uncles are blockchain blocks found by a miner, when a different miner has already found another block for the corresponding place in the blockchain. They are also known as “stale blocks”. The parent of an uncle is an ancestor of the inserting block, located at the tip of the blockchain.
### Uncle beneficiary reward
[`ethon:uncleBeneficiaryReward`](http://ethon.consensys.net/uncleBeneficiaryReward)   
The reward the beneficiary of an uncle receives if a block includes it. The reward amount depends how far up the Uncle is in the blockchain (the number of the block in which it is included minus the uncle's number). An uncle reward is only paid if the distance is smaller than 8. For a distance of 1 the reward is 7/8 of the block reward, for a distance of 7 the reward is 1/8 of the block reward.
## V
### Value Contract Message
[`ethon:ValueContractMsg`](http://ethon.consensys.net/ValueContractMsg)   
A Value Contract Message is a Contract Message that does not call a function in a smart contract and doesn't create a new smart contract. Even though it is called "value" Contract Message, it can have a value of 0 Ether. Value Contract Messages can have a payload as long as that payload doesn't trigger the execution of a function in a smart contract.
### Value Transaction
[`ethon:ValueTx`](http://ethon.consensys.net/ValueTx)   
A Value Transaction is a Transaction that does not call a function in a smart contract and doesn't create a new smart contract. Even though it is called "value" Transaction, Transactions with a value of 0 Ether can be Value Transaction. Value Transactions can have a payload as long as that payload doesn't trigger the execution of a function in a smart contract.
### value in Wei
[`ethon:value`](http://ethon.consensys.net/value)   
A scalar value equal to the number of Wei to be transferred to the Message call's recipient. In the case of contract creation it is the initial balance of the contract account, paid by the sending account.
## W
### World State
[`ethon:WorldState`](http://ethon.consensys.net/WorldState)   
The world state, is a mapping between addresses (160-bit identifiers) of all accounts and their states (a data structure serialised as Recursive Length Prefix). The mapping is not stored on the blockchain itself but in a modified Merkle Patricia tree. An individual state is identified by the root hash of the trie.
## X
## Y
## Z