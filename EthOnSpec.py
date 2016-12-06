#!/usr/bin/env python
# Command line tool for using alethio-scraper

import argparse
from jinja2 import Environment, FileSystemLoader


def main():
    env = Environment(loader=FileSystemLoader('spec_templates'))
    template = env.get_template('ethon_spec.html')
    site = template.render(classes_list="List of classes",
                          object_properties_list="List of object properties",
                          data_properties_list="List of data properties",
                          classes=[
                              {
                                  "rdfs_label": "Account",
                                  "rdfs_comment": "Accounts have an intrinsic balance and transaction count maintained "
                                                  "as part of the Ethereum state. They also have some (possibly empty) "
                                                  "EVM Code and a (possibly empty) Storage State associated with them. "
                                                  "Though homogenous, it makes sense to distinguish between two "
                                                  "practical types of account: those with empty associated EVM Code "
                                                  "(thus the account balance is controlled, if at all, by some external"
                                                  " entity) and those with non-empty associated EVM Code (thus the "
                                                  "account represents an Autonomous Object). Each Account has a single "
                                                  "Address that identifies it. ",
                                  "status": "unstable",
                                  "subclassOf": "EthereumAccountConcept"
                              },
                              {
                                  "rdfs_label": "Block",
                                  "rdfs_comment": "Accounts have an intrinsic balance and transaction count maintained "
                                                  "as part of the Ethereum state. They also have some (possibly empty) "
                                                  "EVM Code and a (possibly empty) Storage State associated with them. "
                                                  "Though homogenous, it makes sense to distinguish between two "
                                                  "practical types of account: those with empty associated EVM Code "
                                                  "(thus the account balance is controlled, if at all, by some external"
                                                  " entity) and those with non-empty associated EVM Code (thus the "
                                                  "account represents an Autonomous Object). Each Account has a single "
                                                  "Address that identifies it. ",
                                  "status": "unstable",
                                  "subclassOf": "EthereumAccountConcept"
                              },
                              {
                                  "rdfs_label": "Transaction",
                                  "rdfs_comment": "Accounts have an intrinsic balance and transaction count maintained "
                                                  "as part of the Ethereum state. They also have some (possibly empty) "
                                                  "EVM Code and a (possibly empty) Storage State associated with them. "
                                                  "Though homogenous, it makes sense to distinguish between two "
                                                  "practical types of account: those with empty associated EVM Code "
                                                  "(thus the account balance is controlled, if at all, by some external"
                                                  " entity) and those with non-empty associated EVM Code (thus the "
                                                  "account represents an Autonomous Object). Each Account has a single "
                                                  "Address that identifies it. ",
                                  "status": "unstable",
                                  "subclassOf": "EthereumAccountConcept"
                              }
                          ]
                          )

    with open("ethon_spec.html", "wb") as fh:
        fh.write(site)

main()
