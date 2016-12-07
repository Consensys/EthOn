#!/usr/bin/env python
# Command line tool for using alethio-scraper

import argparse
import ontospy
from jinja2 import Environment, FileSystemLoader
from rdflib import *


def bootstrapDesc(onto):
    """
    Extract whatever could be used as a description for the ontology
    """
    DCTERMS = Namespace('http://purl.org/dc/terms/')
    DC = Namespace('http://purl.org/dc/elements/1.1/')
    VANN = Namespace('http://purl.org/vocab/vann/')
    VOCAB = Namespace('http://www.w3.org/2003/06/sw-vocab-status/ns#')
    OWL = Namespace('http://www.w3.org/2002/07/owl#')

    DCcontributors = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.contributor)])
    DCcreators = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.creator)])
    VANNprefPrefix = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, VANN.preferredNamespacePrefix)])
    DCtitle = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.title)])
    VOCABterm_status = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, VOCAB.term_status)])
    OWLimports = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, OWL.imports)])
    OWLversionIRI = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, OWL.versionIRI)])


    RDFSlabel = "\n".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, RDFS.label)])
    RDFScomment = "\n".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, RDFS.comment)])

    DCdescription = "\n".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.description)])
    DCTERMSdescription = "\n".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DCTERMS.description)])
    DCTERMStitle = "\n".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, DCTERMS.description)])

    return {
        "comment": RDFScomment,
        "contributors": DCcontributors,
        "creators": DCcreators,
        "prefix": VANNprefPrefix,
        "title": DCtitle,
        "term_status": VOCABterm_status,
        "imports": OWLimports,
        "versionIRI": OWLversionIRI,
        "uri": onto.ontologyURI
    }

def main():
    ETHON = Namespace('http://consensys.net/ethereum-ontology/')
    ontospy.BOOTSTRAP_ONTOLOGIES.append('http://consensys.net/ethereum-ontology/')

    onto = ontospy.Ontospy("ethon.rdf")
    onto.ontologyURI = onto.ontologies[0].uri
    onto.namespaces.append(("ethon", URIRef("http://consensys.net/ethereum-ontology/")))

    for c in onto.classes:
        c.RDFScomment = ", ".join([x for x in c.rdfgraph.objects(c.uri, RDFS.comment)])
        c.RDFSlabel = ", ".join([x for x in c.rdfgraph.objects(c.uri, RDFS.label)])
        c.ETHONsuggestedStringRepresentation = ", ".join([x for x in c.rdfgraph.objects(c.uri, ETHON.suggestedStringRepresentation)])

    for p in onto.properties:
        p.RDFScomment = ", ".join([x for x in p.rdfgraph.objects(p.uri, RDFS.comment)])
        p.RDFSlabel = ", ".join([x for x in p.rdfgraph.objects(p.uri, RDFS.label)])
        p.ETHONsuggestedStringRepresentation = ", ".join([x for x in p.rdfgraph.objects(p.uri, ETHON.suggestedStringRepresentation)])

    env = Environment(loader=FileSystemLoader('spec_templates'))
    template = env.get_template('ethon_spec.html')
    site = template.render(
        meta=bootstrapDesc(onto),
        classes_tree=onto.toplayer,
        properties_tree=onto.toplayerProperties,
        classes=onto.classes,
        a_properties=onto.annotationProperties,
        d_properties=onto.datatypeProperties,
        o_properties=onto.objectProperties
    )

    with open("ethon_spec.html", "wb") as fh:
        fh.write(site)

main()
