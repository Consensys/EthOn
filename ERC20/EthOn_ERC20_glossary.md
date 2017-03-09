# EthOn ERC-20 Token extension Glossary
This glossary is compiled from the _rdfs:comment_ annotations of the EthOn ERC-20 ontology extension.
Please also consider looking at the [specification of ERC-20 EthOn extension](http://ethon.consensys.net/ERC20/EthOn_ERC20_spec.html). 
It is more detailed and includes class/property hierarchy information and restrictions.
## A
## B
### by Delegate
[`ethon:byDelegate`](http://ethon.consensys.net/ERC20/byDelegate)   
Relates a Delegate Token Transfer to the Account that initiated it.
## C
## D
### Delegate Token Transfer
[`ethon:DelegateTokenTransfer`](http://ethon.consensys.net/ERC20/DelegateTokenTransfer)   
A Delgate Token Transfer is a Token Transfer executed by a Spender that has been given an Allowance to spend.
### decimal units
[`ethon:decimalUnits`](http://ethon.consensys.net/ERC20/decimalUnits)   
The standard amount of decimal units that a Token uses.
## E
### ERC-20 Token
[`ethon:ERC20Token`](http://ethon.consensys.net/ERC20/ERC20Token)   
A token is a fungible virtual good that can be traded. ERC-20 Tokens comply to the standard described in the Ethereum ERC-20 proposal.
### EthOn ERC-20 Concept
[`ethon:EthOnERC20Concept`](http://ethon.consensys.net/ERC20/EthOnERC20Concept)   
Groups al EthOn ERC-20 extension concepts.
### EthOn ERC-20 Data Property
[`ethon:EthOnERC20DataProperty`](http://ethon.consensys.net/ERC20/EthOnERC20DataProperty)   
Groups all EthOn ERC-20 extension Data Properties.
### EthOn ERC-20 Object Property
[`ethon:EthOnERC20ObjectProperty`](http://ethon.consensys.net/ERC20/EthOnERC20ObjectProperty)   
Groups all EthOn ERC-20 extension Object Properties
## F
### from
[`ethon:from`](http://ethon.consensys.net/ERC20/from)   
Relates a Token Transfer with the Account it originates from.
## G
## H
### has Approval LogEntry
[`ethon:hasApprovalLogEntry`](http://ethon.consensys.net/ERC20/hasApprovalLogEntry)   
Relates a Token Approval to the LogEntry of the Event that was emitted when it was created.
### has Delegate
[`ethon:hasDelegate`](http://ethon.consensys.net/ERC20/hasDelegate)   
Relates a Token Allowance to the Account that has been delegate to spend it on behalf of the Tokens' owner.
### has Owner
[`ethon:hasOwner`](http://ethon.consensys.net/ERC20/hasOwner)   
Relates a Token Balance with its owner Account.
### has Token Balance
[`ethon:hasTokenBalance`](http://ethon.consensys.net/ERC20/hasTokenBalance)   
Relates a Contract Account to one of its Balances.
### has Transfer
[`ethon:hasTransfer`](http://ethon.consensys.net/ERC20/hasTransfer)   
Relates an ERC20 Token to one of its Transfers.
### has Transfer LogEntry
[`ethon:hasTransferLogEntry`](http://ethon.consensys.net/ERC20/hasTransferLogEntry)   
Relates a Token Transfer to the LogEntry of the Event that was emitted when it was created.
## I
### implements Token
[`ethon:implementsToken`](http://ethon.consensys.net/ERC20/implementsToken)   
Relates a Contract Account to the Token it implements.
### initial Allowance
[`ethon:initialAllowance`](http://ethon.consensys.net/ERC20/initialAllowance)   
A value equal to the initial base units of a Token that may be spent by an Allowance's delegate on behalf of the Tokens' owner.
### initial amount
[`ethon:initialAmount`](http://ethon.consensys.net/ERC20/initialAmount)   
The initial amount of Tokens that are created in the Token Contract.
## J
## K
## L
### last changed by
[`ethon:lastChangedBy`](http://ethon.consensys.net/ERC20/lastChangedBy)   
Relates a Token Balance with the most recent Transfer Event that affected it.
## M
## N
## O
### Owner Token Transfer
[`ethon:OwnerTokenTransfer`](http://ethon.consensys.net/ERC20/OwnerTokenTransfer)   
An Owner Token Transfer is a Token Transfer executed by the Account that owns the corresponding Token Balance.
## P
### provides Allowance
[`ethon:providesAllowance`](http://ethon.consensys.net/ERC20/providesAllowance)   
Relates a Token Balance with an Allowance it provides.
## Q
## R
### remaining Allowance
[`ethon:remainingAllowance`](http://ethon.consensys.net/ERC20/remainingAllowance)   
A value equal to the remaining base units of a Token that may be spent by an Allowance's delegate on behalf of the Tokens' owner. Remaining refers to the most recent known Allowance.
## S
## T
### Token Allowance
[`ethon:Allowance`](http://ethon.consensys.net/ERC20/Allowance)   
A Token Allowance provided by a Token Balance. The Delegate Account of the Allowance can spend a fixed amount of Tokens on behalf of the token owner.
### Token Balance
[`ethon:TokenBalance`](http://ethon.consensys.net/ERC20/TokenBalance)   
The Balance of a Token owned by an Account.
### Token Transfer
[`ethon:TokenTransfer`](http://ethon.consensys.net/ERC20/TokenTransfer)   
A Token Transfer is the record of an amount of tokens being transferred from one Account to another Account. If the Token complies to ERC-20 the Transfer is logged by an Event.
### to
[`ethon:to`](http://ethon.consensys.net/ERC20/to)   
Relates a Token Transfer with the Account it is sent to.
### token name
[`ethon:tokenName`](http://ethon.consensys.net/ERC20/tokenName)   
The name of the Token.
### token symbol
[`ethon:tokenSymbol`](http://ethon.consensys.net/ERC20/tokenSymbol)   
The symbol of a Token.
### total supply
[`ethon:totalSupply`](http://ethon.consensys.net/ERC20/totalSupply)   
The total supply of base units of a Token.
### transfer balance
[`ethon:transferBalance`](http://ethon.consensys.net/ERC20/transferBalance)   
A value equal to the base units of a Token that make up the current balance at the time of the last Transfer Event that affects the Token Balance. This doesn't represent the actual Token balance because it cannot be known what initial balances are defined in the Token Contract. It represents the Token balance of an account minus its initial balance defined in the Token Contract.
## U
## V
### value
[`ethon:value`](http://ethon.consensys.net/ERC20/http://ethon.consensys.net/ERC20/value)   
Value of the Token Transfer given in the Token's base unit.
## W
## X
## Y
## Z