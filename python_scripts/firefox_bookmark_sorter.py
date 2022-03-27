'''Purpose of the module is to extract bookmarks from firefox's
exported file.'''

import json
import os
import sys
import urllib.parse

def extract_bookmarks(json_dict):
    '''Return a list of extracted bookmarks'''
    if json_dict:
        if json_dict['type'] == "text/x-moz-place-container":
            if 'children' in json_dict:
                urls = []
                for child in json_dict['children']:
                    returned_urls = extract_bookmarks(child)
                    urls.extend(returned_urls)
                return urls
            else:
                return []
        else:
            return [json_dict['uri']]
    else:
        return []

def get_set_of_types(json_dict):
    '''Return a unique set of objects'''
    if json_dict:
        if json_dict['type'] == "text/x-moz-place-container":
            type_set = set(['text/x-moz-place-container'])
            if 'children' in json_dict:
                for child in json_dict['children']:
                    returned_set = get_set_of_types(child)
                    for unique_type in returned_set:
                        type_set.add(unique_type)
            return type_set
        else:
            return set([json_dict['type']])
    else:
        return set()

def get_domains(urls_list):
    '''Return a domain from each url in a provided list'''
    for url in urls_list:
        parsed_url = urllib.parse.urlparse(url)
        yield parsed_url.netloc.removeprefix('www.')

def group_urls_by_domains(urls_list, domains_list):
    '''Return a grouped domain->URL-list dict filtered by domain'''
    group_dict = {'__individual_sites': []}
    for domain_name in domains_list:
        selected_urls = []
        for url in urls_list:
            extracted_domain = urllib.parse.urlparse(url).netloc
            extracted_domain = extracted_domain.removeprefix('www.')
            if extracted_domain == domain_name:
                selected_urls.append(url)

        if len(selected_urls) > 1:
            group_dict[domain_name] = selected_urls
        else:
            single_url = selected_urls[0]
            group_dict['__individual_sites'].append(single_url)

    return group_dict

if __name__ == "__main__":
    bookmarks_file_path = sys.argv[1]
    bookmarks_file_path = os.path.expanduser(bookmarks_file_path)
    with open(bookmarks_file_path) as file_obj:
        bookmarks_json = json.load(file_obj)
    urls_list = extract_bookmarks(bookmarks_json)
    domains = list({domain for domain in get_domains(urls_list)})
    domains.sort()
    grouped_urls = group_urls_by_domains(urls_list, domains)
    output_lines = []
    individual_sites = grouped_urls['__individual_sites']
    del grouped_urls['__individual_sites']
    for domain_name, urls in grouped_urls.items():
        output_lines.append(f"***{domain_name}***")
        urls = [f"    {url}" for url in urls]
        output_lines.extend(urls)
    output_lines.append('Individual sites')
    individual_sites = [f"    {url}" for url in individual_sites]
    output_lines.extend(individual_sites)
    print("\n".join(output_lines))
