from emaildiscoverer import EmailDiscoverer
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to print all emails found on discoverable pages in a given '
                                                 'domain')
    parser.add_argument('domain_name', metavar='domain_name', help='Domain name for which to search web pages'
                                                                              ' for email addresses')
    parser.add_argument('--limit_discovery_distance', help='Limits search for discoverable pages to only '
                                                           'links found on initial input page', action='store_true')
    args = parser.parse_args()
    assert args.domain_name
    disc = EmailDiscoverer(args.domain_name, args.limit_discovery_distance)
    disc.discover_emails()
