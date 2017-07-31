#!/usr/bin/env python
# Command line tool for using alethio-scraper

import argparse
from ontospy import core as ontospy
from jinja2 import Environment, FileSystemLoader
from rdflib import *
import collections
import string

class SpecGenerator():
    '''
    Generates a specification from an ontology
    '''

    def __init__(self, namespace, prefix, ontology_file, template_folder, spec_template_file, glossary_template_file, spec_target_file, glossary_target_file):
        ETHON = Namespace(namespace)
        ontospy.BOOTSTRAP_ONTOLOGIES.append(namespace)
        VOCAB = Namespace('http://www.w3.org/2003/06/sw-vocab-status/ns#')

        onto = ontospy.Ontospy(ontology_file, rdf_format='xml')
        onto.ontologyURI = onto.ontologies[0].uri
        onto.namespaces.append((prefix, URIRef(namespace)))

        for c in onto.classes:
            c.RDFScomment = " \n\n".join(sorted([x for x in c.rdfgraph.objects(c.uri, RDFS.comment)]))
            c.RDFSlabel = ", ".join(sorted([x for x in c.rdfgraph.objects(c.uri, RDFS.label)]))
            c.ETHONsuggestedStringRepresentation = ", ".join(
                sorted([x for x in c.rdfgraph.objects(c.uri, ETHON.suggestedStringRepresentation)]))
            c.VOCABterm_status = ", ".join(sorted([x for x in c.rdfgraph.objects(c.uri, VOCAB.term_status)]))
            c.RDFSseeAlso = sorted([x for x in c.rdfgraph.objects(c.uri, RDFS.seeAlso)])
            c.RDFSisDefinedBy = sorted([x for x in c.rdfgraph.objects(c.uri, RDFS.isDefinedBy)])

        for p in onto.properties:
            p.RDFScomment = ", ".join(sorted([x for x in p.rdfgraph.objects(p.uri, RDFS.comment)]))
            p.RDFSlabel = ", ".join(sorted([x for x in p.rdfgraph.objects(p.uri, RDFS.label)]))
            p.ETHONsuggestedStringRepresentation = ", ".join(
                sorted([x for x in p.rdfgraph.objects(p.uri, ETHON.suggestedStringRepresentation)]))
            p.VOCABterm_status = ", ".join(sorted([x for x in p.rdfgraph.objects(p.uri, VOCAB.term_status)]))
            p.RDFSseeAlso = sorted([x for x in p.rdfgraph.objects(p.uri, RDFS.seeAlso)])
            p.RDFSisDefinedBy = sorted([x for x in p.rdfgraph.objects(p.uri, RDFS.isDefinedBy)])

        env = Environment(loader=FileSystemLoader(template_folder))

        # Render specification website
        spec_template = env.get_template(spec_template_file)
        spec = spec_template.render(
            meta=self.bootstrapDesc(onto),
            classes_tree=onto.toplayer,
            properties_tree=onto.toplayerProperties,
            classes=onto.classes,
            properties=onto.properties,
            a_properties=onto.annotationProperties,
            d_properties=onto.datatypeProperties,
            o_properties=onto.objectProperties
        )
        with open(spec_target_file, "wb") as fh:
            fh.write(spec.encode('utf-8'))

        # Render glossary
        glossary_template = env.get_template(glossary_template_file)
        glossary = glossary_template.render(glossary=self.makeGlossary(onto))

        with open(glossary_target_file, "wb") as fh:
            fh.write(glossary.encode('utf-8'))

    def slicedict(self, d, s):
        return {k: v for k, v in d.iteritems() if k.startswith(s)}


    def bootstrapDesc(self, onto):
        """
        Extract whatever could be used as a description for the ontology
        """
        DCTERMS = Namespace('http://purl.org/dc/terms/')
        DC = Namespace('http://purl.org/dc/elements/1.1/')
        VANN = Namespace('http://purl.org/vocab/vann/')
        VOCAB = Namespace('http://www.w3.org/2003/06/sw-vocab-status/ns#')
        OWL = Namespace('http://www.w3.org/2002/07/owl#')

        DCcontributors = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.contributor)]))
        DCcreators = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.creator)]))
        VANNprefPrefix = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, VANN.preferredNamespacePrefix)]))
        DCtitle = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, DC.title)]))
        VOCABterm_status = ", ".join([x for x in onto.rdfgraph.objects(onto.ontologyURI, VOCAB.term_status)])
        OWLimports = sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, OWL.imports)])
        OWLversionIRI = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, OWL.versionIRI)]))
        OWLversionInfo = ", ".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, OWL.versionInfo)]))
        RDFSseeAlso = sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, RDFS.seeAlso)])
        RDFScomment = "\n".join(sorted([x for x in onto.rdfgraph.objects(onto.ontologyURI, RDFS.comment)]))

        return {
            "comment": RDFScomment,
            "contributors": DCcontributors,
            "creators": DCcreators,
            "prefix": VANNprefPrefix,
            "title": DCtitle,
            "term_status": VOCABterm_status,
            "imports": OWLimports,
            "versionIRI": OWLversionIRI,
            "versionInfo": OWLversionInfo,
            "uri": onto.ontologyURI,
            "seeAlso": RDFSseeAlso
        }


    def merge_dicts(self, *dict_args):
        """
        Given any number of dicts, shallow copy and merge into a new dict,
        precedence goes to key value pairs in latter dicts.
        """
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result


    def makeGlossary(self, onto):
        terms = {}

        # the following list serves to exclude the classes and properties that are only used for grouping concepts
        exclude_list = ["AccountDataProperty",
                        "AccountObjectProperty",
                        "AccountConcept",
                        "BlockDataProperty",
                        "BlockObjectProperty",
                        "BlockConcept",
                        "EthOnConcept",
                        "EthOnDataProperty",
                        "MessageObjectProperty",
                        "MessageConcept",
                        "NetworkConcept",
                        "NetworkDataProperty",
                        "NetworkObjectProperty",
                        "EthOnObjectProperty",
                        "StateConcept",
                        "StateObjectProperty"]

        glossary = collections.OrderedDict()
        az = string.uppercase[:26]

        for term in onto.classes:
            if term.locale not in exclude_list:
                terms[term.RDFSlabel] = "[`ethon:"+term.locale+"`]("+term.uri+")   \n" + term.RDFScomment
        for term in onto.properties:
            if term.locale not in exclude_list:
                terms[term.RDFSlabel] = "[`ethon:"+term.locale+"`]("+term.uri+")   \n" + term.RDFScomment

        for letter in az:
            glossary[letter] = collections.OrderedDict(
                sorted(self.merge_dicts(self.slicedict(terms, letter), self.slicedict(terms, letter.lower())).items()))

        return glossary


def main():
    # Generate main EthOn spec
    SpecGenerator(namespace='http://ethon.consensys.net/',
                  prefix='ethon',
                  ontology_file='EthOn.rdf',
                  template_folder='doc_resources/templates',
                  spec_template_file='EthOn_spec_template.html',
                  glossary_template_file='EthOn_glossary_template.md',
                  spec_target_file='EthOn_spec.html',
                  glossary_target_file='EthOn_glossary.md')

    # Generate EthOn ERC-20 extension spec
    erc20path = 'ERC20/'
    SpecGenerator(namespace='http://ethon.consensys.net/ERC20/',
                  prefix='erc20',
                  ontology_file=erc20path+'EthOn_ERC20.rdf',
                  template_folder=erc20path+'doc_resources/templates',
                  spec_template_file='EthOn_ERC20_spec_template.html',
                  glossary_template_file='EthOn_ERC20_glossary_template.md',
                  spec_target_file=erc20path+'EthOn_ERC20_spec.html',
                  glossary_target_file=erc20path+'EthOn_ERC20_glossary.md')

    # Generate EthOn Contracts extension spec
    contractspath = 'Contracts/'
    SpecGenerator(namespace='http://ethon.consensys.net/Contracts/',
                  prefix='contracts',
                  ontology_file=contractspath+'EthOn_Contracts.rdf',
                  template_folder=contractspath+'doc_resources/templates',
                  spec_template_file='EthOn_Contracts_spec_template.html',
                  glossary_template_file='EthOn_Contracts_glossary_template.md',
                  spec_target_file=contractspath+'EthOn_Contracts_spec.html',
                  glossary_target_file=contractspath+'EthOn_Contracts_glossary.md')


main()
